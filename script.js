console.log("test");

function resizeCanvas() {
    const canvas = document.getElementById('my_canvas');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

window.addEventListener('resize', resizeCanvas);
window.addEventListener('load', resizeCanvas);



resizeCanvas();