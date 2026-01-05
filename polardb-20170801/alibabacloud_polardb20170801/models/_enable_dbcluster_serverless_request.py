# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableDBClusterServerlessRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scale_ap_ro_num_max: str = None,
        scale_ap_ro_num_min: str = None,
        scale_max: str = None,
        scale_min: str = None,
        scale_ro_num_max: str = None,
        scale_ro_num_min: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The maximum number of stable AP read-only nodes. Valid values: 0 to 7.
        self.scale_ap_ro_num_max = scale_ap_ro_num_max
        # The minimum number of stable AP read-only nodes. Valid values: 0 to 7.
        self.scale_ap_ro_num_min = scale_ap_ro_num_min
        # The maximum number of PCUs per node for scaling. Valid values: 1 to 8 PCUs.
        self.scale_max = scale_max
        # The minimum number of PolarDB capacity units (PCUs) per node for scaling. Valid values: 1 to 8 PCUs.
        self.scale_min = scale_min
        # The maximum number of read-only nodes for scaling. Valid values: 0 to 7.
        self.scale_ro_num_max = scale_ro_num_max
        # The minimum number of read-only nodes for scaling. Valid values: 0 to 7.
        self.scale_ro_num_min = scale_ro_num_min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scale_ap_ro_num_max is not None:
            result['ScaleApRoNumMax'] = self.scale_ap_ro_num_max

        if self.scale_ap_ro_num_min is not None:
            result['ScaleApRoNumMin'] = self.scale_ap_ro_num_min

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.scale_ro_num_max is not None:
            result['ScaleRoNumMax'] = self.scale_ro_num_max

        if self.scale_ro_num_min is not None:
            result['ScaleRoNumMin'] = self.scale_ro_num_min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScaleApRoNumMax') is not None:
            self.scale_ap_ro_num_max = m.get('ScaleApRoNumMax')

        if m.get('ScaleApRoNumMin') is not None:
            self.scale_ap_ro_num_min = m.get('ScaleApRoNumMin')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('ScaleRoNumMax') is not None:
            self.scale_ro_num_max = m.get('ScaleRoNumMax')

        if m.get('ScaleRoNumMin') is not None:
            self.scale_ro_num_min = m.get('ScaleRoNumMin')

        return self

