from enum import Enum

class Frequency(Enum):
    # in hours
    WEEKLY = int(7 * 24)
    MONTHLY = int(30 * 24)
    QUARTERLY = int(3 * 30 * 24)
    ANNUALY = int(365 * 24)

# compounds per year
compounds = {
    Frequency.ANNUALY: 1,
    Frequency.QUARTERLY: 4,
    Frequency.MONTHLY: 12,
    Frequency.WEEKLY: 52,
}
