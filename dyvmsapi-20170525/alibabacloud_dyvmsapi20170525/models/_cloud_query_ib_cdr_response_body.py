# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudQueryIbCdrResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudQueryIbCdrResponseBodyData = None,
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
            temp_model = main_models.CloudQueryIbCdrResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudQueryIbCdrResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.CloudQueryIbCdrResponseBodyDataList] = None,
    ):
        # 来电通话记录数组
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
                temp_model = main_models.CloudQueryIbCdrResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        return self

class CloudQueryIbCdrResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        answer_time: str = None,
        bridge_duration: str = None,
        bridge_time: str = None,
        call_type: str = None,
        callee_number: str = None,
        cno: str = None,
        customer_area_code: str = None,
        customer_city: str = None,
        customer_number: str = None,
        customer_province: str = None,
        end_reason: str = None,
        end_time: str = None,
        hotline: str = None,
        ivr_name: str = None,
        leave_queue_code: int = None,
        number_trunk: str = None,
        number_trunk_area_code: str = None,
        qno: str = None,
        record_file: List[main_models.CloudQueryIbCdrResponseBodyDataListRecordFile] = None,
        start_time: str = None,
        status: str = None,
        status_code: str = None,
        total_duration: str = None,
        unique_id: str = None,
        user_field: Dict[str, Any] = None,
    ):
        # 座席名称
        self.agent_name = agent_name
        # 系统接听时间，时间戳，精确到s，如1480904471
        self.answer_time = answer_time
        # 服务处理时长秒数，单位是s
        self.bridge_duration = bridge_duration
        # 座席接听时间，时间戳，精确到s，如1480904471
        self.bridge_time = bridge_time
        # 呼叫类型 呼入
        self.call_type = call_type
        # 座席电话 区号 +7或8位的固话号码，区号与固话号码之间无\\"-\\"；或11位长度的手机号码。0104100596
        self.callee_number = callee_number
        # 座席工号，如2000
        self.cno = cno
        # 客户号码区号
        self.customer_area_code = customer_area_code
        # 客户号码归属城市,北京
        self.customer_city = customer_city
        # 客户号码 国内固话或手机，区号 + 7或8位的固话号码，区号与固话号码之间无\\"-\\"；或11位长度的手机号码。如 01041005968或18701051984
        self.customer_number = customer_number
        # 客户号码归属省份，如 北京
        self.customer_province = customer_province
        # 结束原因,接听之后的挂机原因 1000:主通道挂机 1001:非主通道挂机 1002:被强拆
        self.end_reason = end_reason
        # 电话结束时间，时间戳，精确到s，如1480904471
        self.end_time = end_time
        # 热线号码
        self.hotline = hotline
        # IVR名称，默认自定义
        self.ivr_name = ivr_name
        # 离开队列原因 参数说明：-1:该字段没值, 1:呼转座席接听 , 2: 队列中放弃 , 3: 队列中超时溢出 , 4: 队列中无座席溢出
        self.leave_queue_code = leave_queue_code
        # 中继号码
        self.number_trunk = number_trunk
        # 中继号码区号
        self.number_trunk_area_code = number_trunk_area_code
        # 队列号，如1000
        self.qno = qno
        # 通话记录录音数组，json格式
        self.record_file = record_file
        # 电话进入系统时间，时间戳，精确到s，如1480904471
        self.start_time = start_time
        # 外呼结果， 如人工接听
        self.status = status
        # status对应的状态码
        self.status_code = status_code
        # 总通话时长秒数，单位是s
        self.total_duration = total_duration
        # 电话唯一标识
        self.unique_id = unique_id
        # 通话记录自定义字段，json格式
        self.user_field = user_field

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

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.callee_number is not None:
            result['CalleeNumber'] = self.callee_number

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.customer_area_code is not None:
            result['CustomerAreaCode'] = self.customer_area_code

        if self.customer_city is not None:
            result['CustomerCity'] = self.customer_city

        if self.customer_number is not None:
            result['CustomerNumber'] = self.customer_number

        if self.customer_province is not None:
            result['CustomerProvince'] = self.customer_province

        if self.end_reason is not None:
            result['EndReason'] = self.end_reason

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.hotline is not None:
            result['Hotline'] = self.hotline

        if self.ivr_name is not None:
            result['IvrName'] = self.ivr_name

        if self.leave_queue_code is not None:
            result['LeaveQueueCode'] = self.leave_queue_code

        if self.number_trunk is not None:
            result['NumberTrunk'] = self.number_trunk

        if self.number_trunk_area_code is not None:
            result['NumberTrunkAreaCode'] = self.number_trunk_area_code

        if self.qno is not None:
            result['Qno'] = self.qno

        result['RecordFile'] = []
        if self.record_file is not None:
            for k1 in self.record_file:
                result['RecordFile'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        if self.user_field is not None:
            result['UserField'] = self.user_field

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

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('CalleeNumber') is not None:
            self.callee_number = m.get('CalleeNumber')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('CustomerAreaCode') is not None:
            self.customer_area_code = m.get('CustomerAreaCode')

        if m.get('CustomerCity') is not None:
            self.customer_city = m.get('CustomerCity')

        if m.get('CustomerNumber') is not None:
            self.customer_number = m.get('CustomerNumber')

        if m.get('CustomerProvince') is not None:
            self.customer_province = m.get('CustomerProvince')

        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Hotline') is not None:
            self.hotline = m.get('Hotline')

        if m.get('IvrName') is not None:
            self.ivr_name = m.get('IvrName')

        if m.get('LeaveQueueCode') is not None:
            self.leave_queue_code = m.get('LeaveQueueCode')

        if m.get('NumberTrunk') is not None:
            self.number_trunk = m.get('NumberTrunk')

        if m.get('NumberTrunkAreaCode') is not None:
            self.number_trunk_area_code = m.get('NumberTrunkAreaCode')

        if m.get('Qno') is not None:
            self.qno = m.get('Qno')

        self.record_file = []
        if m.get('RecordFile') is not None:
            for k1 in m.get('RecordFile'):
                temp_model = main_models.CloudQueryIbCdrResponseBodyDataListRecordFile()
                self.record_file.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        if m.get('UserField') is not None:
            self.user_field = m.get('UserField')

        return self

class CloudQueryIbCdrResponseBodyDataListRecordFile(DaraModel):
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
        # 取值：record,voicemail 说明：record是录音， voicemail是留言
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

