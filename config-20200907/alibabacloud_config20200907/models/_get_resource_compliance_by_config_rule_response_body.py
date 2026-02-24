# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetResourceComplianceByConfigRuleResponseBody(DaraModel):
    def __init__(
        self,
        compliance_result: main_models.GetResourceComplianceByConfigRuleResponseBodyComplianceResult = None,
        request_id: str = None,
    ):
        self.compliance_result = compliance_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_result:
            self.compliance_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_result is not None:
            result['ComplianceResult'] = self.compliance_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResult') is not None:
            temp_model = main_models.GetResourceComplianceByConfigRuleResponseBodyComplianceResult()
            self.compliance_result = temp_model.from_map(m.get('ComplianceResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetResourceComplianceByConfigRuleResponseBodyComplianceResult(DaraModel):
    def __init__(
        self,
        compliances: List[main_models.GetResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances] = None,
        total_count: int = None,
    ):
        self.compliances = compliances
        self.total_count = total_count

    def validate(self):
        if self.compliances:
            for v1 in self.compliances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Compliances'] = []
        if self.compliances is not None:
            for k1 in self.compliances:
                result['Compliances'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliances = []
        if m.get('Compliances') is not None:
            for k1 in m.get('Compliances'):
                temp_model = main_models.GetResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances()
                self.compliances.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances(DaraModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

