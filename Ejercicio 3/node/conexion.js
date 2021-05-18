const mysql = require('mysql2')

const conexion = mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"",
    database:"gastos"
})

conexion.connect((err, conn)=>{
    if (err) {
        console.log('Ha ocurrido un error al conectrse a la base de datos' + err)
    }else{
        console.log('Conexión exitosa')
        return conn
    }
})

module.exports = conexion