# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class AgentCallListResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        message: str = None,
        model: main_models.AgentCallListResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
        timestamp: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success
        self.timestamp = timestamp

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.AgentCallListResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class AgentCallListResponseBodyModel(DaraModel):
    def __init__(
        self,
        list: List[main_models.AgentCallListResponseBodyModelList] = None,
        page_no: int = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.AgentCallListResponseBodyModelList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class AgentCallListResponseBodyModelList(DaraModel):
    def __init__(
        self,
        agent_extension: str = None,
        agent_id: int = None,
        agent_speaking_duration: int = None,
        agent_speaking_time: str = None,
        agent_tag: str = None,
        answer_time: str = None,
        batch_id: str = None,
        call_begin_time: str = None,
        call_id: str = None,
        call_type: int = None,
        chat_record: str = None,
        hangup_time: str = None,
        hangup_type: int = None,
        import_time: str = None,
        individual_tag: str = None,
        intent_description: str = None,
        intent_tag: str = None,
        intercept_reason: str = None,
        keywords: str = None,
        number: str = None,
        number_md5: str = None,
        properties: str = None,
        remark: str = None,
        ring_time: int = None,
        sms: str = None,
        speaking_duration: int = None,
        speaking_time: str = None,
        speaking_turns: str = None,
        status_code: int = None,
        status_description: str = None,
        tag: str = None,
        task_id: int = None,
        template_id: int = None,
        transfer_status: str = None,
        transfer_status_code: int = None,
        transfer_time: str = None,
    ):
        # 坐席分机
        self.agent_extension = agent_extension
        # 分配坐席ID
        self.agent_id = agent_id
        # 坐席通话时长，单位：秒
        self.agent_speaking_duration = agent_speaking_duration
        # 坐席通话时长，单位：大于1分钟，显示分钟秒，小于1分钟，显示秒
        self.agent_speaking_time = agent_speaking_time
        # 坐席标签
        self.agent_tag = agent_tag
        # 接通时间 格式：2019-11-23 14:47:06
        self.answer_time = answer_time
        # 导入号码时返回的批次号
        self.batch_id = batch_id
        # 开始通话时间, 格式：2019-11-23 14:47:06
        self.call_begin_time = call_begin_time
        # 外呼ID
        self.call_id = call_id
        # 可选项：1001：坐席-人工外呼，1002：坐席-AI外呼-不转人工，1003：坐席-AI外呼-接通转人工，1004：坐席-AI外呼-智能转人工；
        self.call_type = call_type
        # 对话录音
        self.chat_record = chat_record
        # 挂断时间 格式：2019-11-23 14:47:06
        self.hangup_time = hangup_time
        # 挂机方式  AI挂机1，坐席挂机2，客户挂机3
        self.hangup_type = hangup_type
        # 导入时间,格式：2019-11-23 14:47:06
        self.import_time = import_time
        # 个性标签
        self.individual_tag = individual_tag
        # 意向说明 如：确认本人,未承诺还款
        self.intent_description = intent_description
        # 意向标签, 如“C”
        self.intent_tag = intent_tag
        # 拦截原因 当状态为已拦截时，可选值：黑名单拦截，灰名单拦截，异常号码拦截
        self.intercept_reason = intercept_reason
        # 回复关键词
        self.keywords = keywords
        # 外呼号码
        self.number = number
        # 外呼号码MD5
        self.number_md5 = number_md5
        # 导入号码时的参数值
        self.properties = properties
        # 人工备注信息
        self.remark = remark
        # 振铃时长 单位：毫秒
        self.ring_time = ring_time
        # 挂机短信 1:发送，2:不发送
        self.sms = sms
        # 通话时长 单位：秒
        self.speaking_duration = speaking_duration
        # 通话时长 单位：大于1分钟，显示分钟秒，小于1分钟，显示秒
        self.speaking_time = speaking_time
        # 对话轮次
        self.speaking_turns = speaking_turns
        # 外呼状态编码
        self.status_code = status_code
        # 外呼状态，如“已接听”“拒接”，转外呼状态编码与描述对应 1-已接听,2-关机
        self.status_description = status_description
        # 用户自定义标签
        self.tag = tag
        # 外呼任务ID
        self.task_id = task_id
        # AI话术ID
        self.template_id = template_id
        # 转人工状态 0-未触发
        self.transfer_status = transfer_status
        # 转人工状态编码
        self.transfer_status_code = transfer_status_code
        # 转接人工时间
        self.transfer_time = transfer_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_extension is not None:
            result['AgentExtension'] = self.agent_extension

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_speaking_duration is not None:
            result['AgentSpeakingDuration'] = self.agent_speaking_duration

        if self.agent_speaking_time is not None:
            result['AgentSpeakingTime'] = self.agent_speaking_time

        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag

        if self.answer_time is not None:
            result['AnswerTime'] = self.answer_time

        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.call_begin_time is not None:
            result['CallBeginTime'] = self.call_begin_time

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.chat_record is not None:
            result['ChatRecord'] = self.chat_record

        if self.hangup_time is not None:
            result['HangupTime'] = self.hangup_time

        if self.hangup_type is not None:
            result['HangupType'] = self.hangup_type

        if self.import_time is not None:
            result['ImportTime'] = self.import_time

        if self.individual_tag is not None:
            result['IndividualTag'] = self.individual_tag

        if self.intent_description is not None:
            result['IntentDescription'] = self.intent_description

        if self.intent_tag is not None:
            result['IntentTag'] = self.intent_tag

        if self.intercept_reason is not None:
            result['InterceptReason'] = self.intercept_reason

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.number is not None:
            result['Number'] = self.number

        if self.number_md5 is not None:
            result['NumberMD5'] = self.number_md5

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.ring_time is not None:
            result['RingTime'] = self.ring_time

        if self.sms is not None:
            result['Sms'] = self.sms

        if self.speaking_duration is not None:
            result['SpeakingDuration'] = self.speaking_duration

        if self.speaking_time is not None:
            result['SpeakingTime'] = self.speaking_time

        if self.speaking_turns is not None:
            result['SpeakingTurns'] = self.speaking_turns

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.status_description is not None:
            result['StatusDescription'] = self.status_description

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.transfer_status is not None:
            result['TransferStatus'] = self.transfer_status

        if self.transfer_status_code is not None:
            result['TransferStatusCode'] = self.transfer_status_code

        if self.transfer_time is not None:
            result['TransferTime'] = self.transfer_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentExtension') is not None:
            self.agent_extension = m.get('AgentExtension')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentSpeakingDuration') is not None:
            self.agent_speaking_duration = m.get('AgentSpeakingDuration')

        if m.get('AgentSpeakingTime') is not None:
            self.agent_speaking_time = m.get('AgentSpeakingTime')

        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')

        if m.get('AnswerTime') is not None:
            self.answer_time = m.get('AnswerTime')

        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('CallBeginTime') is not None:
            self.call_begin_time = m.get('CallBeginTime')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('ChatRecord') is not None:
            self.chat_record = m.get('ChatRecord')

        if m.get('HangupTime') is not None:
            self.hangup_time = m.get('HangupTime')

        if m.get('HangupType') is not None:
            self.hangup_type = m.get('HangupType')

        if m.get('ImportTime') is not None:
            self.import_time = m.get('ImportTime')

        if m.get('IndividualTag') is not None:
            self.individual_tag = m.get('IndividualTag')

        if m.get('IntentDescription') is not None:
            self.intent_description = m.get('IntentDescription')

        if m.get('IntentTag') is not None:
            self.intent_tag = m.get('IntentTag')

        if m.get('InterceptReason') is not None:
            self.intercept_reason = m.get('InterceptReason')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('NumberMD5') is not None:
            self.number_md5 = m.get('NumberMD5')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RingTime') is not None:
            self.ring_time = m.get('RingTime')

        if m.get('Sms') is not None:
            self.sms = m.get('Sms')

        if m.get('SpeakingDuration') is not None:
            self.speaking_duration = m.get('SpeakingDuration')

        if m.get('SpeakingTime') is not None:
            self.speaking_time = m.get('SpeakingTime')

        if m.get('SpeakingTurns') is not None:
            self.speaking_turns = m.get('SpeakingTurns')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('StatusDescription') is not None:
            self.status_description = m.get('StatusDescription')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TransferStatus') is not None:
            self.transfer_status = m.get('TransferStatus')

        if m.get('TransferStatusCode') is not None:
            self.transfer_status_code = m.get('TransferStatusCode')

        if m.get('TransferTime') is not None:
            self.transfer_time = m.get('TransferTime')

        return self

