#The Activity Analytics Tracker

SELECT 
    interaction_id,
    user_id,
    model_used,
    tokens_consumed,
    
    -- TODO: Step 1 - Use the SUM() aggregate function on the 'tokens_consumed' column.
    -- TODO: Step 2 - Append the OVER() keyword to turn it into a Window Function.
    -- TODO: Step 3 - Inside the OVER() clause, use PARTITION BY to group the calculation by 'user_id'.
    -- Alias the resulting column as 'total_user_tokens'.
    SUM(tokens_consumed) OVER(pARTITION BY user_id)  AS total_user_tokens
   

FROM user_interactions;