# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthorizeResourceServerToClientRequest(DaraModel):
    def __init__(
        self,
        client_application_id: str = None,
        instance_id: str = None,
        resource_server_application_id: str = None,
    ):
        # The unique ID of the client application.
        # 
        # This parameter is required.
        self.client_application_id = client_application_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the resource server application.
        # 
        # This parameter is required.
        self.resource_server_application_id = resource_server_application_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientApplicationId') is not None:
            self.client_application_id = m.get('ClientApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceServerApplicationId') is not None:
            self.resource_server_application_id = m.get('ResourceServerApplicationId')

        return self

