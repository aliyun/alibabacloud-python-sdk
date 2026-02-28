# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeAppStreamingOutTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        templates: List[main_models.DescribeAppStreamingOutTemplatesResponseBodyTemplates] = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.templates = templates
        self.total_num = total_num
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
                temp_model = main_models.DescribeAppStreamingOutTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeAppStreamingOutTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        layout_ids: List[str] = None,
        media_encode: int = None,
        name: str = None,
        template_id: str = None,
    ):
        self.create_time = create_time
        self.layout_ids = layout_ids
        self.media_encode = media_encode
        self.name = name
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

        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')

        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

