import string, os

PATH = os.path.dirname(os.path.realpath(__file__))
MATHJAX_TEST_TEST_DIR = os.path.join(PATH, 'fixtures', 'MathJax')
MATHJAX_TEST_TEXT_DIR = os.path.join(MATHJAX_TEST_TEST_DIR, 'LaTeXToMathML-tex')
MATHJAX_TEST_OUT_DIR = os.path.join(MATHJAX_TEST_TEST_DIR, 'LaTeXToMathML-out')
MAGIC_LINE = "/* EVERYTHING BELOW IS AUTOGENERATED */\n"

template = string.Template("""void test_mathjax__$sanitized_name(void)
{
  fixture_tex = read_fixture_tex("MathJax/LaTeXToMathML-tex/$name.txt");
  fixture_mml = read_fixture_mml("MathJax/LaTeXToMathML-out/$name.html");
  mtex2MML_filter(fixture_tex, strlen(fixture_tex));
  result = mtex2MML_output();

  cl_assert_equal_s(fixture_mml, result);
} """)

fixtures = []
txt_count = xtex_count = no_tex_count = 0
for root, dirs, files in os.walk(MATHJAX_TEST_TEXT_DIR):
    for file in files:
        if file.endswith(".txt"):
            directory = os.path.basename(root)
            name = os.path.splitext(file)[0]
            fixtures.append(directory + "/" + name)
            txt_count += 1
        elif file.endswith(".xtex"):
            xtex_count += 1
        elif file.endswith(".no_tex"):
            no_tex_count += 1

test_file = open(os.path.join(PATH, "mathjax.c"),"r+")
test_file_lines = test_file.readlines()
test_file.seek(0)

autogenerated_index = test_file_lines.index(MAGIC_LINE)
test_file_lines = test_file_lines[:autogenerated_index + 1]

for fixture_name in fixtures:
    sanitized = fixture_name.replace('-', '').replace('/', '')
    test_file_lines.append("\n" + template.substitute(sanitized_name=sanitized, name=fixture_name) + "\n")

for line in test_file_lines:
    test_file.write(line)

test_file.truncate()
test_file.close()

#   done_count = Dir['test/fixtures/MathJax/LaTeXToMathML-tex/**/*.tex'].length
#   skipped_files = filter_array Dir['test/fixtures/MathJax/LaTeXToMathML-tex/**/*.xtex']
#   incomplete_files = filter_array Dir['test/fixtures/MathJax/LaTeXToMathML-tex/**/*.no_tex']
#
#   Dir['test/fixtures/MathJax/LaTeXToMathML-tex/**/*.tex'].each do |tex|
#     # next unless tex =~ /multline-1a.tex$/
#     define_method "test_#{tex}" do
#       tex_contents = File.read(tex)
#       outfile = tex.sub(MATHJAX_TEST_TEX_DIR + File::SEPARATOR, '').sub('.tex', '-ref.html')
#       outfile = File.join(MATHJAX_TEST_OUT_DIR, outfile)
#       expected = File.read(outfile)
#       actual = @mtex.filter(tex_contents)
#
#       write_to_test_file(actual)
#       assert_equal(actual.strip, expected.strip)
#     end
#   end
#
#   skipped_count = skipped_files.count
#   incomplete_file_count = incomplete_files.count
#   if skipped_count > 0
#     total = (done_count + skipped_count).to_f
#     coverage = done_count.fdiv(total) * 100
#     skipped_files = skipped_files.join("\n * ")
#     incomplete_files = incomplete_files.join("\n * ")
#     puts "\n\nNot doing the following #{incomplete_file_count} MathJax tests (because they're non-standard):\n\n * #{incomplete_files}"
#     puts "\n\nSkipping the following MathJax tests:\n\n * #{skipped_files}"
#     puts "\n\n*** You did #{done_count} and skipped #{skipped_count}: #{coverage.round(2)}% coverage ***"
#     puts "*** Tests last fetched: 3e882fd386 ***\n\n"
#   end
# end
