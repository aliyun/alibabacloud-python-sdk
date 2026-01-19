# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetApplicationResourceServerIdentifierRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        client_token: str = None,
        instance_id: str = None,
        resource_server_identifier: str = None,
    ):
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        self.client_token = client_token
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # ResourceServer唯一标识，对应ResourceServer受众
        # 
        # This parameter is required.
        self.resource_server_identifier = resource_server_identifier

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_server_identifier is not None:
            result['ResourceServerIdentifier'] = self.resource_server_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceServerIdentifier') is not None:
            self.resource_server_identifier = m.get('ResourceServerIdentifier')

        return self

