const conexion = require('../conexion')

const todas = (req, res)=>{
    const sql = 'select * from cita'
    conexion.all(sql, (err, result)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send(result)
        }
    })
}

const buscar = (req, res)=>{
    const dia = req.body.dia
    const sql = `select * from cita where dia='${dia}' and estado='Agendada'`
    conexion.all(sql, (err, result)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send(result)
        }
    })
}

const registar = (req, res)=>{
    const {paciente, detalle, dia, hora, estado} = req.body
    const sql = `insert into cita (paciente, detalle, dia, hora, estado) 
    values ('${paciente}', '${detalle}', '${dia}', '${hora}', '${estado}')`
    conexion.run(sql, (err)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send('Registro correto')
        }
    })
}

const modificar = (req, res)=>{
    const {id} = req.params
    const {estado} = req.body
    const sql = `update cita set estado='${estado}' where id=${id}`
    conexion.run(sql, (err)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send('La cita ha sido modificada')
        }
    })

}

const eliminar = (req, res)=>{
    const {id} = req.params
    const sql = `delete from cita where id=${id}`
    conexion.run(sql, (err)=>{
        if (err) {
            res.send('Ha ocurrido un error '+err)
        }else{
            res.send('Se ha eliminado')
        }
    })
}

module.exports = {todas, buscar, registar, modificar, eliminar}