
var input = await File.ReadAllLinesAsync("input.txt");

void Part1()
{
    var result = input
        .Select(l => new Hand
        {
            Cards = l.Split(' ')[0],
            Bid = int.Parse(l.Split(' ')[1]),
        })
        .OrderBy(h => h, new HandComparer())
        .Select((h, i) => h.Bid * (i + 1))
        .Sum();

    Console.WriteLine($"Part 1: {result}");
}

void Part2()
{

    Console.WriteLine($"Part 2: ");
}

Part1();
Part2();

enum HandType
{
    FiveOfAKind,
    FourOfAKind,
    FullHouse,
    ThreeOfAKind,
    TwoPair,
    OnePair,
    HighCard
}


struct Hand
{
    public string Cards { get; set; }
    public int Bid { get; set; }

    public HandType GetHandType()
    {
        var groups = Cards.GroupBy(c => c);
        if (groups.Count() == 1) return HandType.FiveOfAKind;
        if (groups.Any(g => g.Count() == 4)) return HandType.FourOfAKind;
        if (groups.Count() == 2) return HandType.FullHouse;
        if (groups.Any(g => g.Count() == 3)) return HandType.ThreeOfAKind;
        if (groups.Count() == 3) return HandType.TwoPair;
        if (groups.Any(g => g.Count() == 2)) return HandType.OnePair;
        return HandType.HighCard;
    }
}

class HandComparer : IComparer<Hand>
{
    public int Compare(Hand x, Hand y)
    {
        if ((int)x.GetHandType() > (int)y.GetHandType()) return -1;
        if ((int)x.GetHandType() < (int)y.GetHandType()) return 1;

        for (int i = 0; i < 5; i++)
        {
            var xVal = GetCardValue(x.Cards[i]);
            var yVal = GetCardValue(y.Cards[i]);

            if (xVal > yVal) return 1;
            if (xVal < yVal) return -1;
        }

        return 0;
    }

    private int GetCardValue(char card) => card switch
    {
        'A' => 14,
        'K' => 13,
        'Q' => 12,
        'J' => 11,
        'T' => 10,
        _ => card - '0'
    };
}
