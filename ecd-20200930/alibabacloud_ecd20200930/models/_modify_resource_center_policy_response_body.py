# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ModifyResourceCenterPolicyResponseBody(DaraModel):
    def __init__(
        self,
        modify_results: List[main_models.ModifyResourceCenterPolicyResponseBodyModifyResults] = None,
        request_id: str = None,
    ):
        # The modification results.
        self.modify_results = modify_results
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.modify_results:
            for v1 in self.modify_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModifyResults'] = []
        if self.modify_results is not None:
            for k1 in self.modify_results:
                result['ModifyResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.modify_results = []
        if m.get('ModifyResults') is not None:
            for k1 in m.get('ModifyResults'):
                temp_model = main_models.ModifyResourceCenterPolicyResponseBodyModifyResults()
                self.modify_results.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyResourceCenterPolicyResponseBodyModifyResults(DaraModel):
    def __init__(
        self,
        check_result: bool = None,
        resource_id: str = None,
    ):
        # The verification result.
        self.check_result = check_result
        # The resource ID.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_result is not None:
            result['CheckResult'] = self.check_result

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

