#!/usr/bin/perl

sub diagonalDifference {
    # Complete this function   
    my @grabArr = @_;
    my $ref = \@grabArr;

    my $xLine;
    my $yLine;

    my $xTotal = 0;
    my $yTotal = 0;

    print "ref is:" + scalar @$ref;

    foreach my $val (@$ref)
    {
    	foreach my $valSub (@$val)
    	{
    		print "valSub: $valSub \n";
    	}
    }

    for (my $i=0; $i < scalar @$ref; $i++)
    {

    	$xTotal = $xTotal + $ref->[$i]->[$i];
    	$yTotal = $yTotal + $ref->[$i]->[(scalar @$ref-1)-$i];

    }

    print "xTotal: $xTotal AND yTotal:$yTotal\n";
    $absolute = $xTotal - $yTotal;
    abs($absolute);

    return abs($absolute);
}

$n = <STDIN>;
chomp $n;
$a_i = 0;
@a = ();
while($a_i < $n){
   my $a_temp = <STDIN>;
   my @a_t = split / /,$a_temp;
   chomp @a_t;
   push @a,\@a_t;
   $a_i++;
}
$result = diagonalDifference(@a);
print "$result\n";