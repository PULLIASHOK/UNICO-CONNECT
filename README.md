const express = require('express')
const app = express()
app.use(express.json())

const path = require('path')

const {open} = require('sqlite')
const sqlite3 = require('sqlite3')

const dbPath = path.join(__dirname, 'taskdatabase.db')

const intialize = async () => {
  try {
    db = await open({filename: dbPath, driver: sqlite3.Database})
    app.listen(3000, () => {
      console.log('Server running in http://localhost:3000/')
    })
  } catch (e) {
    consol.log(`DB Error ${e.message}`)
    process.exit(1)
  }
}
intialize()

const Tesseract = require('tesseract.js')
const nlp = require('compromise')
const fs = require('fs')

Tesseract.recognize(
  'C:UsersADMINOneDrivePicturesScreenshotsScreenshot 2024-05-23 192011.png',
  'eng',
)
  .then(({data: {text}}) => {
    console.log('Extracted Text:\n', text)

    const doc = nlp(text)
    console.log('\nDates Found:')
    console.log(doc.dates().out('array'))
    console.log('\nMoney Values:')
    console.log(doc.money().out('array'))
  })
  .catch(error => {
    console.log('Error during OCR:', error)
  })

app.get('/users/', async (request, response) => {
  const getAllTheData = SELECT * FROM
  users
  const dbResponse = await db.all(getAllTheData)
  response.send(dbResponse)
})
