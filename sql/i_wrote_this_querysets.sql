
-- Task 1
SELECT bid.b_id as client_number, 
Count(CASE WHEN event_value.outcome='win' THEN 1 ELSE NULL END) as win,
Count(CASE WHEN event_value.outcome='lose' THEN 1 ELSE NULL END) as lose
FROM event_entity    
INNER JOIN event_value         
    ON event_entity.play_id = event_value.play_id 
INNER JOIN bid
    ON event_entity.play_id = bid.play_id 
GROUP BY bid.b_id;

-- Task 2
SELECT games.game as game, Count(DISTINCT games.play_id) as gamse_count
FROM
((SELECT play_id, Concat(event_entity.home_team, ' - ', event_entity.away_team) as game FROM event_entity)
UNION ALL
(SELECT play_id, Concat(event_entity.away_team, ' - ', event_entity.home_team) as game FROM event_entity)) as games
GROUP BY games.game;