// import { VERSION } from "./version"

export function getUID() {
  return `xxxx_$20`.replace(/x/g, () =>
    Math.floor(Math.random() * 16).toString(16)
  )
}
