import { useState, useEffect } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'
import Footer from './Footer'

const phrases = [
  "You'd better pay up, or the invisible hand of the market will smack you so hard you won't sit down for a week",
  "Hankering to toss some coin?",
  "Mhh. Thanks bunches"
]

function App() {
  const [count, setCount] = useState<number | null>(null)
  const [phrase, setPhrase] = useState<String | null>(null)

  const checkPhrase = () => {
    if (count) {
      if (count < 0) 
        setPhrase(phrases[0])
      else if (count >= 0 && count < 11) 
        setPhrase(phrases[1])
      else 
        setPhrase(phrases[2])
    } else {
      setPhrase("Couldn't set phrase: count is null")
    }
  }

  const handleClick = (action: String) => {

    let requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(action)
    }

    fetch(import.meta.env.VITE_REACT_APP_BACKEND_URL, requestOptions)
      .then(res => {
        return res.json()
      })
      .then(data => {
        setCount(data)
      })
  }

  useEffect(() => {
    console.log(import.meta.env.VITE_REACT_APP_BACKEND_URL)
    fetch(import.meta.env.VITE_REACT_APP_BACKEND_URL)
      .then(res => {
        return res.json()
      })
      .then(data => {
        setCount(data)
      })
  }, [])

  useEffect(checkPhrase)

  return (
    <>
      <div className="app-content">
        <h1>Toss a coin to your Witcher</h1>
        <p className="jacquarda">Toss a coin to your Witcher<br></br>Oh, Valley of Plenty...</p>

        <div className="geralt">
          <img src="geralt-720.gif"/>
        </div>

        <div className="status">
          <p>Tossed coins: { count }</p>
          <p>{ phrase }</p>
        </div>

        <div className="button-container">
          <button onClick={() => handleClick("toss")}>Toss</button>
          <button onClick={() => handleClick("steal")}>Steal</button>
        </div>
      </div>
      <Footer></Footer>
    </>
  )
}

export default App
