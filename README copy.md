<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __ih_datamadpt0923_project_m1__

Ironhack Madrid - Data Analytics Part Time - Sep 2023 - Project Module 1

## **Data:**

There are 2 main datasources:

- **CSV Files.** The datasets contains information from the BiciMAD stations including their location (i.e.: latitude / longitude). You may find the `.csv` files in the __data__ folder.

- **API REST.** We will use the API REST from the [Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/), where you can find the __Catálogo de datos__ with more than 70 datasets. The API endpoint is `https://datos.madrid.es/egob`. 

> __IMPORTANT:__ These are the body corresponding to every dataset:

- Alana: `/catalogo/209426-0-templos-catolicas.json`

- Alberto: `/catalogo/209434-0-templos-otros.json`

- Ana: `/catalogo/202162-0-instalaciones-accesibles-municip.json`

- Andrew: `/catalogo/202180-0-instalaciones-accesibles-no-muni.json`

- Carlos: `/catalogo/202311-0-colegios-publicos.json`

- Elena: `/catalogo/203166-0-universidades-educacion.json`

- Guille: `/catalogo/200215-0-instalaciones-deportivas.json`

- John: `/catalogo/200304-0-centros-culturales.json`

- Natalia: `/catalogo/201000-0-embajadas-consulados.json`

- Rodrigo: `/catalogo/300356-0-monumentos-ciudad-madrid.json`

- Sil: `/catalogo/208844-0-monumentos-edificios.json`

- Silvia: `/catalogo/300614-0-centros-educativos.json`

- Tere: `/catalogo/200761-0-parques-jardines.json`

- Tomás: `/catalogo/212808-0-espacio-deporte.json`



---

## **Main Challenge:**

You must create a Python App (**Data Pipeline**) that allow their potential users to find the nearest BiciMAD station to a set of places of interest using the methods included in the module `geo_calculations.py`. The output table should look similar to:

| Place of interest | Type of place (*) | Place address | BiciMAD station | Station location |
|---------|----------|-------|------------|----------|
| Auditorio Carmen Laforet (Ciudad Lineal)   | Centros Culturales | Calle Jazmin, 46 | Legazpi | Calle Bolívar, 3 |
| Centro Comunitario Casino de la Reina | Centros municipales de enseñanzas artísticas | Calle Casino, 3 | Chamartin | Calle Rodríguez Jaén, 40 |
| ...     | ...            | ...        | ...      | ...        |
> __(*)__ This correspond to the type of place assigned to you. 


**Your project must meet the following requirements:**

- It must be contained in a GitHub repository which includes a README file that explains the aim and content of your code. You may follow the structure suggested [here](https://github.com/potacho/data-project-template).

- __It must create, at least, a `.csv` file including the requested table (i.e. Main Challenge).__ Alternatively, you may create an image, pdf, plot or any other output format that you may find convenient. You may also send your output by e-mail, upload it to a cloud repository, etc. 

- It must provide, at least, two options for the final user to select when executing using `argparse`: **(1)** To get the table for every 'Place of interest' included in the dataset (or a set of them), **(2)** To get the table for a specific 'Place of interest' imputed by the user.


**Additionally:**

- You must prepare a 4 minutes presentation (ppt, canva, etc.) to explain your project (Instructors will provide further details about the content of the presentation).

- The last slide of your presentation must include your candidate for the **'Ironhack Data Code Beauty Pageant'**. 


---

### **Bonus 1:**

You may include in your table the availability of bikes in each station.

---

### **Bonus 2:**

You may improve the usability of your app by using [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/).

---

### **Bonus 3:**

Feel free to enrich your output data with any data you may find relevant (e.g.: wiki info for every place of interest) or connect to the [BiciMAD API](https://mobilitylabs.emtmadrid.es/) and update bikes availability realtime or find a better way to calculate distances...there's no limit!!!

--- 


## **Project Main Stack**

- [Requests](https://requests.readthedocs.io/)

- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

- Module `geo_calculations.py`

- [Argparse](https://docs.python.org/3.9/library/argparse.html)












 


 

