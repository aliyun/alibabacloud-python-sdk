# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class GetSummaryInfoResponseBody(DaraModel):
    def __init__(
        self,
        agent_bot_instance_summary_list: List[main_models.GetSummaryInfoResponseBodyAgentBotInstanceSummaryList] = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.agent_bot_instance_summary_list = agent_bot_instance_summary_list
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.agent_bot_instance_summary_list:
            for v1 in self.agent_bot_instance_summary_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AgentBotInstanceSummaryList'] = []
        if self.agent_bot_instance_summary_list is not None:
            for k1 in self.agent_bot_instance_summary_list:
                result['AgentBotInstanceSummaryList'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_bot_instance_summary_list = []
        if m.get('AgentBotInstanceSummaryList') is not None:
            for k1 in m.get('AgentBotInstanceSummaryList'):
                temp_model = main_models.GetSummaryInfoResponseBodyAgentBotInstanceSummaryList()
                self.agent_bot_instance_summary_list.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSummaryInfoResponseBodyAgentBotInstanceSummaryList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        total_call_count: int = None,
        total_call_time: int = None,
        used_recording_storage_space: int = None,
    ):
        self.instance_id = instance_id
        self.total_call_count = total_call_count
        self.total_call_time = total_call_time
        self.used_recording_storage_space = used_recording_storage_space

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.total_call_count is not None:
            result['TotalCallCount'] = self.total_call_count

        if self.total_call_time is not None:
            result['TotalCallTime'] = self.total_call_time

        if self.used_recording_storage_space is not None:
            result['UsedRecordingStorageSpace'] = self.used_recording_storage_space

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TotalCallCount') is not None:
            self.total_call_count = m.get('TotalCallCount')

        if m.get('TotalCallTime') is not None:
            self.total_call_time = m.get('TotalCallTime')

        if m.get('UsedRecordingStorageSpace') is not None:
            self.used_recording_storage_space = m.get('UsedRecordingStorageSpace')

        return self

