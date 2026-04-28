# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudGetAgentResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudGetAgentResponseBodyData = None,
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
            temp_model = main_models.CloudGetAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudGetAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        agent: List[main_models.CloudGetAgentResponseBodyDataAgent] = None,
    ):
        # 座席列表数组
        self.agent = agent

    def validate(self):
        if self.agent:
            for v1 in self.agent:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Agent'] = []
        if self.agent is not None:
            for k1 in self.agent:
                result['Agent'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent = []
        if m.get('Agent') is not None:
            for k1 in m.get('Agent'):
                temp_model = main_models.CloudGetAgentResponseBodyDataAgent()
                self.agent.append(temp_model.from_map(k1))

        return self

class CloudGetAgentResponseBodyDataAgent(DaraModel):
    def __init__(
        self,
        active: int = None,
        agent_type: int = None,
        area_code: str = None,
        asr_call_type: str = None,
        bind_tel: str = None,
        bind_tel_type: int = None,
        call_power: int = None,
        cno: str = None,
        comment: str = None,
        create_time: str = None,
        enterprise_id: int = None,
        ib_record: int = None,
        id: int = None,
        is_asr: int = None,
        is_axb_call: str = None,
        is_ob: int = None,
        is_ob_remember: str = None,
        login_time: str = None,
        mrcp_property: str = None,
        name: str = None,
        ob_clid: str = None,
        ob_clid_property: str = None,
        ob_clid_type: int = None,
        ob_record: int = None,
        permit_ob_preview_time: str = None,
        power: int = None,
        property: str = None,
        queue_list: List[str] = None,
        status: int = None,
        update_time: str = None,
        webrtc_url_type: str = None,
        wrapup: int = None,
    ):
        # 是否启用，0：停用，1：启用，默认启用
        self.active = active
        # 座席类型，1：电话座席，2：电脑座席，默认电话座席
        self.agent_type = agent_type
        # 区号格式
        self.area_code = area_code
        # 允许语音识别的通话类型，1:呼入 4：预览外呼 9：主叫外呼 5：预测外呼 2：webcall
        self.asr_call_type = asr_call_type
        # 座席绑定电话
        self.bind_tel = bind_tel
        # 电话类型，1:固话 2:手机 3:分机 4:软电话
        self.bind_tel_type = bind_tel_type
        # 呼叫权限，0：无限制，1：国内长途，2：国内本市，3：内部呼叫，默认无限制
        self.call_power = call_power
        # 座席工号
        self.cno = cno
        # 备注
        self.comment = comment
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
        # 是否允许axb外呼，默认1开启 0关闭
        self.is_axb_call = is_axb_call
        # 是否允许外呼，0：不允许，1：可以，默认允许
        self.is_ob = is_ob
        # 外呼主叫记忆 1：开启 0：关闭
        self.is_ob_remember = is_ob_remember
        # 坐席最后一次登陆的时间
        self.login_time = login_time
        # 座席axb外呼是否使用mrcp方式推送语音流配置JSON Str格式数据
        self.mrcp_property = mrcp_property
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
        # 可外呼时间段用,号分割
        self.permit_ob_preview_time = permit_ob_preview_time
        # 1：班长席，0：普通座席，默认普通座席
        self.power = power
        # 座席主动挂机配置Json Str 格式数据 unLink 是否允许主动挂断, 0:关, 1:开，prohibitDuration禁止时长
        self.property = property
        # 坐席所属队列
        self.queue_list = queue_list
        # 座席状态，0:离线，1：在线
        self.status = status
        # 更新时间，格式: yyyy-MM-dd HH:mm:ss
        self.update_time = update_time
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

        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.area_code is not None:
            result['AreaCode'] = self.area_code

        if self.asr_call_type is not None:
            result['AsrCallType'] = self.asr_call_type

        if self.bind_tel is not None:
            result['BindTel'] = self.bind_tel

        if self.bind_tel_type is not None:
            result['BindTelType'] = self.bind_tel_type

        if self.call_power is not None:
            result['CallPower'] = self.call_power

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.comment is not None:
            result['Comment'] = self.comment

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

        if self.is_axb_call is not None:
            result['IsAxbCall'] = self.is_axb_call

        if self.is_ob is not None:
            result['IsOb'] = self.is_ob

        if self.is_ob_remember is not None:
            result['IsObRemember'] = self.is_ob_remember

        if self.login_time is not None:
            result['LoginTime'] = self.login_time

        if self.mrcp_property is not None:
            result['MrcpProperty'] = self.mrcp_property

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

        if self.permit_ob_preview_time is not None:
            result['PermitObPreviewTime'] = self.permit_ob_preview_time

        if self.power is not None:
            result['Power'] = self.power

        if self.property is not None:
            result['Property'] = self.property

        if self.queue_list is not None:
            result['QueueList'] = self.queue_list

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.webrtc_url_type is not None:
            result['WebrtcUrlType'] = self.webrtc_url_type

        if self.wrapup is not None:
            result['Wrapup'] = self.wrapup

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')

        if m.get('AsrCallType') is not None:
            self.asr_call_type = m.get('AsrCallType')

        if m.get('BindTel') is not None:
            self.bind_tel = m.get('BindTel')

        if m.get('BindTelType') is not None:
            self.bind_tel_type = m.get('BindTelType')

        if m.get('CallPower') is not None:
            self.call_power = m.get('CallPower')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

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

        if m.get('IsAxbCall') is not None:
            self.is_axb_call = m.get('IsAxbCall')

        if m.get('IsOb') is not None:
            self.is_ob = m.get('IsOb')

        if m.get('IsObRemember') is not None:
            self.is_ob_remember = m.get('IsObRemember')

        if m.get('LoginTime') is not None:
            self.login_time = m.get('LoginTime')

        if m.get('MrcpProperty') is not None:
            self.mrcp_property = m.get('MrcpProperty')

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

        if m.get('PermitObPreviewTime') is not None:
            self.permit_ob_preview_time = m.get('PermitObPreviewTime')

        if m.get('Power') is not None:
            self.power = m.get('Power')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('QueueList') is not None:
            self.queue_list = m.get('QueueList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('WebrtcUrlType') is not None:
            self.webrtc_url_type = m.get('WebrtcUrlType')

        if m.get('Wrapup') is not None:
            self.wrapup = m.get('Wrapup')

        return self

