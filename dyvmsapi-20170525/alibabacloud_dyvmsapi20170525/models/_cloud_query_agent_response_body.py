# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudQueryAgentResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudQueryAgentResponseBodyData = None,
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
            temp_model = main_models.CloudQueryAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudQueryAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        agents: List[main_models.CloudQueryAgentResponseBodyDataAgents] = None,
        total: int = None,
    ):
        # 座席列表数组
        self.agents = agents
        # 总数
        self.total = total

    def validate(self):
        if self.agents:
            for v1 in self.agents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Agents'] = []
        if self.agents is not None:
            for k1 in self.agents:
                result['Agents'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agents = []
        if m.get('Agents') is not None:
            for k1 in m.get('Agents'):
                temp_model = main_models.CloudQueryAgentResponseBodyDataAgents()
                self.agents.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class CloudQueryAgentResponseBodyDataAgents(DaraModel):
    def __init__(
        self,
        agent: main_models.CloudQueryAgentResponseBodyDataAgentsAgent = None,
        queue_list: List[main_models.CloudQueryAgentResponseBodyDataAgentsQueueList] = None,
    ):
        # 座席信息
        self.agent = agent
        # 座席所属队列信息
        self.queue_list = queue_list

    def validate(self):
        if self.agent:
            self.agent.validate()
        if self.queue_list:
            for v1 in self.queue_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()

        result['QueueList'] = []
        if self.queue_list is not None:
            for k1 in self.queue_list:
                result['QueueList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = main_models.CloudQueryAgentResponseBodyDataAgentsAgent()
            self.agent = temp_model.from_map(m.get('Agent'))

        self.queue_list = []
        if m.get('QueueList') is not None:
            for k1 in m.get('QueueList'):
                temp_model = main_models.CloudQueryAgentResponseBodyDataAgentsQueueList()
                self.queue_list.append(temp_model.from_map(k1))

        return self

class CloudQueryAgentResponseBodyDataAgentsQueueList(DaraModel):
    def __init__(
        self,
        announce_position: int = None,
        announce_position_frequency: int = None,
        announce_position_param: int = None,
        announce_position_youarenext: int = None,
        announce_sound: int = None,
        announce_sound_file: str = None,
        announce_sound_frequency: int = None,
        create_time: str = None,
        description: str = None,
        enterprise_id: int = None,
        id: int = None,
        join_empty: int = None,
        max_len: int = None,
        member_timeout: int = None,
        music_class: str = None,
        qno: str = None,
        queue_timeout: int = None,
        retry: int = None,
        say_agentno: bool = None,
        service_level: int = None,
        strategy: str = None,
        vip_support: int = None,
        weight: int = None,
        wrapup_time: int = None,
    ):
        # 位置播报 0关闭 1大于announce_position_param时播放 2小于等于announce_position_param时播放
        self.announce_position = announce_position
        # 位置播报周期，秒数
        self.announce_position_frequency = announce_position_frequency
        # 多余少余n个时播报，必须大于等于2
        self.announce_position_param = announce_position_param
        # 是否播报\\"您是下一位\\",0关闭，1开启
        self.announce_position_youarenext = announce_position_youarenext
        # 播报固定语音 0关闭 1打开
        self.announce_sound = announce_sound
        # 固定语音文件
        self.announce_sound_file = announce_sound_file
        # 播放固定语音周期，秒数
        self.announce_sound_frequency = announce_sound_frequency
        # 创建时间，格式: yyyy-MM-dd HH:mm:ss
        self.create_time = create_time
        # 队列名
        self.description = description
        # 企业编号
        self.enterprise_id = enterprise_id
        # 队列id
        self.id = id
        # 队列中为空时是否可以join，取值：1：置忙 2：通话中 4：振铃 8：无效 16：整理
        self.join_empty = join_empty
        # 最大等待数，设置范围0-999，0表示不做任何限制
        self.max_len = max_len
        # 座席超时时间，取值范围20-60秒，默认25秒
        self.member_timeout = member_timeout
        # 等待语音class
        self.music_class = music_class
        # 队列号
        self.qno = qno
        # 队列超时时间，取值范围5-600秒，默认600秒
        self.queue_timeout = queue_timeout
        # 座席超时无应答,呼叫下一座席的延迟秒数
        self.retry = retry
        # 语音报号，true:播报，false:不播报
        self.say_agentno = say_agentno
        # 服务水平秒数，低于此时间内接听的认为是高服务水平
        self.service_level = service_level
        # 呼叫策略：rrordered:技能优先 rrmemory:轮选 fewestcalls:平均 random:随机 linear:顺序 leastrecent:最长空闲时间
        self.strategy = strategy
        # 是否支持vip，1:支持，0:不支持
        self.vip_support = vip_support
        # 队列优先级，取值范围1-10，数值越高，优先级越高
        self.weight = weight
        # 整理时间，取值范围3-3600秒
        self.wrapup_time = wrapup_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.announce_position is not None:
            result['AnnouncePosition'] = self.announce_position

        if self.announce_position_frequency is not None:
            result['AnnouncePositionFrequency'] = self.announce_position_frequency

        if self.announce_position_param is not None:
            result['AnnouncePositionParam'] = self.announce_position_param

        if self.announce_position_youarenext is not None:
            result['AnnouncePositionYouarenext'] = self.announce_position_youarenext

        if self.announce_sound is not None:
            result['AnnounceSound'] = self.announce_sound

        if self.announce_sound_file is not None:
            result['AnnounceSoundFile'] = self.announce_sound_file

        if self.announce_sound_frequency is not None:
            result['AnnounceSoundFrequency'] = self.announce_sound_frequency

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.id is not None:
            result['Id'] = self.id

        if self.join_empty is not None:
            result['JoinEmpty'] = self.join_empty

        if self.max_len is not None:
            result['MaxLen'] = self.max_len

        if self.member_timeout is not None:
            result['MemberTimeout'] = self.member_timeout

        if self.music_class is not None:
            result['MusicClass'] = self.music_class

        if self.qno is not None:
            result['Qno'] = self.qno

        if self.queue_timeout is not None:
            result['QueueTimeout'] = self.queue_timeout

        if self.retry is not None:
            result['Retry'] = self.retry

        if self.say_agentno is not None:
            result['SayAgentno'] = self.say_agentno

        if self.service_level is not None:
            result['ServiceLevel'] = self.service_level

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        if self.vip_support is not None:
            result['VipSupport'] = self.vip_support

        if self.weight is not None:
            result['Weight'] = self.weight

        if self.wrapup_time is not None:
            result['WrapupTime'] = self.wrapup_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnouncePosition') is not None:
            self.announce_position = m.get('AnnouncePosition')

        if m.get('AnnouncePositionFrequency') is not None:
            self.announce_position_frequency = m.get('AnnouncePositionFrequency')

        if m.get('AnnouncePositionParam') is not None:
            self.announce_position_param = m.get('AnnouncePositionParam')

        if m.get('AnnouncePositionYouarenext') is not None:
            self.announce_position_youarenext = m.get('AnnouncePositionYouarenext')

        if m.get('AnnounceSound') is not None:
            self.announce_sound = m.get('AnnounceSound')

        if m.get('AnnounceSoundFile') is not None:
            self.announce_sound_file = m.get('AnnounceSoundFile')

        if m.get('AnnounceSoundFrequency') is not None:
            self.announce_sound_frequency = m.get('AnnounceSoundFrequency')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JoinEmpty') is not None:
            self.join_empty = m.get('JoinEmpty')

        if m.get('MaxLen') is not None:
            self.max_len = m.get('MaxLen')

        if m.get('MemberTimeout') is not None:
            self.member_timeout = m.get('MemberTimeout')

        if m.get('MusicClass') is not None:
            self.music_class = m.get('MusicClass')

        if m.get('Qno') is not None:
            self.qno = m.get('Qno')

        if m.get('QueueTimeout') is not None:
            self.queue_timeout = m.get('QueueTimeout')

        if m.get('Retry') is not None:
            self.retry = m.get('Retry')

        if m.get('SayAgentno') is not None:
            self.say_agentno = m.get('SayAgentno')

        if m.get('ServiceLevel') is not None:
            self.service_level = m.get('ServiceLevel')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('VipSupport') is not None:
            self.vip_support = m.get('VipSupport')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        if m.get('WrapupTime') is not None:
            self.wrapup_time = m.get('WrapupTime')

        return self

class CloudQueryAgentResponseBodyDataAgentsAgent(DaraModel):
    def __init__(
        self,
        active: str = None,
        agent_type: str = None,
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
        ob_clid_type: str = None,
        ob_record: str = None,
        power: str = None,
        status: str = None,
        webrtc_url_type: str = None,
        wrapup: str = None,
    ):
        # 是否启用，0：停用，1：启用，默认启用
        self.active = active
        # 座席类型，1：电话座席，2：电脑座席，默认电话座席
        self.agent_type = agent_type
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

        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

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

        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

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

