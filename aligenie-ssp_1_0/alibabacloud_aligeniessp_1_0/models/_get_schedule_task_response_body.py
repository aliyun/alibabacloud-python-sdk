# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetScheduleTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetScheduleTaskResponseBodyResult = None,
    ):
        # Response code
        self.code = code
        # Response message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Service response parameters
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetScheduleTaskResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetScheduleTaskResponseBodyResult(DaraModel):
    def __init__(
        self,
        action_topic_list: List[main_models.GetScheduleTaskResponseBodyResultActionTopicList] = None,
        cron: str = None,
        schedule_end_time: str = None,
        schedule_id: int = None,
        schedule_start_time: str = None,
        schedule_type: str = None,
    ):
        # Trigger behavior
        self.action_topic_list = action_topic_list
        # Trigger Cron Expression
        self.cron = cron
        # Validity Period - End Time
        self.schedule_end_time = schedule_end_time
        # Job ID
        self.schedule_id = schedule_id
        # Validity Period - Start Time
        self.schedule_start_time = schedule_start_time
        # Schedule Type
        self.schedule_type = schedule_type

    def validate(self):
        if self.action_topic_list:
            for v1 in self.action_topic_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActionTopicList'] = []
        if self.action_topic_list is not None:
            for k1 in self.action_topic_list:
                result['ActionTopicList'].append(k1.to_map() if k1 else None)

        if self.cron is not None:
            result['Cron'] = self.cron

        if self.schedule_end_time is not None:
            result['ScheduleEndTime'] = self.schedule_end_time

        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id

        if self.schedule_start_time is not None:
            result['ScheduleStartTime'] = self.schedule_start_time

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_topic_list = []
        if m.get('ActionTopicList') is not None:
            for k1 in m.get('ActionTopicList'):
                temp_model = main_models.GetScheduleTaskResponseBodyResultActionTopicList()
                self.action_topic_list.append(temp_model.from_map(k1))

        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('ScheduleEndTime') is not None:
            self.schedule_end_time = m.get('ScheduleEndTime')

        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')

        if m.get('ScheduleStartTime') is not None:
            self.schedule_start_time = m.get('ScheduleStartTime')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        return self

class GetScheduleTaskResponseBodyResultActionTopicList(DaraModel):
    def __init__(
        self,
        custom_action: Dict[str, Any] = None,
    ):
        # Vendor-defined command
        self.custom_action = custom_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_action is not None:
            result['CustomAction'] = self.custom_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAction') is not None:
            self.custom_action = m.get('CustomAction')

        return self

