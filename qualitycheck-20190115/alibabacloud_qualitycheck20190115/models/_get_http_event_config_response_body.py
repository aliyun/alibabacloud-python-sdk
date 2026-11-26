# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetHttpEventConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHttpEventConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetHttpEventConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetHttpEventConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        event_config: main_models.GetHttpEventConfigResponseBodyDataEventConfig = None,
        http_method: str = None,
        switch_flag: bool = None,
    ):
        self.callback_url = callback_url
        self.event_config = event_config
        self.http_method = http_method
        self.switch_flag = switch_flag

    def validate(self):
        if self.event_config:
            self.event_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.event_config is not None:
            result['EventConfig'] = self.event_config.to_map()

        if self.http_method is not None:
            result['HttpMethod'] = self.http_method

        if self.switch_flag is not None:
            result['SwitchFlag'] = self.switch_flag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('EventConfig') is not None:
            temp_model = main_models.GetHttpEventConfigResponseBodyDataEventConfig()
            self.event_config = temp_model.from_map(m.get('EventConfig'))

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('SwitchFlag') is not None:
            self.switch_flag = m.get('SwitchFlag')

        return self

class GetHttpEventConfigResponseBodyDataEventConfig(DaraModel):
    def __init__(
        self,
        complaint_handled_event: bool = None,
        file_reviewed_event: bool = None,
        sync_task_complete_event: bool = None,
        task_complete_event: bool = None,
    ):
        self.complaint_handled_event = complaint_handled_event
        self.file_reviewed_event = file_reviewed_event
        self.sync_task_complete_event = sync_task_complete_event
        self.task_complete_event = task_complete_event

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complaint_handled_event is not None:
            result['ComplaintHandledEvent'] = self.complaint_handled_event

        if self.file_reviewed_event is not None:
            result['FileReviewedEvent'] = self.file_reviewed_event

        if self.sync_task_complete_event is not None:
            result['SyncTaskCompleteEvent'] = self.sync_task_complete_event

        if self.task_complete_event is not None:
            result['TaskCompleteEvent'] = self.task_complete_event

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplaintHandledEvent') is not None:
            self.complaint_handled_event = m.get('ComplaintHandledEvent')

        if m.get('FileReviewedEvent') is not None:
            self.file_reviewed_event = m.get('FileReviewedEvent')

        if m.get('SyncTaskCompleteEvent') is not None:
            self.sync_task_complete_event = m.get('SyncTaskCompleteEvent')

        if m.get('TaskCompleteEvent') is not None:
            self.task_complete_event = m.get('TaskCompleteEvent')

        return self

