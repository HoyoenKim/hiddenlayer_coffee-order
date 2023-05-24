module.exports = {
  HOST: "localhost",
  USER: "hoyeon",
  PASSWORD: "12345678",
  DB: "user_db",
  dialect: "mysql",
  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000
  }
};
