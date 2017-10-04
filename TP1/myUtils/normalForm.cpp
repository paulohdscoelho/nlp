#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>

using namespace std;

void pFile(std::string name) {
  ifstream Infile(name.c_str());
  std::string nameOut = std::string();
  for (unsigned int i = 0, ie = name.size(); i != ie; i++) {
    if(name[i] == '.')
      nameOut += "_NFO";
    nameOut += name[i];
  }
  ofstream Outfile(nameOut.c_str());
  if (!Infile){
    return;
  }

  std::string Line = std::string();
  unsigned LineNo = 1;
  while (!Infile.eof()) {
    Line = std::string();
    std::getline(Infile, Line);
    for (unsigned int i = 0, ie = Line.size(); i != ie; i++) {
      if (Line[i] == '\n')
        continue;
      if (('A' <= Line[i]) && (Line[i] <= 'Z'))
        Line[i] = Line[i] + ('a' - 'A');
      if (('a' > Line[i]) || (Line[i] > 'z'))
        Line[i] = ' ';
    }
    Outfile << Line;
  }
  Infile.close();
  Outfile.close();
}

int main(int argc, char *argv[]) {
  if (argc != 2)
    return 1;
  string name(argv[1]);
  pFile(name);
  return 0;
}
