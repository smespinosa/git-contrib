import React from 'react'

import './App.css'
import { ContributionResponse } from './types/api'

import HeatMap from './components/heat-map/heat-map.component'
import SearchBox from './components/search-box/search-box.component'
import YearSelectBox from './components/year-select-box/year-select-box.component'

function App() {
  const [data, setData] = React.useState<ContributionResponse | null>(null)
  const [searchEmailValue, setSearchEmailValue] = React.useState('')
  const [searchYearValue, setSearchYearValue] = React.useState(2022)

  const fetchContributions = (email: string, year: number) => {
    const apiUrl = `http://localhost:8000/query?email=${email}&year=${year}`
    fetch(apiUrl)
      .then((response) => response.json())
      .then((results) => setData(results))
  }

  const onSearchChange = (event: any) => {
    const searchValueString = event.target.value.toLocaleLowerCase()
    setSearchEmailValue(searchValueString)
  }

  const onYearChange = (event: any) => {
    setSearchYearValue(parseInt(event.target.value))
  }

  return (
    <div className="App">
      <SearchBox onChangeHandler={onSearchChange} />
      <YearSelectBox onChangeHandler={onYearChange} />
      <button
        onClick={() => fetchContributions(searchEmailValue, searchYearValue)}
      >
        Search
      </button>
      <HeatMap data={data} />
    </div>
  )
}

export default App
