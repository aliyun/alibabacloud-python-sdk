# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class CheckModelFeatureFGFeatureResponseBody(DaraModel):
    def __init__(
        self,
        fgcheck_results: List[main_models.CheckModelFeatureFGFeatureResponseBodyFGCheckResults] = None,
        request_id: str = None,
    ):
        self.fgcheck_results = fgcheck_results
        self.request_id = request_id

    def validate(self):
        if self.fgcheck_results:
            for v1 in self.fgcheck_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FGCheckResults'] = []
        if self.fgcheck_results is not None:
            for k1 in self.fgcheck_results:
                result['FGCheckResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fgcheck_results = []
        if m.get('FGCheckResults') is not None:
            for k1 in m.get('FGCheckResults'):
                temp_model = main_models.CheckModelFeatureFGFeatureResponseBodyFGCheckResults()
                self.fgcheck_results.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CheckModelFeatureFGFeatureResponseBodyFGCheckResults(DaraModel):
    def __init__(
        self,
        message: str = None,
        rule_code: str = None,
        status: bool = None,
    ):
        self.message = message
        self.rule_code = rule_code
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.rule_code is not None:
            result['RuleCode'] = self.rule_code

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RuleCode') is not None:
            self.rule_code = m.get('RuleCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

