# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePerformanceViewShrinkRequest(DaraModel):
    def __init__(
        self,
        create_from_view_type: str = None,
        dbcluster_id: str = None,
        fill_origin_view_keys: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        view_detail_shrink: str = None,
        view_name: str = None,
    ):
        # The type of the view.
        self.create_from_view_type = create_from_view_type
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/612397.html) operation to query the IDs of all AnalyticDB for MySQL Data Lakehouse Edition clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to populate the names of the metrics in the original monitoring view when you view the monitoring view. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.fill_origin_view_keys = fill_origin_view_keys
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The information about the monitoring view.
        # 
        # This parameter is required.
        self.view_detail_shrink = view_detail_shrink
        # The name of the view.
        # 
        # This parameter is required.
        self.view_name = view_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_from_view_type is not None:
            result['CreateFromViewType'] = self.create_from_view_type

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.fill_origin_view_keys is not None:
            result['FillOriginViewKeys'] = self.fill_origin_view_keys

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.view_detail_shrink is not None:
            result['ViewDetail'] = self.view_detail_shrink

        if self.view_name is not None:
            result['ViewName'] = self.view_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateFromViewType') is not None:
            self.create_from_view_type = m.get('CreateFromViewType')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FillOriginViewKeys') is not None:
            self.fill_origin_view_keys = m.get('FillOriginViewKeys')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ViewDetail') is not None:
            self.view_detail_shrink = m.get('ViewDetail')

        if m.get('ViewName') is not None:
            self.view_name = m.get('ViewName')

        return self

