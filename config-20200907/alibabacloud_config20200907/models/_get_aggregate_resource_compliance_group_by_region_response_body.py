# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetAggregateResourceComplianceGroupByRegionResponseBody(DaraModel):
    def __init__(
        self,
        compliance_result: main_models.GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResult = None,
        request_id: str = None,
    ):
        # The queried evaluation results.
        self.compliance_result = compliance_result
        # The request ID.
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
            temp_model = main_models.GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResult()
            self.compliance_result = temp_model.from_map(m.get('ComplianceResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResult(DaraModel):
    def __init__(
        self,
        compliance_result_list: List[main_models.GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultList] = None,
    ):
        # The evaluation results grouped by region.
        self.compliance_result_list = compliance_result_list

    def validate(self):
        if self.compliance_result_list:
            for v1 in self.compliance_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComplianceResultList'] = []
        if self.compliance_result_list is not None:
            for k1 in self.compliance_result_list:
                result['ComplianceResultList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_result_list = []
        if m.get('ComplianceResultList') is not None:
            for k1 in m.get('ComplianceResultList'):
                temp_model = main_models.GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultList()
                self.compliance_result_list.append(temp_model.from_map(k1))

        return self

class GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultList(DaraModel):
    def __init__(
        self,
        compliances: List[main_models.GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultListCompliances] = None,
        region_id: str = None,
    ):
        # The queried evaluation results.
        self.compliances = compliances
        # The region ID of the evaluated resource.
        self.region_id = region_id

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliances = []
        if m.get('Compliances') is not None:
            for k1 in m.get('Compliances'):
                temp_model = main_models.GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultListCompliances()
                self.compliances.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultListCompliances(DaraModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        # The evaluation result. Valid values:
        # 
        # *   COMPLIANT: The resource is evaluated as compliant.
        # *   NON_COMPLIANT: The resource is evaluated as non-compliant.
        # *   NOT_APPLICABLE: The rule does not apply to the resource.
        # *   INSUFFICIENT_DATA: No data is available.
        self.compliance_type = compliance_type
        # The total number of evaluation results.
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

