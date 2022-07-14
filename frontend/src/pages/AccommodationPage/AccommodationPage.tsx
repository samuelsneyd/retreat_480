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
    src: '../../../../static/images/accommodation.jpg',
    id: 1
  }
];

const AccommodationPage = () => {
  const [images, setImages] = useState(fallbackImages);

  useEffect(() => {
    return () => {
      axios.get('/api/images?tag=accommodation')
        .then((response) => {
          response.data?.length > 0 ? setImages(response.data) : null;
        })
        .catch(() => setImages(fallbackImages));
    };
  }, []);

  return (
    <Container>
      <PageTitle title={'Your Loft'} />
      <Grid container spacing={2} minHeight={450} sx={{ mb: 1 }}>
        <Grid item xs={12} md={6}>
          <Carousel
            animation={'fade'}
            duration={2000}
            swipe
          >
            {images.map((image) => <CarouselImage key={image.id} image={image} />)}
          </Carousel>
        </Grid>
        <Grid item xs={12} md={6}>
          <Typography variant={'h5'}>
            {'See your loft'}
          </Typography>
          <Typography sx={{ mt: 1, mb: 1 }}>
            {'Luxury accommodation right on the edge of native forests.'}
          </Typography>
          <Typography sx={{ mt: 1, mb: 1 }}>
            {'Features a double bed, living area, full kitchen, and acres of outdoor space.'}
          </Typography>
          <AccommodationIcons />
        </Grid>
      </Grid>
    </Container>
  );
};

export default withAnimation(AccommodationPage);