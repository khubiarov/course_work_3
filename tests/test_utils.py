from utils import sort_func, date_correct_format, executed_data, choose_format

def test_choose_format():
    assert choose_format("MasterCard 8847384717023026") == "MasterCard 8847 38** **** 3026"
    assert choose_format("Счет 34799481846914116850") == 'Счет **6850'

def test_executed_data():
    test_data ="8.12.2019 Открытие вклада\nСчет **5907\n41096.24 USD\n"
    assert executed_data({
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  }) == test_data

def test_date_correct_format():
    assert date_correct_format("2019-05-06T00:17:42.736209") == "6.5.2019"
    assert date_correct_format('2025-07-31') == '31.7.2025'


def test_sort_func():
    assert sort_func([

        {
          "id": 441945886,
          "state": "EXECUTED",
          "date": "2019-08-26T10:50:58.294041",
          "operationAmount": {
            "amount": "31957.58",
            "currency": {
              "name": "руб.",
              "code": "RUB"
            }
          },
          "description": "Перевод организации",
          "from": "Maestro 1596837868705199",
          "to": "Счет 64686473678894779589"
        },
        {
          "id": 41428829,
          "state": "EXECUTED",
          "date": "2019-07-03T18:35:29.512364",
          "operationAmount": {
            "amount": "8221.37",
            "currency": {
              "name": "USD",
              "code": "USD"
            }
          },
          "description": "Перевод организации",
          "from": "MasterCard 7158300734726758",
          "to": "Счет 35383033474447895560"
        },
        {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
            "amount": "9824.07",
            "currency": {
              "name": "USD",
              "code": "USD"
            }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
        },
        {
          "id": 587085106,
          "state": "EXECUTED",
          "date": "2018-03-23T10:45:06.972075",
          "operationAmount": {
            "amount": "48223.05",
            "currency": {
              "name": "руб.",
              "code": "RUB"
            }
          },
          "description": "Открытие вклада",
          "to": "Счет 41421565395219882431"
        },
        {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  },
  {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  },
        {
    "id": 27192367,
    "state": "CANCELED",
    "date": "2018-12-24T20:16:18.819037",
    "operationAmount": {
      "amount": "991.49",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 71687416928274675290",
    "to": "Счет 87448526688763159781"
  }]
    ) == [{
          "id": 441945886,
          "state": "EXECUTED",
          "date": "2019-08-26T10:50:58.294041",
          "operationAmount": {
            "amount": "31957.58",
            "currency": {
              "name": "руб.",
              "code": "RUB"
            }
          },
          "description": "Перевод организации",
          "from": "Maestro 1596837868705199",
          "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },{
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  },
  {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  },{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
            "amount": "9824.07",
            "currency": {
              "name": "USD",
              "code": "USD"
            }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
        },
        {
          "id": 587085106,
          "state": "EXECUTED",
          "date": "2018-03-23T10:45:06.972075",
          "operationAmount": {
            "amount": "48223.05",
            "currency": {
              "name": "руб.",
              "code": "RUB"
            }
          },
          "description": "Открытие вклада",
          "to": "Счет 41421565395219882431"
        }
    ]

