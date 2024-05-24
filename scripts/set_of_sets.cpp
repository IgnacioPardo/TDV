// Set of set implementation

#include <iostream>
#include <set>

using namespace std;

set<set<set<int>>> set_of_sets(set<int> s){
    set<set<set<int>>> res;

    if (s.size() == 0) {
        res.insert(set<set<int>>());
        return res;
    }

    int first = *s.begin();
    s.erase(s.begin());

    set<set<set<int>>> sub = set_of_sets(s);

    for (auto i : sub) {
        for (auto j : i) {
            j.insert(first);
        }
    }

    return sub;

}

int main() {
    set<int> s;
    s.insert(1);
    s.insert(2);
    s.insert(3);

    for (auto i : s) {
        cout << i << " ";
    }
    cout << endl;

    set<set<set<int>>> res = set_of_sets(s);
    cout << "Superset size: " << res.size() << endl;
    for (auto i : res) {
        cout << i.size() << endl;
        for (auto k : i) {
            cout << k.size() << endl;
            for (auto j : k) {
                cout << j << " ";
            }
            cout << endl;
        } 
    }
}
