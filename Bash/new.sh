#!/bin/bash
for i in {1..255}; do
	echo ' ' > /dev/tcp/10.$i.0.2/22 2> /dev/null
done
