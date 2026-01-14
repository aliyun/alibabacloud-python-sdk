# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceManagedControlRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service_managed: bool = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The region ID of the GA instance. Set the value to cn-hangzhou.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource whose control mode you want to change.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource whose control mode you want to change.
        # 
        # Set the value to **Accelerator**, which specifies a standard GA instance.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The control mode of the resource.
        # 
        # Set the value to **false**, which changes the control mode of the resource from managed mode to unmanaged mode.
        # 
        # >  You can change the control mode only from managed mode to unmanaged mode.
        self.service_managed = service_managed

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

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        return self

