Some random code/data about the backdoor I found in my Linksys WAG200G (TCP/32764).
If you don't understand something or want some details, feel free to fill an issue.

The backdoor may be present in other hardware, I'll update this readme accordingly :)

Probable source of the backdoor: 
- SerComm https://news.ycombinator.com/item?id=6998258 (nice finding :) )

Backdoor **LISTENING ON THE INTERNET** confirmed in :
- Netgear DG834B V5.01.14 (https://twitter.com/domainzero/status/419133964528263169)

Backdoor confirmed in:
- Linksys WAG200G
- Netgear DM111Pv2 (https://twitter.com/eguaj/status/418143024019816448)
- Linksys WAG320N  (http://zaufanatrzeciastrona.pl/post/smieszna-tylna-furtka-w-ruterach-linksysa-i-prawdopodobnie-netgeara/)
- Linksys WAG54G2 (https://twitter.com/_xistence/status/418616691040350208)
- DGN1000[B] Netgear N150 (https://github.com/elvanderb/TCP-32764/issues/3)
- NETGEAR DGN1000 (don't know if there is a difference with the others N150 ones... https://github.com/elvanderb/TCP-32764/issues/27)
- Netgear DG834G V2 firmware 4.01.40 (thanks Burn2 Dev)
- Diamond DSL642WLG / SerComm IP806Gx v2 TI (https://news.ycombinator.com/item?id=6998682)
- Linksys WAG120N (https://twitter.com/p_w999/status/418856260973252608/photo/1)
- Cisco WAP4410N (https://github.com/elvanderb/TCP-32764/issues/11#issuecomment-31492435)
- Linksys WAG160n (https://twitter.com/xxchinasaurxx/status/418886166700507136)
- LevelOne WBR3460B (http://www.securityfocus.com/archive/101/507219/30/0/threaded)
- Netgear DGN3500 (https://github.com/elvanderb/TCP-32764/issues/13)
- NetGear DG834 v3 (thanks jd)
- Netgear DG834[GB, N] version < 5 (https://github.com/elvanderb/TCP-32764/issues/19 https://github.com/elvanderb/TCP-32764/issues/25)
- Netgear DGN2000B (https://github.com/elvanderb/TCP-32764/issues/26)
- Linksys WRVS4400N (Firmware Version:V2.0.2.1) (https://github.com/elvanderb/TCP-32764/issues/29)

Backdoor may be present in:
- Netgear DG934 [probability: 99.99%] (http://codeinsecurity.wordpress.com/category/reverse-engineering/)
- Netgear WPNT834 (http://forum1.netgear.com/showthread.php?p=270354)
- Netgear WG602, WGR614 (v3 doesn't work, maybe others...), DGN2000 (http://zaufanatrzeciastrona.pl/post/smieszna-tylna-furtka-w-ruterach-linksysa-i-prawdopodobnie-netgeara/)
- Linksys WAG160N (http://zaufanatrzeciastrona.pl/post/smieszna-tylna-furtka-w-ruterach-linksysa-i-prawdopodobnie-netgeara/)
- all SerComm manufactured devices (https://news.ycombinator.com/item?id=6998258)

Backdoor is not working in:
- Netgear WGR614v7 (thanks "Martin from germany" [your e-mail doesn't work])
- Netgear WNDR3700 (https://twitter.com/juliengrenier/status/418748575842304000)
- Netgear CG3100 (https://github.com/elvanderb/TCP-32764/issues/6)
- Netgear WGR614v9 (https://github.com/elvanderb/TCP-32764/issues/7)
- Linksys WRT54GS v1.52.8 build 001 (thanks Helmut Tessarek)
- Linksys WRT54GL(v1.1) Firmware v4.30.16
- Netgear WGR614v3 (https://github.com/elvanderb/TCP-32764/issues/8)
- Netgear WNDR4500 (https://twitter.com/TechnicalRah/status/418826996873834496)
- Netgear WNDR4000 (https://github.com/elvanderb/TCP-32764/issues/10)
- Netgear R7000 (https://twitter.com/LRFLEW/status/418856141032935424)
- Netgear R6300 (https://github.com/elvanderb/TCP-32764/issues/15)
- Netgear WN2500RP (https://github.com/elvanderb/TCP-32764/issues/15)
- Linksys E3000 fwv 1.0.04 (https://github.com/elvanderb/TCP-32764/issues/16)
- Netgear VMDG480 (aka. VirginMedia SuperHub) swv 2.38.01 (https://github.com/elvanderb/TCP-32764/issues/16)
- Netgear VMDG485 (aka. VirginMedia SuperHub 2) swv1.01.26 (https://github.com/elvanderb/TCP-32764/issues/16)
- Cisco E2000 fwv 1.0.02 (https://github.com/elvanderb/TCP-32764/issues/17)
- Cisco Linksys E4200 V1 fwv 1.0.05 (https://github.com/elvanderb/TCP-32764/issues/18)
- NETGEAR CG3700EMR as provided by ComHem Sweden (https://github.com/elvanderb/TCP-32764/issues/20)
- Netgear RP614v[4,2] V1.0.8_02.02 (https://github.com/elvanderb/TCP-32764/issues/22 https://github.com/elvanderb/TCP-32764/issues/24)
- Netgear DG834G v5 (manufactured by Foxconn as opposed to the previous versions, nice finding anthologist https://github.com/elvanderb/TCP-32764/issues/28)
- NETGEAR WNR3500Lv2

Some clarifications:
I didn't want to lose my time in writing a full report, it's a very simple backdoor that really doesn't deserve more than some crappy slides. Moreover, my English is quite bad
 
I had a lot of fun in writing / drawing those slides, all the necessary informations are in them, if people don't understand them or find them "too full of meme" then - well - it's too bad for them :)
