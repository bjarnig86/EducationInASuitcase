# Rafmyntir - Lokaverkefni

## Einar og Bjarni

Lokaverkefni unnið af Einari Páli Pálssyni (epp5@hi.is) og Bjarna Guðmundssyni (bjg17@hi.is)

Þetta verkefni hefur það að markmiði að koma gögnum sem finna má á [libraries.tutor-web](https://libraries.tutor-web.net/) í gagnagrunn og gera notendum af verkefninu kleift að komast í og birta þessi gögn á fjölbreyttan hátt. Þessi gögn eru samkvæmt Gunnari Stefánssyni unnin upp úr nokkrum gagnagrunnum og birt í töfluformi á ofangreindri síðu.

Verkefninu er skipt upp í tvo hluta, annars vegar sá hluti sem uppfærir gagnagrunninn, köllum þann hluta Gagnagrunnsvirknin, og hinsvegar sá hluti sem gerir notendum kleift að sækja gögnin, köllum þann hluta einfaldlega SmileyCoin Library API.

## Gagnagrunnsvirknin

Í verkefninu er skrá sem heitir `program.py` sem hefur það verkefni að sækja gögn á slóðina [https://libraries.tutor-web.net/tables/alltime.1M.txt](https://libraries.tutor-web.net/tables/alltime.1M.txt) og umbreyta þessi gögn í gagnagrunns hæft form. `program.py` skráin skal vera keyrð daglega og gögnin eru síðan vistuð í grunninn á eftirfarandi hátt.

### Gagnagrunnurinn

**History taflan:** Eftir að gögnunum hefur verið breytt í gagnagrunns hæft form eins og nefnt er hér að ofan eru gögnin borin saman við þau gögn sem nú þegar eru til staðar í gagnagrunninum. Ef breytingar finnast í samanburðinum þá er mismunurinn á gögnunum skráður í gagnagrunninn undir töfluheitinu History. Þessi tafla inniheldur allar breytingar sem eiga sér stað frá og með þeim degi sem verkefnið er sett í loftið.

**AllTime taflan:** Eftir að gögnunum hefur verið breytt í gagnagrunns hæft form eins og nefnt er hér að ofan þá og aðgerðirnar fyrir history töfluna eru einnig búnar er fyrri gögnum skiðt út fyrir nýju. Þessi tafla inniheldur því alltaf jafnmargar raðir og fjöldi bókasafna og inniheldur [töfluna](https://libraries.tutor-web.net/tables/alltime.1M.txt) eins og hún leggur sig.

**Library taflan:** Þessi tafla breytist aldrei og inniheldur einungis aukagögn um bókasöfnin. Um er að ræða aukagögn frá eftirfarandi slóð: [https://libraries.tutor-web.net/tables/mapdata.txt](https://libraries.tutor-web.net/tables/mapdata.txt). Þessi tafla er einungis notuð sem "auka" tafla við hinar tvær töflurnar í SmileyCoin Library API hluta verkefnisins.

## SmileyCoin Library API

Þessi hluti verkefnisins ser sá sem er sýnilegur öllum á slóðinni [https://mu8j82.deta.dev/docs](https://mu8j82.deta.dev/docs). Þessi hluti gerir notanda kleift að sækja þau bókasafnsgögn sem honum sýnist og fá þau í hendurnar á JSON formi sem er mjög vinsælt gagnaform fyrir vefsíður. Notanda gefst valkostur á að sækja öll bókasöfn, eitt tiltækt bókasafn, saga allra bókasafna eða saga tiltekinna bókasafna.

ATH: Til að verkefnið virki á sem bestan hátt þarf sá server sem hýsir SmileyCoin Library API að keyra crontab á skrá sem heitir `program.py`. Í okkar tilfelli, þar sem um var að ræða fría hýsingarlausn, var ekki hægt að gera slíkt. (Deta býður ekki upp á það). Þetta er mikilvægur partur af verkefninu en þar sem um er að ræða skólaverkefni er ekki til fjármagn til að hýsa server til að sjá um það að keyra `program.py` 24/7.
