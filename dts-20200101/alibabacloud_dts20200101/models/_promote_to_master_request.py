# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PromoteToMasterRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        master_db_instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        slave_db_instance_id: str = None,
    ):
        self.instance_id = instance_id
        self.master_db_instance_id = master_db_instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.slave_db_instance_id = slave_db_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.master_db_instance_id is not None:
            result['MasterDbInstanceId'] = self.master_db_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.slave_db_instance_id is not None:
            result['SlaveDbInstanceId'] = self.slave_db_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MasterDbInstanceId') is not None:
            self.master_db_instance_id = m.get('MasterDbInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlaveDbInstanceId') is not None:
            self.slave_db_instance_id = m.get('SlaveDbInstanceId')

        return self

