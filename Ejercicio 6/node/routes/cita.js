const express = require('express')
const router = express.Router()
const citaController = require('../controllers/cita')

router.get('/todas', citaController.todas)
router.get('/buscar', citaController.buscar)
router.post('/registrar', citaController.registar)
router.post('/modificar/:id', citaController.modificar)
router.post('/eliminar/:id', citaController.eliminar)

module.exports = router
