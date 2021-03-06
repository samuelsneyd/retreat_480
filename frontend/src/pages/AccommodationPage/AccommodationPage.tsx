import * as React from 'react';
import { useEffect, useState } from 'react';
import { Container, Grid, Typography } from '@mui/material';
import axios from 'axios';
import Carousel from 'react-material-ui-carousel';
import AccommodationIcons from '../../components/AccommodationIcons/AccommodationIcons';
import CarouselImage from '../../components/CarouselImage/CarouselImage';
import PageTitle from '../../components/PageTitle/PageTitle';
import withAnimation from '../../hooks/withAnimation';

const fallbackImages = [
  {
    title: 'Accommodation',
    alt: 'Accommodation',
    image: '../../../../static/images/accommodation.jpg',
    src: ''
  }
];

const AccommodationPage = () => {
  const [images, setImages] = useState(fallbackImages);

  useEffect(() => {
    axios.get('/api/images?tag=accommodation')
      .then((response) => {
        response.data?.length > 0 ? setImages(response.data) : null;
      })
      .catch(() => setImages(fallbackImages));
  }, []);

  return (
    <Container>
      <PageTitle title={'Your Studio'} />
      <Grid container spacing={2} minHeight={450} sx={{ mb: 1 }}>
        <Grid item xs={12} md={6}>
          <Carousel
            animation={'fade'}
            duration={2000}
            swipe
          >
            {images.map((image) => <CarouselImage key={image.title} image={image} />)}
          </Carousel>
        </Grid>
        <Grid item xs={12} md={6}>
          <Typography variant={'h5'}>
            {'See your studio'}
          </Typography>
          <Typography sx={{ my: 1 }}>
            {'Set on two levels, your spacious studio includes a kitchen and dining area downstairs with two decks.'}
          </Typography>
          <Typography sx={{ my: 1 }}>
            {'Upstairs is a large open plan bedroom with bathroom. '}
            {'Your shower is outside nestled in the trees but under cover in case it rains.'}
          </Typography>
          <AccommodationIcons />
        </Grid>
      </Grid>
    </Container>
  );
};

export default withAnimation(AccommodationPage);
