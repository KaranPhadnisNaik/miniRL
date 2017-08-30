import { Component } from 'react';
import { Button } from 'reactstrap';

class SearchBox extends Component {
  constructor(props) {
    super(props);

    this.state = {
      url: '',
    };
  }

  updateUrl = event => this.setState({ url: event.target.value });

  submitUrl = () => {
    this.props.onSubmit(this.state.url);
  };

  renderButton = () => {
    if (this.props.loading) {
      return <Button color="primary">Loading...</Button>;
    }
    return (
      <Button color="primary" onClick={this.submitUrl}>
        Minify
      </Button>
    );
  };

  render() {
    return (
      <div className="d-flex urlField">
        <input
          type="text"
          className="form-control"
          value={this.state.url}
          onChange={this.updateUrl}
        />

        {this.renderButton()}

        {styles()}
      </div>
    );
  }
}

const styles = () =>
  (<style global jsx>
    {`
      .urlField {
        min-width: 350px;
        max-width: 800px;
        display: flex;
      }

      .urlField > input {
        opacity: 0.9;
        width: 100%;
        flex: 1;
        font-size: 16px;
        border: 0;
        border-radius: 0;
        border-top-left-radius: 2px;
        border-bottom-left-radius: 2px;
      }

      .urlField > button {
        font-size: 16px;
        border: 0;
        border-radius: 0;
        border-top-right-radius: 2px;
        border-bottom-right-radius: 2px;
        cursor: pointer;
      }
    `}
  </style>);

export default SearchBox;
