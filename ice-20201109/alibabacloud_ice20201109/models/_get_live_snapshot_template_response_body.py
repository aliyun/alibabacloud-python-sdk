# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLiveSnapshotTemplateResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        last_modified: str = None,
        overwrite_format: str = None,
        request_id: str = None,
        sequence_format: str = None,
        template_id: str = None,
        template_name: str = None,
        time_interval: int = None,
        type: str = None,
    ):
        # The time when the configuration was modified.
        self.create_time = create_time
        # The time when the template was created.
        self.last_modified = last_modified
        # The naming format of the snapshot captured in overwrite mode.
        self.overwrite_format = overwrite_format
        # The request ID.
        self.request_id = request_id
        # The naming format of the snapshot captured in time series mode.
        self.sequence_format = sequence_format
        # The template ID.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The interval between two adjacent snapshots.
        self.time_interval = time_interval
        # The type of the template.
        # 
        # Valid values:
        # 
        # *   system
        # *   custom
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.overwrite_format is not None:
            result['OverwriteFormat'] = self.overwrite_format

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sequence_format is not None:
            result['SequenceFormat'] = self.sequence_format

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('OverwriteFormat') is not None:
            self.overwrite_format = m.get('OverwriteFormat')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SequenceFormat') is not None:
            self.sequence_format = m.get('SequenceFormat')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

