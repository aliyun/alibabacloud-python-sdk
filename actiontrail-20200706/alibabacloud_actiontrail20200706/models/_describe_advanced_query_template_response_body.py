# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class DescribeAdvancedQueryTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template_page: main_models.DescribeAdvancedQueryTemplateResponseBodyTemplatePage = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The paginated list of templates.
        self.template_page = template_page

    def validate(self):
        if self.template_page:
            self.template_page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_page is not None:
            result['TemplatePage'] = self.template_page.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplatePage') is not None:
            temp_model = main_models.DescribeAdvancedQueryTemplateResponseBodyTemplatePage()
            self.template_page = temp_model.from_map(m.get('TemplatePage'))

        return self

class DescribeAdvancedQueryTemplateResponseBodyTemplatePage(DaraModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
        template_list: List[main_models.DescribeAdvancedQueryTemplateResponseBodyTemplatePageTemplateList] = None,
        total: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The maximum number of results returned.
        # Default value: 20.
        self.page_size = page_size
        # The list of template details.
        self.template_list = template_list
        # The total number of records.
        self.total = total

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

        result['TemplateList'] = []
        if self.template_list is not None:
            for k1 in self.template_list:
                result['TemplateList'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.template_list = []
        if m.get('TemplateList') is not None:
            for k1 in m.get('TemplateList'):
                temp_model = main_models.DescribeAdvancedQueryTemplateResponseBodyTemplatePageTemplateList()
                self.template_list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeAdvancedQueryTemplateResponseBodyTemplatePageTemplateList(DaraModel):
    def __init__(
        self,
        simple_query: bool = None,
        template_id: str = None,
        template_name: str = None,
        template_sql: str = None,
    ):
        # Indicates whether the simple query mode is enabled.
        self.simple_query = simple_query
        # The template ID.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The query statement.
        self.template_sql = template_sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.simple_query is not None:
            result['SimpleQuery'] = self.simple_query

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_sql is not None:
            result['TemplateSql'] = self.template_sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SimpleQuery') is not None:
            self.simple_query = m.get('SimpleQuery')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateSql') is not None:
            self.template_sql = m.get('TemplateSql')

        return self

