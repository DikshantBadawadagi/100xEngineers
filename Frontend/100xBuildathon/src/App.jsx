import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Mainlayout from './components/Mainlayout'

const browserRouter = createBrowserRouter([
  {
    path: "/",
    element: <Mainlayout/>,  
  },
])
function App() {

  return (
    <>
    <RouterProvider router= { browserRouter}>

    </RouterProvider>
    </>
  )
}

export default App
