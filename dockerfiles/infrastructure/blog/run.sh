#!/bin/bash
# Map the port environment provided by Railway / other providers
export server__port=$PORT
node current/index.js