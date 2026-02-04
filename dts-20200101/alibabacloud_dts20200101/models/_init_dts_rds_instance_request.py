# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitDtsRdsInstanceRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        endpoint_cen_id: str = None,
        endpoint_instance_id: str = None,
        endpoint_instance_type: str = None,
        endpoint_region: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the data synchronization task.
        self.dts_instance_id = dts_instance_id
        # If the node is a self-managed MySQL database that is connected over CEN, you must specify the ID of the CEN instance.
        # 
        # > You must specify the **EndpointRegion** and **EndpointInstanceId** parameters or the EndpointCenId parameter based on the type of the node.
        self.endpoint_cen_id = endpoint_cen_id
        # If the node is an ApsaraDB RDS for MySQL instance, you must specify the ID of the ApsaraDB RDS for MySQL instance.
        # 
        # > *   You must also specify the **EndpointRegion** parameter.
        # >*   You must specify the EndpointInstanceId parameter or the **EndpointCenId** parameter based on the type of the node.
        self.endpoint_instance_id = endpoint_instance_id
        # The type of the node. Valid values:
        # 
        # *   **RDS**: an ApsaraDB RDS for MySQL instance
        # *   **CEN**: a self-managed MySQL database that is connected over CEN
        self.endpoint_instance_type = endpoint_instance_type
        # If the node is an ApsaraDB RDS for MySQL instance, you must specify the region in which the ApsaraDB RDS for MySQL instance resides.
        # 
        # > *   You must also specify the **EndpointInstanceId** parameter.
        # >*   You must specify the EndpointRegion parameter or the **EndpointCenId** parameter based on the type of the node.
        self.endpoint_region = endpoint_region
        # The ID of the region in which the active geo-redundancy database cluster resides.
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.endpoint_cen_id is not None:
            result['EndpointCenId'] = self.endpoint_cen_id

        if self.endpoint_instance_id is not None:
            result['EndpointInstanceId'] = self.endpoint_instance_id

        if self.endpoint_instance_type is not None:
            result['EndpointInstanceType'] = self.endpoint_instance_type

        if self.endpoint_region is not None:
            result['EndpointRegion'] = self.endpoint_region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('EndpointCenId') is not None:
            self.endpoint_cen_id = m.get('EndpointCenId')

        if m.get('EndpointInstanceId') is not None:
            self.endpoint_instance_id = m.get('EndpointInstanceId')

        if m.get('EndpointInstanceType') is not None:
            self.endpoint_instance_type = m.get('EndpointInstanceType')

        if m.get('EndpointRegion') is not None:
            self.endpoint_region = m.get('EndpointRegion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

