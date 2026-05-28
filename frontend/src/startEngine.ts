// import the engine entry class
// import { BrowserContainer } from "./engine/container/browsercontainer"
import { getCanvas } from "./engine/utils/dom"

// export function startEngine() {
//   console.log("Starting billiards engine...")

//   // find canvas in the HTML page
//   const canvas = getCanvas("viewP1") as HTMLCanvasElement

//   // url params (engine expects this)
//   const params = new URLSearchParams(window.location.search)

//   // create and start engine
//   const engine = new BrowserContainer(canvas, params)
//   engine.start()
// }

import { BrowserContainer } from "./engine/container/browsercontainer"

export function startEngine() {
  console.log("starting engine...")

  const canvas = document.getElementById("viewP1") as HTMLCanvasElement

  console.log("canvas found:", canvas)

  const params = new URLSearchParams(window.location.search)

  const engine = new BrowserContainer(canvas, params)

  console.log("engine created")

  engine.start()

  console.log("engine started")
}