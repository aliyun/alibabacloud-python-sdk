# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class DescribeSearchTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        template_list: List[main_models.DescribeSearchTemplatesResponseBodyTemplateList] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The maximum number of results returned.
        # 
        # Default value: 20.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of template details.
        self.template_list = template_list

    def validate(self):
        if self.template_list:
            for v1 in self.template_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TemplateList'] = []
        if self.template_list is not None:
            for k1 in self.template_list:
                result['TemplateList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.template_list = []
        if m.get('TemplateList') is not None:
            for k1 in m.get('TemplateList'):
                temp_model = main_models.DescribeSearchTemplatesResponseBodyTemplateList()
                self.template_list.append(temp_model.from_map(k1))

        return self

class DescribeSearchTemplatesResponseBodyTemplateList(DaraModel):
    def __init__(
        self,
        charts: str = None,
        description: str = None,
        params: str = None,
        scene_id: str = None,
        sql: str = None,
        template_id: str = None,
        template_name: str = None,
        token: str = None,
        type: str = None,
    ):
        # The list of dashboards. This parameter is deprecated.
        # 
        # > This parameter is deprecated and no longer returns valid data. The returned value is always an empty array `[]`. Stop using this parameter and remove its dependency from your code.
        self.charts = charts
        # The template description.
        self.description = description
        # The filter conditions.<br>This parameter is returned as a JSON-serialized string that contains a structured list of filter conditions. Use a standard JSON deserialization tool for your programming language to parse the string into an array of objects.
        self.params = params
        # The scenario ID.
        self.scene_id = scene_id
        # The query statement.
        self.sql = sql
        # The template ID.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The identifier for the template category.
        self.token = token
        # The template type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charts is not None:
            result['Charts'] = self.charts

        if self.description is not None:
            result['Description'] = self.description

        if self.params is not None:
            result['Params'] = self.params

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.token is not None:
            result['Token'] = self.token

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Charts') is not None:
            self.charts = m.get('Charts')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

