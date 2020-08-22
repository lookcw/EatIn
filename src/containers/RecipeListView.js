import React from "react";
import { List, Avatar, Button, Skeleton, Spin } from "antd";
import InfiniteScroll from "react-infinite-scroller";

// const reducer = (accumulator, currentValue) => accumulator + currentValue.ingredient + "\n";

function RecipeList(props) {
  return (
    <div className="list-container">
      <InfiniteScroll
        className="recipe-list"
        initialLoad={false}
        pageStart={0}
        hasMore={props.hasMore}
        useWindow={false}
        loadMore={props.onLoadMore}
        prefill={true}
      >
        <List
          dataSource={props.list}
          renderItem={(item, index) => (
            <List.Item>
              <List.Item.Meta
                avatar={<Avatar src={item.picture_link} />}
                title={<a onClick={props.onClick(index)}>{item.title}</a>}
                description=""
              />
            </List.Item>
          )}
        >
          {props.isLoading && (
            <div className="demo-loading-container">
              <Spin />
            </div>
          )}{" "}
        </List>
      </InfiniteScroll>
    </div>
  );
}

export default RecipeList;
