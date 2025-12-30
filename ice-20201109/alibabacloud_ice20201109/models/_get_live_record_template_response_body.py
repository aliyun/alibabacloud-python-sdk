# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetLiveRecordTemplateResponseBody(DaraModel):
    def __init__(
        self,
        record_template: main_models.GetLiveRecordTemplateResponseBodyRecordTemplate = None,
        request_id: str = None,
    ):
        # The recording template.
        self.record_template = record_template
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.record_template:
            self.record_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_template is not None:
            result['RecordTemplate'] = self.record_template.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordTemplate') is not None:
            temp_model = main_models.GetLiveRecordTemplateResponseBodyRecordTemplate()
            self.record_template = temp_model.from_map(m.get('RecordTemplate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLiveRecordTemplateResponseBodyRecordTemplate(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        last_modified: str = None,
        name: str = None,
        record_format_list: List[main_models.GetLiveRecordTemplateResponseBodyRecordTemplateRecordFormatList] = None,
        template_id: str = None,
        type: str = None,
    ):
        # The time when the job was created.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.create_time = create_time
        # The time when the template was last modified.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.last_modified = last_modified
        # The template name.
        self.name = name
        # The list of recording formats.
        self.record_format_list = record_format_list
        # The template ID.
        self.template_id = template_id
        # The type of the template.
        # 
        # Valid values:
        # 
        # *   system
        # *   custom
        self.type = type

    def validate(self):
        if self.record_format_list:
            for v1 in self.record_format_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.name is not None:
            result['Name'] = self.name

        result['RecordFormatList'] = []
        if self.record_format_list is not None:
            for k1 in self.record_format_list:
                result['RecordFormatList'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.record_format_list = []
        if m.get('RecordFormatList') is not None:
            for k1 in m.get('RecordFormatList'):
                temp_model = main_models.GetLiveRecordTemplateResponseBodyRecordTemplateRecordFormatList()
                self.record_format_list.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetLiveRecordTemplateResponseBodyRecordTemplateRecordFormatList(DaraModel):
    def __init__(
        self,
        cycle_duration: int = None,
        format: str = None,
        oss_object_prefix: str = None,
        slice_duration: int = None,
        slice_oss_object_prefix: str = None,
    ):
        # The duration of the recording cycle. Unit: seconds. If you do not specify this parameter, the default value 6 hours is used.
        self.cycle_duration = cycle_duration
        # The output file format.
        self.format = format
        # The name of the recording file that is stored in Object Storage Service (OSS).
        self.oss_object_prefix = oss_object_prefix
        # The duration of a single segment. Unit: seconds.
        self.slice_duration = slice_duration
        # The name of the TS segment.
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

