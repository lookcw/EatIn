import React from "react";
import { Form, Input, Button } from "antd";
import axios from "axios";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const { TextArea } = Input;
class IngInput extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: "" };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log("A text was submitted: " + this.state.value);
    let ing_arr = this.state.value.split(/[\n,]+/);
    let req_json = {
      start: 0,
      end: 4,
      ing_arr: ing_arr,
    };
    const requestOptions = {
      headers: { "Content-Type": "application/json" },
      data: req_json,
    };
    axios
      .post("https://eat-in.herokuapp.com/api/ing_query", requestOptions)
      .then((response) => response.data)
      .then((data) => this.props.callback(data));
  }

  handleFake = (event) => {
    const requestOptions = {
      headers: { "Content-Type": "application/json" },
    };
    axios
      .get("https://eat-in.herokuapp.com:8000/api/allrecipes", requestOptions)
      .then((response) => response.data)
      .then((data) => this.props.callback(data));
  };

  render() {
    const tailLayout = {
      wrapperCol: { offset: 8, span: 16 },
    };
    return (
      <form>
        <div className="ing-input">
          <h2>Input ingredients here</h2>
          <p>separated by commas or new lines</p>
          <TextArea
            placeholder="Input ingredients here"
            className="ing-text"
            rows={15}
            onChange={this.handleChange}
          />
          <Button type="primary" htmlType="submit" onClick={this.handleSubmit}>
            Get Recipes!
          </Button>
          <Button type="primary" onClick={this.handleFake}>
            LoadAll
          </Button>
        </div>
      </form>
    );
  }
}

export default IngInput;
