-- script that Lists all bands with Glam as their main style, ranked by their longevity

SELECT band_name, (YEAR('2022-01-01') - formed) AS lifespan
FROM bands
WHERE FIND_IN_SET('Glam rock', style) > 0
ORDER BY lifespan DESC;

