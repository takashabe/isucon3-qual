#!/bin/sh
mysql -uroot -proot isucon -e 'create index a on memos (is_private, created_at, id);'
mysql -uroot -proot isucon -e 'create index b on memos (user, created_at);'
mysql -uroot -proot isucon -e 'create index c on memos (user, is_private, created_at);'
