import { Component } from 'react';
import { Button } from 'reactstrap';
import { TransitionGroup } from 'react-transition-group';
import axios from 'axios';

import SearchBox from './SearchBox';
import ResultCard from './ResultCard';

class InputBox extends Component {
  constructor(props) {
    super(props);

    this.state = {
      loading: false,
      miniRl: '',
      url: '',
    };
  }

  submitUrl = (url) => {
    this.setState({
      loading: true,
      miniRl: '',
      url: '',
    });

    // Handle API request here
    let miniRl = '';

    axios
      .post('http://localhost:9000/link', {
        url,
      })
      .then((response) => {
        miniRl = `http://localhost:9000/${response.data.hash}`;
      })
      .catch((error) => {
        console.log(error);
      });

    setTimeout(() => {
      this.setState({
        loading: false,
        title: 'Title goes here',
        miniRl,
        url,
      });
    }, 1500);
  };

  renderResult = () => {
    if (this.state.miniRl) {
      return (
        <ResultCard url={this.state.url} miniRl={this.state.miniRl} title={this.state.title} />
      );
    }
  };

  render() {
    return (
      <div className="inputBox">
        <div className="inputTop">
          <div className="logo">miniRL</div>
          <SearchBox onSubmit={this.submitUrl} loading={this.state.loading} />
        </div>

        <div className="resultsContainer">
          <TransitionGroup>
            {this.renderResult()}
          </TransitionGroup>
        </div>

        {styles()}
      </div>
    );
  }
}

const styles = () =>
  (<style global jsx>
    {`
      .inputBox {
        text-align: 'center';
        width: 600px;
      }
      .inputTop {
        transition: all 3s;
      }
      .logo {
        font-size: 60px;
        color: #dfebff;
      }

      .resultsContainer {
        margin-top: 20px;
      }
    `}
  </style>);

export default InputBox;
