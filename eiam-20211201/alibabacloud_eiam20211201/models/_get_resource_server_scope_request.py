# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceServerScopeRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        instance_id: str = None,
        resource_server_scope_id: str = None,
    ):
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # ResourceServer下Scope唯一标识。
        # 
        # This parameter is required.
        self.resource_server_scope_id = resource_server_scope_id

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

        if self.resource_server_scope_id is not None:
            result['ResourceServerScopeId'] = self.resource_server_scope_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceServerScopeId') is not None:
            self.resource_server_scope_id = m.get('ResourceServerScopeId')

        return self

