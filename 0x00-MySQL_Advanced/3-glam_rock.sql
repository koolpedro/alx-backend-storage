-- script that Lists all bands with Glam as their main style, ranked by their longevity

SELECT band_name, (2022 - CAST(formed AS INT) + 1) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
