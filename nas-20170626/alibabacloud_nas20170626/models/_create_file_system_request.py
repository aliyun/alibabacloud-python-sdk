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
        # The maximum throughput of the file system.
        # 
        # Unit: MB/s.
        # 
        # For available specification values, see the actual specifications on the buy page.
        # 
        # <props="china">
        # 
        # [Parallel file system CPFS pay-as-you-go buy page](https://common-buy.aliyun.com/?commodityCode=nas_cpfs_post#/buy)
        # 
        # 
        # 
        # <props="intl">
        # 
        # [Parallel file system CPFS pay-as-you-go buy page](https://common-buy-intl.alibabacloud.com/?spm=5176.nas_overview.0.0.7ea01dbft0dTui&commodityCode=nas_cpfspost_public_intl#/buy)
        self.bandwidth = bandwidth
        # The capacity of the file system. Unit: GiB.
        # This parameter is required and takes effect only when FileSystemType is set to extreme, cpfs, or cpfsse.
        # 
        # For available values, see the actual specifications on the buy page:
        # 
        # <props="china">
        # 
        # -  [Extreme NAS pay-as-you-go buy page](https://common-buy.aliyun.com/?commodityCode=nas_extreme_post#/buy)
        # - [Parallel file system CPFS pay-as-you-go buy page](https://common-buy.aliyun.com/?commodityCode=nas_cpfs_post#/buy)
        # 
        # 
        # 
        # <props="intl">
        # 
        # - [Extreme NAS pay-as-you-go buy page](https://common-buy-intl.alibabacloud.com/?commodityCode=nas_extpost_public_intl#/buy)
        # 
        # - [Parallel file system CPFS pay-as-you-go buy page](https://common-buy-intl.alibabacloud.com/?spm=5176.nas_overview.0.0.7ea01dbft0dTui&commodityCode=nas_cpfspost_public_intl#/buy)
        self.capacity = capacity
        # The billing method.
        # 
        # Valid values:
        # 
        # - PayAsYouGo (default): Pay-as-you-go.
        # - Subscription: Subscription.
        self.charge_type = charge_type
        # Ensures the idempotence of the request. Generate a unique parameter value from your client. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # The description of the file system.
        # 
        # Limits:
        # 
        # - The description must be 2 to 128 characters in length.
        # - The description must start with a letter and cannot start with `http://` or `https://`.
        # - The description can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run for this request.
        # 
        # A dry run checks parameter validity and resource availability without actually creating the instance or incurring charges.
        # 
        # Valid values:  
        # - true: Sends a dry run request without creating the instance. The check items include required parameters, request format, service limits, and NAS inventory. If the check fails, the corresponding error is returned. If the check succeeds, HTTP status code 200 is returned, but FileSystemId is empty.  
        # - false (default): Sends a normal request. After the check succeeds, the instance is created.
        self.dry_run = dry_run
        # The subscription duration.
        # 
        # Unit: months. This parameter is required and takes effect only when ChargeType is set to Subscription.
        # 
        # If a subscription instance is not renewed upon expiration, the instance is automatically released.
        self.duration = duration
        # Specifies whether to encrypt the file system.
        # 
        # Uses keys managed by Key Management Service (KMS) to encrypt data stored on the file system. No decryption is required when reading or writing encrypted data.
        # 
        # Valid values:
        # 
        # - 0 (default): Not encrypted.
        # - 1: NAS-managed key. Supported when FileSystemType is set to standard or extreme.
        # - 2: Custom Key (KMS). Supported when FileSystemType is set to standard or extreme.
        # 
        # > - Extreme NAS: The Custom Key (KMS) feature is supported in all regions except China (Hangzhou) Finance Cloud.
        # > - General-purpose NAS: The Custom Key (KMS) feature is supported in all regions.
        self.encrypt_type = encrypt_type
        # The type of the file system.
        # 
        # Valid values:
        # - standard (default): General-purpose NAS file system.
        # - extreme: Extreme NAS file system.
        # - cpfs: Cloud Parallel File Storage (CPFS) (locally redundant).
        # - cpfsse: Cloud Parallel File Storage (CPFS) SE (zone-redundant).
        self.file_system_type = file_system_type
        # The KMS key ID.
        # 
        # This parameter is required only when EncryptType is set to 2.
        self.kms_key_id = kms_key_id
        # The file transfer protocol type.
        # 
        # - If FileSystemType is set to standard, valid values: NFS and SMB.
        # - If FileSystemType is set to extreme, valid values: NFS.
        # - If FileSystemType is set to cpfs, valid values: cpfs.
        # - If FileSystemType is set to cpfsse, valid values: cpfs.
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The storage redundancy type. This parameter takes effect only for CPFS SE.
        # Valid values: ZRS.
        self.redundancy_type = redundancy_type
        # The list of zone-redundant vSwitch IDs.
        # If RedundancyType is set to ZRS, this parameter is required. You must specify three vSwitch IDs, each from a different zone.
        self.redundancy_vswitch_ids = redundancy_vswitch_ids
        # The resource group ID.
        # 
        # You can view resource group IDs in the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups?).
        self.resource_group_id = resource_group_id
        # The snapshot ID.
        # 
        # This parameter is supported only for Extreme NAS file systems with the Advanced storage type.
        # > A file system created from a snapshot has the same version as the source file system of the snapshot. For example, if the source file system version is 1 and you want to create a version 2 file system, first create file system A from the snapshot, then create file system B that meets the version 2 configuration. Copy the data from file system A to file system B, and migrate your workloads to file system B after the copy is complete.
        self.snapshot_id = snapshot_id
        # The storage type.
        # 
        # - If FileSystemType is set to standard, valid values: Performance, Capacity, and Premium.
        # - If FileSystemType is set to extreme, valid values: standard and advance.
        # - If FileSystemType is set to cpfs, valid values: advance_100 (100 MB/s/TiB baseline), advance_200 (200 MB/s/TiB baseline), and economic.
        # - If FileSystemType is set to cpfsse, valid values: advance_100 (100 MB/s/TiB baseline).
        # 
        # This parameter is required.
        self.storage_type = storage_type
        # The tags.
        # 
        # Array length: 1 to 20. If the array contains multiple tag objects, the tag key (Key) must be unique.
        self.tag = tag
        # The vSwitch ID.
        # 
        # - If FileSystemType is set to cpfs, this parameter is required.
        # - If FileSystemType is not set to cpfs, this parameter is reserved and does not take effect. You do not need to configure it.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        # 
        # - If FileSystemType is set to cpfs or cpfsse, this parameter is required.
        # - If FileSystemType is set to standard or extreme, this parameter is reserved and does not take effect. You do not need to configure it.
        self.vpc_id = vpc_id
        # The zone ID.
        # 
        # A zone is an independent physical area within a region that has its own power supply and network.
        # 
        # If FileSystemType is set to standard, this parameter is optional. By default, an active zone that matches the conditional ProtocolType and StorageType is randomly selected.
        # 
        # If FileSystemType is set to extreme or cpfs, this parameter is required.
        # 
        # >  - File systems and Elastic Computing Service (ECS) instances in different zones of the same region can communicate with each other.
        # >  - Place the file system and the ECS server in the same zone to avoid cross-zone latency.
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
        # 
        # Limits:
        # 
        # - The tag key cannot be empty.
        # - The tag key can be up to 128 characters in length.
        # - The tag key cannot start with `aliyun` or `acs:`.
        # - The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value.
        # 
        # Limits:
        # - The tag value cannot be empty.
        # - The tag value can be up to 128 characters in length.
        # - The tag value cannot contain `http://` or `https://`.
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

