var map = L.map('map').setView([3.102147222, 9.989638889], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
var myRenderer = L.canvas({ padding: 0.5 });
fetch('./data.csv')
   .then(response => {
       return response.text();
   })
   .then(data => {
       console.log(data)
       let color = null
       let sites = $.csv.toObjects(data, {separator:';'})
       console.log(sites)
       for(let site of sites){
        if (parseFloat(site['DLPck LossR UPlaneRTP CS']) <= 0.7 ) {
            color = 'green'
          
            }
            else if (parseFloat(site['DLPck LossR UPlaneRTP CS']) <=1 && parseFloat(site['DLPck LossR UPlaneRTP CS']) > 0.7) {
                color = 'yellow'
            }
            else if (parseFloat(site['DLPck LossR UPlaneRTP CS']) > 1 && parseFloat(site['DLPck LossR UPlaneRTP CS']) <=100) {
                color = 'red'
            }
            else {
                color='white'
            }
        L.circleMarker([site.Latitude, site.Longitude],  {
            renderer: myRenderer,
            radius:3,
            color
        }).addTo(map).bindPopup(site['Nom du Site'] + '  ' + site['DLPck LossR UPlaneRTP CS']);

        // L.marker([site.Longitude, site.Latitude]).addTo(map);

       }
       //console.log(this.users);
   })
   
   .catch(function () {
       this.dataError = true;
   })

  