# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class CreateFileSystemRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        capacity: int = None,
        charge_type: str = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        duration: int = None,
        encrypt_type: int = None,
        file_system_type: str = None,
        hpn_zone: str = None,
        kms_key_id: str = None,
        protocol_type: str = None,
        redundancy_type: str = None,
        redundancy_vswitch_ids: List[str] = None,
        resource_group_id: str = None,
        snapshot_id: str = None,
        storage_type: str = None,
        tag: List[main_models.CreateFileSystemRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The maximum throughput of the file system. Unit: MB/s.
        # For valid values, refer to the specifications on the buy page.
        # 
        # <props="china">
        # 
        # [Buy page for pay-as-you-go Parallel file systems](https://common-buy.aliyun.com/?commodityCode=nas_cpfs_post#/buy)
        # 
        # 
        # 
        # <props="intl">
        # 
        # [Buy page for pay-as-you-go Parallel file systems](https://common-buy-intl.alibabacloud.com/?spm=5176.nas_overview.0.0.7ea01dbft0dTui&commodityCode=nas_cpfspost_public_intl#/buy)
        self.bandwidth = bandwidth
        # The capacity of the file system. Unit: GiB.
        # This parameter is required and valid only when FileSystemType is set to extreme, cpfs, or cpfsse.
        # For valid values, refer to the specifications on the buy page:
        # 
        # <props="china">
        # 
        # - [Buy page for pay-as-you-go Extreme NAS file systems](https://common-buy.aliyun.com/?commodityCode=nas_extreme_post#/buy)
        # - [Buy page for pay-as-you-go Parallel file systems](https://common-buy.aliyun.com/?commodityCode=nas_cpfs_post#/buy)
        # 
        # 
        # 
        # <props="intl">
        # 
        # - [Buy page for pay-as-you-go Extreme NAS file systems](https://common-buy-intl.alibabacloud.com/?commodityCode=nas_extpost_public_intl#/buy)
        # 
        # - [Buy page for pay-as-you-go Parallel file systems](https://common-buy-intl.alibabacloud.com/?spm=5176.nas_overview.0.0.7ea01dbft0dTui&commodityCode=nas_cpfspost_public_intl#/buy)
        self.capacity = capacity
        # The billing method. Valid values:
        # - PayAsYouGo: pay-as-you-go. This is the default value.
        # - Subscription: subscription.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        #  
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request may be different.
        self.client_token = client_token
        # The description of the file system.
        # Limits:
        # - The description must be 2 to 128 characters in length.
        # - It must start with a letter and cannot start with `http://` or `https://`.
        # - It can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run on the creation request.
        # A dry run checks whether the parameters are valid and whether resources are sufficient, but does not actually create the instance or incur fees.
        # Valid values:  
        # - true: performs a dry run without creating the instance. The system checks whether required parameters are specified, the request format is valid, the service limits are met, and NAS resources are sufficient. If the request fails the dry run, an error message is returned. If the request passes the dry run, the 200 HTTP status code is returned, but FileSystemId is empty.  
        # - false: performs a normal request and creates the instance directly after the request passes the check. This is the default value.
        self.dry_run = dry_run
        # The subscription duration. Unit: months. This parameter is required and valid only when ChargeType is set to Subscription.
        # If a subscription instance is not renewed upon expiration, it is automatically released.
        self.duration = duration
        # Specifies whether to encrypt the file system.
        # Uses KMS-managed keys to encrypt data at rest in the file system. You do not need to perform decryption when reading or writing the encrypted data.
        # Valid values:
        # - 0: Not encrypted. This is the default value.
        # - 1: NAS-managed key. Supported when FileSystemType is set to standard or extreme.
        # - 2: Custom key. Supported when FileSystemType is set to standard or extreme.
        # 
        # > - Extreme NAS file systems: The custom key (KMS) feature is supported in all regions except China East 1 Finance Cloud.
        # > - General-purpose NAS file systems: The custom key (KMS) feature is supported in all regions.
        self.encrypt_type = encrypt_type
        # The file system type. Valid values:
        # - standard: General-purpose NAS file system. This is the default value.
        # - extreme: Extreme NAS file system.
        # - cpfs: Cloud Parallel File Storage (CPFS) with locally redundant storage (LRS).
        # - cpfsse: Cloud Parallel File Storage SE with zone-redundant storage (ZRS).
        self.file_system_type = file_system_type
        # The cluster ID of the high-performance network zone. This parameter is required when FileSystemType is set to bmcpfs and cannot be modified after creation. You can call the DescribeSpecifications operation to query valid values. Example: B1.
        self.hpn_zone = hpn_zone
        # The ID of the KMS key.
        # This parameter is required only when EncryptType is set to 2.
        self.kms_key_id = kms_key_id
        # The file transfer protocol type.
        # - When FileSystemType is set to standard, valid values are NFS and SMB.
        # - When FileSystemType is set to extreme, the valid value is NFS.
        # - When FileSystemType is set to cpfs, the valid value is cpfs.
        # - When FileSystemType is set to cpfsse, the valid value is cpfs.
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The storage redundancy type. This parameter takes effect only for CPFS SE. Valid value: ZRS.
        self.redundancy_type = redundancy_type
        # The zone-redundant vSwitch IDs.
        # This parameter is required when RedundancyType is set to ZRS. You must specify three vSwitch IDs, and they must belong to three different zones.
        self.redundancy_vswitch_ids = redundancy_vswitch_ids
        # The resource group ID.
        # You can view the resource group ID in the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups?).
        self.resource_group_id = resource_group_id
        # The snapshot ID.
        # This parameter is supported only for Extreme NAS file systems with the Advanced storage type.
        # > When you create a file system from a snapshot, the created file system has the same version as the source file system of the snapshot. For example, if the source file system of the snapshot is version 1 and you want to create a version 2 file system, you can first create File System A from the snapshot, then create File System B that meets the version 2 configurations, copy the data from File System A to File System B, and migrate your business to File System B after the copy is complete.
        self.snapshot_id = snapshot_id
        # The storage type.
        # - When FileSystemType is set to standard, valid values are Performance, Capacity, Premium, and Agentic.
        # - When FileSystemType is set to extreme, valid values are standard and advance.
        # - When FileSystemType is set to cpfs, valid values are advance_100 (100 MB/s/TiB baseline), advance_200 (200 MB/s/TiB baseline), and economic (Economy).
        # - When FileSystemType is set to cpfsse, the valid value is advance_100 (100 MB/s/TiB baseline).
        # 
        # This parameter is required.
        self.storage_type = storage_type
        # The tags.
        # Array length: 1 to 20. If the array contains multiple tag objects, the tag keys must be unique.
        self.tag = tag
        # The vSwitch ID.
        # - This parameter is required when FileSystemType is set to cpfs.
        # - This parameter is reserved and does not take effect when FileSystemType is not set to cpfs. You do not need to configure it.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        # - This parameter is required when FileSystemType is set to cpfs or cpfsse.
        # - This parameter is reserved and does not take effect when FileSystemType is set to standard or extreme. You do not need to configure it.
        self.vpc_id = vpc_id
        # The zone ID.
        # A zone is a physical area with independent power grids and networks in the same region.
        # When FileSystemType is set to standard, this parameter is optional. By default, a zone that meets the conditional requirements is randomly selected based on the ProtocolType and StorageType settings.
        # When FileSystemType is set to extreme or cpfs, this parameter is required.
        # 
        # > - File systems and Elastic Compute Service (ECS) instances in different zones of the same region can communicate with each other.
        # > - Deploy the file system and the ECS instance in the same zone to avoid cross-zone latency.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.redundancy_type is not None:
            result['RedundancyType'] = self.redundancy_type

        if self.redundancy_vswitch_ids is not None:
            result['RedundancyVSwitchIds'] = self.redundancy_vswitch_ids

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RedundancyType') is not None:
            self.redundancy_type = m.get('RedundancyType')

        if m.get('RedundancyVSwitchIds') is not None:
            self.redundancy_vswitch_ids = m.get('RedundancyVSwitchIds')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateFileSystemRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateFileSystemRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # Limits:
        # - It cannot be empty or an empty string.
        # - It can be up to 128 characters in length.
        # - It cannot start with `aliyun` or `acs:`.
        # - It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value.
        # Limits:
        # - It cannot be empty or an empty string.
        # - It can be up to 128 characters in length.
        # - It cannot contain `http://` or `https://`.
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

