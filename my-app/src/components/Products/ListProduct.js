import React, { Component } from "react";
import { NotificationContainer, NotificationManager } from 'react-notifications';
import axios from 'axios';
class ListProduct extends Component {
  constructor(props) {
    super(props);
    this.state = {
      ProductList : "",
      errors: {}
    };
  }
  handleForm = e => {
    e.preventDefault();
};
  handleInput = e => {
    e.preventDefault();
  };
  componentDidMount() {
    fetch("http://127.0.0.1:8000/ecom/products")
      .then(res => res.json())
      .then(
        (result) => {
          console.log(result);
          // this.setState({
          //   isLoaded: true,
          //   items: result.items
          // });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          // this.setState({
          //   isLoaded: true,
          //   error
          // });
        }
      )
    // axios.get('http://127.0.0.1:8000/ecom/products',{
    // headers: {
    //   'Access-Control-Allow-Origin': '*',
    // },
    // proxy: {
    //   host: '127.0.0.1',
    //   port: 3000
    // }})
    //   .then(function (response) {
    //      this.setState({ ProductList: response.data })
    //     console.log(this.state);
    //   })
    //   .catch(function (error) {
    //     // handle error
    //     console.log(error);
    //   })
    //   .then(function () {
    //     // always executed
    //   });
  }


  render() {
    return (
      <div className="content">
        <NotificationContainer />
                <form onSubmit={this.handleForm}>
                    <div className="card">
                        <div className="card-header text-center">Product List</div>
                        <div className="card-body">
                          <div className="row" style={{ marginTop: 20 }}>
                            <div className="col-sm-12">
                              Product List
                            </div>
                          </div>
                        </div>
                        <div className="card-footer text-center"> <button type="submit" className="btn btn-primary text-center">Add Product</button></div>
                    </div>
                   

                </form>
            </div>
    );
  }
}


export default ListProduct;

