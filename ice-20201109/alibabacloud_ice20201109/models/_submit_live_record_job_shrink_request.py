# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitLiveRecordJobShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        notify_url: str = None,
        record_output_shrink: str = None,
        stream_input_shrink: str = None,
        template_id: str = None,
    ):
        # The name of the recording job.
        # 
        # This parameter is required.
        self.name = name
        # The callback URL.
        self.notify_url = notify_url
        # The storage address of the recording.
        # 
        # This parameter is required.
        self.record_output_shrink = record_output_shrink
        # The URL of the live stream.
        # 
        # This parameter is required.
        self.stream_input_shrink = stream_input_shrink
        # The ID of the recording template.
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
        if self.name is not None:
            result['Name'] = self.name

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.record_output_shrink is not None:
            result['RecordOutput'] = self.record_output_shrink

        if self.stream_input_shrink is not None:
            result['StreamInput'] = self.stream_input_shrink

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('RecordOutput') is not None:
            self.record_output_shrink = m.get('RecordOutput')

        if m.get('StreamInput') is not None:
            self.stream_input_shrink = m.get('StreamInput')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

