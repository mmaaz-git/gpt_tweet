READ_FILE_PATH = "twitter_archive/data/tweets.js"
WRITE_FILE_PATH = "twitter_archive/data/tweets_prepared_short.jsonl" # make sure it is a .jsonl
N_TWEETS = 500 # will only parse the first 500

write_lines = []
count = 0
with open(READ_FILE_PATH, 'r', encoding='utf-8') as file:
    for line in file:
        if '"full_text" : ' in line:
            tweet = line.strip().replace('\n', ' ').replace('"full_text" : ', '')[1:-2] # kinda hacky lol
            write_lines.append('{"messages": [{"role": "system", "content": ""}, {"role": "user", "content": ""}, {"role": "assistant", "content": "' 
                               + tweet 
                               + '"}]}')
            count += 1

            if count == N_TWEETS:
                break

with open(WRITE_FILE_PATH, 'w', encoding='utf-8') as file:
    for line in write_lines:
        file.write(f"{line}\n")