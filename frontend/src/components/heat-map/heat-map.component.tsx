import React from 'react'
import './heat-map.style.css'

import { ContributionResponse } from '../../types/api'
import { gradient } from '../../lib/util'

type Props = {
  data: ContributionResponse | null
}

const HeatMap = ({ data }: Props) => {
  if (!data) {
    return <></>
  }

  const weeks = data.weeks
  const color1 = 'FFFFFF'
  const color2 = 'FF69B4'
  const steps = 5

  const colors = gradient(color1, color2, steps)

  const maxRow = data.weeks.map(function (row) {
    return Math.max.apply(Math, row)
  })
  const max = Math.max.apply(null, maxRow)

  return (
    <div className="heat-map-container">
      {weeks.map((week: number[], idx: number) => {
        return (
          <div className="heat-map-week" key={idx}>
            {week.map((day: number, idx: number) => {
              let cellColor = '#000'
              if (day !== null) {
                const ratio = max / steps

                const percentile = (day / max) * ratio
                const colorIndex = Math.round(percentile * ratio)
                cellColor = '#' + colors[colorIndex]
              }

              return (
                <div
                  className={`heat-map-day`}
                  style={{ backgroundColor: cellColor }}
                  key={idx}
                ></div>
              )
            })}
          </div>
        )
      })}
    </div>
  )
}

export default HeatMap
