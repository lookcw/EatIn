import React from "react";
import RecipeList from "../containers/RecipeListView.js";
import Recipe from "./Recipe.js";
import { Container, Row, Col } from "react-bootstrap";
import IngInput from "./IngInput.js";
import axios from "axios";
var count = 4;

class RecipeSelect extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      initLoading: true,
      isLoading: false,
      data: [],
      list: [],
      curr: 0,
      selectedRecipe: 2,
      hasMore: true,
    };
  }

  componentDidMount() {
    count = 10;
    this.getData((res) => {
      this.setState({
        initLoading: false,
        data: res,
        list: res,
      });
    });
  }

  getData = (callback) => {
    axios(
      `https://eat-in.herokuapp.com/api/slicerecipes?start=${this.state.curr}&count=${count}`
    ).then((response) => callback(response.data));
  };

  onLoadMore = () => {
    console.log("loading more");
    this.setState({
      isLoading: true,
      curr: this.state.curr + count,
    });
    this.getData((res) => {
      if (!Array.isArray(res) || !res.length) {
        this.setState({ hasMore: false });
        console.log('received all ')
      }
      const data = this.state.data.concat(res);
      this.setState(
        {
          data,
          list:data,
          loading: false,
        },
        () => {
          window.dispatchEvent(new Event("resize"));
        }
      );
      console.log("curr");
    });
    this.setState({ isLoading: false });
  };

  setList = (recipeList) => {
    this.setState({ list: recipeList });
  };

  render() {
    return (
      <Container fluid>
        <Row>
          <Col xs={3}>
            <IngInput callback={this.setList} className="ing-input" />
          </Col>
          <Col xs={4}>
            <RecipeList
              onLoadMore={this.onLoadMore}
              list={this.state.list}
              onClick={(index) => () =>
                this.setState({ selectedRecipe: index })}
              hasMore={this.state.hasMore}
            />
          </Col>
          <Col>
            <Recipe recipe={this.state.list[this.state.selectedRecipe]} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default RecipeSelect;
