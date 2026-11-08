# Recomputed tables

Source: `data/extraction_table.csv`. Rows coded from PDFs: **15 of 39**. All rebuilt tables below cover only the coded rows unless marked 'manuscript labels'.

## A. Manuscript labels for all 39 (not rebuilt; for reference)

### Mode, manuscript labels (Table V) (n = 39)

| Category | n (%) |
|---|---|
| Teleoperation | 5 (12.8%) |
| Supervisory Control | 4 (10.3%) |
| Shared-Collaborative Control | 3 (7.7%) |
| Fully Autonomous | 27 (69.2%) |

### Platform, manuscript labels (Table VI) (n = 39)

| Category | n (%) |
|---|---|
| UAV | 13 (33.3%) |
| UGV | 13 (33.3%) |
| Legged | 2 (5.1%) |
| UUV / USV | 1 (2.6%) |
| Hybrid / Multi-Platform | 7 (17.9%) |
| Abstract / Unspecified | 3 (7.7%) |

### Mode x Platform, manuscript labels (Table VII) (n = 39)

| manuscript_mode \ manuscript_platform | UAV | UGV | Legged | UUV / USV | Hybrid / Multi-Platform | Abstract / Unspecified | Total |
|---|---|---|---|---|---|---|---|
| Teleoperation | 0 | 2 | 0 | 0 | 3 | 0 | 5 |
| Supervisory Control | 1 | 2 | 0 | 0 | 1 | 0 | 4 |
| Shared-Collaborative Control | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| Fully Autonomous | 9 | 9 | 2 | 1 | 3 | 3 | 27 |

## B. Rebuilt from PDFs (coded rows only)

### Table V Mode (n = 15)

| Category | n (%) |
|---|---|
| Teleoperation | 5 (33.3%) |
| Supervisory Control | 4 (26.7%) |
| Shared-Collaborative Control | 3 (20.0%) |
| Fully Autonomous | 3 (20.0%) |

### Table VI Platform (n = 15)

| Category | n (%) |
|---|---|
| UAV | 5 (33.3%) |
| UGV | 6 (40.0%) |
| Legged | 0 (0.0%) |
| UUV / USV | 0 (0.0%) |
| Hybrid / Multi-Platform | 4 (26.7%) |
| Abstract / Unspecified | 0 (0.0%) |

### Table VII Mode x Platform (n = 15)

| mode_clean \ platform_clean | UAV | UGV | Legged | UUV / USV | Hybrid / Multi-Platform | Abstract / Unspecified | Total |
|---|---|---|---|---|---|---|---|
| Teleoperation | 0 | 2 | 0 | 0 | 3 | 0 | 5 |
| Supervisory Control | 1 | 2 | 0 | 0 | 1 | 0 | 4 |
| Shared-Collaborative Control | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| Fully Autonomous | 1 | 2 | 0 | 0 | 0 | 0 | 3 |

### Table VIII Sensor prevalence (multi-select, n = 15)

| Modality | n (%) |
|---|---|
| visual | 8 (53.3%) |
| thermal | 1 (6.7%) |
| depth | 3 (20.0%) |
| lidar | 7 (46.7%) |
| gps | 2 (13.3%) |
| imu | 5 (33.3%) |
| acoustic | 2 (13.3%) |
| gas | 2 (13.3%) |
| rf | 1 (6.7%) |
| physio | 2 (13.3%) |
| none | 2 (13.3%) |

### Table IX Architecture (n = 15)

| Category | n (%) |
|---|---|
| PC/Offline | 5 (33.3%) |
| Onboard/Edge | 4 (26.7%) |
| Hybrid | 6 (40.0%) |
| Cloud | 0 (0.0%) |

### Table X Validation (n = 15)

| Category | n (%) |
|---|---|
| Simulation only | 5 (33.3%) |
| Real-world field test | 6 (40.0%) |
| Partial | 3 (20.0%) |
| Prototype bench test | 1 (6.7%) |

### Table XI Mode x Validation (n = 15)

| mode_clean \ validation_clean | Simulation only | Real-world field test | Partial | Prototype bench test | Total |
|---|---|---|---|---|---|
| Teleoperation | 0 | 3 | 1 | 1 | 5 |
| Supervisory Control | 0 | 3 | 1 | 0 | 4 |
| Shared-Collaborative Control | 2 | 0 | 1 | 0 | 3 |
| Fully Autonomous | 3 | 0 | 0 | 0 | 3 |

### Platform x Validation (n = 15)

| platform_clean \ validation_clean | Simulation only | Real-world field test | Partial | Prototype bench test | Total |
|---|---|---|---|---|---|
| UAV | 3 | 1 | 1 | 0 | 5 |
| UGV | 2 | 1 | 2 | 1 | 6 |
| Hybrid / Multi-Platform | 0 | 4 | 0 | 0 | 4 |

### Table XII Scenario (n = 15)

| Category | n (%) |
|---|---|
| Generic/Unspecified | 8 (53.3%) |
| Underground/Mine/Tunnel/Cave | 2 (13.3%) |
| Earthquake/Structural Collapse | 2 (13.3%) |
| Wilderness/Mountain/Forest | 3 (20.0%) |
| Maritime/Water | 0 (0.0%) |
| Wildfire/Fire | 0 (0.0%) |
| Other (single-occurrence hazard) | 0 (0.0%) |

### FA cluster x Validation (n = 3)

| fa_cluster \ validation_clean | Simulation only | Real-world field test | Partial | Prototype bench test | Total |
|---|---|---|---|---|---|
| multi-robot coordination | 3 | 0 | 0 | 0 | 3 |

### Environmental-realism limitation (author-stated)

- Coded rows: Y = 10 (66.7%), N = 5
- Borderline codes (refs): 15, 17, 18, 23
- N codes (refs): 10, 11, 16, 17, 22
- Upper bound on corpus Y if every uncoded row were Y: 34/39
- Generic: 4 (50.0%); hazard-specific: 6 (85.7%)

### Human role modelled x Mode (n = 15)

| mode_clean \ human_role_modelled | Y | N | Total |
|---|---|---|---|
| Teleoperation | 3 | 2 | 5 |
| Supervisory Control | 4 | 0 | 4 |
| Shared-Collaborative Control | 3 | 0 | 3 |
| Fully Autonomous | 0 | 3 | 3 |

### VDR score by mode (n = 15)

| Mode | n | VDR values | mean VDR | stat = Y |
|---|---|---|---|---|
| Teleoperation | 5 | [4, 4, 5, 5, 5] | 4.60 | 4 |
| Supervisory Control | 4 | [4, 5, 5, 6] | 5.00 | 3 |
| Shared-Collaborative Control | 3 | [3, 3, 4] | 3.33 | 2 |
| Fully Autonomous | 3 | [3, 3, 4] | 3.33 | 3 |

### Agreement with manuscript labels (coded rows)

- mode_agrees: {'Y': 15}
- platform_agrees: {'Y': 15}
- fa_cluster_agrees: {'Y': 3}
