# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class BatchCreateLlmTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.BatchCreateLlmTemplatesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.BatchCreateLlmTemplatesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchCreateLlmTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        llm_template_ids: List[str] = None,
        skipped_items: List[main_models.BatchCreateLlmTemplatesResponseBodyDataSkippedItems] = None,
        success_count: int = None,
        total_count: int = None,
    ):
        self.llm_template_ids = llm_template_ids
        self.skipped_items = skipped_items
        self.success_count = success_count
        self.total_count = total_count

    def validate(self):
        if self.skipped_items:
            for v1 in self.skipped_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.llm_template_ids is not None:
            result['LlmTemplateIds'] = self.llm_template_ids

        result['SkippedItems'] = []
        if self.skipped_items is not None:
            for k1 in self.skipped_items:
                result['SkippedItems'].append(k1.to_map() if k1 else None)

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LlmTemplateIds') is not None:
            self.llm_template_ids = m.get('LlmTemplateIds')

        self.skipped_items = []
        if m.get('SkippedItems') is not None:
            for k1 in m.get('SkippedItems'):
                temp_model = main_models.BatchCreateLlmTemplatesResponseBodyDataSkippedItems()
                self.skipped_items.append(temp_model.from_map(k1))

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class BatchCreateLlmTemplatesResponseBodyDataSkippedItems(DaraModel):
    def __init__(
        self,
        llm_code: str = None,
        reason: str = None,
    ):
        self.llm_code = llm_code
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.llm_code is not None:
            result['LlmCode'] = self.llm_code

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LlmCode') is not None:
            self.llm_code = m.get('LlmCode')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

