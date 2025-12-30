# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class UpdateLiveRecordTemplateRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        record_format: List[main_models.UpdateLiveRecordTemplateRequestRecordFormat] = None,
        template_id: str = None,
    ):
        # The template name.
        # 
        # This parameter is required.
        self.name = name
        # The list of recording formats.
        # 
        # This parameter is required.
        self.record_format = record_format
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        if self.record_format:
            for v1 in self.record_format:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        result['RecordFormat'] = []
        if self.record_format is not None:
            for k1 in self.record_format:
                result['RecordFormat'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.record_format = []
        if m.get('RecordFormat') is not None:
            for k1 in m.get('RecordFormat'):
                temp_model = main_models.UpdateLiveRecordTemplateRequestRecordFormat()
                self.record_format.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class UpdateLiveRecordTemplateRequestRecordFormat(DaraModel):
    def __init__(
        self,
        cycle_duration: int = None,
        format: str = None,
        oss_object_prefix: str = None,
        slice_duration: int = None,
        slice_oss_object_prefix: str = None,
    ):
        # The duration of the recording cycle. Unit: seconds If you do not specify this parameter, the default value 6 hours is used.
        # 
        # > 
        # 
        # *   If a live stream is interrupted during a recording cycle but is resumed within 3 minutes, the stream is recorded in the same recording before and after the interruption.
        # 
        # *   If a live stream is interrupted for more than 3 minutes, a new recording is generated. To change the default stream interruption time, submit a ticket.
        self.cycle_duration = cycle_duration
        # The format of recording files.
        # 
        # >  If you set this parameter to m3u8, you must also specify the SliceOssObjectPrefix and SliceDuration parameters.
        # 
        # This parameter is required.
        self.format = format
        # The name of the recording that is stored in Object Storage Service (OSS).
        # 
        # *   The name must be less than 256 bytes in length and can contain the {JobId}, {Sequence}, {StartTime}, {EndTime}, {EscapedStartTime}, and {EscapedEndTime} variables.
        # *   The name must contain the {StartTime} and {EndTime} variables or the {EscapedStartTime} and {EscapedEndTime} variables.
        self.oss_object_prefix = oss_object_prefix
        # The duration of a single segment. Unit: seconds
        # 
        # >  This parameter takes effect only if you set Format to m3u8.
        # 
        # If you do not specify this parameter, the default value 30 seconds is used. Valid values: 5 to 30.
        self.slice_duration = slice_duration
        # The name of the TS segment.
        # 
        # >  This parameter is required only if you set Format to m3u8. By default, the duration of a segment is 30 seconds. The segment name must be less than 256 bytes in length and can contain the {JobId}, {UnixTimestamp}, and {Sequence} variables.
        # 
        # The segment name must contain the {UnixTimestamp} and {Sequence} variables.
        self.slice_oss_object_prefix = slice_oss_object_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_duration is not None:
            result['CycleDuration'] = self.cycle_duration

        if self.format is not None:
            result['Format'] = self.format

        if self.oss_object_prefix is not None:
            result['OssObjectPrefix'] = self.oss_object_prefix

        if self.slice_duration is not None:
            result['SliceDuration'] = self.slice_duration

        if self.slice_oss_object_prefix is not None:
            result['SliceOssObjectPrefix'] = self.slice_oss_object_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleDuration') is not None:
            self.cycle_duration = m.get('CycleDuration')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('OssObjectPrefix') is not None:
            self.oss_object_prefix = m.get('OssObjectPrefix')

        if m.get('SliceDuration') is not None:
            self.slice_duration = m.get('SliceDuration')

        if m.get('SliceOssObjectPrefix') is not None:
            self.slice_oss_object_prefix = m.get('SliceOssObjectPrefix')

        return self

