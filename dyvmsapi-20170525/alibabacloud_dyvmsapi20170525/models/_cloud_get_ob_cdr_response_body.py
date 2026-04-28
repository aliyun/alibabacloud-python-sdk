# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudGetObCdrResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudGetObCdrResponseBodyData = None,
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
            temp_model = main_models.CloudGetObCdrResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudGetObCdrResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.CloudGetObCdrResponseBodyDataList] = None,
    ):
        # 座席外呼通话记录详情
        self.list = list

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.CloudGetObCdrResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        return self

class CloudGetObCdrResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        answer_time: str = None,
        call_id: str = None,
        call_type: str = None,
        call_type_code: str = None,
        callee_area_code: str = None,
        callee_number: str = None,
        clid: str = None,
        cno: str = None,
        display_number: str = None,
        end_reason: str = None,
        end_time: str = None,
        gno: str = None,
        id: str = None,
        join_queue_time: str = None,
        main_call_type: str = None,
        main_unique_id: str = None,
        qno: str = None,
        queue_name: str = None,
        record_file: List[str] = None,
        ringing_time: str = None,
        sip_cause: str = None,
        sip_cause_str: str = None,
        start_time: str = None,
        status: str = None,
        status_code: str = None,
        task_name: str = None,
        total_duration: str = None,
        trunk_group_key: str = None,
        tsi_file: str = None,
        unique_id: str = None,
        xnumber: str = None,
    ):
        self.agent_name = agent_name
        # 客户接听时间，时间戳，精确到s，如1480904471
        self.answer_time = answer_time
        # 通话唯一标识
        self.call_id = call_id
        # 呼叫类型 转移
        self.call_type = call_type
        # 呼叫类型编码，如102
        self.call_type_code = call_type_code
        # 被叫号码区号
        self.callee_area_code = callee_area_code
        # 呼叫的号码，可能是座席也可能是普通电话
        self.callee_number = callee_number
        # 外显号码
        self.clid = clid
        # 座席工号，如2000
        self.cno = cno
        # 客户侧真实外显号码，当使用AXB场景进行外呼时，客户侧真实外显号码为虚拟号
        self.display_number = display_number
        # 结束原因,接听之后的挂机原因 1000:主通道挂机 1001:非主通道挂机 1002:被强拆
        self.end_reason = end_reason
        # 电话结束时间，时间戳，精确到s，如1480904471
        self.end_time = end_time
        self.gno = gno
        # Id
        self.id = id
        # 入队列时间，时间戳，精确到s，如1480904471
        self.join_queue_time = join_queue_time
        # 主通话记录来电类型 主叫外呼
        self.main_call_type = main_call_type
        # 主外呼通话记录唯一标识
        self.main_unique_id = main_unique_id
        # 队列号
        self.qno = qno
        # 进入队列时间
        self.queue_name = queue_name
        self.record_file = record_file
        # 响铃时间，时间戳，精确到s，如1480904471
        self.ringing_time = ringing_time
        # SIP响应码：200 ~ 699
        self.sip_cause = sip_cause
        # 呼叫结果
        self.sip_cause_str = sip_cause_str
        # 呼叫客户时间，时间戳，精确到s，如1480904471
        self.start_time = start_time
        # 外呼结果，如接听
        self.status = status
        self.status_code = status_code
        self.task_name = task_name
        # 总通话时长秒数，单位是s
        self.total_duration = total_duration
        # 中继群组代号
        self.trunk_group_key = trunk_group_key
        # 号码状态识别录音文件名
        self.tsi_file = tsi_file
        # 从通道唯一标识
        self.unique_id = unique_id
        self.xnumber = xnumber

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.answer_time is not None:
            result['AnswerTime'] = self.answer_time

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.call_type_code is not None:
            result['CallTypeCode'] = self.call_type_code

        if self.callee_area_code is not None:
            result['CalleeAreaCode'] = self.callee_area_code

        if self.callee_number is not None:
            result['CalleeNumber'] = self.callee_number

        if self.clid is not None:
            result['Clid'] = self.clid

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.display_number is not None:
            result['DisplayNumber'] = self.display_number

        if self.end_reason is not None:
            result['EndReason'] = self.end_reason

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gno is not None:
            result['Gno'] = self.gno

        if self.id is not None:
            result['Id'] = self.id

        if self.join_queue_time is not None:
            result['JoinQueueTime'] = self.join_queue_time

        if self.main_call_type is not None:
            result['MainCallType'] = self.main_call_type

        if self.main_unique_id is not None:
            result['MainUniqueId'] = self.main_unique_id

        if self.qno is not None:
            result['Qno'] = self.qno

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.record_file is not None:
            result['RecordFile'] = self.record_file

        if self.ringing_time is not None:
            result['RingingTime'] = self.ringing_time

        if self.sip_cause is not None:
            result['SipCause'] = self.sip_cause

        if self.sip_cause_str is not None:
            result['SipCauseStr'] = self.sip_cause_str

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration

        if self.trunk_group_key is not None:
            result['TrunkGroupKey'] = self.trunk_group_key

        if self.tsi_file is not None:
            result['TsiFile'] = self.tsi_file

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        if self.xnumber is not None:
            result['XNumber'] = self.xnumber

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AnswerTime') is not None:
            self.answer_time = m.get('AnswerTime')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('CallTypeCode') is not None:
            self.call_type_code = m.get('CallTypeCode')

        if m.get('CalleeAreaCode') is not None:
            self.callee_area_code = m.get('CalleeAreaCode')

        if m.get('CalleeNumber') is not None:
            self.callee_number = m.get('CalleeNumber')

        if m.get('Clid') is not None:
            self.clid = m.get('Clid')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('DisplayNumber') is not None:
            self.display_number = m.get('DisplayNumber')

        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Gno') is not None:
            self.gno = m.get('Gno')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JoinQueueTime') is not None:
            self.join_queue_time = m.get('JoinQueueTime')

        if m.get('MainCallType') is not None:
            self.main_call_type = m.get('MainCallType')

        if m.get('MainUniqueId') is not None:
            self.main_unique_id = m.get('MainUniqueId')

        if m.get('Qno') is not None:
            self.qno = m.get('Qno')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RecordFile') is not None:
            self.record_file = m.get('RecordFile')

        if m.get('RingingTime') is not None:
            self.ringing_time = m.get('RingingTime')

        if m.get('SipCause') is not None:
            self.sip_cause = m.get('SipCause')

        if m.get('SipCauseStr') is not None:
            self.sip_cause_str = m.get('SipCauseStr')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')

        if m.get('TrunkGroupKey') is not None:
            self.trunk_group_key = m.get('TrunkGroupKey')

        if m.get('TsiFile') is not None:
            self.tsi_file = m.get('TsiFile')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        if m.get('XNumber') is not None:
            self.xnumber = m.get('XNumber')

        return self

