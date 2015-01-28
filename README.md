**I WILL NOT MANUALLY UPDATE THIS REPOSITORY ANYMORE**

If you want to add a router in the list, please make a pull-request, also remember to **USE THE POC** and paste the result in your pull-request.
Telnet clients and other solutions may not be relevant (some false negative / positive reported).

Some random code/data about the backdoor I found in my Linksys WAG200G (TCP/32764).

The backdoor may be present in other hardware, I'll update this readme accordingly. :)

Possible fix :
- if it's listening on the internet: add a firewall rule in the web UI ([@domainzero](https://twitter.com/domainzero/status/419146140999626752))
- it also seems to work on the LAN side. ([issue 35](https://github.com/elvanderb/TCP-32764/issues/35#issuecomment-31592308))
- but apparently, not for every body ([issue 57](https://github.com/elvanderb/TCP-32764/issues/57)) so use the PoC again after adding the rule to make sure the firewall does its job.
- install an open source firmware (for example OpenWRT or Tomato) this is NOT magical, OpenWAG200 is vuln: http://sourceforge.net/projects/openwag200/files/OpenWAG200/1.4/
- kill the backdoor after each reboot ([issue 61](https://github.com/elvanderb/TCP-32764/issues/61) & [TCP-32764-First-Aid](https://github.com/lahdekorpi/TCP-32764-First-Aid/))
- use this alternative firmware: [amod](http://alfie.altervista.org/amod/) (thank you [pidocchio](https://github.com/elvanderb/TCP-32764/issues/13#issuecomment-32546542) and [nremond](https://github.com/elvanderb/TCP-32764/issues/13#issuecomment-34008200))
- redirect the port traffic in your router firewall to a local unused IP and done (\[@osisecurite\])

Probable source of the backdoor: 
- SerComm https://news.ycombinator.com/item?id=6998258 (nice finding :) )
- Confirmed by a header ([socket_header.h](https://github.com/elvanderb/TCP-32764/blob/master/socket_header.h)) in [cisco gpl sources](ftp://ftp-eng.cisco.com/pub/opensource/smallbusiness/wap4410n/2.0.1.0/wap4410n_v2.0.1.0_gpl.tgz) (thank you Andreas Fett!)


Backdoor **LISTENING ON THE INTERNET** confirmed in :
- Linksys WAG120N ([@p_w999](https://twitter.com/p_w999/status/419444989051940864))
- Netgear DG834B V5.01.14 ([@domainzero](https://twitter.com/domainzero/status/419133964528263169))
- Netgear DGN2000 1.1.1, 1.1.11.0, 1.3.10.0, 1.3.11.0, 1.3.12.0 ([issue 44](https://github.com/elvanderb/TCP-32764/issues/44))
- Netgear WPNT834 ([issue 79](https://github.com/elvanderb/TCP-32764/issues/79))
- OpenWAG200 maybe a little bit TOO open ;) ([issue 49](https://github.com/elvanderb/TCP-32764/issues/49))

Backdoor confirmed in:
- Cisco RVS4000 fwv 2.0.3.2 & 1.3.0.5 ([issue 57](https://github.com/elvanderb/TCP-32764/issues/57))
- Cisco WAP4410N ([issue 11](https://github.com/elvanderb/TCP-32764/issues/11#issuecomment-31492435))
- Cisco WRVS4400N
- Cisco WRVS4400N ([issue 36](https://github.com/elvanderb/TCP-32764/issues/36))
- Diamond DSL642WLG / SerComm IP806Gx v2 TI (https://news.ycombinator.com/item?id=6998682)
- LevelOne WBR3460B (http://www.securityfocus.com/archive/101/507219/30/0/threaded)
- Linksys RVS4000 Firmware V1.3.3.5 ([issue 55](https://github.com/elvanderb/TCP-32764/issues/55))
- Linksys WAG120N ([issue 58](https://github.com/elvanderb/TCP-32764/issues/58))
- Linksys WAG160n v1 and v2 ([@xxchinasaurxx](https://twitter.com/xxchinasaurxx/status/418886166700507136) [@saltspork](https://twitter.com/saltspork/status/419450202362097664))
- Linksys WAG200G
- Linksys WAG320N (http://zaufanatrzeciastrona.pl/post/smieszna-tylna-furtka-w-ruterach-linksysa-i-prawdopodobnie-netgeara/)
- Linksys WAG54G2 ([@_xistence](https://twitter.com/_xistence/status/418616691040350208))
- Linksys WAG54GS ([@henkka7](https://twitter.com/henkka7/status/419210405399912448))
- Linksys WRT350N v2 fw 2.00.19 ([issue 39](https://github.com/elvanderb/TCP-32764/issues/39))
- Linksys WRT300N fw 2.00.17 ([issue 34](https://github.com/elvanderb/TCP-32764/issues/34))
- Netgear DG834[∅, GB, N, PN, GT] version < 5 ([issue 19](https://github.com/elvanderb/TCP-32764/issues/19) & [issue 25](https://github.com/elvanderb/TCP-32764/issues/25) & [issue 62](https://github.com/elvanderb/TCP-32764/issues/62) & jd & Burn2 Dev)
- Netgear DGN1000 (don't know if there is a difference with the others N150 ones... [issue 27](https://github.com/elvanderb/TCP-32764/issues/27))
- Netgear DGN1000[B] N150 ([issue 3](https://github.com/elvanderb/TCP-32764/issues/3))
- Netgear DGN2000B ([issue 26](https://github.com/elvanderb/TCP-32764/issues/26))
- Netgear DGN3500 ([issue 13](https://github.com/elvanderb/TCP-32764/issues/13))
- Netgear DGND3300 ([issue 56](https://github.com/elvanderb/TCP-32764/issues/56))
- Netgear DGND3300Bv2 fwv 2.1.00.53_1.00.53GR ([issue 59](https://github.com/elvanderb/TCP-32764/issues/59))
- Netgear DM111Pv2 ([@eguaj](https://twitter.com/eguaj/status/418143024019816448))
- Netgear JNR3210 ([issue 37](https://github.com/elvanderb/TCP-32764/issues/37))

Backdoor may be present in:
- all SerComm manufactured devices (https://news.ycombinator.com/item?id=6998258)
- Linksys WAG160N (http://zaufanatrzeciastrona.pl/post/smieszna-tylna-furtka-w-ruterach-linksysa-i-prawdopodobnie-netgeara/)
- Netgear DG934 probability: probability: 99.99% (http://codeinsecurity.wordpress.com/category/reverse-engineering/)
- Netgear WG602, WGR614 (v3 doesn't work, maybe others...) (http://zaufanatrzeciastrona.pl/post/smieszna-tylna-furtka-w-ruterach-linksysa-i-prawdopodobnie-netgeara/)

Backdoor is not working in:
- Belkin F5D7230-4 6000 (SerComm manufactured product) ([issue 51](https://github.com/elvanderb/TCP-32764/issues/51))
- Belkin F9K1002 v3 (SerComm manufactured product)
- Cisco E2000 fwv 1.0.02 ([issue 17](https://github.com/elvanderb/TCP-32764/issues/17))
- Cisco Linksys E4200 V1 fwv 1.0.05 ([issue 18](https://github.com/elvanderb/TCP-32764/issues/18))
- Cisco Linksys X2000 ([issue 40](https://github.com/elvanderb/TCP-32764/issues/40))
- Cisco EPC3925 
- Cisco RV082 v03 fw4.2.2.08 ([issue 94](https://github.com/elvanderb/TCP-32764/issues/94))
- Linksys E2500 ([@Antoniojojojo](https://twitter.com/Antoniojojojo/status/419493174227529728))
- Linksys E3000 fwv 1.0.04 ([issue 16](https://github.com/elvanderb/TCP-32764/issues/16))
- Linksys E3200 Firmware Version: 1.0.04 (Build 1)
- Linksys E4200 Firmware Version: 2.0.26 ([issue 53](https://github.com/elvanderb/TCP-32764/issues/53))
- Linksys RV082 v02 fw2.0.2.01-tm ([issue 94](https://github.com/elvanderb/TCP-32764/issues/94))
- Linksys WAG354G V.2 EU ([issue 69](https://github.com/elvanderb/TCP-32764/issues/69))
- Linksys WRT100 fwv 1.0.00 ([Issue 71](https://github.com/elvanderb/TCP-32764/issues/71))
- Linksys WRT110 fwv 1.0.07 ([issue 70](https://github.com/elvanderb/TCP-32764/issues/70))
- Linksys WRT120N fwv 1.0.07 ([@viniciuskmax](https://twitter.com/viniciuskmax/status/419886554245394432))
- Linksys WRT160Nv2 ([issue 43](https://github.com/elvanderb/TCP-32764/issues/43))
- Linksys WRT160Nv3 
- Linksys WRT320N ([issue 31](https://github.com/elvanderb/TCP-32764/issues/31))
- Linksys WRT54GL(v1.1) Firmware v4.30.16
- Linksys WRT54GS v1.52.8 build 001 (thanks Helmut Tessarek)
- Linksys WRT600N running 1.01.36 build 3 ([@shanetheclassic](https://twitter.com/shanetheclassic/status/419213153369485312) & [issue 46](https://github.com/elvanderb/TCP-32764/issues/46))
- Linksys WRT610N V1 fwv 1.00.03 B15 ([issue 60](https://github.com/elvanderb/TCP-32764/issues/60))
- Netgear CG3100 ([issue 6](https://github.com/elvanderb/TCP-32764/issues/6))
- Netgear CG3700EMR as provided by ComHem Sweden ([issue 20](https://github.com/elvanderb/TCP-32764/issues/20))
- Netgear DG834G v5 (manufactured by Foxconn as opposed to the previous versions, nice finding anthologist [issue 28](https://github.com/elvanderb/TCP-32764/issues/28))
- Netgear DGN2200Bv3 (V1.1.00.23_1.00.23) ([issue 41](https://github.com/elvanderb/TCP-32764/issues/41))
- Netgear DGN3500 (amod 9.3.1 based on official 1.1.00.34 - http://alfie.altervista.org/amod)
- Netgear DGND3700 ([issue 33](https://github.com/elvanderb/TCP-32764/issues/33))
- Netgear DGND4000 (V1.1.00.14_1.00.14) ([issue 67](https://github.com/elvanderb/TCP-32764/issues/67))
- Netgear ProSafe FVS318G fwv 3.1.1-14 (thank you Jason Leake :) )
- Netgear R4500 firmware V1.0.0.4_1.0.3 ([issue 64](https://github.com/elvanderb/TCP-32764/issues/64))
- Netgear R6300 ([issue 15](https://github.com/elvanderb/TCP-32764/issues/15))
- Netgear R7000 ([@LRFLEW](https://twitter.com/LRFLEW/status/418856141032935424))
- Netgear RP614v[4,2] V1.0.8_02.02 ([issue 22](https://github.com/elvanderb/TCP-32764/issues/22) & [issue 24](https://github.com/elvanderb/TCP-32764/issues/24))
- Netgear VMDG480 (aka. VirginMedia SuperHub) swv 2.38.01 ([issue 16](https://github.com/elvanderb/TCP-32764/issues/16))
- Netgear VMDG485 (aka. VirginMedia SuperHub 2) swv1.01.26 ([issue 16](https://github.com/elvanderb/TCP-32764/issues/16))
- Netgear WGR614v3 ([issue 8](https://github.com/elvanderb/TCP-32764/issues/8))
- Netgear WGR614v7 (thanks "Martin from germany" [your e-mail doesn't work])
- Netgear WGR614v9 ([issue 7](https://github.com/elvanderb/TCP-32764/issues/7))
- Netgear WN2500RP ([issue 15](https://github.com/elvanderb/TCP-32764/issues/15))
- Netgear WNDR3700 ([@juliengrenier](https://twitter.com/juliengrenier/status/418748575842304000))
- Netgear WNDR4000 ([issue 10](https://github.com/elvanderb/TCP-32764/issues/10))
- Netgear WNDR4500 ([@TechnicalRah](https://twitter.com/TechnicalRah/status/418826996873834496))
- Netgear WNR2000v3 ([issue 43](https://github.com/elvanderb/TCP-32764/issues/43))
- Netgear WNR3500L firmware V1.2.2.30_34.0.37 ([issue 65](https://github.com/elvanderb/TCP-32764/issues/65))
- Netgear WNR3500Lv2
- Sercomm AD81ABA

Some clarifications:
I didn't want to waste my time in writing a full report, it's a very simple backdoor that really doesn't deserve more than some crappy slides. Moreover, my English is quite bad.
 
I had a lot of fun in writing / drawing the slides, all the necessary information is in them.  If people don't understand them or find them "too full of meme" then - well - it's too bad for them. :)
