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
        # Specify a value based on the specifications on the buy page.
        # 
        # [CPFS (Pay-as-you-go)](https://common-buy-intl.alibabacloud.com/?spm=5176.nas_overview.0.0.7ea01dbft0dTui\\&commodityCode=nas_cpfspost_public_intl#/buy)
        self.bandwidth = bandwidth
        # Specify the capacity of the file system. Unit: GiB. This parameter is required and valid when FileSystemType is set to extreme, cpfs, or cpfsse.
        # 
        # Specify a value based on the specifications on the following buy page:
        # 
        # *   [Extreme NAS (Pay-as-you-go)](https://common-buy-intl.alibabacloud.com/?commodityCode=nas_extpost_public_intl#/buy)
        # *   [CPFS (Pay-as-you-go)](https://common-buy-intl.alibabacloud.com/?spm=5176.nas_overview.0.0.7ea01dbft0dTui\\&commodityCode=nas_cpfspost_public_intl#/buy)
        self.capacity = capacity
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo (default): pay-as-you-go
        # *   Subscription
        self.charge_type = charge_type
        # A client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. ClientToken only supports ASCII characters and cannot exceed 64 characters. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The description of the file system.
        # 
        # Limits:
        # 
        # *   Must be 2 to 128 characters in length.
        # *   Must start with a letter but cannot start with `http://` or `https://`.
        # *   Can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Whether to precheck the creation request.
        # 
        # The precheck operation helps you check the validity of parameters and verify inventory. It does not actually create instances and does not incur fees.
        # 
        # Valid values:
        # 
        # *   true: Checks the request without creating an instance. The system checks the required parameters, request syntax, service limits, and available NAS resources. If the request fails to pass the check, an error message is returned. If the request passes the check, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): Sends the request. If the request passes the check, the instance is created.
        self.dry_run = dry_run
        # The subscription duration.
        # 
        # This parameter is valid and required if ChargeType is set to Subscription. Unit: months.
        # 
        # If you do not renew a subscription file system when the file system expires, the file system is automatically released.
        self.duration = duration
        # Specifies whether to encrypt data in the file system.
        # 
        # You can use the keys that are managed by Key Management Service (KMS) to encrypt data in a file system. When you read and write the encrypted data, the data is automatically decrypted.
        # 
        # Valid values:
        # 
        # *   0 (default): The data in the file system is not encrypted.
        # *   1: A NAS-managed key is used to encrypt the data in the file system. This value is valid if FileSystemType is set to standard or extreme.
        # *   2: A KMS-managed key is used to encrypt the data in the file system. This value is valid if the FileSystemType parameter is set to standard or extreme.
        # 
        # > 
        # 
        # *   Extreme NAS: All regions except China East 1 Finance support KMS-managed keys.
        # 
        # *   General-purpose NAS: All regions support KMS-managed keys.
        self.encrypt_type = encrypt_type
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose NAS
        # *   extreme: Extreme NAS
        # *   cpfs: CPFS (locally redundant storage)
        # *   cpfsse: CPFS SE (zone-redundant storage)
        self.file_system_type = file_system_type
        # The ID of the KMS key.
        # 
        # This parameter is required if EncryptType is set to 2.
        self.kms_key_id = kms_key_id
        # Specify the protocol type.
        # 
        # *   If FileSystemType is set to standard, set this parameter to NFS or SMB.
        # *   If FileSystemType is set to extreme, set this parameter to NFS.
        # *   If FileSystemType is set to cpfs, set this parameter to cpfs.
        # *   If FileSystemType is set to cpfsse, set this parameter to cpfs.
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # Storage redundancy type. Only available for CPFS SE.
        # 
        # Valid values:
        # 
        # *   ZRS
        self.redundancy_type = redundancy_type
        # A list of IDs for the zone-redundant vSwitches. This parameter is required if RedundancyType is set to ZRS. You must enter three vSwitch IDs from three different zones.
        self.redundancy_vswitch_ids = redundancy_vswitch_ids
        # The resource group ID.
        # 
        # You can log on to the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups?) to view resource group IDs.
        self.resource_group_id = resource_group_id
        # The snapshot ID.
        # 
        # This parameter is available only for advanced Extreme NAS file systems.
        # 
        # > You can create a file system from a snapshot. The version of the file system is the same as that of the source file system. For example, the source file system of the snapshot uses version 1. To create a file system of version 2, create File System A from the snapshot and create File System B of version 2. Then copy the data and migrate your business from File System A to File System B.
        self.snapshot_id = snapshot_id
        # The storage type.
        # 
        # *   If FileSystemType is set to standard, set this parameter to Performance, Capacity, or Premium.
        # *   If FileSystemType is set to extreme, set this parameter to standard or advance.
        # *   If FileSystemType is set to cpfs, set this parameter to advance_100 (100 MB/s/TiB Baseline), advance_200 (200 MB/s/TiB Baseline), or economic.
        # *   If FileSystemType is set to cpfsse, set this parameter to advance_100 (100 MB/s/TiB Baseline).
        # 
        # This parameter is required.
        self.storage_type = storage_type
        # An array of tags.
        # 
        # You can specify up to 20 tags. If you specify multiple tags, each tag key must be unique.
        self.tag = tag
        # The vSwitch ID.
        # 
        # *   This parameter is required if FileSystemType is set to cpfs.
        # *   If FileSystemType is not set to cpfs, this parameter is reserved and not required.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        # 
        # *   This parameter is required if FileSystemType is set to cpfs or cpfsse.
        # *   This parameter is reserved and not required if FileSystemType is set to standard or extreme.
        self.vpc_id = vpc_id
        # The ID of the zone.
        # 
        # Each region has multiple isolated locations known as zones. Each zone has its own independent power supply and network.
        # 
        # This parameter is not required if FileSystemType is set to standard. By default, a random zone is selected based on the protocol type and storage type.
        # 
        # This parameter is required if FileSystemType is set to extreme or cpfs.
        # 
        # > 
        # 
        # *   An Elastic Compute Service (ECS) instance and a file system that reside in different zones of the same region can access each other.
        # 
        # *   We recommend that you select the zone where the ECS instance resides. This prevents cross-zone latency between the file system and the ECS instance.
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
        # *   Cannot be null or an empty string.
        # *   Can be up to 128 characters in length.
        # *   Cannot start with `aliyun` or `acs:`.
        # *   Cannot contain `http://` or `https://`.
        self.key = key
        # The tag value.
        # 
        # Limits:
        # 
        # *   Cannot be null or an empty string.
        # *   Can be up to 128 characters in length.
        # *   Cannot contain `http://` or `https://`.
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

