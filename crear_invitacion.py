<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calíope - Mi primer añito </title>

  <!-- Miniatura -->
  <link rel="icon" type="image/jpeg" href="Miniatura.jpg">

  <!-- Open Graph -->
  <meta property="og:title" content="Calíope - Mi primer añito 💚">
  <meta property="og:description" content="¡Te invito a mi Califest! Música, flores y diversión 🌸💚">
  <meta property="og:image" content="Miniatura.jpg">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://tusuario.github.io/PrimeraCaliFest/">

  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap" rel="stylesheet">

  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Quicksand', sans-serif;
      background: linear-gradient(180deg, #c8f5df, #f4fffa);
      color: #2d7a5b;
      text-align: center;
      overflow-x: hidden;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      position: relative;
    }

    h1 {
      font-size: 2em;
      margin-top: 10px;
      animation: fadeInDown 1.2s ease;
      padding: 0 10px;
    }

    @keyframes fadeInDown {
      from { opacity: 0; transform: translateY(-20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    p {
      font-size: 1.1em;
      margin: 10px 15px;
      animation: fadeIn 2s ease-in;
    }

    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    img {
      width: 80%;
      max-width: 320px;
      border-radius: 20px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.2);
      margin-top: 15px;
      cursor: pointer;
      transition: transform 0.3s ease;
      z-index: 2;
    }

    img:hover {
      transform: scale(1.05);
    }

    .buttons {
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 25px;
      align-items: center;
      z-index: 2;
      width: 100%;
    }

    .buttons button {
      background: linear-gradient(90deg, #6cc8a2, #57b48c);
      border: none;
      color: #fff;
      font-size: 1em;
      padding: 12px 20px;
      border-radius: 15px;
      cursor: pointer;
      transition: transform 0.3s ease;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      width: 80%;
      max-width: 280px;
    }

    .buttons button:hover {
      transform: scale(1.05);
    }

    footer {
      margin-top: 25px;
      font-size: 1em;
      color: #2d7a5b;
      font-style: italic;
      animation: fadeIn 3s ease-in;
      z-index: 2;
      margin-bottom: 15px;
    }

    /* 🌸 FLORES DE FONDO */
    .flower {
      position: absolute;
      width: 70px;
      opacity: 0.7;
      animation: float 14s infinite ease-in-out;
      z-index: 1;
      pointer-events: none;
    }

    @keyframes float {
      0% { transform: translateY(100vh) rotate(0deg); opacity: 0.5; }
      50% { opacity: 1; }
      100% { transform: translateY(-10vh) rotate(360deg); opacity: 0.3; }
    }

    .flower:nth-child(1) { left: 5%; animation-delay: 0s; }
    .flower:nth-child(2) { left: 25%; animation-delay: 2s; }
    .flower:nth-child(3) { left: 50%; animation-delay: 4s; }
    .flower:nth-child(4) { left: 75%; animation-delay: 6s; }
    .flower:nth-child(5) { left: 90%; animation-delay: 8s; }

    @media (max-width: 600px) {
      h1 { font-size: 1.6em; }
      p { font-size: 1em; }
      img { max-width: 280px; }
    }
  </style>
</head>

<body>
  <img class="flower" src="flores/Flor1.png" alt="Flor">
  <img class="flower" src="flores/Flor2.png" alt="Flor">
  <img class="flower" src="flores/Flor3.png" alt="Flor">
  <img class="flower" src="flores/Flor4.png" alt="Flor">
  <img class="flower" src="flores/Flor5.png" alt="Flor">

  <h1>Calíope - Mi primer añito 💚</h1>
  <p>Los invito a festejar mi primer añito y a pasar un lindo momento.</p>
  <p><strong>Soy la bebé más guarachera</strong> 💃 y si no me creés, ¡tocá mi foto!</p>

  <img id="foto-bebe" src="foto_bebe.jpg" alt="Calíope">

  <div class="buttons">
    <button onclick="window.open('https://maps.google.com/?q=-34.8557038,-58.3888914','_blank')">📍 Cómo llegar</button>
    <button onclick="window.open('https://calendar.google.com/calendar/render?action=TEMPLATE&text=Cumple+de+Calíope&dates=20251206T160000Z/20251206T190000Z&details=Primer+añito+en+Tano+Eventos&location=Tano+Eventos','_blank')">📅 Guardar fecha</button>
    <button id="confirmar-btn" onclick="window.open('https://wa.me/5491156637770?text=Confirmo%20asistencia%20al%20cumple%20de%20Calíope%20💚','_blank')">💬 Confirmar asistencia</button>
  </div>

  <footer>Los esperamos a todos 💚</footer>

  <audio id="bg-music" preload="auto">
    <source src="musica.mp3" type="audio/mpeg">
  </audio>

  <script>
    const foto = document.getElementById('foto-bebe');
    const audio = document.getElementById('bg-music');
    let isPlaying = false;

    foto.addEventListener('click', () => {
      if (!isPlaying) {
        audio.play().then(() => {
          isPlaying = true;
        }).catch(err => {
          alert("Tocá de nuevo para activar la música 🎶");
        });
      } else {
        audio.pause();
        isPlaying = false;
      }
    });
  </script>
</body>
</html>
