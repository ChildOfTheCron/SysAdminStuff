#!/usr/bin/perl

sub aVeryBigSum {
   my ($n, @arr) = @_;

   my $arrTotal = 0;

   for (my $i=0; $i <= $n; $i++)
   {
      $arrTotal = $arrTotal + $arr[$i];
   }

   return $arrTotal;
}

$n = <STDIN>;
chomp $n;
$ar_temp = <STDIN>;
@ar = split / /,$ar_temp;
chomp @ar;
$result = aVeryBigSum($n, @ar);
print "$result\n";