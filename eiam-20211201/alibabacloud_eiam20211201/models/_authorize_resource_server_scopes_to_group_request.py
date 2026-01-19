# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AuthorizeResourceServerScopesToGroupRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        client_token: str = None,
        group_id: str = None,
        instance_id: str = None,
        resource_server_scope_ids: List[str] = None,
    ):
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.client_token = client_token
        # 组ID。
        # 
        # This parameter is required.
        self.group_id = group_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_server_scope_ids is not None:
            result['ResourceServerScopeIds'] = self.resource_server_scope_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceServerScopeIds') is not None:
            self.resource_server_scope_ids = m.get('ResourceServerScopeIds')

        return self

