import React, { useEffect, useState } from 'react';
import TextField from '@mui/material/TextField';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';

export default function BasicDatePicker(props) {
  const { handleDate, fieldName } = props;
  const [value, setValue] = useState(null);

  useEffect(() => {
    handleDate(value);
  })

  return (
    <LocalizationProvider dateAdapter={AdapterDateFns}>
      <DatePicker
        label={fieldName}
        value={value}
        onChange={(newValue) => {
          setValue(newValue);
        }}
        renderInput={(params) => <TextField {...params} />}
      />
    </LocalizationProvider>
  );
}