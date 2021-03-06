GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
PLACE_CHOICES = (
    ('01', '上海市'),
    ('02', '北京市'),
    ('03', '山东省'),
    ('04', '黑龙江省'),
    ('05', '吉林省'),
    ('06', '辽宁省'),
    ('07', '河北省'),
    ('08', '内蒙古自治区'),
    ('09', '天津市'),
    ('10', '山西省'),
    ('11', '陕西省'),
    ('12', '甘肃省'),
    ('13', '新疆维吾尔自治区'),
    ('14', '青海省'),
    ('15', '河南省'),
    ('16', '宁夏回族自治区'),
    ('17', '西藏自治区'),
    ('18', '四川省'),
    ('19', '湖北省'),
    ('20', '湖南省'),
    ('21', '江苏省'),
    ('22', '浙江省'),
    ('23', '安徽省'),
    ('24', '福建省'),
    ('25', '云南省'),
    ('26', '贵州省'),
    ('27', '广东省'),
    ('28', '广西壮族自治区'),
    ('29', '重庆市'),
    ('30', '海南省'),
    ('31', '江西省'),
    ('32', '境外')
)
PLACE_CHOICES_1 = (
    ('上海', '上海市'),
    ('北京', '北京市'),
    ('山东', '山东省'),
    ('黑龙江', '黑龙江省'),
    ('吉林', '吉林省'),
    ('辽宁', '辽宁省'),
    ('河内', '河北省'),
    ('内蒙古', '内蒙古自治区'),
    ('天津', '天津市'),
    ('山西', '山西省'),
    ('陕西', '陕西省'),
    ('甘肃', '甘肃省'),
    ('新疆', '新疆维吾尔自治区'),
    ('青海', '青海省'),
    ('海南', '河南省'),
    ('宁夏', '宁夏回族自治区'),
    ('西藏', '西藏自治区'),
    ('四川', '四川省'),
    ('湖北', '湖北省'),
    ('湖南', '湖南省'),
    ('江苏', '江苏省'),
    ('浙江', '浙江省'),
    ('安徽', '安徽省'),
    ('福建', '福建省'),
    ('云南', '云南省'),
    ('贵州', '贵州省'),
    ('广东', '广东省'),
    ('广西', '广西壮族自治区'),
    ('重庆', '重庆市'),
    ('海南', '海南省'),
    ('江西', '江西省'),
    ('境外', '境外')
)
visa_choices = (
    ('A', '一次入境签证'),
    ('B', '多次入境签证'),
)
duty_choices = (
        ('A', '所长'),
        ('B', '副所长'),
        ('C', '书记'),
        ('D', '无'),
)
identity_choices = (
        ('A', '研究员'),
        ('B', '副研究员'),
        ('C', '助理研究员'),
        ('D', '工程师'),
        ('E', '高级工程师'),
        ('F', '正高级工程师'),
        ('G', '博士后、在读学生'),
)
race_choices = (
        ('01', '汉族'),
        ('02', '满族'),
        ('03', '回族'),
        ('04', '藏族'),
        ('05', '壮族'),
        ('06', '其他'),
)
political_choices = (
        ('01', '中共党员'),
        ('02', '中共预备党员'),
        ('03', '共青团员'),
        ('04', '民革党员'),
        ('05', '民盟盟员'),
        ('06', '民建会员'),
        ('07', '民进会员'),
        ('08', '农工党党员'),
        ('09', '致公党党员'),
        ('10', '九三学社社员'),
        ('11', '台盟盟员'),
        ('12', '无党派人士'),
        ('13', '群众'),
)
securety_choices = (
        ('A', '绝密'),
        ('B', '机密'),
        ('C', '秘密'),
        ('D', '不涉密'),
)
health_choices = (
        ('A', '健康'),
        ('B', '一般'),
        ('C', '较差'),
)
delegation_choices = (
        ('A', '教学科研类团组'),
        ('B', '非教学科研类团组'),
)

delegation_tag_choices = (
        ('01', '合作研究'),
        ('02', '学术访问'),
        ('03', '出席国际会议'),
        ('04', '教学活动'),
        ('05', '科学观测'),
        ('06', '科学考察'),
        ('07', '科研仪器调试'),
        ('08', '科技展览'),
        ('09', '出席国际组织活动'),
        ('10', '人才招聘'),
        ('11', '其他'),
)


cash_choices=(
    (1, '美元'),
    (2, '欧元'),
    (3, '英镑'),
    (4, '日元'),
)

process_tag=(
    ('01', '填表'),
    ('02', '公示'),
    ('03', '申请表、arp所内审批'),
    ('04', 'arp院审批'),
    ('05', '护照留指纹'),
    ('06', '办理新护照'),
    ('07', '准备签证材料'),
    ('08', '签证过程中'),
    ('09', '申领外汇'),
    ('10', '执行出访任务'),
    ('11', '出访总结'),
    ('12', '事后公示'),
    ('13', '外汇核销'),
    ('14', '人民币报销'),
    ('15', '完结'),
)

unexpected_tag = (
    ('1', '正常'),
    ('2', '全团取消出访'),
    ('3', '部分成员取消出访'),
)