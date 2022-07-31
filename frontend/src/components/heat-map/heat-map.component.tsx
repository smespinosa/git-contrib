import React from 'react'
import { ContributionResponse } from '../../types/api'

type Props = {
  data: ContributionResponse | null
}

const HeatMap = ({ data }: Props) => {
  if (!data) {
    return <></>
  }

  const weeks = data.weeks

  console.log(weeks)
  return (
    <div className="heat-map">
      {weeks.map((week: number[], idx: number) => {
        return (
          <div className="heat-map-week" key={idx}>
            {week.map((day: number, idx: number) => {
              return (
                <div className="heat-map-day" key={idx}>
                  {day}
                </div>
              )
            })}
          </div>
        )
      })}
    </div>
  )
}

export default HeatMap
