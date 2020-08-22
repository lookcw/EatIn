import React from "react";

// const reducer = (accumulator, currentValue) => accumulator + currentValue.ingredient + "\n";

function formatList(stri) {
  return stri.split(/\r?\n/).map((currElement, index) => {
  return `${index+1}. ${currElement}`; //equivalent to list[index]
}).join("\n");
}

function Recipe(props) {

  if (props.recipe) {
  return (
    <div className="instructions">
      <h1> {props.recipe.title}</h1>
      <h3>ingredients: </h3>
      <p>{formatList(props.recipe.ingredients.map(x => `${x.quantity} ${x.ingredient}`).join("\n"))}</p>      
      <h3>Instructions: </h3>
      <p>{formatList(props.recipe.instructions)}</p>
    </div>
  );
  }
  else {
    return (
      <div>
      <h2>
      No recipe selected
      </h2>
      </div>
    )
  }
}

export default Recipe;
