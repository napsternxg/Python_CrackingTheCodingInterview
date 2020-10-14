vocab = "IVXLCDM"
values = [1, 5, 10, 50, 100, 500, 1000]
v2v = dict(zip(vocab, values))

def to_decimal(roman):
    decimal = 0
    prev = 0
    for d in roman:
        v = v2v[d]
        if prev and v > prev:
            v = v - 2*prev
        decimal += v
        prev = v2v[d]
    return decimal

if __name__ == "__main__":
  decimals = [to_decimal(roman) for roman in ["I", "II", "III", "IV"]]
  print(decimals)
  decimals = [to_decimal(roman) for roman in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]]
  print(decimals)
  decimals = [to_decimal(roman) for roman in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XIV", "XV", "XVI"]]
  print(decimals)
  decimals = [to_decimal(roman) for roman in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XIV", "XV", "XVI", "XX", "XXXIV", "XLVI"]]
  print(decimals)
  decimals = [to_decimal(roman) for roman in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XIV", "XV", "XVI", "XX", "XXXIV", "XLVI", "LXVI"]]
  print(decimals)
