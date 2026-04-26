import { useState } from "react"
import Grid from "../components/Grid"
import Modal from "../components/Modal"

const Home = () => {
    const [openModal, setOpenModal] = useState(false)
    return(
        <div className="main">
            <div className="nav">
                <div className="g-8">
                    <button onClick={()=> setOpenModal(true)}>Nova Operação</button>
                    <button>Atualizar</button>
                </div>
                
                <div><input type="text"/></div>
            </div>
            <Grid></Grid>
            {openModal && (
                <Modal></Modal>
            )}
        </div>
    )
}

export default Home