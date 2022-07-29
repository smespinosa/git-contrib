import React from 'react';
import "./search-box.style.css";

type Props = {
    onChangeHandler: React.FormEventHandler<HTMLInputElement>
  };

const SearchBox = ({ onChangeHandler }: Props) => {
    return (
        <input
            className={`search-box`}
            type="search"
            onKeyUp={(e)=>{
                if (e.key === "Enter") {
                    onChangeHandler(e);
                }
            }}
        />
    )
};

export default SearchBox;