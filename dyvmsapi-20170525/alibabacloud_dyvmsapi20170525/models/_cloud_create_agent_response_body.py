# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudCreateAgentResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudCreateAgentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CloudCreateAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudCreateAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        agent: main_models.CloudCreateAgentResponseBodyDataAgent = None,
        agent_skills: List[main_models.CloudCreateAgentResponseBodyDataAgentSkills] = None,
    ):
        # 座席配置信息
        self.agent = agent
        # 座席所需技能数组
        self.agent_skills = agent_skills

    def validate(self):
        if self.agent:
            self.agent.validate()
        if self.agent_skills:
            for v1 in self.agent_skills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()

        result['AgentSkills'] = []
        if self.agent_skills is not None:
            for k1 in self.agent_skills:
                result['AgentSkills'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = main_models.CloudCreateAgentResponseBodyDataAgent()
            self.agent = temp_model.from_map(m.get('Agent'))

        self.agent_skills = []
        if m.get('AgentSkills') is not None:
            for k1 in m.get('AgentSkills'):
                temp_model = main_models.CloudCreateAgentResponseBodyDataAgentSkills()
                self.agent_skills.append(temp_model.from_map(k1))

        return self

class CloudCreateAgentResponseBodyDataAgentSkills(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        cno: str = None,
        create_time: str = None,
        enterprise_id: str = None,
        id: str = None,
        skill_id: str = None,
        skill_level: str = None,
    ):
        # 座席id
        self.agent_id = agent_id
        self.cno = cno
        # 创建时间，格式: yyyy-MM-dd HH:mm:ss
        self.create_time = create_time
        # 企业编号
        self.enterprise_id = enterprise_id
        # queueSkill关系表中id
        self.id = id
        # skill的id
        self.skill_id = skill_id
        # 技能值
        self.skill_level = skill_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.id is not None:
            result['Id'] = self.id

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_level is not None:
            result['SkillLevel'] = self.skill_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillLevel') is not None:
            self.skill_level = m.get('SkillLevel')

        return self



class CloudCreateAgentResponseBodyDataAgent(DaraModel):
    def __init__(
        self,
        active: str = None,
        area_code: str = None,
        bind_tel: str = None,
        bind_tel_type: str = None,
        call_power: str = None,
        cno: str = None,
        create_time: str = None,
        enterprise_id: str = None,
        ib_record: str = None,
        id: str = None,
        is_asr: str = None,
        is_ob: str = None,
        is_quality_check: str = None,
        name: str = None,
        ob_clid: str = None,
        ob_clid_property: str = None,
        ob_clid_type: str = None,
        ob_record: str = None,
        power: str = None,
        status: str = None,
        webrtc_url_type: str = None,
        wrapup: str = None,
    ):
        # 是否启用，0：停用，1：启用，默认启用
        self.active = active
        # 区号格式
        self.area_code = area_code
        # 座席绑定电话
        self.bind_tel = bind_tel
        # 电话类型，1:固话 2:手机 3:分机 4:软电话
        self.bind_tel_type = bind_tel_type
        # 呼叫权限，0：无限制，1：国内长途，2：国内本市，3：内部呼叫，默认无限制
        self.call_power = call_power
        # 座席工号
        self.cno = cno
        # 创建时间，格式: yyyy-MM-dd HH:mm:ss
        self.create_time = create_time
        # 企业编号
        self.enterprise_id = enterprise_id
        # 呼入是否录音，0：不录用，1：录音，默认录音
        self.ib_record = ib_record
        # 座席id
        self.id = id
        # 是否开启ASR转写：0：不开启，1：开启，默认不开启
        self.is_asr = is_asr
        # 是否允许外呼，0：不允许，1：可以，默认允许
        self.is_ob = is_ob
        self.is_quality_check = is_quality_check
        # 座席姓名
        self.name = name
        # 外显号码
        self.ob_clid = ob_clid
        # 外显规则属性，JSON格式
        self.ob_clid_property = ob_clid_property
        # 外显规则 1：企业默认 2：随机 3：按区号 4：动态外显
        self.ob_clid_type = ob_clid_type
        # 外呼是否录音，0：不录音，1：录音，默认录音
        self.ob_record = ob_record
        # 1：班长席，0：普通座席，默认普通座席
        self.power = power
        # 座席状态，0:离线，1：在线
        self.status = status
        # webrtc软电话返回地址，0：企业默认 1：公网域名 2：专线域名 3：公网IP 4：专线IP
        self.webrtc_url_type = webrtc_url_type
        # 整理时间，秒数，默认10秒
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

        if self.bind_tel is not None:
            result['BindTel'] = self.bind_tel

        if self.bind_tel_type is not None:
            result['BindTelType'] = self.bind_tel_type

        if self.call_power is not None:
            result['CallPower'] = self.call_power

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.ib_record is not None:
            result['IbRecord'] = self.ib_record

        if self.id is not None:
            result['Id'] = self.id

        if self.is_asr is not None:
            result['IsAsr'] = self.is_asr

        if self.is_ob is not None:
            result['IsOb'] = self.is_ob

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

        if self.power is not None:
            result['Power'] = self.power

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('BindTel') is not None:
            self.bind_tel = m.get('BindTel')

        if m.get('BindTelType') is not None:
            self.bind_tel_type = m.get('BindTelType')

        if m.get('CallPower') is not None:
            self.call_power = m.get('CallPower')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('IbRecord') is not None:
            self.ib_record = m.get('IbRecord')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsAsr') is not None:
            self.is_asr = m.get('IsAsr')

        if m.get('IsOb') is not None:
            self.is_ob = m.get('IsOb')

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

        if m.get('Power') is not None:
            self.power = m.get('Power')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WebrtcUrlType') is not None:
            self.webrtc_url_type = m.get('WebrtcUrlType')

        if m.get('Wrapup') is not None:
            self.wrapup = m.get('Wrapup')

        return self

