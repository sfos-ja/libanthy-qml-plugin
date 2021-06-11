# Anthy

## Build Anthy with Sailfish SDK

```bash
# configure SDK
PATH=$PATH:~/SailfishOS/bin/

export OS_VERSION=4.1.0.24
export ARCHITECTURE=aarch64

sfdk config "no-fix-version"
sfdk config "target=SailfishOS-${OS_VERSION}-${ARCHITECTURE}"

# build Anthy package
tar xf anthy-9100h.tar.gz && cd anthy-9100h
mkdir rpm
cp ../anthy.spec rpm

sfdk build --enable-debug

# install package to current SDK target
sfdk tools exec "SailfishOS-${OS_VERSION}-${ARCHITECTURE}" rpm -if $(pwd)/RPMS/anthy-9100h-2.aarch64.rpm
```

## Known issue

### Segmentation fault on mkdepgraph

`mkdepgraph` requires root permission in sb2, see [full sb2 log](https://gist.github.com/knokmki612/d5b548e30dbb281db013c762b99a0381)

```
1516194436.977 (8)	test.sh{sh}[10260]	EXEC: file:/srv/mer/targets/SailfishOS-2.1.3.7-i486/lib/ld-linux.so.2 argv:/srv/mer/targets/SailfishOS-2.1.3.7-i486/lib/ld-linux.so.2 --rpath-prefix /srv/mer/targets/SailfishOS-2.1.3.7-i486 --nodefaultdirs --argv0 depgraph/.libs/mkdepgraph /home/mersdk/libanthy-qml-plugin/anthy/anthy-9100h/depgraph/.libs/mkdepgraph	[preload/execgates.c:76]
1516194436.977 (5)	test.sh{sh}[10260]	EXEC: i_pid=10257 file='/srv/mer/targets/SailfishOS-2.1.3.7-i486/lib/ld-linux.so.2'	[preload/execgates.c:123]
1516194436.977 (8)	mkdepgraph[10260]	getenv(SBOX_MAPPING_LOGFORMAT)	[preload/privatewrappers.c:14]
1516194436.977 (5)	mkdepgraph[10260]	---------- Starting (2.3.90) [] ppid=10257 <depgraph/.libs/mkdepgraph> (Target) ----------	[sblib/sb_log.c:273]
1516194436.977 (8)	mkdepgraph[10260]	global vars initialized from env	[preload/libsb2.c:353]
1516194436.977 (8)	mkdepgraph[10260]	getenv(SBOX_SIGTRAP)	[preload/privatewrappers.c:14]
1516194436.977 (8)	mkdepgraph[10260]	getenv(__SB2_LD_PRELOAD)	[preload/privatewrappers.c:14]
1516194436.977 (8)	mkdepgraph[10260]	Revert env.var:Clear LD_PRELOAD	[preload/libsb2.c:272]
1516194436.977 (8)	mkdepgraph[10260]	unsetenv(LD_PRELOAD)	[preload/privatewrappers.c:39]
1516194436.977 (8)	mkdepgraph[10260]	sbox_find_next_symbol: unsetenv	[preload/libsb2.c:114]
1516194436.977 (8)	mkdepgraph[10260]	getenv(__SB2_LD_LIBRARY_PATH)	[preload/privatewrappers.c:14]
1516194436.977 (8)	mkdepgraph[10260]	Revert env.var:LD_LIBRARY_PATH=/home/mersdk/libanthy-qml-plugin/anthy/anthy-9100h/src-main/.libs:/home/mersdk/libanthy-qml-plugin/anthy/anthy-9100h/src-worddic/.libs: (__SB2_LD_LIBRARY_PATH)	[preload/libsb2.c:268]
1516194436.977 (8)	mkdepgraph[10260]	setenv(LD_LIBRARY_PATH)	[preload/privatewrappers.c:64]
1516194436.977 (8)	mkdepgraph[10260]	sbox_find_next_symbol: setenv	[preload/libsb2.c:114]
1516194436.977 (8)	mkdepgraph[10260]	sb2_preload_library_constructor: done	[preload/sb2context.c:211]
1516194436.977 (8)	mkdepgraph[10260]	sbox_find_next_symbol: getuid	[preload/libsb2.c:114]
1516194436.977 (8)	mkdepgraph[10260]	initialize_simulated_ids: Initializing UIDs from env: 1001 1001 1001 1001	[preload/vperm_uid_gid_gates.c:67]
1516194436.977 (8)	mkdepgraph[10260]	initialize_simulated_ids: Initializing GIDs from env: 100000 100000 100000 100000	[preload/vperm_uid_gid_gates.c:85]
1516194436.977 (8)	mkdepgraph[10260]	getuid: 1001	[preload/vperm_uid_gid_gates.c:251]
1516194436.977 (8)	mkdepgraph[10260]	pthread library not found	[sblib/sb2_pthread_if.c:102]
1516194436.977 (8)	mkdepgraph[10260]	sbox_map_path_internal__c_engine: fopen(/etc/passwd) class=0x1	[pathmapping/pathresolution.c:1264]
1516194436.977 (8)	mkdepgraph[10260]	getenv(SBOX_DISABLE_MAPPING)	[preload/privatewrappers.c:14]
1516194436.977 (8)	mkdepgraph[10260]	attach_ruletree(/tmp/sb2-mersdk-20180117-130712.d10114/RuleTree.bin)	[rule_tree/rule_tree.c:211]
1516194436.977 (8)	mkdepgraph[10260]	open_ruletree_file => 4	[rule_tree/rule_tree.c:125]
1516194436.977 (8)	mkdepgraph[10260]	ruletree mmap'ed ok	[rule_tree/rule_tree.c:152]
1516194436.977 (8)	mkdepgraph[10260]	rule tree file has been closed.	[rule_tree/rule_tree.c:237]
1516194436.977 (8)	mkdepgraph[10260]	attach_ruletree() => OK	[rule_tree/rule_tree.c:240]
1516194436.977 (8)	mkdepgraph[10260]	ruletree_to_memory: attach(/tmp/sb2-mersdk-20180117-130712.d10114/RuleTree.bin) = 0	[rule_tree/rule_tree.c:1265]
1516194436.977 (8)	mkdepgraph[10260]	sbox_map_path_internal__c_engine: process '/etc/passwd', n='/etc/passwd'	[pathmapping/pathresolution.c:1405]
1516194436.977 (8)	mkdepgraph[10260]	ruletree_get_rule_list_offs: rule list locations: fwd @23554, rev @81476	[pathmapping/paths_ruletree_mapping.c:249]
1516194436.977 (8)	mkdepgraph[10260]	ruletree_translate_path(/etc/passwd)	[pathmapping/paths_ruletree_mapping.c:772]
1516194436.977 (8)	mkdepgraph[10260]	map_to: /srv/mer/targets/SailfishOS-2.1.3.7-i486	[pathmapping/paths_ruletree_mapping.c:437]
1516194436.977 (8)	mkdepgraph[10260]	sbox_find_next_symbol: readlink	[preload/libsb2.c:114]
1516194436.977 (8)	mkdepgraph[10260]	ruletree_translate_path(/etc/passwd)	[pathmapping/paths_ruletree_mapping.c:772]
1516194436.977 (8)	mkdepgraph[10260]	map_to: /srv/mer/targets/SailfishOS-2.1.3.7-i486	[pathmapping/paths_ruletree_mapping.c:437]
1516194436.977 (5)	mkdepgraph[10260]	mapped: fopen '/etc/passwd' -> '/srv/mer/targets/SailfishOS-2.1.3.7-i486/etc/passwd' (readonly-if-not-root)	[pathmapping/pathlistutils.c:445]
1516194436.977 (8)	mkdepgraph[10260]	sbox_find_next_symbol: fopen	[preload/libsb2.c:114]
1516194436.977 (8)	mkdepgraph[10260]	vperm_multiopen: fileptr=fopen(path='/srv/mer/targets/SailfishOS-2.1.3.7-i486/etc/passwd',mode='rce')	[preload/vperm_filestatgates.c:1181]
1516194436.978 (5)	test.sh{sh}[10257]	waitpid: child 10260 terminated by signal 11	[preload/miscgates.c:638]
1516194436.978 (8)	test.sh{sh}[10257]	sbox_find_next_symbol: exit	[preload/libsb2.c:114]
1516194436.978 (5)	test.sh{sh}[10257]	exit: status=139	[preload/miscgates.c:582]
```
