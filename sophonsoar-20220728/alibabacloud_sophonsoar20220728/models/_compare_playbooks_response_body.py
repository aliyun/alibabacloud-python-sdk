# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class ComparePlaybooksResponseBody(DaraModel):
    def __init__(
        self,
        compare_result: main_models.ComparePlaybooksResponseBodyCompareResult = None,
        request_id: str = None,
    ):
        # The comparison result.
        self.compare_result = compare_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.compare_result:
            self.compare_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compare_result is not None:
            result['CompareResult'] = self.compare_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareResult') is not None:
            temp_model = main_models.ComparePlaybooksResponseBodyCompareResult()
            self.compare_result = temp_model.from_map(m.get('CompareResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class ComparePlaybooksResponseBodyCompareResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        new: bool = None,
        same: bool = None,
    ):
        # The description of the comparison result.
        self.description = description
        # Indicates whether the second version provides more information than the first version. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.new = new
        # Indicates whether the configurations of the two versions are the same. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.same = same

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.new is not None:
            result['New'] = self.new

        if self.same is not None:
            result['Same'] = self.same

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('New') is not None:
            self.new = m.get('New')

        if m.get('Same') is not None:
            self.same = m.get('Same')

        return self

