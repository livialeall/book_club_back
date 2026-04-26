const Modal = () => {
    return(
    <div className="modal">
        <div className="modal-header">
                <h2>Cadastro Operação</h2>
            </div>
        <form action="POST" className="modal-form">
        <label>Nome:
            <input type="text" />
        </label>
        <label>Operação:
            <input type="text" />
        </label>
        <label>Quantidade:
            <input type="text" />
        </label>
        <div className="button-div">
            <button>
                Cancelar
            </button>
            <button>
                Enviar
            </button>
        </div>
        </form>
    </div>
    )
}

export default Modal