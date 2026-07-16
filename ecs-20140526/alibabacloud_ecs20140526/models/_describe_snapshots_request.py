# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSnapshotsRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.DescribeSnapshotsRequestFilter] = None,
        category: str = None,
        disk_id: str = None,
        dry_run: bool = None,
        encrypted: bool = None,
        instance_id: str = None,
        kmskey_id: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snapshot_ids: str = None,
        snapshot_link_id: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        source_disk_type: str = None,
        status: str = None,
        tag: List[main_models.DescribeSnapshotsRequestTag] = None,
        usage: str = None,
    ):
        self.filter = filter
        # The category of the snapshot. Valid values:
        # - Standard: standard snapshot.
        # - Flash: local snapshot. This value is about to be deprecated. Local snapshots have been replaced by the snapshot instant access feature. The metric description is as follows:
        #   - If you used local snapshots before December 14, 2020, you can use this parameter. The parameter is active.
        #   - If you did not use local snapshots before December 14, 2020, you cannot use this parameter.
        # - archive: archive snapshot.
        # 
        # 
        # 
        # <props="china">For more information, see [Chinese site notice on snapshot service upgrade and new billing items on December 14](https://help.aliyun.com/noticelist/articleid/1060755542.html).
        self.category = category
        # The ID of the disk.
        self.disk_id = disk_id
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # - true: performs only a dry run. The system checks the request for potential issues, including invalid AccessKey pairs, unauthorized RAM users, and missing parameter values. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # - false (default): performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # Specifies whether to filter encrypted snapshots. Default value: false.
        self.encrypted = encrypted
        # The instance ID. Specify this parameter to query snapshot information of disks attached to the instance.
        self.instance_id = instance_id
        # The ID of the Key Management Service (KMS) key used by the data disk.
        self.kmskey_id = kmskey_id
        # The maximum number of entries per page for paging. Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token. Obtained from the response of the previous request.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter is about to be deprecated. Use NextToken and MaxResults for paging instead.
        self.page_number = page_number
        # > This parameter is about to be deprecated. Use NextToken and MaxResults for paging instead.
        self.page_size = page_size
        # The region ID of the disk. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. When you use this parameter to filter resources, the resource count cannot exceed 1000.
        # 
        # > Filtering by default resource group is not supported.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IDs of snapshots. The value is a JSON array that consists of up to 100 snapshot IDs. Separate the IDs with commas (,).
        self.snapshot_ids = snapshot_ids
        # The ID of the snapshot chain.
        self.snapshot_link_id = snapshot_link_id
        # The name of the snapshot.
        self.snapshot_name = snapshot_name
        # The type of automatic creation. Valid values: 
        #          
        # - auto: automatic snapshot.
        # - user: manual snapshot.
        # - all (default): All automatic creation types.
        self.snapshot_type = snapshot_type
        # The type of the source disk. Valid values: 
        #      
        # - system: system disk.
        # - data: data disk.
        # 
        # > The value is case-insensitive.
        self.source_disk_type = source_disk_type
        # The status of the snapshot. Valid values: 
        #          
        # - progressing: The snapshot is being created.
        # - accomplished: The snapshot is created.
        # - failed: The snapshot failed to be created.
        # - all (default): All snapshot statuses.
        self.status = status
        # The tags.
        self.tag = tag
        # Specifies whether the snapshot has been used to create images or disks. Valid values: 
        # 
        # - image: The snapshot has been used to create custom images.
        # - disk: The snapshot has been used to create disks.
        # - image_disk: The snapshot has been used to create both data disks and custom images.
        # - none: The snapshot has not been used.
        self.usage = usage

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.category is not None:
            result['Category'] = self.category

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids

        if self.snapshot_link_id is not None:
            result['SnapshotLinkId'] = self.snapshot_link_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type

        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribeSnapshotsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')

        if m.get('SnapshotLinkId') is not None:
            self.snapshot_link_id = m.get('SnapshotLinkId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')

        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeSnapshotsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class DescribeSnapshotsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the snapshot. Valid values of N: 1 to 20.
        # 
        # If you use a single tag to filter resources, the resource count with the specified tag cannot exceed 1000. If you use multiple tags to filter resources, the resource count with all specified tags attached cannot exceed 1000. If the resource count exceeds 1000, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation.
        self.key = key
        # The tag value of the snapshot. Valid values of N: 1 to 20.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeSnapshotsRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter key used to query resources. Set the value to `CreationStartTime`. When you specify both `Filter.1.Key` and `Filter.1.Value`, you can query resources created after the specified point in time.
        self.key = key
        # The filter value used to query resources. When you specify this parameter, you must also specify `Filter.1.Key`. Specify the time in the `yyyy-MM-ddTHH:mmZ` format in UTC.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

