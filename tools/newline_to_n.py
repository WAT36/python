import sys

# テキストファイルを入力して文中の改行を全て'¥n'に置換して別ファイルに書き込んで出力させるスクリプト
# 途中で区切りたい時は入力するテキストファイル中の区切りたい行を'---'とさせる
# 個人ツールの前処理用として作成

#入力ファイル名と出力ファイル名を引数にとる
files=sys.argv

if len(files) != 3:
    print("Error. Argument is no valid. Usage:python newline_to_n.py [inputfile] [outputfile]")
    sys.exit(1)

input_file=files[1]
output_file=files[2]

#"---"を境として、その間の内容を１行となるようにして読み取る
indata=""
sentence_i="¥n"
sentences=[]
with open(input_file,'r') as f:
    for fline in f:
        indata=fline
        indata=indata.replace('\n','¥n')
        indata=indata.replace("'",'_')
        if(indata=="---¥n"):
            sentences.append(sentence_i)
            sentence_i="¥n"
        else:
            sentence_i+=indata
    else:
        sentences.append(sentence_i)
        sentence_i="¥n"

#読み取った内容を１行ずつ書き込む
with open(output_file,'w') as f:
    f.write('\n'.join(sentences))