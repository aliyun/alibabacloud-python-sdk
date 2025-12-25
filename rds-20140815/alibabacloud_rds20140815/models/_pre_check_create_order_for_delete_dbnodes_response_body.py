# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class PreCheckCreateOrderForDeleteDBNodesResponseBody(DaraModel):
    def __init__(
        self,
        failures: main_models.PreCheckCreateOrderForDeleteDBNodesResponseBodyFailures = None,
        pre_check_result: bool = None,
        request_id: str = None,
    ):
        # The information about the failed order.
        self.failures = failures
        # The precheck result.
        self.pre_check_result = pre_check_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.failures:
            self.failures.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failures is not None:
            result['Failures'] = self.failures.to_map()

        if self.pre_check_result is not None:
            result['PreCheckResult'] = self.pre_check_result

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failures') is not None:
            temp_model = main_models.PreCheckCreateOrderForDeleteDBNodesResponseBodyFailures()
            self.failures = temp_model.from_map(m.get('Failures'))

        if m.get('PreCheckResult') is not None:
            self.pre_check_result = m.get('PreCheckResult')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PreCheckCreateOrderForDeleteDBNodesResponseBodyFailures(DaraModel):
    def __init__(
        self,
        failures: List[main_models.PreCheckCreateOrderForDeleteDBNodesResponseBodyFailuresFailures] = None,
    ):
        self.failures = failures

    def validate(self):
        if self.failures:
            for v1 in self.failures:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Failures'] = []
        if self.failures is not None:
            for k1 in self.failures:
                result['Failures'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failures = []
        if m.get('Failures') is not None:
            for k1 in m.get('Failures'):
                temp_model = main_models.PreCheckCreateOrderForDeleteDBNodesResponseBodyFailuresFailures()
                self.failures.append(temp_model.from_map(k1))

        return self

class PreCheckCreateOrderForDeleteDBNodesResponseBodyFailuresFailures(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The response code. Valid values:
        # 
        # *   **200**: success
        # *   **400**: client error
        # *   **401**: identity authentication failed
        # *   **404**: requested page not found
        # *   **500**: server error
        self.code = code
        # The returned message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

