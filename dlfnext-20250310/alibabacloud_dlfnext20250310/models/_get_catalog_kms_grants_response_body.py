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
        self.data_access_role_arn = data_access_role_arn
        self.key_policy_statement = key_policy_statement
        self.region = region
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

