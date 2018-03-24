// 建表
use student 
create table S(SNO char(4),SNAME char(8),SEX char(2),AGE char(2),SDEPT char(10),LOGN char(20),PSWD char(20), primary key(SNO)) default charset utf8;
create table C(CNO char(4),CNAME char(20),CREDI int(11),CDEPT char(10),TNAME char(8), primary key(CNO)) default charset utf8;
create table SC(SNO char(4),CNO char(4),GRADE int(11), primary key(SNO, CNO), foreign key(CNO)references C(CNO), foreign key(SNO)references S(SNO)) default charset utf8;

insert into S values('S1','李铭','男','19','计算机软件','S1','S1');
insert into S values('S2','刘晓鸣','男','20','计算机应用','S2','S2');
insert into S values('S3','李明','男','22','计算机应用','S3','S3');
insert into S values('S4','张鹰','女','21','计算机软件','S4','S4');
insert into S values('S5','刘竟静','女','22','计算机软件','S5','S5');
insert into S values('S6','刘成刚','男','21','计算机软件','S6','S6');
insert into S values('S7','王铭','男','22','计算机应用','S7','S7');
insert into S values('S8','宣明尼','女','18','计算机应用','S8','S8');
insert into S values('S9','柳红利','女','19','计算机软件','S9','S9');

insert into C values('C1', 'PASCAL', 4, '计算机应用', '王晓名');
insert into C values('C2', '数据结构', 4, '计算机应用', '刘红');
insert into C values('C3', '离散数学', 4, '计算机应用', '李严劲');
insert into C values('C4', '计算机原理', 6, '计算机软件', '王晓名');
insert into C values('C5', '数据库原理', 4, '计算机应用', '吴志刚');
insert into C values('C6', 'Windows技术', 4, '计算机软件', '吴志刚');
insert into C values('C7', '编译原理', 4, '计算机软件', '蒋莹岳');
insert into C values('C8', '系统结构', 6, '计算机应用', '刘红');

insert into SC values('S1', 'C2', 56);
insert into SC values('S1', 'C4', 78);
insert into SC values('S1', 'C6', 66);
insert into SC values('S1', 'C8', 88);
insert into SC values('S3', 'C1', 88);
insert into SC values('S3', 'C2', 76);
insert into SC values('S4', 'C1', 67);
insert into SC values('S4', 'C2', 76);
insert into SC values('S4', 'C3', 67);
insert into SC values('S5', 'C1', 67);
insert into SC values('S5', 'C2', 78);
insert into SC values('S5', 'C3', 91);
insert into SC values('S6', 'C1', 78);
