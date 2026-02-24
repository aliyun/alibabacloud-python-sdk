# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetAggregateResourceComplianceByPackResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_compliance_result: main_models.GetAggregateResourceComplianceByPackResponseBodyResourceComplianceResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The compliance results of the resources in the compliance package.
        self.resource_compliance_result = resource_compliance_result

    def validate(self):
        if self.resource_compliance_result:
            self.resource_compliance_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_compliance_result is not None:
            result['ResourceComplianceResult'] = self.resource_compliance_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceComplianceResult') is not None:
            temp_model = main_models.GetAggregateResourceComplianceByPackResponseBodyResourceComplianceResult()
            self.resource_compliance_result = temp_model.from_map(m.get('ResourceComplianceResult'))

        return self

class GetAggregateResourceComplianceByPackResponseBodyResourceComplianceResult(DaraModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        compliant_count: int = None,
        ignored_count: int = None,
        insufficient_data_count: int = None,
        non_compliant_count: int = None,
        not_applicable_count: int = None,
        total_count: int = None,
    ):
        # The ID of the compliance package.
        self.compliance_pack_id = compliance_pack_id
        # The total number of compliant resources.
        self.compliant_count = compliant_count
        # The total number of ignored resources.
        self.ignored_count = ignored_count
        # The total number of resources for which the evaluation data is insufficient.
        self.insufficient_data_count = insufficient_data_count
        # The number of non-compliant resources.
        self.non_compliant_count = non_compliant_count
        # The total number of resources that are not applicable.
        self.not_applicable_count = not_applicable_count
        # The total number of resources evaluated by the compliance package.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.compliant_count is not None:
            result['CompliantCount'] = self.compliant_count

        if self.ignored_count is not None:
            result['IgnoredCount'] = self.ignored_count

        if self.insufficient_data_count is not None:
            result['InsufficientDataCount'] = self.insufficient_data_count

        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count

        if self.not_applicable_count is not None:
            result['NotApplicableCount'] = self.not_applicable_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('CompliantCount') is not None:
            self.compliant_count = m.get('CompliantCount')

        if m.get('IgnoredCount') is not None:
            self.ignored_count = m.get('IgnoredCount')

        if m.get('InsufficientDataCount') is not None:
            self.insufficient_data_count = m.get('InsufficientDataCount')

        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')

        if m.get('NotApplicableCount') is not None:
            self.not_applicable_count = m.get('NotApplicableCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

