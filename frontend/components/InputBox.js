import { Component } from 'react';
import { Button } from 'reactstrap';

class InputBox extends Component {
  render() {
    return (
      <div className="inputBox">
        <div className="logo">miniRL</div>

        <div className="d-flex urlField">
          <input type="text" className="form-control" />
          <Button color="primary">Minify</Button>
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
        align-self: 'center';
        text-align: 'center';
        width: 600px;
      }
      .logo {
        font-size: 60px;
        color: #dfebff;
      }
      .urlField {
        min-width: 350px;
        max-width: 800px;
        display: flex;
      }

      .urlField > input {
        opacity: 0.8;
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

export default InputBox;
