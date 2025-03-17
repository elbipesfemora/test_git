list_songs = input('Введите названия песен разделенные запятыми: ')
list_groups = input('Введите название исполнителей разделенные запятыми: ')

songs = [song.strip() for song in list_songs.split(',')]
groups = [group.strip() for group in list_groups.split(',')]

if len(songs) != len(groups):
    print("Ошибка: количество песен и исполнителей должно быть одинаковым.")
else:
    play_list = {}

for song, group in zip(songs, groups):
    if group not in play_list:
        play_list[group] = []
    play_list[group].append(song)

print('Плейлист:')
for i, (song, group) in enumerate(zip(songs, groups), start = 1):
    print(f'{i}. {song} - {group}')