import * as React from 'react';
import Typography from '@mui/material/Typography';
import AppAppBar from '../../components/AppAppBar/AppAppBar';
import AppFooter from '../../components/AppFooter/AppFooter';
import withRoot from '../../config/withRoot';

function AboutPage() {
  return (
    <>
      <AppAppBar/>
      <main style={{ padding: '1rem' }}>
        <Typography>{'Coming soon'}</Typography>
      </main>
      <AppFooter/>
    </>
  );
}

export default withRoot(AboutPage);