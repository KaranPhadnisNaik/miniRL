import { Component } from 'react';
import { Button } from 'reactstrap';
import { TweenMax } from 'gsap';

class ResultCard extends Component {
  componentWillEnter(callback) {
    const el = this.container;
    TweenMax.fromTo(el, 0.5, { y: -50, opacity: 0 }, { y: 0, opacity: 1, onComplete: callback });
  }

  componentWillLeave(callback) {
    const el = this.container;
    TweenMax.fromTo(el, 0.5, { y: 0, opacity: 1 }, { y: 50, opacity: 0, onComplete: callback });
  }

  render() {
    return (
      <div className="card resultCard" ref={c => (this.container = c)}>
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
