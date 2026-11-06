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
        # The snapshot category. Valid values:
        # - Standard: Standard snapshot.
        # - Flash: Local snapshot. This value will soon be deprecated. Local snapshots are replaced by the snapshot instant access feature. The parameter description is as follows:
        #   - If you used local snapshots before December 14, 2020, you can use this parameter normally.
        #   - If you did not use local snapshots before December 14, 2020, you cannot use this parameter.
        # - archive: Archive snapshot.
        # 
        # 
        # 
        # <props="china">For more information, see [Notice on Alibaba Cloud Snapshot Service Upgrade and New Billing Items on December 14](https://help.aliyun.com/noticelist/articleid/1060755542.html).
        self.category = category
        # The ID of the disk.
        self.disk_id = disk_id
        # Specifies whether to only perform a dry run for this request.
        # 
        # - true: The system sends a check request without querying resources. The check items include whether the AccessKey pair is valid, the authorization of Resource Access Management (RAM) users, and whether required parameters are specified. If the check fails, the system returns an error. If the check succeeds, the system returns the error code DryRunOperation.
        # - false (default): The system sends a normal request. If the request passes the check, the system returns an HTTP status code 2xx and queries resources.
        self.dry_run = dry_run
        # Specifies whether to filter encrypted snapshots. Default value: false.
        self.encrypted = encrypted
        # The specified instance ID. This parameter specifies the instance whose disk snapshots you want to query.
        self.instance_id = instance_id
        # The ID of the KMS key that corresponds to the data disk.
        self.kmskey_id = kmskey_id
        # The number of entries per page for a paged query. Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token. You can obtain the token from the response of the previous request.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter will be deprecated soon. We recommend that you use the NextToken and MaxResults parameters to perform a paged query.
        self.page_number = page_number
        # > This parameter will be deprecated soon. We recommend that you use the NextToken and MaxResults parameters to perform a paged query.
        self.page_size = page_size
        # The region ID of the disk. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. When you use this parameter to filter resources, the resource count cannot exceed 1,000.
        # 
        # > Filtering by the default resource group is not supported.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The snapshot IDs. The value can be a JSON array that consists of up to 100 snapshot IDs. Separate multiple IDs with commas (,).
        self.snapshot_ids = snapshot_ids
        # The ID of the snapshot chain.
        self.snapshot_link_id = snapshot_link_id
        # The snapshot name.
        self.snapshot_name = snapshot_name
        # The automatic creation type. Valid values: 
        #          
        # - auto: The snapshot is automatically created.
        # - user: The snapshot is manually created.
        # - all (default): All automatic creation types.
        self.snapshot_type = snapshot_type
        # The type of the source disk from which the snapshot is created. Valid values: 
        #      
        # - system: System disk.
        # - data: Data disk.
        # 
        # > The values are not case-sensitive.
        self.source_disk_type = source_disk_type
        # The snapshot status. Valid values: 
        #          
        # - progressing: The snapshot is being created.
        # - accomplished: The snapshot is created.
        # - failed: The snapshot fails to be created.
        # - all (default): All snapshot statuses.
        self.status = status
        # The list of tags.
        self.tag = tag
        # The usage of the snapshot. Valid values: 
        # 
        # - image: The snapshot is used to create a custom image.
        # - disk: The snapshot is used to create a disk.
        # - image_disk: The snapshot is used to create a data disk and a custom image.
        # - none: The snapshot is not used.
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
        # If you use a single tag to filter resources, the resource count under this tag cannot exceed 1,000. If you use multiple tags to filter resources, the resource count of resources that are attached with multiple tags cannot exceed 1,000. If the resource count exceeds 1,000, use the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query the resources.
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
        # The filter key used when querying resources. The value must be `CreationStartTime`. If you specify both `Filter.1.Key` and `Filter.1.Value`, you can query the resources created after the specified point in time.
        self.key = key
        # The filter value used when querying resources. If you specify this parameter, you must also specify the `Filter.1.Key` parameter. The value must be in the `yyyy-MM-ddTHH:mmZ` format and use the UTC+0 time zone.
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

