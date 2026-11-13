# JSON data

Each file is a JSON object with one key, holding a flat array of records. Every record has every key, with `null` where there is no value. Key names are camelCase and match the column headers in [`../csv/`](../csv/README.md), which holds the same data.

| File | Root key | Records |
|---|---|---|
| [`contestants.json`](#contestantsjson) | `contestants` | One per contestant (21) |
| [`main_game.json`](#main_gamejson) | `mainGame` | One per player per episode or round table (179) |
| [`end_game.json`](#end_gamejson) | `endGame` | One per player per end game round (16) |
| [`prize_fund.json`](#prize_fundjson) | `prizeFund` | One per episode (10) |

## Hosted copies

These files are also hosted, and can be loaded directly from a URL:

| Dataset | URL |
|---|---|
| Contestants | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/json/contestants.json` |
| Main game | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/json/main_game.json` |
| End game | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/json/end_game.json` |
| Prize fund | `https://storage.googleapis.com/play-static-content/celebrity-traitors-uk/data/json/prize_fund.json` |

## `contestants.json`

The people who took part.

```json
{
    "contestants": [
        {
            "name": "kenny",
            "firstName": "Kenny",
            "lastName": "Ojuederie",
            "knownAs": "King Kenny",
            "profession": "Youtuber",
            "age": 29,
            "gender": "M",
            "nationality": "English",
            "wikipedia": "https://en.wikipedia.org/wiki/King_Kenny_(internet_personality)"
        }
    ]
}
```

| Key | Type | Description |
|---|---|---|
| `name` | string | Short lower-case id, used by the other files as `player` and in the image file names. |
| `firstName`, `lastName` | string | The contestant's name. |
| `knownAs` | string or `null` | Another name they are known by, where there is one. |
| `profession` | string | For example `Actor`, `Comedian`, `Broadcaster`. |
| `age` | number | Age. |
| `gender` | string | `M`, `F` or `X`. |
| `nationality` | string | For example `English`, `Welsh`. |
| `wikipedia` | string | Link to the contestant's Wikipedia page. |

## `main_game.json`

What happened to each player over the main game: episodes 1 to 10. Each record is one player at one point in an episode.

```json
{
    "mainGame": [
        {
            "player": "richard",
            "episode": 3,
            "episodeDate": "08/10/2026",
            "roundTable": 1,
            "status": "traitor",
            "shield": false,
            "votedFor": "bella",
            "votes": 1,
            "outcome": "banished",
            "recruitment": null,
            "power": null
        }
    ]
}
```

| Key | Type | Description |
|---|---|---|
| `player` | string | A contestant's `name`. |
| `episode` | number | Episode number, 1 to 10. |
| `episodeDate` | string | When the episode aired, `DD/MM/YYYY`. |
| `roundTable` | number or `null` | Round table number, counted across the whole series from 1. `null` when the record is not at a round table. |
| `status` | string | `faithful` or `traitor`, as at that point in the episode. |
| `shield` | boolean | Whether the player held a shield in that episode. |
| `votedFor` | string or `null` | The `player` they voted to banish at that round table. |
| `votes` | number or `null` | How many votes their vote counted for: `1`, or `2` when they used the dagger. |
| `outcome` | string or `null` | `banished` (at this round table) or `murdered` (revealed in this episode). |
| `recruitment` | string or `null` | The result of a recruitment offer, for example `accepted`. |
| `power` | string or `null` | A power used at this round table, for example `dagger`. |

How the records work:

- **Episodes 1 and 2** have no round table. There is one record per player, with `roundTable` and the vote fields `null`.
- **From episode 3**, each round table has one record per player who was there. Episodes 3 and 8 have two round tables each, so those players have two records in the episode. `status` and `shield` are repeated on each one.
- **Murders** are revealed at the start of the next episode, so a murdered player gets one record in that episode with `roundTable` `null` and `outcome` `murdered`. They took no other part in it. Their earlier records are unchanged.
- **Banishments** are recorded on the banished player's record for the round table where it happened. Ties lead to another vote (episode 8, round tables 7 and 8), and the tied players do not vote in the revote, so their `votedFor` is `null`.
- **A `null` vote** can mean there was no round table, or that the player was there but did not vote.

## `end_game.json`

The final stage, played as rounds between the remaining players.

```json
{
    "endGame": [
        {
            "player": "romesh",
            "round": 1,
            "status": "faithful",
            "decision": "continue",
            "votedFor": "leigh-anne",
            "outcome": null
        }
    ]
}
```

| Key | Type | Description |
|---|---|---|
| `player` | string | A contestant's `name`. |
| `round` | number | End game round, 1 to 4. |
| `status` | string | `faithful` or `traitor`. |
| `decision` | string | `continue` or `end`, the player's choice in that round. In a tie-break round players can't change it, so it repeats their choice from the previous round. |
| `votedFor` | string or `null` | The `player` they voted for. `null` for a player who sits out a tie-break round. |
| `outcome` | string or `null` | `banished` or `winner`. |

After a tied vote the next round is a tie-break: the players named in the tie sit out (`votedFor` is `null`) and the others vote to break it. In round 3 here, james_b and kenny sit out after tying in round 2.

## `prize_fund.json`

The prize money offered and won in each episode.

```json
{
    "prizeFund": [
        {
            "episode": 2,
            "prizeOffered": 10000,
            "prizeWon": 5000
        }
    ]
}
```

| Key | Type | Description |
|---|---|---|
| `episode` | number | Episode number. |
| `prizeOffered` | number | Prize money on offer in the episode. |
| `prizeWon` | number | Prize money won in the episode. |
