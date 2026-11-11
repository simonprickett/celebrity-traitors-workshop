# Who played the best game?

We asked Claude:

> "Looking at all the data available to you in this repository who do you think played the best game in this series and how do you define that?"

An analysis of the series 2 data in [`data/`](data/README.md). The short answer: **Kenny** played the best game overall, and **Sebastian** was the best player on the faithful side. How you define "best" decides it, so the definition and its limits come first.

## How "best" is defined

The data records outcomes and votes. It can't see persuasion, missions or the social game, so this analysis only judges what the data can show. Each side is judged on its own aim:

- **A traitor** plays well by staying undetected. The measure is how many faithful votes they drew at the round tables they attended.
- **A faithful** plays well by finding traitors. The measure is how often their vote landed on a player who was a traitor at that moment, plus whether they survived to the end.

## Traitors

| Traitor | Round tables attended as a traitor | Faithful votes against |
|---|---|---|
| kenny | 6 | 0 |
| maya | 10 | 3 |
| james_a | 9 | 5 |
| hannah | 4 | 17 |
| richard | 1 | 13 |

Maya lasted longest, but Kenny was the one who was never suspected. No faithful voted for him at any of the six round tables he attended as a traitor, and he reached the end game. Earlier in the series, as a faithful, he also voted for a traitor in 3 of his 4 votes, the best rate of anyone.

He used the dagger in episode 8, which doubled his vote in both rounds of that episode (sharon, then joanne). He lost in the end because the faithful finalists, romesh and sebastian, voted him out in round 3 of the end game.

## Faithfuls

Votes that landed on a traitor, out of votes cast while faithful:

| Player | Votes at traitors / votes cast |
|---|---|
| kenny | 3 / 4 |
| joe | 3 / 5 |
| sebastian | 5 / 10 |
| james_b | 4 / 10 |
| leigh-anne | 4 / 10 |
| romesh | 4 / 10 |
| ross | 2 / 5 |
| jerry | 2 / 6 |
| miranda | 2 / 6 |
| sharon | 2 / 7 |
| michael | 3 / 9 |
| julie | 1 / 3 |
| rob | 1 / 3 |
| bella | 1 / 2 |
| myhala | 1 / 2 |
| joanne | 0 / 7 |

Sebastian cast the most votes at traitors (5) and was still in the game at the end. He is marked `winner` in the final end game round, and he held a shield in 2 episodes. Romesh is marked `winner` in end game round 3 and had a similar record (4 of 10). Sebastian comes out slightly ahead, but it is close.

## Method

All figures come from `data/json/main_game.json` and `data/json/end_game.json`.

- A vote counts as a vote at a traitor if the player voted for is marked `traitor` in the same episode.
- "Faithful votes against" only counts votes from players who were faithful at that table, and a dagger vote counts as 2.
- A player's status can change during the series, so the same person can appear in both the traitor and faithful tables. Kenny does.
- Only rows with a `votedFor` value count as votes. Players who sat out a tie-break, or did not vote, are not counted as having cast one.

## Caveats

- **The samples are small.** Kenny's faithful accuracy rests on 4 votes.
- **Kenny's recruitment is not confirmed.** It is one of the two `recruitment` values still marked `TODO review` in `main_game.csv` (episode 6). If it changes, the point where his status turns changes with it, and so would his faithful voting record and his count of traitor round tables.
- **The winners are an interpretation.** Romesh and sebastian are read as the winners from the `winner` markers in `end_game`. If those markers mean something else, the ranking among the finalists changes.
- **Other definitions would give other answers.** For example, ranking by who influenced the most banishments, or by money won, would need different measures.
