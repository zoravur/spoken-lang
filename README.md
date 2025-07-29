# Spock, a programming language that you speak.

Yet unstable.

For an introduction to Spock, click [here](https://zoravur.com/spock-a-spoken)

## Get started

To run the code:
- Clone the repository and its submodules
- Install dependencies
- Run the following command in a terminal:
```
$ python whisper_online_server.py
$ # Run a client for the server, and pipe the text output to spock/main.py, for instance,
$ arecord -f S16_LE -c1 -r 16000 -t raw -D default | nc localhost 43001 | python spock/main.py

```

## Requirements
- Either an Nvidia GPU to run whisper locally, or an openai api key. See https://github.com/ufal/whisper_streaming for more details
- Some way of recording audio to a port.

## Examples
- See [the test folder](https://github.com/zoravur/spoken-lang/tree/master/test/v2grammar).

## Tutorial
- Coming soon!
