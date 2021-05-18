const express = require('express')
const router = express.Router()
const movimientoController = require('../controllers/movimiemto')

router.get('/todos', movimientoController.todos)
router.get('/buscar/:id', movimientoController.buscar)
router.post('/registrar', movimientoController.registrar)
router.post('/modificar/:id', movimientoController.modificar)
router.post('/eliminar/:id', movimientoController.eliminar)

module.exports = router

