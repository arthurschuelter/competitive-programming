class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        d = {}

        for c in s1:
            d[c] = 1 + d.get(c, 0)

        def verifyDict(di):
            for k, v in di.items():
                if v != 0:
                    return False
            return True

        d1 = d
        for i in range(n2):
            d1 = d.copy()

            if d1.get(s2[i], -1) < 0:
                continue
            
            d1[s2[i]] -= 1
            j = i+1
            while j < n2 and j - i < n1:
                if d1.get(s2[j], -1) < 0:
                    break

                d1[s2[j]] -= 1
                j += 1
            
            if (verifyDict(d1)):
                return True
            
        return False

import pytest

solution = Solution()

@pytest.mark.parametrize("s1, s2, expected", [
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False),
    ("adc", "dcda", True),
    ("hello", "ooolleoooleh", False),
    ("abc", "bbbca", True),
    ("abc", "cccccbabbbaaaa", True),
    ("paoolrbebsqumnolusfdaavvkdmyulelajnilqxsujdycieizlwvuwcnwfemijpyixbjamphkufjfvfvjvdjbdkthlxrtyahuifdjqlvpvccajaosgffminewnhyzymgvwbsgirfwnjszjswffrolsuupwkiwjjtbcgqbyarskbyxdigcusygjpvdcubzmmpfzzwhuwibivbxjklpptfryfbamafxuzpzagivenlctomtcymlmkbzozyncdwvabqjvvzuwivzfjcqhrixwinyxqsnckkhjmfsomdkujzecihamydgkyntwztemhawvxpahtiwrjwysrzmrhwxkbazynwmgtyclyjqsrfkddjdmvxhtwnvxrlxfxnpyevsafmqmbvbnueqxegkcuwzwdmqqpdlegyrjhgytgfxtzagazguoadzycnwwhdlkogbzrwiwjxxvlpvxfbtrxtqahcfrbzixqyftlddwmwtorfvjzenksaukrevkddgnafwqtgsizisktrrmqvkeagjngtngqiithdxxefqpcdwmglvvjerwcwitdzlsozczimmbwxwvpccjyemhyyekruqejgrnhpfnxiodwmworpenustqtaswegjordqwqmdsmgbpxytptvnwtjmxwhfsnszscafeiyyuikthfnzcoassldzlkdgclyezsquhksisjvmcsxlwdpplwrwxthuipsjjfhtfqhcrnfcomnkbthyvhaelbtsyhrmjharxzhymxxbcwtxansrcwqsgzzdxzcqbphtccnjhikhhovezgbkgcwkavkrbydyctgizqferucmghsihyxgbpmehtwpwcwunitcrgdmcnodipruqegudtkluswpnvbdqyukspwvgchexiaxuebqfvitnmukebchkzmtnwcuymbnmyqgmzefnelwqnhleaadekwjehlkydpuwybendymsluptckrvbglxmamohiyszwkslittmdbfmxkmqomxfuskubytbgfvnlebmzxcsreqnjuctcjriszjpojywsitudelqljtufsbxmnykadnryjz", "pwjurfxfwxotemsiyitndgrtvzksgniyqolgwfhofhmnwmxbmphratrwdskjwutemrzivnndkxfmzzpenueyiztqcydbeftbuobqwyazibaettbqbueeaiayutaoqvmckemxhrecvptegifgemdsjkepzsedvkfixtvikviadomqsrwowftrnqdumlabwtbfsxkoytkgznmkfzbtntumlbjhxeaoxbuoshxsjnosnsrtzrtcqdifbiyvmrbwteajksskklrpkmbylwwprapfdhujoigcrqhtgtwolwjmoudnzlnmpnchwslpibwvffbcbbefpvfygnpluzyjrqipupidoxtgglbvnxmtzjaglglpkryudoskkyspuxmxrkmcxkueluiuvxsdwkorxgjikyoniicljvddfgfuhujplkakjnvskuozvmmavmyzdgzbohjrnfvsslyarxscfxscijsyhcqxnceqfavyzofvysilqdnpjypgtpjatklrnzhkygyfoaupibuqtuxbfsfcawiiulgohigutukhywypthyymvcabnsdsjtrdrtmifarhrcimzrpcbdfjtpwqsndlpiuletacqcccpnziupvclsinkdffnojfrvgypdajujzkdixugrbhqmwyjztfvvokmgdrbfmrdprmzoslldcssvkofxqsdrwapobietvmoonfipeejlgtuvpcbcfnsmupwjsgliheexediefcfrglliqoxjjsdjtpehqmkxkvkkflhwbvohryjpfgebcvkjqtcetxzhtfysomusfzsztqweekxbdcruwjgpdrwokseyaqznhihjulevycglkuacfgzlargjoquxoupfrhdegpqzrshmbierjjvzsdwsibinlrslimfgrsaacxijthbzmxnyuslffnfxziudxcdwfwnkmdeucbyydkhqkestxzvdraxjjcuzdgayabmxsltqdnsikxaasugkcovnvwfxiuozaphegpkhtmtqxxmwhrtblrtxvrtidkcluorcrksklgmismylsrwwtlhlnqnqlfmmefzltunpqozqpnxhtqvpovckbiaaejtwejjuuzmtargntaqehigzibxfczkwcthqijyhcdtupeqbtnnorrgmktlsgjortvsgjhrgzccgvlfjeqjfywufbqwnerpzxlnczxwjttiiokqfigqhgqaatzwynivuhpukuzgsijrfpganfroohnruzlijwinapnemwsxveqfremhwqwqwhxlmvfsnuglnkkqynvflxgdqayxpklerojawlidelttqlfvfmjoiwhylwrillyjjoxrfkayddfeytomjphsgzzbgxhbgdwonzrqrcbnrztgvoodyxrzbinqgeaptvyfkdizuzbxdiulvfqlsllkxkvmprritvhkdoghouifwpprblaeauyxyhlipccqjnorphmrelbsashkmmhnperidnmmizijbtfqkhgboniuphozbdgmlfieqjjpywvqggmsliocmvdkhxszrvqyjoxdvspqlljtbztjybmpwebavgmldxxohjfrmxpljszfjploblpsenjxqxdvmmwljoxmagpgxunlnoibvupfluyclemsywizdmrzchiujcqnlmcjkutxbzeibruvvknviojcflxfhyjhjkwerwgfowucgtyrimxiehdgwrifbpdaaqffgzssxiemrcyxpezijuyptdynatoivsqbkqbgutgmikqywkhcwhknunsnfsdkkhwwxvttohjwydlzihsjtwbzbtbemhssndaubxegtvinucugvvascicyfgqnhsidgcrrctjwrjjqbgcsfioebytsmalmnnnpznxcjlyvfykwsqbewxfgiazugkqdoggrjukpplsnaovwsliyiojnyhmiloyjkkwtrdcsyjxllfhvizydwlqlojidvzjylhzfvksneyduudibadamaoifenrvdduvljircjtlnohxxckjnfeiaagyqxyoyezloucybulpjrlhdwkdkagbukvjrkxjddpsahymtcfaivfaeioyynxykdacbloejpnnhtcxepzzuhzrnjrmpwvngrivioukkolckoskxjmjyzaqysaqbjevvqibbimxhehlkuyknwqkhfabgdnuwgzofmyetruzxszdcypmqouxyqyuvfvijircklyfifwbypgwbwvwrvxxmoyzdlpecfsbinlthrdnckqagstfgyzhduluvscnmmwzapxaraxcvkndddlfrcnzpkyhksxerhgaulwetciqaefwmmzdsqfldtouxlqqgrqsvksyrnspqmkiewwhrjkoahzpacgylikhnoswnsyzuvxzdrlxgcfflogzezkofstastmpvftshxvizunhsuakqqjscycfrqejprsogqzlkuskvnbgbjisbasgdjlmgpiklkhbfoaqjfrjmmtzfggyrsyymtfkuuqtrbvtnnzcaiuqjlgosortmyjqqzmadqgjijrofedppddtfdyijinvxehpbanizoqtowugvzflscmcfqelycotzwpwhxzmdsaxrwhgvlaookontbwunqfiuxarlztainztyooiuazebwmukvgcpvnkllkjoazejdmocpeuurhfarzjdybgxusmocaiaqxicgdorwdrvrrmjczfajbbmjnmvohjfsprufofokpaoolrbebsqumnolusfdaavvkdmyelelajniwqxsujdycieizlwviwcnwfcmijpyixbjamphkufkmvfvjvdjbdkthlxrtyahuifdjqlvpvccajaosgffminewnhyzymgvwbsgirfwnjszjswffkolsuupwkiwjjtbcgqbyarskbyxdigcusygjpvdcubzmmpfzzwhuwibivbxjklpptfryfbamafxuzpzagivenlctomtcymlmkbzozyncdwvabqjvvbuwivzfjcqhrixwinyxqsnckkhimfsomdkujtecihamydgkyntwztemhawvxpahtiwrjwysrzmrhwxkfazynwmgtyclyjqsrfkddjdmvxhzwnvxrlxfxnpyevsafmqmbvbnueqxegkcuwzidmqqpdlegyrjhgytgfxtzagazguoydzycnwwhdlkogbzrwiwjxxvlgvxfbtrxtqahcfrbzixqyftlddwmwtorfvjzenksaukrevkddgnafwqtgswzisktrrmqvkeagjngtnjqiithdxxefqpcdwmglvvjerwcwitdzlsozczimmbwxwvpccjyemhyyekruqejgrnhpfnxjodwmworpenustqoaswegjordqlqmdsmgbpxytptvnwtjmxwhfsnszscafeiyyuikthfnzcoassldzlkdgclyezsquhksisjvmcsxlwdpplwrwxthuupsjjfhtfqhcrnfcomnkbthyvhaelbtsyhrhjharxzhymxxbcwtxansrcwqsgzzdxzcqbpmtccnjhikhhovezgbkgcwkavkrbydyctgizqferucmghsihyxgbpmehtwpwewunitcrgdmcnodipruqegudtkluswpnvbdqyukspwvgchexiakuebqfvitnmukebchkzmtnwcuymbnmyqgfzefnelwqnhleaadekwjehljydpuwybendymsluptckrvbplxmamohiyszwrslittmdbfmxkmqtmxfusxubatbgfvnlebmzxcsruqnjuctcjriszjpogywsitudelqljtubszxmnykadnryjzhosyorgzvpzolmpbafnvcrrzfaxoqaulbcbnrucuydqbppnpgrdoyugbpiqdafccgordlqbwcgzirbbpaftoqtujqrljdqjrtwaqskcfqjqhvlgzbdmarajevjjrphkdzturmpqomzcewxxrpglsjehpfhmwmgeotxbswzswftewfchvxpqjyzlwwkxmssxpmdrtclakalcsgpwkvntjshydpvjauqilqkeyjojgehwwlattlhlgdgpotxhlrmffspdyxmjfonkzwdjkambqnwicehfzjvrxwsrbkztmtermdjjlaxlremdxnnfavmtclhvhesujoasmqonrjzlznywprupsfdafmuhunpigohenjnmpwdxcolvwuyptjigbihzcotxqjgskupqeomwlosbxqdjxwhmifbxzptjmvnfbpswtbjlmijpprzfelgzxbigrijgxlvmurzdvhxskpczyqrdelsyuqmfdxhzodxlhtsfxapwreaqtmzdhkibnwvsfsdolvwzwwjmgysrqfihakhhbbpfhbtvknsenzyvwyzudvvwgxjavcjyweomjfkucztlevmbbxqwznytbhdaowmecfkcfmiyvcfundeflybuifpvkvezezadmauwjzyfmdkxdvsfqkdkwydqhmmxfblfhnzqanonlmj", True),
])

def test_solution(s1, s2, expected):
    assert solution.checkInclusion(s1, s2) == expected

