/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [country]
      ,[date]
      ,case when [daily_vaccinations] = null
	  then 
	  select median from
	  ( WITH CTE AS
(   SELECT  country,
            [daily_vaccinations], 
            [half1] = NTILE(2) OVER(PARTITION BY country ORDER BY [daily_vaccinations]), 
            [half2] = NTILE(2) OVER(PARTITION BY country ORDER BY [daily_vaccinations] DESC)
    FROM    [dwh_model].[dbo].[data]
    WHERE   [daily_vaccinations] IS NOT NULL
)
SELECT  country,
        (MAX(CASE WHEN Half1 = 1 THEN [daily_vaccinations] END) + 
        MIN(CASE WHEN Half2 = 1 THEN [daily_vaccinations] END)) / 2.0 as median
FROM    CTE
GROUP BY country
)
	  else [daily_vaccinations]
	  end as [daily_vaccinations]
      ,[vaccines]
  FROM [dwh_model].[dbo].[data]

  order by daily_vaccinations desc