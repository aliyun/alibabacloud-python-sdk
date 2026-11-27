# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeAppRecordTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        templates: List[main_models.DescribeAppRecordTemplatesResponseBodyTemplates] = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The list of templates.
        self.templates = templates
        # The total number of records.
        self.total_num = total_num
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.DescribeAppRecordTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeAppRecordTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        delay_stop_time: int = None,
        file_prefix: str = None,
        file_split_interval: int = None,
        formats: List[str] = None,
        layout_ids: List[str] = None,
        media_encode: int = None,
        name: str = None,
        template_id: str = None,
    ):
        # The creation time. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format. The time is in UTC.
        self.create_time = create_time
        # The delay time before stopping the recording. Unit: seconds.
        self.delay_stop_time = delay_stop_time
        # The naming rule for recording files.
        # > To ensure the uniqueness of recording file names, the current naming rule is record/{AppId}/{ChannelId}_{TaskId}/{EscapedStartTime}_{EscapedEndTime}.
        self.file_prefix = file_prefix
        # The splitting duration of the recording file. The value must be greater than or equal to 1800. Unit: seconds.
        self.file_split_interval = file_split_interval
        # The formats of the recording file. Valid values: .m3u8, .mp4, and .flv.
        # > Only lowercase letters are supported for file formats.
        self.formats = formats
        # The list of layout IDs.
        self.layout_ids = layout_ids
        # The encoding options.
        self.media_encode = media_encode
        # The template name.
        self.name = name
        # The template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.delay_stop_time is not None:
            result['DelayStopTime'] = self.delay_stop_time

        if self.file_prefix is not None:
            result['FilePrefix'] = self.file_prefix

        if self.file_split_interval is not None:
            result['FileSplitInterval'] = self.file_split_interval

        if self.formats is not None:
            result['Formats'] = self.formats

        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids

        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode

        if self.name is not None:
            result['Name'] = self.name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DelayStopTime') is not None:
            self.delay_stop_time = m.get('DelayStopTime')

        if m.get('FilePrefix') is not None:
            self.file_prefix = m.get('FilePrefix')

        if m.get('FileSplitInterval') is not None:
            self.file_split_interval = m.get('FileSplitInterval')

        if m.get('Formats') is not None:
            self.formats = m.get('Formats')

        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')

        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

