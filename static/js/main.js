const pickUpDateInput = document.getElementById('pick-up-date');
const dropOffDateInput = document.getElementById('drop-off-date');

// Get the current date
const currentDate = new Date();
const tomorrowDate = new Date(currentDate);
tomorrowDate.setDate(currentDate.getDate() + 1);

const tomorrow = tomorrowDate.toISOString().split('T')[0];

pickUpDateInput.min = tomorrow;
dropOffDateInput.min = tomorrow;

pickUpDateInput.addEventListener('input', function() {
  const selectedPickUpDate = new Date(this.value);
  const nextDayDate = new Date(selectedPickUpDate);
  nextDayDate.setDate(selectedPickUpDate.getDate() + 1);

  const nextDay = nextDayDate.toISOString().split('T')[0];
  dropOffDateInput.min = nextDay;

  // Check if the selected drop-off date is before the selected pick-up date
  const selectedDropOffDate = new Date(dropOffDateInput.value);
  if (selectedDropOffDate < nextDayDate) {
    dropOffDateInput.value = nextDay;
  }
});




