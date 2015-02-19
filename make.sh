for i in *geojson; do ogr2ogr $i.shp $i  -lco ENCODING=UTF-8 ; done
