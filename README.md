# long-siteswaps
Generate siteswaps which are also valid if you take 4 throws off the end

For example, these siteswaps are all valid:
- 669744956468557746884466758556
- 66974495646855774688446675
- 6697449564685577468844
- 669744956468557746
- 66974495646855
- 6697449564
- 669744

## But why?
If you consider 669744 as a 4-handed siteswap, one person is doing self, double pass flip and the other is doing self, single pass, flip.
Now consider 6697449564. Person one is doing self, double pass, flip, double pass, self. The first three throws they are doing are the same and two have been added on the end.

To juggle 669744956468557746884466758556 each juggler needs to memorise a series of 15 throws. But they can first memorise a series of three throws and then keept adding two throws at a time until they reach the full pattern!

## How do I use it?
You need to run the script generator.py

Currently it will only build patterns out of 2s, 6s, 7s, 8s and 9s. If you want some 5s, for example, just add 5 to the list of throws.