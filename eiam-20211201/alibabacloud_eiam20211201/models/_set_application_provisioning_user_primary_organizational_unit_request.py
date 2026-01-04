# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetApplicationProvisioningUserPrimaryOrganizationalUnitRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        instance_id: str = None,
        user_primary_organizational_unit_id: str = None,
    ):
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 组织ID。
        # 
        # This parameter is required.
        self.user_primary_organizational_unit_id = user_primary_organizational_unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.user_primary_organizational_unit_id is not None:
            result['UserPrimaryOrganizationalUnitId'] = self.user_primary_organizational_unit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UserPrimaryOrganizationalUnitId') is not None:
            self.user_primary_organizational_unit_id = m.get('UserPrimaryOrganizationalUnitId')

        return self

