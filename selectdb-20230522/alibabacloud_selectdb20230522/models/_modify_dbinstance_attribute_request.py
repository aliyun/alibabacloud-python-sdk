# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        instance_attribute_type: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        value: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The attribute to modify. Valid values:
        # 
        # - **MaintainTime**: modifies the O&M time. The format is hh:mm-hh:mm.
        # 
        # - **DBInstanceDescription**: modifies the instance description.
        # 
        # This parameter is required.
        self.instance_attribute_type = instance_attribute_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The new value of the attribute. Valid values:
        # 
        # - If InstanceAttributeType is set to MaintainTime, set this parameter to a time range such as 00:00-06:00.
        # 
        # - If InstanceAttributeType is set to DBInstanceDescription, set this parameter to a description such as testdb.
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

