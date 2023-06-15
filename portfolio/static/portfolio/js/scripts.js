function displayDate() {
    const dataAtual = new Date();

    const meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ];

    const dia = dataAtual.getDate();
    const mes = meses[dataAtual.getMonth()];
    const ano = dataAtual.getFullYear();

    const dataFormatada = `${dia} de ${mes}, ${ano}`;

    document.getElementById("date").innerHTML = dataFormatada;
}

function displayText() {
    document.getElementById("date").innerHTML = "Data aqui!";
}

function calcular() {
    const expressao = document.getElementById("expressao").value;
    const resultado = eval(expressao);
    document.getElementById("result").innerText = resultado;
}
  
function limparResultado() {
    document.getElementById("result").innerText = "";
}

function colocarFraseImg() {
    var input = document.getElementById("input").value;
    var imagem = document.getElementById("imagem");
    var frase = document.createElement("p");

    frase.innerHTML = input;

    frase.style.position = "absolute";
    frase.style.top = "50%";
    frase.style.left = "50%";
    frase.style.transform = "translate(-50%, -50%)";
    frase.style.color = "white";
    frase.style.fontSize = "24px";

    imagem.parentNode.insertBefore(frase, imagem.nextSibling);

    return false;
  }

function displayTextHome() {
    document.getElementById("hero").innerHTML = "Home";
}

function displayTextPortfolio() {
    document.getElementById("portfolio").innerHTML = "Portfolio";
}

function displayTextSobreMim() {
    document.getElementById("portfolio").innerHTML = "Sobre Mim";
}

function displayLeftArrow() {
    document.getElementById("hero").innerHTML = '<i class="fas fa-arrow-left"></i>';
}

function displayLeftArrow2() {
    document.getElementById("portfolio").innerHTML = '<i class="fas fa-arrow-left"></i>';
}

function displayRightArrow() {
    document.getElementById("portfolio").innerHTML = '<i class="fas fa-arrow-right"></i>';
}