import zipfile

# Contenu complet du fichier index.html
html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>L’art des ongles signée Gaëlle</title>
  <style>
    body { font-family: "Poppins", sans-serif; margin: 0; padding: 0; background-color: #fff9fa; color: #333; }
    header { background-color: #eec7cb; color: white; text-align: center; padding: 60px 20px; }
    header h1 { font-size: 2.8em; margin: 0; letter-spacing: 1px; }
    header p { font-size: 1.2em; margin-top: 10px; }
    nav { background-color: #f8e1e5; text-align: center; padding: 10px 0; }
    nav a { color: #c76d7e; text-decoration: none; margin: 0 15px; font-weight: bold; }
    nav a:hover { text-decoration: underline; }
    section { padding: 60px 20px; max-width: 1100px; margin: auto; }
    .about { display: flex; flex-wrap: wrap; align-items: center; gap: 30px; }
    .about img { width: 320px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
    .services { background-color: #fff0f2; border-radius: 10px; padding: 40px; }
    .services h2 { text-align: center; color: #c76d7e; }
    .service-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 30px; }
    .card { background-color: white; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); padding: 20px; text-align: center; transition: transform 0.2s ease; }
    .card:hover { transform: scale(1.02); }
    .card h3 { color: #c76d7e; }
    .gallery { margin-top: 40px; text-align: center; }
    .gallery h2 { color: #c76d7e; margin-bottom: 30px; }
    .gallery-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; }
    .gallery-grid img { width: 100%; height: 250px; object-fit: cover; border-radius: 10px; transition: transform 0.3s ease; }
    .gallery-grid img:hover { transform: scale(1.05); }
    .contact { background-color: #f8e1e5; padding: 50px 20px; border-radius: 10px; text-align: center; }
    .contact h2 { color: #c76d7e; }
    .contact p, .contact a { color: #333; }
    form { max-width: 500px; margin: 30px auto 0; text-align: left; }
    form label { display: block; margin-bottom: 5px; font-weight: bold; color: #c76d7e; }
    form input, form textarea { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; margin-bottom: 15px; font-family: inherit; }
    form button { background-color: #c76d7e; color: white; border: none; padding: 12px 25px; border-radius: 5px; cursor: pointer; font-size: 1em; display: block; margin: auto; }
    form button:hover { background-color: #b35867; }
    footer { background-color: #eec7cb; color: white; text-align: ce
