# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateNetworkAccessEndpointRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        network_access_endpoint_name: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        vpc_region_id: str = None,
    ):
        # Ensures the idempotency of the request. Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters. For more information, see [How to ensure idempotence](https://www.alibabacloud.com/help/en/ecs/developer-reference/how-to-ensure-idempotence).
        self.client_token = client_token
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Network access endpoint name.
        # 
        # This parameter is required.
        self.network_access_endpoint_name = network_access_endpoint_name
        # List of specified vSwitches connected to the network access endpoint.
        self.v_switch_ids = v_switch_ids
        # VPC ID connected to the network access endpoint.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # Region of the VPC ID connected to the network access endpoint.
        # 
        # This parameter is required.
        self.vpc_region_id = vpc_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_access_endpoint_name is not None:
            result['NetworkAccessEndpointName'] = self.network_access_endpoint_name

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkAccessEndpointName') is not None:
            self.network_access_endpoint_name = m.get('NetworkAccessEndpointName')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        return self

