const conexion = require('../conexion')

const todos = (req, res)=>{
    const sql = 'select * from movimiento'
    conexion.query(sql, (err, result)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send(result)
        }
    })
}

const buscar = (req, res)=>{
    const id = req.params.id
    const sql = `select * from movimiento where id=${id}`
    conexion.query(sql, (err, result)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send(result)
        }
    })
}

const registrar = (req, res)=>{
    const sql = 'insert into movimiento set ?'
    conexion.query(sql, req.body, (err)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send('Registro correcto')
        }
    })
}

const modificar = (req, res)=>{
    const id = req.params.id
    const campo = req.body.campo
    const nuevo_valor = req.body.nuevo_valor
    const sql = `update movimiento set ${campo}='${nuevo_valor}' where id=${id} `
    conexion.query(sql, (err)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send('Se ha actualizado correctamente')
        }
    })
}

const eliminar = (req, res)=>{
    const id = req.params.id
    const sql = `delete from movimiento where id=${id}`
    conexion.query(sql, (err)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send('Se ha eliminado correctamente')
        }
    })
}

module.exports = {
    todos, buscar, registrar, modificar, eliminar 
}