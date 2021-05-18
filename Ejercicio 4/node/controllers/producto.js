const {pool} = require('../conexion')

const todos = (req, res)=>{
    const sql = "select * from producto order by id"
    pool.query(sql, (err, result)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send(result.rows)
        }
    })
}

const buscar = (req, res)=>{
    const id = req.params.id
    const sql = `select * from producto where id=${id}`
    pool.query(sql, (err, result)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send(result.rows)
        }
    })
}

const registrar = (req, res)=>{
    const nombre = req.body.nombre
    const descripcion = req.body.descripcion
    const precio = req.body.precio
    const sql = `insert into producto (nombre, descripcion, precio) values ('${nombre}', '${descripcion}', ${precio})`
    pool.query(sql, (err)=>{
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
    sql = ''
    if (campo=='1'){
        sql = `update producto set nombre='${nuevo_valor}' where id=${id}`
    }
    else if (campo=='2'){
        sql = `update producto set descripcion='${nuevo_valor}' where id=${id}`
    }else if (campo=='3'){
        sql = `update producto set precio='${nuevo_valor}' where id=${id}`
    }
    pool.query(sql, (err)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send('Se ha actualizado')
        }
    })

}

const eliminar= (req, res)=>{
    const id = req.params.id
    const sql = `delete from producto where id=${id}`
    pool.query(sql, (err)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send('Se ha eliminado')
        }
    })
}

module.exports = {todos, buscar, registrar, modificar, eliminar}