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
        # The ID of the ResourceServer application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # A client-generated token that you must make unique among different requests to ensure idempotence. ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://www.alibabacloud.com/help/zh/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # A list of Scope permission IDs under the ResourceServer.
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

