document.getElementById("home").addEventListener("click", goHome);

goHome = () => {
    window.location.href = "{{ url_for('index') }}";
}
