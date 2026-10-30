const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const vm = require('node:vm');

const html = readFileSync(join(__dirname, '..', 'index.html'), 'utf8');
const source = html.match(/<script>([\s\S]*?)<\/script>/)[1];
const context = vm.createContext({window: {addEventListener() {}}, setTimeout});
vm.runInContext(source, context);
const midia = {titulo: 'Ecos do Tempo', genero: 'Ficção Científica', ano: 1992, tipo: 'filme'};
const svg = uri => decodeURIComponent(uri.split(',').slice(1).join(','));

test('gerador produz capa própria sem dependência externa', () => {
    const uri = vm.runInContext("gerador.gerarImagem('Ecos do Tempo', 'Ficção Científica', 1992, 'filme')", context);
    assert.ok(uri.startsWith('data:image/svg+xml;charset=utf-8,'));
    assert.ok(svg(uri).includes('Ecos do Tempo'));
    assert.ok(svg(uri).includes('1992'));
    assert.ok(!svg(uri).includes('<image'));
});

test('capas permanecem consistentes e variam por título e gênero', () => {
    const capa = context.gerarCapaSVG(midia);
    assert.equal(capa, context.gerarCapaSVG({...midia}));
    assert.notEqual(capa, context.gerarCapaSVG({...midia, titulo: 'Horizonte Perdido'}));
    assert.notEqual(capa, context.gerarCapaSVG({...midia, genero: 'Terror'}));
});

test('título com caracteres XML é tratado como texto', () => {
    const capa = svg(context.gerarCapaSVG({titulo: '<script>alert("x")</script> & ação', genero: 'Drama'}));
    assert.ok(!capa.includes('<script>'));
    assert.ok(capa.includes('&lt;script&gt;'));
    assert.ok(capa.includes('&amp;'));
});

test('mídia sem imagem recebe capa e URL de protocolo inválido é ignorada', () => {
    const semImagem = context.renderizarCapa(midia);
    assert.match(semImagem, /src="data:image\/svg\+xml/);
    const invalida = context.renderizarCapa({...midia, imagem_url: 'javascript:alert(1)'});
    assert.ok(!invalida.includes('javascript:'));
});

test('imagem externa é preservada e recebe alternativa', () => {
    const capa = context.renderizarCapa({...midia, imagem_url: 'https://example.com/poster.jpg'});
    assert.ok(capa.includes('src="https://example.com/poster.jpg"'));
    assert.ok(capa.includes('data-capa-alternativa="data:image/svg+xml'));
});

test('falha de imagem troca para capa alternativa uma única vez', () => {
    const alternativa = context.gerarCapaSVG(midia);
    const imagem = {src: 'https://example.com/inexistente.jpg', onerror() {}, dataset: {capaAlternativa: alternativa}};
    context.aplicarCapaAlternativa(imagem);
    assert.equal(imagem.src, alternativa);
    assert.equal(imagem.onerror, null);
});

test('aspas no título e na URL não criam atributos HTML', () => {
    const capa = context.renderizarCapa({titulo: '\" onload=\"alert(1)', imagem_url: 'https://example.com/\" onload=\"alert(1)'});
    assert.ok(capa.includes('&quot;'));
    assert.ok(!capa.includes(' onload="'));
});
