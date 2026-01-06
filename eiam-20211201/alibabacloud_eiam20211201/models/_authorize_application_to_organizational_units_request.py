# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AuthorizeApplicationToOrganizationalUnitsRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_role_id: str = None,
        instance_id: str = None,
        organizational_unit_ids: List[str] = None,
    ):
        # The ID of the application on which you want to grant permissions.
        # 
        # This parameter is required.
        self.application_id = application_id
        # 应用角色ID。
        self.application_role_id = application_role_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IDs of the organizations to which you want to grant permissions. You can grant permissions to a maximum of 100 organizations at a time.
        # 
        # This parameter is required.
        self.organizational_unit_ids = organizational_unit_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_role_id is not None:
            result['ApplicationRoleId'] = self.application_role_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationRoleId') is not None:
            self.application_role_id = m.get('ApplicationRoleId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')

        return self

