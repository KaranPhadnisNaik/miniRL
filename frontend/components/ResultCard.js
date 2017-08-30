import { Component } from 'react';
import { Button } from 'reactstrap';

class ResultCard extends Component {
  render() {
    return (
      <div className="card resultCard">
        <div className="card-block">
          <h4 className="card-title">
            {this.props.title}
          </h4>
          <h6 className="card-subtitle">
            {this.props.url}
          </h6>
          <p className="card-text">
            <a href={this.props.miniRl}>
              {this.props.miniRl}
            </a>
          </p>
        </div>
        {styles()}
      </div>
    );
  }
}

const styles = () =>
  (<style global jsx>
    {`
      .resultCard {
        opacity: 0.9;
      }

      .card-subtitle {
        font-style: italic;
        color: gray;
      }

      .card-text {
        margin-top: 10px;
        font-size: 16px;
        color: #454876;
      }
    `}
  </style>);

export default ResultCard;
