# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCustomRoutingEndpointGroupDestinationsRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        endpoint_group_id: str = None,
        from_port: int = None,
        listener_id: str = None,
        page_number: int = None,
        page_size: int = None,
        protocols: List[str] = None,
        region_id: str = None,
        to_port: int = None,
    ):
        # The ID of the GA instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The ID of the endpoint group.
        self.endpoint_group_id = endpoint_group_id
        # The start port of the backend service port range of the endpoint group.
        # 
        # Valid values: **1** to **65499**. The **FromPort** value must be smaller than or equal to the **ToPort** value.
        self.from_port = from_port
        # The ID of the listener.
        self.listener_id = listener_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The backend service protocols of the endpoint group. Valid values:
        # 
        # - **TCP**: TCP.
        # - **UDP**: UDP.
        # - **TCP,UDP**: TCP and UDP.
        # 
        # If this parameter is empty, all types of protocols are queried.
        # 
        # You can specify up to 10 protocols.
        self.protocols = protocols
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The end port of the backend service port range of the endpoint group.
        # 
        # Valid values: **1** to **65499**. The **FromPort** value must be smaller than or equal to the **ToPort** value.
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.from_port is not None:
            result['FromPort'] = self.from_port

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.to_port is not None:
            result['ToPort'] = self.to_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')

        return self

