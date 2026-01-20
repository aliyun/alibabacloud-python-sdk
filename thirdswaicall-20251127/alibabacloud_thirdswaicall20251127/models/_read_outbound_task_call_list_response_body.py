# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_thirdswaicall20251127 import models as main_models
from darabonba.model import DaraModel

class ReadOutboundTaskCallListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        message: str = None,
        records: List[main_models.ReadOutboundTaskCallListResponseBodyRecords] = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        timestamp: str = None,
        total: int = None,
        trace_id: str = None,
    ):
        self.code = code
        self.current = current
        self.message = message
        self.records = records
        self.request_id = request_id
        self.size = size
        self.success = success
        self.timestamp = timestamp
        self.total = total
        self.trace_id = trace_id

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current is not None:
            result['Current'] = self.current

        if self.message is not None:
            result['Message'] = self.message

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.total is not None:
            result['Total'] = self.total

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ReadOutboundTaskCallListResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class ReadOutboundTaskCallListResponseBodyRecords(DaraModel):
    def __init__(
        self,
        call_end_time: str = None,
        call_id: str = None,
        call_start_time: str = None,
        call_summary: str = None,
        channel: str = None,
        customer_name: str = None,
        customer_phone: str = None,
        dialogue_list: List[main_models.ReadOutboundTaskCallListResponseBodyRecordsDialogueList] = None,
        display_status: str = None,
        duration: int = None,
        duration_text: str = None,
        ext_info: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        label_tags: List[str] = None,
        record_detail_ready: bool = None,
        record_url: str = None,
        retry_count: int = None,
        scene_id: str = None,
        status: str = None,
        task_id: str = None,
        tenant_id: str = None,
        tts_voice_code: str = None,
        tts_voice_desc: str = None,
        user_id: str = None,
    ):
        self.call_end_time = call_end_time
        self.call_id = call_id
        self.call_start_time = call_start_time
        self.call_summary = call_summary
        self.channel = channel
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.dialogue_list = dialogue_list
        self.display_status = display_status
        self.duration = duration
        self.duration_text = duration_text
        self.ext_info = ext_info
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.label_tags = label_tags
        self.record_detail_ready = record_detail_ready
        self.record_url = record_url
        self.retry_count = retry_count
        self.scene_id = scene_id
        self.status = status
        self.task_id = task_id
        self.tenant_id = tenant_id
        self.tts_voice_code = tts_voice_code
        self.tts_voice_desc = tts_voice_desc
        self.user_id = user_id

    def validate(self):
        if self.dialogue_list:
            for v1 in self.dialogue_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_end_time is not None:
            result['CallEndTime'] = self.call_end_time

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_start_time is not None:
            result['CallStartTime'] = self.call_start_time

        if self.call_summary is not None:
            result['CallSummary'] = self.call_summary

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name

        if self.customer_phone is not None:
            result['CustomerPhone'] = self.customer_phone

        result['DialogueList'] = []
        if self.dialogue_list is not None:
            for k1 in self.dialogue_list:
                result['DialogueList'].append(k1.to_map() if k1 else None)

        if self.display_status is not None:
            result['DisplayStatus'] = self.display_status

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.duration_text is not None:
            result['DurationText'] = self.duration_text

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.label_tags is not None:
            result['LabelTags'] = self.label_tags

        if self.record_detail_ready is not None:
            result['RecordDetailReady'] = self.record_detail_ready

        if self.record_url is not None:
            result['RecordUrl'] = self.record_url

        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tts_voice_code is not None:
            result['TtsVoiceCode'] = self.tts_voice_code

        if self.tts_voice_desc is not None:
            result['TtsVoiceDesc'] = self.tts_voice_desc

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallEndTime') is not None:
            self.call_end_time = m.get('CallEndTime')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallStartTime') is not None:
            self.call_start_time = m.get('CallStartTime')

        if m.get('CallSummary') is not None:
            self.call_summary = m.get('CallSummary')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')

        if m.get('CustomerPhone') is not None:
            self.customer_phone = m.get('CustomerPhone')

        self.dialogue_list = []
        if m.get('DialogueList') is not None:
            for k1 in m.get('DialogueList'):
                temp_model = main_models.ReadOutboundTaskCallListResponseBodyRecordsDialogueList()
                self.dialogue_list.append(temp_model.from_map(k1))

        if m.get('DisplayStatus') is not None:
            self.display_status = m.get('DisplayStatus')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('DurationText') is not None:
            self.duration_text = m.get('DurationText')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LabelTags') is not None:
            self.label_tags = m.get('LabelTags')

        if m.get('RecordDetailReady') is not None:
            self.record_detail_ready = m.get('RecordDetailReady')

        if m.get('RecordUrl') is not None:
            self.record_url = m.get('RecordUrl')

        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TtsVoiceCode') is not None:
            self.tts_voice_code = m.get('TtsVoiceCode')

        if m.get('TtsVoiceDesc') is not None:
            self.tts_voice_desc = m.get('TtsVoiceDesc')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self



class ReadOutboundTaskCallListResponseBodyRecordsDialogueList(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        role: str = None,
        text: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.role = role
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.role is not None:
            result['Role'] = self.role

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

