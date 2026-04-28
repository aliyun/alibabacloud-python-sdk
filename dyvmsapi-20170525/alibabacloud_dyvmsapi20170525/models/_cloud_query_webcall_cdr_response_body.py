# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudQueryWebcallCdrResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudQueryWebcallCdrResponseBodyData = None,
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
            temp_model = main_models.CloudQueryWebcallCdrResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudQueryWebcallCdrResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.CloudQueryWebcallCdrResponseBodyDataList] = None,
    ):
        # webcall通话记录数组
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
                temp_model = main_models.CloudQueryWebcallCdrResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        return self

class CloudQueryWebcallCdrResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        answer_time: str = None,
        bridge_duration: str = None,
        bridge_time: str = None,
        call_id: str = None,
        call_type: str = None,
        callee_clid: str = None,
        callee_display_number: str = None,
        callee_number: str = None,
        callee_ringing_time: str = None,
        clid: str = None,
        cno: str = None,
        customer_city: str = None,
        customer_number: str = None,
        customer_province: str = None,
        detail_ringing_time: str = None,
        display_number: str = None,
        down_grade: str = None,
        down_grade_counts: str = None,
        end_reason: str = None,
        end_time: str = None,
        gno: str = None,
        id: str = None,
        is_real_answer: str = None,
        ivr_name: str = None,
        number_trunk: str = None,
        qno: str = None,
        real_answer_time: str = None,
        record_file: List[main_models.CloudQueryWebcallCdrResponseBodyDataListRecordFile] = None,
        request_unique_id: str = None,
        sip_cause: str = None,
        sip_cause_str: str = None,
        start_time: str = None,
        status: str = None,
        status_code: str = None,
        task_file_id: str = None,
        task_id: str = None,
        total_duration: str = None,
        trunk_group_key: str = None,
        unique_id: str = None,
        wait_duration: str = None,
    ):
        self.agent_name = agent_name
        # 系统接听时间，时间戳，精确到s，如1480904471
        self.answer_time = answer_time
        # 服务处理时长秒数，单位是s
        self.bridge_duration = bridge_duration
        # 座席接听时间，时间戳，精确到s，如1480904471
        self.bridge_time = bridge_time
        # 通话唯一标识
        self.call_id = call_id
        # 呼叫类型 webcall
        self.call_type = call_type
        # 第二侧外显号码
        self.callee_clid = callee_clid
        # 第二侧真实外显号码
        self.callee_display_number = callee_display_number
        # 座席电话 区号 +7或8位的固话号码，区号与固话号码之间无\\"-\\"；或11位长度的手机号码。0104100596
        self.callee_number = callee_number
        # 客户响铃时间，时间戳，精确到s，如1480904471
        self.callee_ringing_time = callee_ringing_time
        # 外显号码
        self.clid = clid
        # 座席工号，如2000
        self.cno = cno
        # 客户号码归属城市,北京
        self.customer_city = customer_city
        # 客户号码 国内固话或手机，区号 + 7或8位的固话号码，区号与固话号码之间无\\"-\\"；或11位长度的手机号码。如 01041005968或18701051984 或虚拟号-分机号场景格式，如 18701051984-7538
        self.customer_number = customer_number
        # 客户号码归属省份，如 北京
        self.customer_province = customer_province
        # 转话机后,话机响铃时间
        self.detail_ringing_time = detail_ringing_time
        # 真实外显号码，当使用AXB场景进行外呼时，真实外显号码为虚拟号
        self.display_number = display_number
        self.down_grade = down_grade
        self.down_grade_counts = down_grade_counts
        # 结束原因,接听之后的挂机原因 1000:主通道挂机 1001:非主通道挂机 1002:被强拆
        self.end_reason = end_reason
        # 电话结束时间，时间戳，精确到s，如1480904471
        self.end_time = end_time
        self.gno = gno
        # Id
        self.id = id
        # 是否真人接听：1 - 是、0 - 否、空值
        self.is_real_answer = is_real_answer
        # IVR名称，默认自定义
        self.ivr_name = ivr_name
        # 中继号码
        self.number_trunk = number_trunk
        # 队列号，如1000
        self.qno = qno
        # 真人接听时间，时间戳，精确到s，如1480904471
        self.real_answer_time = real_answer_time
        # 通话记录录音数组
        self.record_file = record_file
        # 用户自定义通话标识字段
        self.request_unique_id = request_unique_id
        # 号码状态识别编码，详见
        self.sip_cause = sip_cause
        # 呼叫结果
        self.sip_cause_str = sip_cause_str
        # 电话进入系统时间，时间戳，精确到s，如1480904471
        self.start_time = start_time
        # 外呼结果， 如客户接听
        self.status = status
        # status对应的状态码
        self.status_code = status_code
        # 任务文件id
        self.task_file_id = task_file_id
        # 任务id
        self.task_id = task_id
        # 总通话时长秒数，单位是s
        self.total_duration = total_duration
        # 中继组标识
        self.trunk_group_key = trunk_group_key
        # 电话唯一标识
        self.unique_id = unique_id
        self.wait_duration = wait_duration

    def validate(self):
        if self.record_file:
            for v1 in self.record_file:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.answer_time is not None:
            result['AnswerTime'] = self.answer_time

        if self.bridge_duration is not None:
            result['BridgeDuration'] = self.bridge_duration

        if self.bridge_time is not None:
            result['BridgeTime'] = self.bridge_time

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.callee_clid is not None:
            result['CalleeClid'] = self.callee_clid

        if self.callee_display_number is not None:
            result['CalleeDisplayNumber'] = self.callee_display_number

        if self.callee_number is not None:
            result['CalleeNumber'] = self.callee_number

        if self.callee_ringing_time is not None:
            result['CalleeRingingTime'] = self.callee_ringing_time

        if self.clid is not None:
            result['Clid'] = self.clid

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.customer_city is not None:
            result['CustomerCity'] = self.customer_city

        if self.customer_number is not None:
            result['CustomerNumber'] = self.customer_number

        if self.customer_province is not None:
            result['CustomerProvince'] = self.customer_province

        if self.detail_ringing_time is not None:
            result['DetailRingingTime'] = self.detail_ringing_time

        if self.display_number is not None:
            result['DisplayNumber'] = self.display_number

        if self.down_grade is not None:
            result['DownGrade'] = self.down_grade

        if self.down_grade_counts is not None:
            result['DownGradeCounts'] = self.down_grade_counts

        if self.end_reason is not None:
            result['EndReason'] = self.end_reason

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gno is not None:
            result['Gno'] = self.gno

        if self.id is not None:
            result['Id'] = self.id

        if self.is_real_answer is not None:
            result['IsRealAnswer'] = self.is_real_answer

        if self.ivr_name is not None:
            result['IvrName'] = self.ivr_name

        if self.number_trunk is not None:
            result['NumberTrunk'] = self.number_trunk

        if self.qno is not None:
            result['Qno'] = self.qno

        if self.real_answer_time is not None:
            result['RealAnswerTime'] = self.real_answer_time

        result['RecordFile'] = []
        if self.record_file is not None:
            for k1 in self.record_file:
                result['RecordFile'].append(k1.to_map() if k1 else None)

        if self.request_unique_id is not None:
            result['RequestUniqueId'] = self.request_unique_id

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

        if self.task_file_id is not None:
            result['TaskFileId'] = self.task_file_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration

        if self.trunk_group_key is not None:
            result['TrunkGroupKey'] = self.trunk_group_key

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        if self.wait_duration is not None:
            result['WaitDuration'] = self.wait_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AnswerTime') is not None:
            self.answer_time = m.get('AnswerTime')

        if m.get('BridgeDuration') is not None:
            self.bridge_duration = m.get('BridgeDuration')

        if m.get('BridgeTime') is not None:
            self.bridge_time = m.get('BridgeTime')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('CalleeClid') is not None:
            self.callee_clid = m.get('CalleeClid')

        if m.get('CalleeDisplayNumber') is not None:
            self.callee_display_number = m.get('CalleeDisplayNumber')

        if m.get('CalleeNumber') is not None:
            self.callee_number = m.get('CalleeNumber')

        if m.get('CalleeRingingTime') is not None:
            self.callee_ringing_time = m.get('CalleeRingingTime')

        if m.get('Clid') is not None:
            self.clid = m.get('Clid')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('CustomerCity') is not None:
            self.customer_city = m.get('CustomerCity')

        if m.get('CustomerNumber') is not None:
            self.customer_number = m.get('CustomerNumber')

        if m.get('CustomerProvince') is not None:
            self.customer_province = m.get('CustomerProvince')

        if m.get('DetailRingingTime') is not None:
            self.detail_ringing_time = m.get('DetailRingingTime')

        if m.get('DisplayNumber') is not None:
            self.display_number = m.get('DisplayNumber')

        if m.get('DownGrade') is not None:
            self.down_grade = m.get('DownGrade')

        if m.get('DownGradeCounts') is not None:
            self.down_grade_counts = m.get('DownGradeCounts')

        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Gno') is not None:
            self.gno = m.get('Gno')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsRealAnswer') is not None:
            self.is_real_answer = m.get('IsRealAnswer')

        if m.get('IvrName') is not None:
            self.ivr_name = m.get('IvrName')

        if m.get('NumberTrunk') is not None:
            self.number_trunk = m.get('NumberTrunk')

        if m.get('Qno') is not None:
            self.qno = m.get('Qno')

        if m.get('RealAnswerTime') is not None:
            self.real_answer_time = m.get('RealAnswerTime')

        self.record_file = []
        if m.get('RecordFile') is not None:
            for k1 in m.get('RecordFile'):
                temp_model = main_models.CloudQueryWebcallCdrResponseBodyDataListRecordFile()
                self.record_file.append(temp_model.from_map(k1))

        if m.get('RequestUniqueId') is not None:
            self.request_unique_id = m.get('RequestUniqueId')

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

        if m.get('TaskFileId') is not None:
            self.task_file_id = m.get('TaskFileId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')

        if m.get('TrunkGroupKey') is not None:
            self.trunk_group_key = m.get('TrunkGroupKey')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        if m.get('WaitDuration') is not None:
            self.wait_duration = m.get('WaitDuration')

        return self

class CloudQueryWebcallCdrResponseBodyDataListRecordFile(DaraModel):
    def __init__(
        self,
        file: str = None,
        monitor_type: int = None,
        type: str = None,
    ):
        # 录音文件名
        self.file = file
        # 1. 混音 2. 分线录音（保留2个单声道WAV） 3.留言 5. 分线录音（保留1个双声道WAV）
        self.monitor_type = monitor_type
        # 取值：record,voicemail说明：record是录音， voicemail是留言
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file is not None:
            result['File'] = self.file

        if self.monitor_type is not None:
            result['Monitor_type'] = self.monitor_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('File') is not None:
            self.file = m.get('File')

        if m.get('Monitor_type') is not None:
            self.monitor_type = m.get('Monitor_type')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

