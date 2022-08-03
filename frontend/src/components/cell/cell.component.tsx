import React from 'react'
import './cell.style.css'

type Props = {
  cellColor: string
}
const Cell = ({ cellColor }: Props) => {
  return (
    <div
      className={`heat-map-day`}
      style={{ backgroundColor: cellColor }}
    ></div>
  )
}

export default Cell
