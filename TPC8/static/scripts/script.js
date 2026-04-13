function apagar_conceito(designacao){
        $.ajax("/conceitos/" + designacao, {
            method: "DELETE",
            success: function(response){
                alert("Correu bem!")
                window.location.href= "/conceitos"
        },
        error:function(response){
            alert("Correu mal!")
            console.log(response)
    }
    });
    }

// Pesquisa

const campo = document.getElementById("campoPesquisa");

if (campo) {

    function destacar(texto, query, caseSensitive) {
        if (!query) return texto;
        const flags = caseSensitive ? "g" : "gi";
        const escaped = query.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
        return texto.replace(new RegExp(escaped, flags), match => `<strong>${match}</strong>`);
    }

    function fazerPesquisa() {
        const query = campo.value;
        const exact = document.getElementById("exactMatch")?.checked ?? false;
        const caseSensitive = document.getElementById("caseSensitive")?.checked ?? false;

        if (query.length < 2) {
            document.getElementById("resultados").innerHTML = "";
            return;
        }

        const params = new URLSearchParams({
            q: query,
            exact: exact,
            case: caseSensitive
        });

        $.ajax("/pesquisar?" + params.toString(), {
            method: "GET",
            headers: { "X-Requested-With": "XMLHttpRequest" },
            success: function (data) {
                const div = document.getElementById("resultados");

                if (Object.keys(data).length === 0) {
                    div.innerHTML = "<p class='text-muted'>Nenhum conceito encontrado.</p>";
                    return;
                }

                let html = '<div class="list-group">';
                for (const [designacao, descricao] of Object.entries(data)) {
                    const designacaoHL = destacar(designacao, query, caseSensitive);
                    const descricaoHL  = destacar(descricao.substring(0, 120), query, caseSensitive);

                    html += `
                        <a href="/conceitos/${designacao}" 
                            class="list-group-item list-group-item-action">
                            ${designacaoHL} — ${descricaoHL}...
                        </a>`;
                }
                html += "</div>";
                div.innerHTML = html;
            }
        });
    }

    campo.addEventListener("input", fazerPesquisa);

    document.getElementById("exactMatch")?.addEventListener("change", fazerPesquisa);
    document.getElementById("caseSensitive")?.addEventListener("change", fazerPesquisa);
}
