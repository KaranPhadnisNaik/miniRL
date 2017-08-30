import { Component } from 'react';

const Footer = () =>
  (<footer style={styles.footerStyle}>
    <div>Made with &#10084; in San Francisco by @danishmughal and @karanphadnisnaik.</div>
  </footer>);

const styles = {
  footerStyle: {
    alignSelf: 'center',
    fontSize: '12px',
    color: '#dfebff',
    paddingBottom: '20px',
    textAlign: 'center',
  },
};

export default Footer;
