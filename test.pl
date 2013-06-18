#!/usr/bin/perl  

# PROGRAM NAME: perl.txt

# Example of talking to the signal generator via SCPI-over-sockets 

#  

use IO::Socket;  

# Change to your instrument's hostname 

my $instrumentName = "test"; 

# Get socket 

$sock = new IO::Socket::INET ( PeerAddr => $instrumentName,  

                               PeerPort => 5025,  

                               Proto => 'tcp',  

                               );  

die "Socket Could not be created, Reason: $!\n" unless $sock;  

# Set freq 

print "Setting frequency...\n"; 

print $sock "freq 1 GHz\n"; 

# Wait for completion 

print "Waiting for source to settle...\n"; 

print $sock "*opc?\n"; 

my $response = <$sock>; 

chomp $response;           # Removes newline from response 

if ($response ne "1")  

{ 

   die "Bad response to '*OPC?' from instrument!\n"; 

}

# Send identification query 

print $sock "*IDN?\n";  

$response = <$sock>;  

chomp $response; 

print "Instrument ID: $response\n"; 
