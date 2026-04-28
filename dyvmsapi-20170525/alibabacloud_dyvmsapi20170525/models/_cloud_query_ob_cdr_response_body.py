# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudQueryObCdrResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudQueryObCdrResponseBodyData = None,
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
            temp_model = main_models.CloudQueryObCdrResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudQueryObCdrResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.CloudQueryObCdrResponseBodyDataList] = None,
    ):
        # 座席外呼通话记录数组
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
                temp_model = main_models.CloudQueryObCdrResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        return self

class CloudQueryObCdrResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_clid: str = None,
        agent_name: str = None,
        agent_number: str = None,
        answer_time: str = None,
        bridge_duration: str = None,
        bridge_time: str = None,
        call_id: str = None,
        call_type: str = None,
        callee_ringing_time: str = None,
        clid: str = None,
        cno: str = None,
        customer_area_code: str = None,
        customer_city: str = None,
        customer_number: str = None,
        customer_province: str = None,
        display_number: str = None,
        down_grade: str = None,
        down_grade_counts: str = None,
        end_reason: str = None,
        end_time: str = None,
        gno: str = None,
        hangup_reason: str = None,
        id: str = None,
        is_real_answer: str = None,
        left_display_number: str = None,
        main_ringing_time: str = None,
        real_answer_time: str = None,
        record_file: List[main_models.CloudQueryObCdrResponseBodyDataListRecordFile] = None,
        request_unique_id: str = None,
        rtc_total_duration: str = None,
        sip_cause: str = None,
        start_time: str = None,
        status: str = None,
        status_code: str = None,
        status_reason: str = None,
        task_id: str = None,
        total_duration: str = None,
        trunk_group_key: str = None,
        tsi_file: str = None,
        tsi_file_format: str = None,
        unique_id: str = None,
        user_field: Dict[str, Any] = None,
        vad_in: str = None,
        vad_out: str = None,
        wait_duration: str = None,
        xnumber: str = None,
    ):
        # 座席侧外显号码
        self.agent_clid = agent_clid
        # 座席名称
        self.agent_name = agent_name
        # 座席电话 区号 +7或8位的固话号码，区号与固话号码之间无\\"-\\"；或11位长度的手机号码。0104100596
        self.agent_number = agent_number
        # 座席接听时间，时间戳，精确到s，如1480904471
        self.answer_time = answer_time
        # 服务处理时长秒数，单位是s
        self.bridge_duration = bridge_duration
        # 双方接听时间，时间戳，精确到s，如1480904471
        self.bridge_time = bridge_time
        # 通话唯一标识
        self.call_id = call_id
        # 呼叫类型：4、预览外呼; 6、主叫外呼
        self.call_type = call_type
        # 客户侧响铃时间，时间戳，精确到s，如1480904471
        self.callee_ringing_time = callee_ringing_time
        # 客户侧外显号码，当使用虚拟号进行AXB外呼且开关打开时，实际返回的客户侧外显号码是虚拟号
        self.clid = clid
        # 座席工号，如2000
        self.cno = cno
        # 客户号码区号
        self.customer_area_code = customer_area_code
        # 客户号码归属城市,北京
        self.customer_city = customer_city
        # 客户号码 国内固话或手机，区号 + 7或8位的固话号码，区号与固话号码之间无\\"-\\"；或11位长度的手机号码。如 01041005968或18701051984 或虚拟号-分机号场景格式，如 18701051984-7538
        self.customer_number = customer_number
        # 客户号码归属省份，如 北京
        self.customer_province = customer_province
        # 座席侧真实外显号码，当使用AXB场景进行外呼时，座席侧真实外显号码为虚拟号
        self.display_number = display_number
        # 是否呼叫降级, 0-否, 1-是
        self.down_grade = down_grade
        # 降级次数
        self.down_grade_counts = down_grade_counts
        # 结束原因,接听之后的挂机原因 1000:主通道挂机 1001:非主通道挂机 1002:被强拆
        self.end_reason = end_reason
        # 电话结束时间，时间戳，精确到s，如1480904471
        self.end_time = end_time
        self.gno = gno
        self.hangup_reason = hangup_reason
        # Id
        self.id = id
        # 是否真人接听：1 - 是、0 - 否、空值
        self.is_real_answer = is_real_answer
        # 客户侧真实外显号码，当使用AXB场景进行外呼时，客户侧真实外显号码为虚拟号
        self.left_display_number = left_display_number
        # 分机外呼，话机响铃时间
        self.main_ringing_time = main_ringing_time
        # 真人接听时间，时间戳，精确到s，如1480904471
        self.real_answer_time = real_answer_time
        # 通话记录录音数组，json格式
        self.record_file = record_file
        # 请求唯一id
        self.request_unique_id = request_unique_id
        # RTC总通话时长秒数，单位是s，在呼叫类型为主叫外呼(RTC)时有效，计算规则：endTime-startTime
        self.rtc_total_duration = rtc_total_duration
        # SIP响应码：200 ~ 699 详见 注：主叫外呼RTC座席侧没有SIP协商的概念，并未发起呼叫，因此该值默认为0
        self.sip_cause = sip_cause
        # 座席开始外呼时间，时间戳，精确到s，如1480904471
        self.start_time = start_time
        # 外呼结果：30 座席未接听; 31 座席接听,未呼叫客户; 32 座席接听,客户未接听; 33 双方接听; 50 主叫外呼接听; 51 主叫外呼,客户未接听; 52 主叫外呼,双方接听。
        self.status = status
        self.status_code = status_code
        # 通话状态原因（主叫外呼）描述：1 - 企业黑名单; 2 - 风控系统拦截; 20001 - 呼叫限制；20002 - 黑名单或非白名单；20003 - 禁拨时间段； 3 - 无效的外显号码; 4 - 错误的语音导航; 5 - 企业停机; 6 - 无权限外呼; 7 - 超出呼叫次数限制; 8 - 错误号码; 9 - 其他错误；
        self.status_reason = status_reason
        # 座席自动外呼任务id
        self.task_id = task_id
        # 总通话时长秒数，单位是s
        self.total_duration = total_duration
        # 中继群组代号
        self.trunk_group_key = trunk_group_key
        # 彩铃文件名称
        self.tsi_file = tsi_file
        # 彩铃文件类型
        self.tsi_file_format = tsi_file_format
        # 电话唯一标识
        self.unique_id = unique_id
        # 通话记录自定义字段，json格式
        self.user_field = user_field
        # 通话质量百分比,数据是0-100之间，in方向说话占用的百分比
        self.vad_in = vad_in
        # 通话质量百分比,数据是0-100之间，out方向说话占用的百分比
        self.vad_out = vad_out
        # 客户等待时长秒数，单位是s
        self.wait_duration = wait_duration
        # 虚拟号码
        self.xnumber = xnumber

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
        if self.agent_clid is not None:
            result['AgentClid'] = self.agent_clid

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.agent_number is not None:
            result['AgentNumber'] = self.agent_number

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

        if self.callee_ringing_time is not None:
            result['CalleeRingingTime'] = self.callee_ringing_time

        if self.clid is not None:
            result['Clid'] = self.clid

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

        if self.hangup_reason is not None:
            result['HangupReason'] = self.hangup_reason

        if self.id is not None:
            result['Id'] = self.id

        if self.is_real_answer is not None:
            result['IsRealAnswer'] = self.is_real_answer

        if self.left_display_number is not None:
            result['LeftDisplayNumber'] = self.left_display_number

        if self.main_ringing_time is not None:
            result['MainRingingTime'] = self.main_ringing_time

        if self.real_answer_time is not None:
            result['RealAnswerTime'] = self.real_answer_time

        result['RecordFile'] = []
        if self.record_file is not None:
            for k1 in self.record_file:
                result['RecordFile'].append(k1.to_map() if k1 else None)

        if self.request_unique_id is not None:
            result['RequestUniqueId'] = self.request_unique_id

        if self.rtc_total_duration is not None:
            result['RtcTotalDuration'] = self.rtc_total_duration

        if self.sip_cause is not None:
            result['SipCause'] = self.sip_cause

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration

        if self.trunk_group_key is not None:
            result['TrunkGroupKey'] = self.trunk_group_key

        if self.tsi_file is not None:
            result['TsiFile'] = self.tsi_file

        if self.tsi_file_format is not None:
            result['TsiFileFormat'] = self.tsi_file_format

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        if self.user_field is not None:
            result['UserField'] = self.user_field

        if self.vad_in is not None:
            result['VadIn'] = self.vad_in

        if self.vad_out is not None:
            result['VadOut'] = self.vad_out

        if self.wait_duration is not None:
            result['WaitDuration'] = self.wait_duration

        if self.xnumber is not None:
            result['XNumber'] = self.xnumber

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentClid') is not None:
            self.agent_clid = m.get('AgentClid')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AgentNumber') is not None:
            self.agent_number = m.get('AgentNumber')

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

        if m.get('CalleeRingingTime') is not None:
            self.callee_ringing_time = m.get('CalleeRingingTime')

        if m.get('Clid') is not None:
            self.clid = m.get('Clid')

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

        if m.get('HangupReason') is not None:
            self.hangup_reason = m.get('HangupReason')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsRealAnswer') is not None:
            self.is_real_answer = m.get('IsRealAnswer')

        if m.get('LeftDisplayNumber') is not None:
            self.left_display_number = m.get('LeftDisplayNumber')

        if m.get('MainRingingTime') is not None:
            self.main_ringing_time = m.get('MainRingingTime')

        if m.get('RealAnswerTime') is not None:
            self.real_answer_time = m.get('RealAnswerTime')

        self.record_file = []
        if m.get('RecordFile') is not None:
            for k1 in m.get('RecordFile'):
                temp_model = main_models.CloudQueryObCdrResponseBodyDataListRecordFile()
                self.record_file.append(temp_model.from_map(k1))

        if m.get('RequestUniqueId') is not None:
            self.request_unique_id = m.get('RequestUniqueId')

        if m.get('RtcTotalDuration') is not None:
            self.rtc_total_duration = m.get('RtcTotalDuration')

        if m.get('SipCause') is not None:
            self.sip_cause = m.get('SipCause')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')

        if m.get('TrunkGroupKey') is not None:
            self.trunk_group_key = m.get('TrunkGroupKey')

        if m.get('TsiFile') is not None:
            self.tsi_file = m.get('TsiFile')

        if m.get('TsiFileFormat') is not None:
            self.tsi_file_format = m.get('TsiFileFormat')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        if m.get('UserField') is not None:
            self.user_field = m.get('UserField')

        if m.get('VadIn') is not None:
            self.vad_in = m.get('VadIn')

        if m.get('VadOut') is not None:
            self.vad_out = m.get('VadOut')

        if m.get('WaitDuration') is not None:
            self.wait_duration = m.get('WaitDuration')

        if m.get('XNumber') is not None:
            self.xnumber = m.get('XNumber')

        return self

class CloudQueryObCdrResponseBodyDataListRecordFile(DaraModel):
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

