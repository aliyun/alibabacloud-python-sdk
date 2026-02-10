# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageBaselineDetailResponseBody(DaraModel):
    def __init__(
        self,
        baseline_detail: main_models.DescribeImageBaselineDetailResponseBodyBaselineDetail = None,
        request_id: str = None,
    ):
        # The details about the image baseline.
        self.baseline_detail = baseline_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.baseline_detail:
            self.baseline_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_detail is not None:
            result['BaselineDetail'] = self.baseline_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineDetail') is not None:
            temp_model = main_models.DescribeImageBaselineDetailResponseBodyBaselineDetail()
            self.baseline_detail = temp_model.from_map(m.get('BaselineDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageBaselineDetailResponseBodyBaselineDetail(DaraModel):
    def __init__(
        self,
        advice: str = None,
        baseline_class_alias: str = None,
        baseline_item_alias: str = None,
        baseline_item_key: str = None,
        baseline_name_alias: str = None,
        description: str = None,
        level: str = None,
        prompt: str = None,
        result_id: str = None,
    ):
        # The suggestion for the management of the risk item.
        self.advice = advice
        # The alias of the baseline type.
        self.baseline_class_alias = baseline_class_alias
        # The alias of the baseline check item.
        self.baseline_item_alias = baseline_item_alias
        # The key of the baseline check item.
        self.baseline_item_key = baseline_item_key
        # The alias of the baseline.
        self.baseline_name_alias = baseline_name_alias
        # The description of the risk item.
        self.description = description
        # The risk level of the baseline check item. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.level = level
        # The issue that is detected by using the baseline.
        self.prompt = prompt
        # The ID of the asynchronous request.
        self.result_id = result_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice is not None:
            result['Advice'] = self.advice

        if self.baseline_class_alias is not None:
            result['BaselineClassAlias'] = self.baseline_class_alias

        if self.baseline_item_alias is not None:
            result['BaselineItemAlias'] = self.baseline_item_alias

        if self.baseline_item_key is not None:
            result['BaselineItemKey'] = self.baseline_item_key

        if self.baseline_name_alias is not None:
            result['BaselineNameAlias'] = self.baseline_name_alias

        if self.description is not None:
            result['Description'] = self.description

        if self.level is not None:
            result['Level'] = self.level

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.result_id is not None:
            result['ResultId'] = self.result_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')

        if m.get('BaselineClassAlias') is not None:
            self.baseline_class_alias = m.get('BaselineClassAlias')

        if m.get('BaselineItemAlias') is not None:
            self.baseline_item_alias = m.get('BaselineItemAlias')

        if m.get('BaselineItemKey') is not None:
            self.baseline_item_key = m.get('BaselineItemKey')

        if m.get('BaselineNameAlias') is not None:
            self.baseline_name_alias = m.get('BaselineNameAlias')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')

        return self

