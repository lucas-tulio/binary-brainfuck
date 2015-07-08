# binary-brainfuck

A variation of Brainfuck that uses binary numbers instead of punctuation.

### Usage

- Convert from Binary Brainfuck to Brainfuck:

`python bbf-to-bf.py inputfile`

The output file `out.b` will contain your Brainfuck code.

- Convert from Brainfuck to Binary Brainfuck:

`python bf-to-bbf.py inputfile`

The output file `out.bbf` will contain your Binary Brainfuck code.

### How Binary Brainfuck works:

Instead of using the punctuation characters you'd normally use in Brainfuck, you use these:

Brainfuck | Binary Brainfuck
`>` | `000`
`<` | `001`
`+` | `010`
`-` | `011`
`.` | `100`
`,` | `101`
`[` | `110`
`]` | `111`

So, "Hello World" in Binary Brainfuck would look something like this:

```
010010010010010010010010110000010010010010110000010010000010
010010000010010010000010001001001001011111000010000010000011
000000010110001111001011111000000100000011011011100010010010
010010010010100100010010010100000000100001011100001100010010
010100011011011011011011100011011011011011011011011100000000
010100000010010100
```
