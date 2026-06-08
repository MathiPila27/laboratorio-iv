// Parte III - Frontend integrado (script.js) - Actividad 3.3
const API_URL = "/api/tareas";

async function cargarTareas() {
    const res = await fetch(API_URL);
    const tareas = await res.json();
    const cont = document.getElementById('resultado');
    cont.innerHTML = "";
    tareas.forEach(t => {
        const div = document.createElement('div');
        div.className = "tarea";
        div.innerHTML = `<span><b>#${t.id}</b> ${t.titulo} — ${t.descripcion}</span>
                         <button class="del" onclick="eliminarTarea(${t.id})">Eliminar</button>`;
        cont.appendChild(div);
    });
}

async function crearTarea() {
    const titulo = document.getElementById('titulo').value;
    const descripcion = document.getElementById('descripcion').value;
    if (!titulo) { alert("El título es obligatorio"); return; }
    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titulo, descripcion })
    });
    document.getElementById('titulo').value = "";
    document.getElementById('descripcion').value = "";
    cargarTareas();
}

async function eliminarTarea(id) {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    cargarTareas();
}

cargarTareas();
