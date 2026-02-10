# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSimilarEventScenariosResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scenarios: List[main_models.DescribeSimilarEventScenariosResponseBodyScenarios] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The scenarios in which alerts triggered by the same rule or rules of the same type are handled.
        self.scenarios = scenarios

    def validate(self):
        if self.scenarios:
            for v1 in self.scenarios:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Scenarios'] = []
        if self.scenarios is not None:
            for k1 in self.scenarios:
                result['Scenarios'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scenarios = []
        if m.get('Scenarios') is not None:
            for k1 in m.get('Scenarios'):
                temp_model = main_models.DescribeSimilarEventScenariosResponseBodyScenarios()
                self.scenarios.append(temp_model.from_map(k1))

        return self

class DescribeSimilarEventScenariosResponseBodyScenarios(DaraModel):
    def __init__(
        self,
        code: str = None,
    ):
        # The code of the scenario. Valid values:
        # 
        # *   **default**: the same alert type
        # *   **same_file_content**: the same file content rule.
        # *   **same_ip**: the same IP address rule.
        # *   **same_url**: the same URL rule.
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        return self

