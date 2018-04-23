#------------------------------------------------------------------------
# InstallProvisioningProfile
# This sub lets us install provisioning profiles without the use of xcode
# It does what xcode does when clicking the install button in the accounts
# menu. It'll copy across the profile and rename it using the profiles UDID
#------------------------------------------------------------------------
sub InstallProvisioningProfile
{
  my ($profileName)   = @_;

  my $profile         = "$profileName.mobileprovision";
  my $user            = qx ( "whoami");
  my $result          = GetProfileUUID($profile);

  print ( "Installing profile: [$profileName.mobileprovision] as [$result.mobileprovision]\n" );
  qx ( "cp", "$profile", "/Users/$user/Library/MobileDevice/Provisioning\ Profiles/$result.mobileprovision" );
}

#------------------------------------------------------------------------
# GetProfileUUID
# Before XCode8 we had to specify provisioning profiles via their UUID
# This is what the subroutine is for, as of XCode8 we can just use the
# filename.
#------------------------------------------------------------------------
sub GetProfileUUID
{
  my ( $profile )   = @_;

  # This is the important bit, read binary file as text
  my $UUID          = qx ( "grep", "UUID", "-A1", "-a", "$profile" );

  # Parse some regex to get what we want
  $UUID             =~ s/\n//;
  $UUID             =~ s/.*<string>(.*)<\/string>.*/$1/;

  return $UUID;
}

#------------------------------------------------------------------------
# GetProfileInternalName
# This will return the name of the provisioning profile from inside the
# profile itself.
#------------------------------------------------------------------------
sub GetProfileInternalName
{
  my ( $profile )   = @_;
  my $file          = qx ( "grep", "Name", "-A1", "-a", "$profile" );

  $file             =~ s/\n//g;
  $file             =~ s/\s//g;
  $file             =~ s/\t//g;

  $file             =~ s/.*<key>Name<\/key><string>(.*?)<\/string>.*/$1/;

  return $file;
}
