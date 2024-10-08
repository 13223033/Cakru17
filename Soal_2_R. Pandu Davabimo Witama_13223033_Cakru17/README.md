# Battle of Robots

Battle of Robots adalah game sederhana yang dibuat menggunakan Python, di mana pemain dapat memilih robot untuk bertarung melawan robot lain. Game ini menerapkan prinsip Object-Oriented Programming (OOP) dengan penggunaan kelas dan objek untuk mendefinisikan robot, pertarungan, dan logika game.

## Fitur

- Pemilihan robot untuk bertarung.
- Robot menyerang satu sama lain hingga salah satu robot kalah.
- Menampilkan hasil pertarungan, termasuk damage yang dilakukan dan health yang tersisa.

## Kelas

### 1. Robot

Kelas `Robot` merepresentasikan robot dalam permainan. Kelas ini memiliki atribut berikut:

- `name`: Nama robot.
- `health`: Hitpoints robot.
- `attack_power`: Kekuatan attack robot.

#### Metode

- `get_name()`: Mengembalikan nama robot.
- `get_health()`: Mengembalikan hitpoints robot saat ini.
- `is_alive()`: Memeriksa apakah robot masih hidup.
- `attack(other_robot)`: Menyerang robot lain dan mengurangi hitpointsnya.
- `take_damage(damage)`: Mengurangi hitpoints robot sesuai dengan damage yang diterima.

### 2. Battle

Kelas `Battle` mengelola pertarungan antara dua robot. Kelas ini memiliki atribut berikut:

- `robot1`: Robot pertama dalam pertarungan.
- `robot2`: Robot kedua dalam pertarungan.

#### Metode

- `start_fight()`: Memulai pertarungan antara kedua robot.
- `declare_winner()`: Mengumumkan pemenang dan yang kalah setelah pertarungan selesai.

### 3. Game

Kelas `Game` mengelola daftar robot yang tersedia untuk bertarung. Kelas ini memiliki atribut berikut:

- `robots`: Daftar robot yang ada dalam game.

#### Metode

- `add_robot(robot)`: Menambahkan robot ke dalam daftar.
- `start_game()`: Memulai game dan memungkinkan pemain untuk memilih dua robot untuk bertarung.
