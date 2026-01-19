# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RevokeResourceServerScopesFromClientRequest(DaraModel):
    def __init__(
        self,
        client_application_id: str = None,
        instance_id: str = None,
        resource_server_application_id: str = None,
        resource_server_scope_ids: List[str] = None,
    ):
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.client_application_id = client_application_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.resource_server_application_id = resource_server_application_id
        # ResourceServer权限ID。
        # 
        # This parameter is required.
        self.resource_server_scope_ids = resource_server_scope_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_application_id is not None:
            result['ClientApplicationId'] = self.client_application_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_server_application_id is not None:
            result['ResourceServerApplicationId'] = self.resource_server_application_id

        if self.resource_server_scope_ids is not None:
            result['ResourceServerScopeIds'] = self.resource_server_scope_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientApplicationId') is not None:
            self.client_application_id = m.get('ClientApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceServerApplicationId') is not None:
            self.resource_server_application_id = m.get('ResourceServerApplicationId')

        if m.get('ResourceServerScopeIds') is not None:
            self.resource_server_scope_ids = m.get('ResourceServerScopeIds')

        return self

