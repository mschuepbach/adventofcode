
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
    var result = input
        .Select(l => new Hand
        {
            Cards = l.Split(' ')[0],
            Bid = int.Parse(l.Split(' ')[1]),
            Joker = true
        })
        .OrderBy(h => h, new HandComparer(true))
        .Select((h, i) => h.Bid * (i + 1))
        .Sum();

    Console.WriteLine($"Part 2: {result}");
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
    public bool Joker { get; set; }

    public HandType GetHandType()
    {
        var groups = Cards.GroupBy(c => c).ToDictionary(g => g.Key, g => g.ToArray());
        HandType handType;
        if (groups.Count == 1) handType = HandType.FiveOfAKind;
        else if (groups.Any(g => g.Value.Length == 4)) handType = HandType.FourOfAKind;
        else if (groups.Count == 2) handType = HandType.FullHouse;
        else if (groups.Any(g => g.Value.Length == 3)) handType = HandType.ThreeOfAKind;
        else if (groups.Count == 3) handType = HandType.TwoPair;
        else if (groups.Any(g => g.Value.Length == 2)) handType = HandType.OnePair;
        else handType = HandType.HighCard;

        var jokers = groups.TryGetValue('J', out var j) ? j.Length : 0;
        if (!Joker || jokers == 0) return handType;
        if (handType == HandType.HighCard) return handType - 1;
        if (handType == HandType.TwoPair && jokers == 2) return handType - 3;
        return (HandType)Math.Max((int)HandType.FiveOfAKind, (int)(handType - 2));
    }
}

class HandComparer(bool joker = false) : IComparer<Hand>
{
    public int Compare(Hand x, Hand y)
    {
        if ((int)x.GetHandType() > (int)y.GetHandType()) return -1;
        if ((int)x.GetHandType() < (int)y.GetHandType()) return 1;

        for (int i = 0; i < 5; i++)
        {
            var xVal = GetCardValue(x.Cards[i], joker);
            var yVal = GetCardValue(y.Cards[i], joker);

            if (xVal > yVal) return 1;
            if (xVal < yVal) return -1;
        }

        return 0;
    }

    private int GetCardValue(char card, bool joker = false) => card switch
    {
        'A' => 14,
        'K' => 13,
        'Q' => 12,
        'J' => joker ? 1 : 11,
        'T' => 10,
        _ => card - '0'
    };
}
