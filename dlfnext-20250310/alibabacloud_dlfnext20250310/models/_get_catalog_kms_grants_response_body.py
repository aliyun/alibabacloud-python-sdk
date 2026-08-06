# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCatalogKmsGrantsResponseBody(DaraModel):
    def __init__(
        self,
        data_access_role_arn: str = None,
        key_policy_statement: str = None,
        region: str = None,
        workflow_role_arn: str = None,
    ):
        # The ARN of the RAM role used by DLF to access catalog data. When configuring the KMS key policy, you must grant this role permissions to use the customer master key.
        self.data_access_role_arn = data_access_role_arn
        # The authorization statement that must be added to the customer master key policy. This statement grants the DLF data access role corresponding to dataAccessRoleArn the KMS permissions required for data encryption and decryption.
        self.key_policy_statement = key_policy_statement
        # The region ID to which the catalog belongs.
        self.region = region
        # The DLF workflow role ARN. In the current version, the workflow role is not granted customer master key access permissions based on the least privilege principle. Therefore, this field returns an empty value.
        self.workflow_role_arn = workflow_role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_access_role_arn is not None:
            result['dataAccessRoleArn'] = self.data_access_role_arn

        if self.key_policy_statement is not None:
            result['keyPolicyStatement'] = self.key_policy_statement

        if self.region is not None:
            result['region'] = self.region

        if self.workflow_role_arn is not None:
            result['workflowRoleArn'] = self.workflow_role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataAccessRoleArn') is not None:
            self.data_access_role_arn = m.get('dataAccessRoleArn')

        if m.get('keyPolicyStatement') is not None:
            self.key_policy_statement = m.get('keyPolicyStatement')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('workflowRoleArn') is not None:
            self.workflow_role_arn = m.get('workflowRoleArn')

        return self

