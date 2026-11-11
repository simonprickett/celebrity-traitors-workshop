# CSV data

Each file has one header row of camelCase column names, then one row per record. The same data, with the same names, is in [`../json/`](../json/README.md).

- Lines end with CRLF, including the last one.
- An **empty field means no value** (`null` in JSON). A row such as `amol,1,01/10/2026,,faithful,false,,,,,` has empty fields in the middle and at the end.
- Booleans are written `true` / `false`. Dates are `DD/MM/YYYY`.
- Fields are only quoted when they contain a comma, a double quote or a new line. Values with an apostrophe (such as `Myha'la`) are not quoted.

| File | Rows |
|---|---|
| [`contestants.csv`](#contestantscsv) | One per contestant (21) |
| [`main_game.csv`](#main_gamecsv) | One per player per episode or round table (179) |
| [`end_game.csv`](#end_gamecsv) | One per player per end game round (16) |
| [`prize_fund.csv`](#prize_fundcsv) | One per episode (10) |

## `contestants.csv`

The people who took part.

```
name,firstName,lastName,knownAs,profession,age,gender,nationality,wikipedia
kenny,Kenny,Ojuederie,King Kenny,Youtuber,29,M,English,https://en.wikipedia.org/wiki/King_Kenny_(internet_personality)
```

| Column | Description |
|---|---|
| `name` | Short lower-case id, used by the other files as `player` and in the image file names. |
| `firstName`, `lastName` | The contestant's name. |
| `knownAs` | Another name they are known by. Empty when there isn't one. |
| `profession` | For example `Actor`, `Comedian`, `Broadcaster`. |
| `age` | Age. |
| `gender` | `M`, `F` or `X`. |
| `nationality` | For example `English`, `Welsh`. |
| `wikipedia` | Link to the contestant's Wikipedia page. |

## `main_game.csv`

What happened to each player over the main game: episodes 1 to 10.

```
player,episode,episodeDate,roundTable,status,shield,votedFor,votes,outcome,recruitment,power
richard,3,08/10/2026,1,traitor,false,bella,1,banished,,
```

| Column | Description |
|---|---|
| `player` | A contestant's `name`. |
| `episode` | Episode number, 1 to 10. |
| `episodeDate` | When the episode aired, `DD/MM/YYYY`. |
| `roundTable` | Round table number, counted across the whole series from 1. Empty when the row is not at a round table. |
| `status` | `faithful` or `traitor`, as at that point in the episode. |
| `shield` | `true` if the player held a shield in that episode, otherwise `false`. |
| `votedFor` | The `player` they voted to banish at that round table. |
| `votes` | How many votes their vote counted for: `1`, or `2` when they used the dagger. |
| `outcome` | `banished` (at this round table) or `murdered` (revealed in this episode). |
| `recruitment` | The result of a recruitment offer, for example `accepted`. |
| `power` | A power used at this round table, for example `dagger`. |

How the rows work:

- **Episodes 1 and 2** have no round table: one row per player, with `roundTable` and the vote columns empty.
- **From episode 3**, each round table has one row per player who was there. Episodes 3 and 8 have two round tables each, so those players have two rows in the episode. `status` and `shield` are repeated on each one.
- **Murders** are revealed at the start of the next episode, so a murdered player gets one row in that episode with `roundTable` empty and `outcome` set to `murdered`. They took no other part in it. For example:

  ```
  sharon,9,29/10/2026,,faithful,false,,,murdered,,
  ```

- **Banishments** are on the banished player's row for the round table where it happened. Ties lead to another vote (episode 8, round tables 7 and 8), and the tied players do not vote in the revote, so their `votedFor` is empty.
- **An empty vote** can mean there was no round table, or that the player was there but did not vote.
- **To check:** two `recruitment` values still say `TODO review` (james_a in episode 2, kenny in episode 6).

## `end_game.csv`

The final stage, played as rounds between the remaining players.

```
player,round,status,decision,votedFor,outcome
romesh,1,faithful,continue,leigh-anne,
```

| Column | Description |
|---|---|
| `player` | A contestant's `name`. |
| `round` | End game round, 1 to 4. |
| `status` | `faithful` or `traitor`. |
| `decision` | `continue` or `end`, the player's choice in that round. Empty when no choice was made. |
| `votedFor` | The `player` they voted for. |
| `outcome` | `banished` or `winner`. |

## `prize_fund.csv`

The prize money offered and won in each episode.

```
episode,prizeOffered,prizeWon
2,10000,5000
```

| Column | Description |
|---|---|
| `episode` | Episode number. |
| `prizeOffered` | Prize money on offer in the episode. |
| `prizeWon` | Prize money won in the episode. |
