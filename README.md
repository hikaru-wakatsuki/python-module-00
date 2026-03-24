*This project has been created as part of the 42 curriculum by hwakatsu.*

# Growing Code

## Description / 説明

### English
Growing Code is an introductory Python project focused on basic syntax and core programming concepts through community-garden examples. Its goal is to teach how simple functions work with printing, variables, user input, arithmetic, conditionals, loops, recursion, and a first explicit use of type annotations.

This repository contains eight exercises:

- `ex0/ft_hello_garden.py`: a first function that prints a greeting
- `ex1/ft_plot_area.py`: user input and arithmetic for plot area calculation
- `ex2/ft_harvest_total.py`: summing harvest values from multiple inputs
- `ex3/ft_plant_age.py`: conditional logic for harvest readiness
- `ex4/ft_water_reminder.py`: conditional reminder logic
- `ex5/ft_count_harvest_iterative.py`: counting with a loop
- `ex5/ft_count_harvest_recursive.py`: counting with recursion
- `ex6/ft_garden_summary.py`: collecting and displaying summary information
- `ex7/ft_seed_inventory.py`: parameterized output with type annotations

From the code in this repository, the project demonstrates:

- how to define simple functions
- how to receive user input and convert values
- how to use variables and arithmetic expressions
- how to make decisions with `if` / `else`
- how to repeat actions with iteration and recursion
- how to write a function signature with basic type annotations

### 日本語
Growing Code は、コミュニティガーデンを題材に Python の基本文法と中核概念を学ぶ入門プロジェクトです。目的は、print、変数、ユーザー入力、四則演算、条件分岐、ループ、再帰、そして最初の型アノテーションを使ったシンプルな関数の作り方を身につけることです。

このリポジトリには 8 つの exercise があります。

- `ex0/ft_hello_garden.py`: あいさつを表示する最初の関数
- `ex1/ft_plot_area.py`: 入力と四則演算による区画面積計算
- `ex2/ft_harvest_total.py`: 複数入力の合計計算
- `ex3/ft_plant_age.py`: 収穫可否を判断する条件分岐
- `ex4/ft_water_reminder.py`: 水やり判定の条件分岐
- `ex5/ft_count_harvest_iterative.py`: ループによるカウント
- `ex5/ft_count_harvest_recursive.py`: 再帰によるカウント
- `ex6/ft_garden_summary.py`: 入力内容をまとめて表示
- `ex7/ft_seed_inventory.py`: 型アノテーション付き引数を使った表示処理

このリポジトリの実装では、次の内容が確認できます。

- シンプルな関数定義の方法
- ユーザー入力の受け取りと値変換
- 変数と算術式の使い方
- `if` / `else` による条件判断
- iteration と recursion による繰り返し処理
- 基本的な type annotation を持つ関数シグネチャ

## Instructions / 実行方法

### English

Requirements:

- Python 3.10 or later
- No external dependencies

This project is written as individual function files. If you want to test them manually, import the function you need from Python or use the helper `main.py` mentioned in the subject if available in your local testing setup.

Example interactive testing:

```bash
python3 -c "from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()"
python3 -c "from ex7.ft_seed_inventory import ft_seed_inventory; ft_seed_inventory('tomato', 15, 'packets')"
```

Optional lint check:

```bash
flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6 ex7
```

There is no compilation or installation step. The exercises are plain Python functions intended to be imported and tested.

### 日本語

必要環境:

- Python 3.10 以上
- 外部依存関係なし

このプロジェクトは個別の関数ファイルとして書かれています。手動で試す場合は、Python から必要な関数を import して実行するか、課題文で案内されている `main.py` ヘルパーが手元にあればそれを使ってテストできます。

対話的なテスト例:

```bash
python3 -c "from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()"
python3 -c "from ex7.ft_seed_inventory import ft_seed_inventory; ft_seed_inventory('tomato', 15, 'packets')"
```

任意の lint チェック:

```bash
flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6 ex7
```

コンパイルやインストールは不要です。各 exercise は import してテストする前提のシンプルな Python 関数です。

## Features / 主な内容

### English

- Basic function definitions with direct input/output behavior
- Numeric input conversion with `int()`
- Arithmetic operations for area and totals
- Conditional branching for garden-state decisions
- Iterative and recursive counting
- A typed function signature in the final exercise

### 日本語

- 入出力を直接扱う基本的な関数定義
- `int()` を使った数値入力変換
- 面積計算や合計計算の算術処理
- ガーデン状態を判断する条件分岐
- iteration と recursion の両方によるカウント
- 最終 exercise における型付き関数シグネチャ

## Usage Overview / 使い方の概要

### English

- `ex0` to `ex2` focus on basic input, output, and arithmetic.
- `ex3` and `ex4` focus on conditional logic.
- `ex5` compares loop-based and recursive repetition.
- `ex6` formats multiple pieces of input into a report.
- `ex7` introduces explicit parameter typing and unit-based branching.

### 日本語

- `ex0` から `ex2` は基本的な入出力と算術処理に焦点があります。
- `ex3` と `ex4` は条件分岐に焦点があります。
- `ex5` は loop ベースと recursion ベースの繰り返しを比較します。
- `ex6` は複数の入力をまとめて表示します。
- `ex7` は明示的な引数型と unit ごとの分岐を導入します。

## Resources / 参考資料

### English

Classic references related to the topic:

- [Python Documentation: An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
- [Python Documentation: Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Documentation: Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Python Documentation: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Documentation: Type Hints](https://docs.python.org/3/library/typing.html)
- [Real Python: Python Basics](https://realpython.com/python-basics/)
- [Real Python: Recursion in Python](https://realpython.com/python-recursion/)
- [flake8 Documentation](https://flake8.pycqa.org/)

AI usage in this project:

- AI was used for documentation support and README drafting.
- It was used to inspect the repository structure, summarize the educational goal of each exercise, and provide bilingual English/Japanese wording.

### 日本語

この課題に関連する代表的な参考資料:

- [Python Documentation: An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
- [Python Documentation: Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Documentation: Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Python Documentation: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Documentation: Type Hints](https://docs.python.org/3/library/typing.html)
- [Real Python: Python Basics](https://realpython.com/python-basics/)
- [Real Python: Recursion in Python](https://realpython.com/python-recursion/)
- [flake8 Documentation](https://flake8.pycqa.org/)

このプロジェクトにおける AI の利用:

- AI はドキュメント補助と README 作成支援に使用しました。
- リポジトリ構造の確認、各 exercise の学習目的の要約、英語と日本語の文章作成に利用しました。

## Notes / 補足

### English
This project is intentionally simple and function-oriented. The important part is learning how small pieces of Python syntax work before moving on to larger class-based systems.

### 日本語
このプロジェクトは意図的にシンプルで、関数中心の構成になっています。重要なのは、より大きなクラスベース設計に進む前に、小さな Python 文法要素の働きを理解することです。
