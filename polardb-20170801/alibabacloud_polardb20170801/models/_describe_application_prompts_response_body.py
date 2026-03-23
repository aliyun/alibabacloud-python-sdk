# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationPromptsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeApplicationPromptsResponseBodyItems] = None,
        page_number: str = None,
        page_record_count: str = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeApplicationPromptsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeApplicationPromptsResponseBodyItems(DaraModel):
    def __init__(
        self,
        prompt_enabled: int = None,
        prompt_id: str = None,
        prompt_name: str = None,
        prompt_type: str = None,
        prompt_value: str = None,
    ):
        self.prompt_enabled = prompt_enabled
        self.prompt_id = prompt_id
        self.prompt_name = prompt_name
        self.prompt_type = prompt_type
        self.prompt_value = prompt_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prompt_enabled is not None:
            result['PromptEnabled'] = self.prompt_enabled

        if self.prompt_id is not None:
            result['PromptId'] = self.prompt_id

        if self.prompt_name is not None:
            result['PromptName'] = self.prompt_name

        if self.prompt_type is not None:
            result['PromptType'] = self.prompt_type

        if self.prompt_value is not None:
            result['PromptValue'] = self.prompt_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromptEnabled') is not None:
            self.prompt_enabled = m.get('PromptEnabled')

        if m.get('PromptId') is not None:
            self.prompt_id = m.get('PromptId')

        if m.get('PromptName') is not None:
            self.prompt_name = m.get('PromptName')

        if m.get('PromptType') is not None:
            self.prompt_type = m.get('PromptType')

        if m.get('PromptValue') is not None:
            self.prompt_value = m.get('PromptValue')

        return self

