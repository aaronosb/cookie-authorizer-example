import React from "react";
import Amplify from "aws-amplify";
import "bootstrap/dist/js/bootstrap.bundle.min";
let config = {
  apiGateway: {
    REGION: "us-east-1",
    URL: "https://example-api-gateway-url.com/dev"
  }
};

Amplify.configure({
  API: {
    endpoints: [
      {
        name: "example",
        endpoint: example.apiGateway.URL,
        region: config.apiGateway.REGION,
        custom_header: async () => {
          return {
            Authorization: "random" // <- You still need to set the Authorization Header!
          };
        }
      }
    ]
  }
});

import React from "react";

class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      response: null
    };
  }

  componentDidMount() {
    // NOTE For this to work a cookie needs to be set with your API Gateway URL included in the
    // cookies "domain" so that it can access it. You also need to set withCredentials: true
    // like below for Amplify to pass your cookie with the request

    API.get("example", "/", { withCredentials: true })
      .then(response => {
        this.setState({
          response: response
        });
      })
      .catch(error => {});
  }

  render() {
    return (
      <div className="row mt-3">
        <div className="col-sm-12">
          <div className="jumbotron">
            <h3>Example</h3>
            <hr className="my-4" />
            <div>Response : {this.state.response}</div>
          </div>
        </div>
      </div>
    );
  }
}

render(<Main />, document.getElementById("root"));
