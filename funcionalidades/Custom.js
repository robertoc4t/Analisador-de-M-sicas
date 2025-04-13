
function analisarMusica() {
    const file = document.getElementById('audioFile').files[0];
    const output = document.getElementById('output');

    if (!file) {
      output.textContent = "Por favor, selecione um arquivo de áudio.";
      return;
    }

    // Simulação de análise (substituir com lógica real se necessário)
    const tipos = ["Rock", "Pop", "Jazz", "Clássico", "Eletrônica", "Funk", "Sertanejo"];
    const tipoAleatorio = tipos[Math.floor(Math.random() * tipos.length)];

    output.textContent = `Tipo musical: ${tipoAleatorio}`;
  }