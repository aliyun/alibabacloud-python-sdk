# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLiveSnapshotTemplateRequest(DaraModel):
    def __init__(
        self,
        overwrite_format: str = None,
        sequence_format: str = None,
        template_name: str = None,
        time_interval: int = None,
    ):
        # The naming format of the snapshot captured in overwrite mode.
        # 
        # *   The value cannot start with a forward slash (/). Only the suffix .jpg is supported.
        # *   It cannot exceed 255 characters in length.
        # *   The {JobId} placeholder is supported. It specifies the ID of the snapshot job.
        # *   Placeholders such as {UnixTimestamp}, {Sequence}, and {Date} are not allowed.
        # *   You must specify at least one of the OverwriteFormat and SequenceFormat parameters.
        self.overwrite_format = overwrite_format
        # The naming format of the snapshot captured in time series mode.
        # 
        # *   The value cannot start with a forward slash (/). Only the suffix .jpg is supported.
        # *   It cannot exceed 255 characters in length.
        # *   The {JobId}, {Date}, {UnixTimestamp}, and {Sequence} placeholders are supported. {JobId} specifies the ID of the snapshot job. {Date} specifies the date on which the snapshot is captured. {UnixTimestamp} specifies the timestamp of the snapshot. {Sequence} specifies the sequence number of the snapshot. You must specify at least one of the {UnixTimestamp} and {Sequence} placeholders.
        # *   You must specify at least one of the OverwriteFormat and SequenceFormat parameters.
        self.sequence_format = sequence_format
        # The name of the template.
        # 
        # *   It cannot exceed 128 characters in length.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The interval between two adjacent snapshots. Unit: seconds.
        # 
        # *   Valid values: [5,3600].
        # 
        # This parameter is required.
        self.time_interval = time_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overwrite_format is not None:
            result['OverwriteFormat'] = self.overwrite_format

        if self.sequence_format is not None:
            result['SequenceFormat'] = self.sequence_format

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverwriteFormat') is not None:
            self.overwrite_format = m.get('OverwriteFormat')

        if m.get('SequenceFormat') is not None:
            self.sequence_format = m.get('SequenceFormat')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')

        return self

