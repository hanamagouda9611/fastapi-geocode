from fastapi import APIRouter, Query
from database import get_db

router = APIRouter()

@router.get("/search")
def forward_geocode(
    q: str = Query(..., description="Search POIs by name or address"),
    limit: int = Query(10, description="Max number of results")
):
    conn = get_db()
    cursor = conn.cursor()
    try:
        pattern = f"%{q}%"

        query = """
        SELECT 
            name, 
            amenity, 
            "addr:housename" AS housename, 
            "addr:housenumber" AS housenumber,
            tags -> 'landmark' AS landmark,
            tags -> 'addr:street' AS street,
            tags -> 'secon_sree' AS secondary_street,
            tags -> 'addr:suburb' AS locality,
            tags -> 'addr:hamlet' AS sublocality,
            tags -> 'state' AS state,
            tags -> 'addr:city' AS city,
            tags -> 'addr:postcode' AS postcode,
            tags -> 'website' AS website,
            tags -> 'days_of_wo' AS days,
            ST_Y(ST_Transform(way, 4326)) AS latitude, 
            ST_X(ST_Transform(way, 4326)) AS longitude,
            TRIM(BOTH ', ' FROM
                CONCAT_WS(', ',
                    CASE WHEN tags -> 'landmark' NOT IN ('', 'None') THEN tags -> 'landmark' END,
                    CASE WHEN tags -> 'addr:street' NOT IN ('', 'None') THEN tags -> 'addr:street' END,
                    CASE WHEN tags -> 'secon_sree' NOT IN ('', 'None') THEN tags -> 'secon_sree' END,
                    CASE WHEN tags -> 'addr:hamlet' NOT IN ('', 'None') THEN tags -> 'addr:hamlet' END,
                    CASE WHEN tags -> 'addr:suburb' NOT IN ('', 'None') THEN tags -> 'addr:suburb' END,
                    CASE WHEN tags -> 'addr:city' NOT IN ('', 'None') THEN tags -> 'addr:city' END,
                    CASE WHEN tags -> 'state' NOT IN ('', 'None') THEN tags -> 'state' END,
                    CASE WHEN tags -> 'addr:postcode' NOT IN ('', 'None') THEN tags -> 'addr:postcode' END
                )
            ) AS description

        FROM planet_osm_point
        WHERE way IS NOT NULL AND (
            name ILIKE %s OR
            "addr:housename" ILIKE %s OR
            "addr:housenumber" ILIKE %s OR
            tags -> 'landmark' ILIKE %s OR
            tags -> 'addr:street' ILIKE %s OR
            tags -> 'secon_sree' ILIKE %s OR
            tags -> 'addr:suburb' ILIKE %s OR
            tags -> 'addr:hamlet' ILIKE %s OR
            tags -> 'state' ILIKE %s OR
            tags -> 'addr:city' ILIKE %s OR
            tags -> 'addr:postcode' ILIKE %s
        )
        LIMIT %s;
        """

        cursor.execute(query, (
            pattern, pattern, pattern,
            pattern, pattern, pattern,
            pattern, pattern, pattern,
            pattern, pattern,
            limit
        ))

        results = cursor.fetchall()
        return results or {"message": "No POIs found matching query."}
    finally:
        cursor.close()
        conn.close()





