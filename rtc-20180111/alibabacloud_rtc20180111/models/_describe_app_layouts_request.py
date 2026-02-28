# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeAppLayoutsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        condition: main_models.DescribeAppLayoutsRequestCondition = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.condition = condition
        self.page_num = page_num
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
            temp_model = main_models.DescribeAppLayoutsRequestCondition()
            self.condition = temp_model.from_map(m.get('Condition'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class DescribeAppLayoutsRequestCondition(DaraModel):
    def __init__(
        self,
        layout_id: str = None,
        name: str = None,
    ):
        self.layout_id = layout_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

