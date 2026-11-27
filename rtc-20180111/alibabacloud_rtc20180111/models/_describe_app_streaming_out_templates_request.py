# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeAppStreamingOutTemplatesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        condition: main_models.DescribeAppStreamingOutTemplatesRequestCondition = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # Application ID, created and queried through the console. Only a single ID is supported.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Search condition.
        self.condition = condition
        # Page number. By default, page 1 is queried.
        self.page_num = page_num
        # Number of entries per page. The default value is 10.
        self.page_size = page_size

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.condition is not None:
            result['Condition'] = self.condition.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Condition') is not None:
            temp_model = main_models.DescribeAppStreamingOutTemplatesRequestCondition()
            self.condition = temp_model.from_map(m.get('Condition'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class DescribeAppStreamingOutTemplatesRequestCondition(DaraModel):
    def __init__(
        self,
        name: str = None,
        template_id: str = None,
    ):
        # Template Name.
        self.name = name
        # Template ID.
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

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

