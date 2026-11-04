# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEventRecordPlanRequest(DaraModel):
    def __init__(
        self,
        event_types: str = None,
        name: str = None,
        pre_record_duration: int = None,
        record_duration: int = None,
        template_id: str = None,
    ):
        # The types of intelligent alert events. Valid values:
        # - 0: all intelligent alert events.
        # - Multiple intelligent alert events: enter the sequence numbers of the intelligent alert events and separate them with commas (,). Example: `10001,10002`.
        # > You can specify up to 10 intelligent alert events at a time.
        # 
        # To view all types of intelligent alert events, log on to the IoT Platform console, go to the **Product Details** page, and click the **Define Feature** tab. For more information, see [View intelligent alert event types](https://help.aliyun.com/document_detail/207701.html).
        self.event_types = event_types
        # The name of the recording plan.
        # 
        # The name must be less than 48 characters in length and can contain letters, digits, and the following special characters: hyphens (-), underscores (_), at signs (@), periods (.), and colons (:).
        # 
        # This parameter is required.
        self.name = name
        # The pre-recording duration in seconds. Default value: 0. Maximum value: 10.
        self.pre_record_duration = pre_record_duration
        # The recording duration in seconds, including the pre-recording duration. Valid values: 10 to 60.
        # 
        # This parameter is required.
        self.record_duration = record_duration
        # The ID of the time template. You can call the [QueryTimeTemplate](https://help.aliyun.com/document_detail/107890.html) operation to query the ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_types is not None:
            result['EventTypes'] = self.event_types

        if self.name is not None:
            result['Name'] = self.name

        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration

        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')

        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

