# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudCreateAgentRequest(DaraModel):
    def __init__(
        self,
        active: int = None,
        area_code: str = None,
        call_power: int = None,
        cno: str = None,
        comment: str = None,
        enterprise_id: int = None,
        ib_record: int = None,
        is_asr: int = None,
        is_ob: int = None,
        is_ob_remember: str = None,
        is_quality_check: int = None,
        name: str = None,
        ob_clid: str = None,
        ob_clid_property: str = None,
        ob_clid_type: int = None,
        ob_record: int = None,
        owner_id: int = None,
        permit_ob_preview_time: str = None,
        power: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        skill_ids: str = None,
        skill_levels: str = None,
        webrtc_url_type: int = None,
        wrapup: int = None,
    ):
        # 是否激活；取值0或1，取值说明 0：不激活，1激活，默认激活
        self.active = active
        # 座席所属区号；区号格式
        # 
        # This parameter is required.
        self.area_code = area_code
        # 呼叫权限；取值说明 0：无限制，1：国内长途，2：国内本市，3：内部呼叫，默认无限制
        self.call_power = call_power
        # 座席工号；正整数，取值3-10位数字
        # 
        # This parameter is required.
        self.cno = cno
        # 备注
        self.comment = comment
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 呼入是否录音；取值说明 0：不录用，1：录音，默认录音
        self.ib_record = ib_record
        # 是否开启ASR转写；取值说明：0：不开启，1：开启，默认不开启
        self.is_asr = is_asr
        # 是否允许外呼；取值说明 0：不允许，1：可以，默认允许
        self.is_ob = is_ob
        # 外呼主叫记忆开关；取值说明：0：关闭 1：开启；默认开启
        self.is_ob_remember = is_ob_remember
        # 是否开启座席质检；取值说明：0：不开启，1：开启，默认开启
        self.is_quality_check = is_quality_check
        # 座席姓名；需进行UTF-8格式的URLEncode编码
        # 
        # This parameter is required.
        self.name = name
        # 透传号码；可传入企业中继号码或设置好的客户侧外显号码，当obClidType值为2或3时必选
        self.ob_clid = ob_clid
        # 外显属性；取值：{"isMatchCapital":0,"areaCodeRule":1,"isRandom":1}；obClidType=4时，isMatchCapital表示是否匹配省会号码，1是 0否，areaCodeRule表示区号匹配规则，1座席区号 2客户号码区号 ;isRandom 随机外显
        self.ob_clid_property = ob_clid_property
        # 外显规则；取值：1:默认 2:随机 3:按区号 4 动态外显 ，默认值为1
        self.ob_clid_type = ob_clid_type
        # 外呼是否录音；取值说明 0：不录音，1：录音，默认录音
        self.ob_record = ob_record
        self.owner_id = owner_id
        # 可外呼时间段；格式：08:00,20:00
        self.permit_ob_preview_time = permit_ob_preview_time
        # 座席权限；取值1或0，取值说明 1：班长席，0：普通座席，默认为0 普通座席
        self.power = power
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 所选的技能id；可选择多个，多个之间使用英文标点逗号间隔.例如:"1,2,3"；传入skillIds时，需要同时传入skillLevels
        self.skill_ids = skill_ids
        # 所选的技能的等级；值越小技能越高，多个间用英文标点逗号间隔。(与技能id相对应) 例如:"5,1,1"表示技能id为1的等级是5; 技能id为2的等级是1; 技能id为3的等级是1.
        self.skill_levels = skill_levels
        # webrtc软电话返回地址；取值说明：0：企业默认 1：公网域名 2：专线域名 3：公网IP 4：专线IP
        self.webrtc_url_type = webrtc_url_type
        # 整理时间；单位秒数，默认10秒
        self.wrapup = wrapup

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.area_code is not None:
            result['AreaCode'] = self.area_code

        if self.call_power is not None:
            result['CallPower'] = self.call_power

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.ib_record is not None:
            result['IbRecord'] = self.ib_record

        if self.is_asr is not None:
            result['IsAsr'] = self.is_asr

        if self.is_ob is not None:
            result['IsOb'] = self.is_ob

        if self.is_ob_remember is not None:
            result['IsObRemember'] = self.is_ob_remember

        if self.is_quality_check is not None:
            result['IsQualityCheck'] = self.is_quality_check

        if self.name is not None:
            result['Name'] = self.name

        if self.ob_clid is not None:
            result['ObClid'] = self.ob_clid

        if self.ob_clid_property is not None:
            result['ObClidProperty'] = self.ob_clid_property

        if self.ob_clid_type is not None:
            result['ObClidType'] = self.ob_clid_type

        if self.ob_record is not None:
            result['ObRecord'] = self.ob_record

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.permit_ob_preview_time is not None:
            result['PermitObPreviewTime'] = self.permit_ob_preview_time

        if self.power is not None:
            result['Power'] = self.power

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.skill_ids is not None:
            result['SkillIds'] = self.skill_ids

        if self.skill_levels is not None:
            result['SkillLevels'] = self.skill_levels

        if self.webrtc_url_type is not None:
            result['WebrtcUrlType'] = self.webrtc_url_type

        if self.wrapup is not None:
            result['Wrapup'] = self.wrapup

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')

        if m.get('CallPower') is not None:
            self.call_power = m.get('CallPower')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('IbRecord') is not None:
            self.ib_record = m.get('IbRecord')

        if m.get('IsAsr') is not None:
            self.is_asr = m.get('IsAsr')

        if m.get('IsOb') is not None:
            self.is_ob = m.get('IsOb')

        if m.get('IsObRemember') is not None:
            self.is_ob_remember = m.get('IsObRemember')

        if m.get('IsQualityCheck') is not None:
            self.is_quality_check = m.get('IsQualityCheck')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObClid') is not None:
            self.ob_clid = m.get('ObClid')

        if m.get('ObClidProperty') is not None:
            self.ob_clid_property = m.get('ObClidProperty')

        if m.get('ObClidType') is not None:
            self.ob_clid_type = m.get('ObClidType')

        if m.get('ObRecord') is not None:
            self.ob_record = m.get('ObRecord')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PermitObPreviewTime') is not None:
            self.permit_ob_preview_time = m.get('PermitObPreviewTime')

        if m.get('Power') is not None:
            self.power = m.get('Power')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SkillIds') is not None:
            self.skill_ids = m.get('SkillIds')

        if m.get('SkillLevels') is not None:
            self.skill_levels = m.get('SkillLevels')

        if m.get('WebrtcUrlType') is not None:
            self.webrtc_url_type = m.get('WebrtcUrlType')

        if m.get('Wrapup') is not None:
            self.wrapup = m.get('Wrapup')

        return self

