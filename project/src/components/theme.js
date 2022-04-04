import { createTheme } from '@mui/material/styles';
import { green, deepOrange } from '@mui/material/colors';

export const theme = createTheme({
  palette: {
    primary: {
      main: deepOrange[500],
    },
    secondary: {
      main: green[500],
    },
  },
});

