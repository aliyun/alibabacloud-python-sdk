# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSnapshotLinksRequest(DaraModel):
    def __init__(
        self,
        disk_ids: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snapshot_link_ids: str = None,
    ):
        # The IDs of disks. You can specify up to 100 disk IDs at a time. The DiskIds parameter is a JSON array. Separate multiple IDs with commas (,).
        self.disk_ids = disk_ids
        # The instance ID.
        self.instance_id = instance_id
        # The maximum number of entries per page for a paged query. Maximum value: 100.
        # Default value:
        # - If this parameter is not specified or is set to a value less than 10, the default value is 10.
        # - If this parameter is set to a value greater than 100, the default value is 100.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the disk status list. Minimum value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page for a paged query. Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the disk. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IDs of snapshot chains. You can specify up to 100 snapshot chain IDs at a time. The SnapshotLinkIds parameter is a JSON array. Separate multiple IDs with commas (,).
        self.snapshot_link_ids = snapshot_link_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.snapshot_link_ids is not None:
            result['SnapshotLinkIds'] = self.snapshot_link_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SnapshotLinkIds') is not None:
            self.snapshot_link_ids = m.get('SnapshotLinkIds')

        return self

