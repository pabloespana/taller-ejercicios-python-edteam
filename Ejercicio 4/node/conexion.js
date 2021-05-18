const Pool = require('pg').Pool

const pool = new Pool({
    host: 'localhost',
    user: 'postgres',
    password: '123456',
    database: 'ventas',
    port: 5432
})

module.exports = {pool}