#!/usr/bin/env perl

use strict;
use warnings;

sub genFile
{
	print "Starting Run:\n";

	for (my $count = 1; $count <=64; $count++)
	{
		my $filename = "tmp/$count";
		open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
		print $fh $count;
		close $fh;
	}
}

genFile();
