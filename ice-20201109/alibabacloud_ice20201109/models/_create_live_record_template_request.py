# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateLiveRecordTemplateRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        record_format: List[main_models.CreateLiveRecordTemplateRequestRecordFormat] = None,
    ):
        # The name of the Live Record Template.
        # 
        # This parameter is required.
        self.name = name
        # The list of recording formats.
        # 
        # This parameter is required.
        self.record_format = record_format

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.record_format = []
        if m.get('RecordFormat') is not None:
            for k1 in m.get('RecordFormat'):
                temp_model = main_models.CreateLiveRecordTemplateRequestRecordFormat()
                self.record_format.append(temp_model.from_map(k1))

        return self

class CreateLiveRecordTemplateRequestRecordFormat(DaraModel):
    def __init__(
        self,
        cycle_duration: int = None,
        format: str = None,
        oss_object_prefix: str = None,
        slice_duration: int = None,
        slice_oss_object_prefix: str = None,
    ):
        # The duration of a recording cycle in seconds. If you omit this parameter, it defaults to 6 hours.
        # 
        # > - If a stream interruption during a recording cycle lasts less than 3 minutes, the recording continues in the same Recording File.
        # 
        # - A Recording File is finalized only after a stream interruption lasts for more than 3 minutes. To change this default 3-minute threshold, submit a ticket.
        self.cycle_duration = cycle_duration
        # The recording format.
        # 
        # > If you set this parameter to `m3u8`, you must also specify the `SliceOssObjectPrefix` and `SliceDuration` parameters.
        # 
        # This parameter is required.
        self.format = format
        # The name of the Recording File stored in Object Storage Service (OSS).
        # 
        # - The file name must be less than 256 bytes and supports the following variables: {JobId}, {Sequence}, {StartTime}, {EndTime}, {EscapedStartTime}, and {EscapedEndTime}.
        # 
        # - The value must include either the {StartTime} or {EscapedStartTime} variable and either the {EndTime} or {EscapedEndTime} variable.
        self.oss_object_prefix = oss_object_prefix
        # The duration of each slice in seconds.
        # 
        # > This parameter is valid only when `Format` is set to `m3u8`.
        # 
        # The default value is 30. The value must be an integer from 5 to 30.
        self.slice_duration = slice_duration
        # The name of the TS slice.
        # 
        # > This parameter is required only when `Format` is set to `m3u8`.
        # 
        # - The file name must be less than 256 bytes and supports the following variables: {JobId}, {UnixTimestamp}, and {Sequence}.
        # 
        # - The value must include the {UnixTimestamp} and {Sequence} variables.
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

