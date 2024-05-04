# Organizations

Methods:

- <code title="post /organizations/create">client.organizations.<a href="./src/farquest/resources/organizations.py">create</a>(\*\*<a href="src/farquest/types/organization_create_params.py">params</a>) -> None</code>

# Session

Methods:

- <code title="post /session/{correlatedId}">client.session.<a href="./src/farquest/resources/session.py">create_correlated</a>(\*, path_correlated_id, \*\*<a href="src/farquest/types/session_create_correlated_params.py">params</a>) -> None</code>

# Auth

Methods:

- <code title="post /auth/callback">client.auth.<a href="./src/farquest/resources/auth.py">callback</a>(\*\*<a href="src/farquest/types/auth_callback_params.py">params</a>) -> None</code>
- <code title="get /auth/{state}">client.auth.<a href="./src/farquest/resources/auth.py">retrieve_state</a>(state) -> None</code>

# Quest

Methods:

- <code title="post /quest/create">client.quest.<a href="./src/farquest/resources/quest/quest.py">create</a>(\*\*<a href="src/farquest/types/quest_create_params.py">params</a>) -> None</code>
- <code title="get /quest/{id}">client.quest.<a href="./src/farquest/resources/quest/quest.py">retrieve</a>(id) -> None</code>
- <code title="get /quest/list/{filter}">client.quest.<a href="./src/farquest/resources/quest/quest.py">list</a>(filter) -> None</code>

## Types

Methods:

- <code title="get /quest/types">client.quest.types.<a href="./src/farquest/resources/quest/types.py">list</a>() -> None</code>

## Completions

Methods:

- <code title="get /quest/completions/count/{id}">client.quest.completions.<a href="./src/farquest/resources/quest/completions.py">count</a>(id) -> None</code>

## Validation

Methods:

- <code title="get /quest/validation/{id}">client.quest.validation.<a href="./src/farquest/resources/quest/validation.py">retrieve</a>(id) -> None</code>

# Quests

Methods:

- <code title="post /quest/complete">client.quests.<a href="./src/farquest/resources/quests.py">complete</a>(\*\*<a href="src/farquest/types/quest_complete_params.py">params</a>) -> None</code>
