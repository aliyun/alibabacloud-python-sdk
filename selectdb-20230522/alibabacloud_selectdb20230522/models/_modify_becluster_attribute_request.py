# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBEClusterAttributeRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        instance_attribute_type: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        value: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The attribute type of the instance. Set this parameter to DBInstanceDescription.
        # 
        # Valid values:
        # 
        # *   MaintainTime
        # *   DBInstanceDescription
        # 
        # This parameter is required.
        self.instance_attribute_type = instance_attribute_type
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The new name of the cluster.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.instance_attribute_type is not None:
            result['InstanceAttributeType'] = self.instance_attribute_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('InstanceAttributeType') is not None:
            self.instance_attribute_type = m.get('InstanceAttributeType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

