# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDisksRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.DescribeDisksRequestFilter] = None,
        additional_attributes: List[str] = None,
        auto_snapshot_policy_id: str = None,
        category: str = None,
        delete_auto_snapshot: bool = None,
        delete_with_instance: bool = None,
        disk_charge_type: str = None,
        disk_ids: str = None,
        disk_name: str = None,
        disk_type: str = None,
        dry_run: bool = None,
        enable_auto_snapshot: bool = None,
        enable_automated_snapshot_policy: bool = None,
        enable_shared: bool = None,
        encrypted: bool = None,
        instance_id: str = None,
        kmskey_id: str = None,
        lock_reason: str = None,
        max_results: int = None,
        multi_attach: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        portable: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snapshot_id: str = None,
        status: str = None,
        tag: List[main_models.DescribeDisksRequestTag] = None,
        zone_id: str = None,
    ):
        self.filter = filter
        # The additional attributes. Set the value to `Placement`, which indicates the data storage locations of the disk.
        # 
        # >  This attribute is valid only for Regional Enterprise SSDs (ESSDs).
        self.additional_attributes = additional_attributes
        # The ID of the automatic snapshot policy that is applied to the cloud disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The disk category. Valid values:
        # 
        # *   all: all disk categories
        # *   cloud: basic disk
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD
        # *   cloud_essd: Enterprise SSD (ESSD)
        # *   cloud_auto: ESSD AutoPL disk
        # *   cloud_regional_disk_auto: Regional ESSD
        # *   cloud_essd_entry: ESSD Entry disk
        # *   elastic_ephemeral_disk_standard: standard elastic ephemeral disk
        # *   elastic_ephemeral_disk_premium: premium elastic ephemeral disk
        # *   local_ssd_pro: I/O-intensive local disk
        # *   local_hdd_pro: throughput-intensive local disk
        # *   ephemeral: retired local disk
        # *   ephemeral_ssd: retired local SSD
        # 
        # Default value: all.
        # 
        # Enumerated values:
        # 
        # *   all: all disks categories
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD
        # *   local_ssd_pro: I/O-intensive local disk
        # *   ephemeral: retired local disk
        # *   cloud_essd_entry: ESSD Entry disk
        # *   elastic_ephemeral_disk_premium: premium elastic ephemeral disk
        # *   cloud: basic disk
        # *   ephemeral_ssd: retired local SSD
        # *   cloud_auto: ESSD AutoPL disk
        # *   cloud_regional_disk_auto: Regional ESSD
        # *   cloud_essd: ESSD
        # *   elastic_ephemeral_disk_standard: standard elastic ephemeral disk
        # *   local_hdd_pro: throughput-intensive local disk
        self.category = category
        # Specifies whether to delete the automatic snapshots of the cloud disk after the disk is released.
        # 
        # *   true
        # *   false
        # 
        # Default value: false
        self.delete_auto_snapshot = delete_auto_snapshot
        # Specifies whether the disk is released when the associated instance is released. Valid values:
        # 
        # *   true: The disk is released when the associated instance is released.
        # *   false: The disk is retained as a pay-as-you-go data disk when the associated instance is released.
        # 
        # Default value: false.
        self.delete_with_instance = delete_with_instance
        # The billing method of the disk. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid: pay-as-you-go
        self.disk_charge_type = disk_charge_type
        # The IDs of cloud disks, local disks, or elastic ephemeral disks. The value is a JSON array that consists of up to 100 disk IDs. Separate the disk IDs with commas (,).
        self.disk_ids = disk_ids
        # The name of the disk. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        self.disk_name = disk_name
        # The type of the disk. Valid values:
        # 
        # *   all: system disk and data disk
        # *   system: system disk
        # *   data: data disk
        # 
        # Default value: all.
        # 
        # >  Elastic ephemeral disks cannot be used as system disks.
        self.disk_type = disk_type
        # Specifies whether to perform only a dry run without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run. The systems checks whether your AccessKey pair is valid, whether RAM users are granted permissions, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   false: performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        # 
        # Default value: false
        self.dry_run = dry_run
        # Specifies whether the automatic snapshot policy feature is enabled for the cloud disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is deprecated. By default, the automatic snapshot policy feature is enabled for cloud disks. You need to only apply an automatic snapshot policy to a cloud disk before you can use the automatic snapshot policy.
        self.enable_auto_snapshot = enable_auto_snapshot
        # Specifies whether an automatic snapshot policy is applied to the cloud disk.
        # 
        # *   true: An automatic snapshot policy is applied to the cloud disk.
        # *   false: No automatic snapshot policy is applied to the cloud disk.
        # 
        # Default value: false
        self.enable_automated_snapshot_policy = enable_automated_snapshot_policy
        # Specifies whether the disk is a Shared Block Storage device.
        self.enable_shared = enable_shared
        # Specifies whether to query only encrypted cloud disks.
        # 
        # *   true: queries only encrypted cloud disks.
        # *   false: does not query encrypted cloud disks.
        # 
        # Default value: false
        self.encrypted = encrypted
        # The ID of the Elastic Compute Service (ECS) instance to which the disk is attached.
        self.instance_id = instance_id
        # The ID of the Key Management Service (KMS) key that is used by the cloud disk.
        self.kmskey_id = kmskey_id
        # The reason why the disk is locked. Valid values:
        # 
        # *   financial: The disk is locked due to overdue payments.
        # *   security: The disk is locked due to security reasons.
        self.lock_reason = lock_reason
        # The maximum number of entries per page. Valid values: 10 to 500.
        # 
        # Default value:
        # 
        # *   If you do not specify this parameter or you set this parameter to a value less than 10, the default value is 10.
        # *   If you set this parameter to a value greater than 500, the default value is 500.
        self.max_results = max_results
        # Specifies whether to enable the multi-attach feature for the disk. Valid values:
        # 
        # *   Disabled
        # *   Enabled
        # *   LegacyShared: Shared Block Storage devices are queried.
        self.multi_attach = multi_attach
        # The query token. Set the value to the `NextToken` value that was returned in the last call to this operation.
        # 
        # For more information about how to check the responses returned by this operation, see the preceding "Description" section.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # >  This parameter will be removed in the future. We recommend that you use `NextToken` and `MaxResults` for a paged query.
        self.page_number = page_number
        # >  This parameter will be removed in the future. We recommend that you use `NextToken` and `MaxResults` for a paged query.
        self.page_size = page_size
        # Specifies whether the disk is removable. Valid values:
        # 
        # *   true: The disk is removable. A removable disk can independently exist and can be attached to or detached from an instance within the same zone.
        # *   false: The disk is not removable. A disk that is not removable cannot independently exist or be attached to or detached from an instance within the same zone.
        # 
        # The `Portable` attribute of the following types of disks is `false`, and these types of disks share the same lifecycle with their associated instances:
        # 
        # *   Local disks
        # *   Local SSDs
        # *   Subscription data disks
        self.portable = portable
        # The region ID of the disk. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the disk belongs. If this parameter is specified to query resources, up to 1,000 resources that belong to the specified resource group can be displayed in the response.
        # 
        # >  Resources in the default resource group are displayed in the response regardless of the value specified for this parameter.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the snapshot from which you create the cloud disk.
        self.snapshot_id = snapshot_id
        # The status of the disk. For more information, see [Disk states](https://help.aliyun.com/document_detail/25689.html). Valid values:
        # 
        # *   In_use
        # *   Available
        # *   Attaching
        # *   Detaching
        # *   Creating
        # *   ReIniting
        # *   All
        # 
        # Default value: All.
        self.status = status
        # The tags of the disk.
        self.tag = tag
        # The zone ID.
        self.zone_id = zone_id

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

        if self.additional_attributes is not None:
            result['AdditionalAttributes'] = self.additional_attributes

        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.category is not None:
            result['Category'] = self.category

        if self.delete_auto_snapshot is not None:
            result['DeleteAutoSnapshot'] = self.delete_auto_snapshot

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type

        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_auto_snapshot is not None:
            result['EnableAutoSnapshot'] = self.enable_auto_snapshot

        if self.enable_automated_snapshot_policy is not None:
            result['EnableAutomatedSnapshotPolicy'] = self.enable_automated_snapshot_policy

        if self.enable_shared is not None:
            result['EnableShared'] = self.enable_shared

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.multi_attach is not None:
            result['MultiAttach'] = self.multi_attach

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

        if self.portable is not None:
            result['Portable'] = self.portable

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribeDisksRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('AdditionalAttributes') is not None:
            self.additional_attributes = m.get('AdditionalAttributes')

        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteAutoSnapshot') is not None:
            self.delete_auto_snapshot = m.get('DeleteAutoSnapshot')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')

        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableAutoSnapshot') is not None:
            self.enable_auto_snapshot = m.get('EnableAutoSnapshot')

        if m.get('EnableAutomatedSnapshotPolicy') is not None:
            self.enable_automated_snapshot_policy = m.get('EnableAutomatedSnapshotPolicy')

        if m.get('EnableShared') is not None:
            self.enable_shared = m.get('EnableShared')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MultiAttach') is not None:
            self.multi_attach = m.get('MultiAttach')

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

        if m.get('Portable') is not None:
            self.portable = m.get('Portable')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDisksRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDisksRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the disk. Valid values of N: 1 to 20.
        # 
        # If you specify a single tag to query resources, up to 1,000 resources to which the tag is added are returned. If you specify multiple tags to query resources, up to 1,000 resources to which all specified tags are added are returned. To query more than 1,000 resources that have specified tags added, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation.
        self.key = key
        # The value of tag N of the disk. Valid values of N: 1 to 20.
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

class DescribeDisksRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of filter 1 used to query resources. Set the value to `CreationStartTime`. You can specify a time by setting both `Filter.1.Key` and `Filter.1.Value` to query resources that were created after the specified time.
        self.key = key
        # The value of filter 1 used to query resources. Set the value to a time. If you specify this parameter, you must also specify the `Filter.1.Key` parameter. Specify the time in the `yyyy-MM-ddTHH:mmZ` format. The time must be in UTC.
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

