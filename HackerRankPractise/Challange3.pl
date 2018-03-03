#!/usr/bin/perl

sub solve {
   my @store = (@_);
   my $aliceTotal = 0;
   my $bobTotal = 0;

   for (my $i=0; $i < (scalar @store/2); $i++)
   {
   		print "Run $i \n";
   		if ($store[$i] > $store[$i+3])
   		{
   			print "alice!\n";
   			$aliceTotal++;
   		}
   		elsif ($store[$i] < $store[$i+3])
   		{
   			print "bob!\n";
   			$bobTotal++;
   		}
   }  
   
  # my $returnString = $aliceTotal + $bobTotal;
   
   return ("$aliceTotal",  "$bobTotal");
}

$a0_temp = <STDIN>;
@a0_arr = split / /,$a0_temp;
$a0 = $a0_arr[0];
chomp $a0; 
$a1 = $a0_arr[1];
chomp $a1;
$a2 = $a0_arr[2];
chomp $a2;
$b0_temp = <STDIN>;
@b0_arr = split / /,$b0_temp;
$b0 = $b0_arr[0];
chomp $b0; 
$b1 = $b0_arr[1];
chomp $b1;
$b2 = $b0_arr[2];
chomp $b2;
($resultAlice, $resultBob) = solve($a0, $a1, $a2, $b0, $b1, $b2);
print "$resultAlice $resultBob\n";
#print join(" ", @result); why overcomplicate return values?