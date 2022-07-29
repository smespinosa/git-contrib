import React from "react";

import "./App.css";

import SearchBox from "./components/search-box/search-box.component";
import YearSelectBox from "./components/year-select-box/year-select-box.component";
import HeatMap from "./components/heat-map/heat-map.component";

function App() {
  const [data, setData] = React.useState([]);
  const [searchEmailValue, setSearchEmailValue] = React.useState("");
  const [searchYearValue, setSearchYearValue] = React.useState(2022);

  const fetchContributions = async (email: string, year: number) => {
    const apiUrl = `http://localhost:8000/query?email=${email}&year=${year}`;
    fetch(apiUrl)
      .then((response) => response.json())
      .then((results) => setData(results));
  };

  const onSearchChange = (event: any) => {
    const searchValueString = event.target.value.toLocaleLowerCase();
    setSearchEmailValue(searchValueString);
  };

  const onYearChange = (event: any) => {
    setSearchYearValue(parseInt(event.target.value));
  };

  React.useEffect(() => {
    if (searchEmailValue.length > 0) {
      fetchContributions(searchEmailValue, searchYearValue);
    }
  }, [searchEmailValue, searchYearValue]);

  return (
    <div className="App">
      <SearchBox onChangeHandler={onSearchChange} />
      <YearSelectBox onChangeHandler={onYearChange} />
      <HeatMap data={data} />
    </div>
  );
}

export default App;
