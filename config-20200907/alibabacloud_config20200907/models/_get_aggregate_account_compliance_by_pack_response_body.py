# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetAggregateAccountComplianceByPackResponseBody(DaraModel):
    def __init__(
        self,
        account_compliance_result: main_models.GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResult = None,
        request_id: str = None,
    ):
        # The compliance evaluation results of member accounts for which the compliance package takes effect in an account group.
        self.account_compliance_result = account_compliance_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.account_compliance_result:
            self.account_compliance_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_compliance_result is not None:
            result['AccountComplianceResult'] = self.account_compliance_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountComplianceResult') is not None:
            temp_model = main_models.GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResult()
            self.account_compliance_result = temp_model.from_map(m.get('AccountComplianceResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResult(DaraModel):
    def __init__(
        self,
        account_compliances: List[main_models.GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResultAccountCompliances] = None,
        compliance_pack_id: str = None,
        non_compliant_count: int = None,
        total_count: int = None,
    ):
        # The compliance evaluation result of member accounts.
        self.account_compliances = account_compliances
        # The ID of the compliance package.
        self.compliance_pack_id = compliance_pack_id
        # The number of non-compliant member accounts.
        self.non_compliant_count = non_compliant_count
        # The total number of member accounts.
        self.total_count = total_count

    def validate(self):
        if self.account_compliances:
            for v1 in self.account_compliances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountCompliances'] = []
        if self.account_compliances is not None:
            for k1 in self.account_compliances:
                result['AccountCompliances'].append(k1.to_map() if k1 else None)

        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_compliances = []
        if m.get('AccountCompliances') is not None:
            for k1 in m.get('AccountCompliances'):
                temp_model = main_models.GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResultAccountCompliances()
                self.account_compliances.append(temp_model.from_map(k1))

        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResultAccountCompliances(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        compliance_type: str = None,
    ):
        # The ID of the member account in the account group.
        self.account_id = account_id
        # The name of the member account in the account group.
        self.account_name = account_name
        # The compliance evaluation result. Valid values:
        # 
        # *   COMPLIANT: The resource was evaluated as compliant.
        # *   NON_COMPLIANT: The resource was evaluated as incompliant.
        # *   NOT_APPLICABLE: The rule did not apply to your resource.
        # *   INSUFFICIENT_DATA: No resource data was available.
        self.compliance_type = compliance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        return self

