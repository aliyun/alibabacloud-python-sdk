# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartServiceInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # A client token to ensure the idempotence of the request. The token must be unique for each request. The token can contain only ASCII characters and cannot be longer than 64 characters.
        self.client_token = client_token
        # The region ID of the service instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # Call the [ListServiceInstances](https://help.aliyun.com/document_detail/396200.html) operation to obtain the service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

