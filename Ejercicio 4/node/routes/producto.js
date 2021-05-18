const express = require('express')
const router = express.Router()
const productoController = require('../controllers/producto')

router.get('/todos', productoController.todos)
router.get('/buscar/:id', productoController.buscar)
router.post('/registrar', productoController.registrar)
router.post('/modificar/:id', productoController.modificar)
router.post('/eliminar/:id', productoController.eliminar)

module.exports = router