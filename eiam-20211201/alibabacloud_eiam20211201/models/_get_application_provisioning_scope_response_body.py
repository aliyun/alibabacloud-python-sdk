# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetApplicationProvisioningScopeResponseBody(DaraModel):
    def __init__(
        self,
        application_provisioning_scope: main_models.GetApplicationProvisioningScopeResponseBodyApplicationProvisioningScope = None,
        request_id: str = None,
    ):
        # The scope of account synchronization.
        self.application_provisioning_scope = application_provisioning_scope
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application_provisioning_scope:
            self.application_provisioning_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_provisioning_scope is not None:
            result['ApplicationProvisioningScope'] = self.application_provisioning_scope.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationProvisioningScope') is not None:
            temp_model = main_models.GetApplicationProvisioningScopeResponseBodyApplicationProvisioningScope()
            self.application_provisioning_scope = temp_model.from_map(m.get('ApplicationProvisioningScope'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationProvisioningScopeResponseBodyApplicationProvisioningScope(DaraModel):
    def __init__(
        self,
        group_ids: List[str] = None,
        max_quota: int = None,
        organizational_unit_ids: List[str] = None,
        used_quota: int = None,
    ):
        # Synchronize the list of authorized groups.
        self.group_ids = group_ids
        # Instance Indicates the maximum quota number of authorized agents.
        self.max_quota = max_quota
        # The list of organizational units that are authorized for account synchronization.
        self.organizational_unit_ids = organizational_unit_ids
        # Indicates the quota number of used authorized agents.
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.max_quota is not None:
            result['MaxQuota'] = self.max_quota

        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids

        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('MaxQuota') is not None:
            self.max_quota = m.get('MaxQuota')

        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')

        if m.get('UsedQuota') is not None:
            self.used_quota = m.get('UsedQuota')

        return self

