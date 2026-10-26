# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class AttachReviewersToReviewRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        principals: List[main_models.AttachReviewersToReviewRuleRequestPrincipals] = None,
        region_id: str = None,
        review_rule_id: int = None,
    ):
        # The ID of the Bastionhost instance.
        # > You can call the DescribeInstances operation to obtain the Bastionhost instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The information about the auditors to be associated with the audit policy.
        self.principals = principals
        # The region ID of the Bastionhost instance.
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the audit policy.
        # > You can invoke the ListReviewRules operation to obtain this parameter.
        # 
        # This parameter is required.
        self.review_rule_id = review_rule_id

    def validate(self):
        if self.principals:
            for v1 in self.principals:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Principals'] = []
        if self.principals is not None:
            for k1 in self.principals:
                result['Principals'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.review_rule_id is not None:
            result['ReviewRuleId'] = self.review_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.principals = []
        if m.get('Principals') is not None:
            for k1 in m.get('Principals'):
                temp_model = main_models.AttachReviewersToReviewRuleRequestPrincipals()
                self.principals.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReviewRuleId') is not None:
            self.review_rule_id = m.get('ReviewRuleId')

        return self

class AttachReviewersToReviewRuleRequestPrincipals(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
    ):
        # The ID of the RAM user or the ARN of the RAM role of the auditor to be associated. If PrincipalType is set to RamUser, specify the RAM user ID. If PrincipalType is set to RamRole, specify the ARN of the RAM role.
        self.principal_id = principal_id
        # The display name of the RAM user or RAM role of the associated auditor.
        self.principal_name = principal_name
        # The type of the auditor to be associated. Valid values:
        # 
        # - **RamUser**: Resource Access Management (RAM) user.
        # 
        # - **RamRole**: RAM role.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

