# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AssociateSourceServersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        source_id: List[str] = None,
        workgroup_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # The IDs of migration sources. You can specify up to 50 IDs.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The ID of the workgroup.
        # 
        # This parameter is required.
        self.workgroup_id = workgroup_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.workgroup_id is not None:
            result['WorkgroupId'] = self.workgroup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('WorkgroupId') is not None:
            self.workgroup_id = m.get('WorkgroupId')
        return self


class AssociateSourceServersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateSourceServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateSourceServersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateSourceServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessTokenRequest(TeaModel):
    def __init__(
        self,
        count: str = None,
        description: str = None,
        name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        time_to_live_in_days: str = None,
    ):
        # The maximum number of times that the activation code can be used to import the information of migration sources. Valid values: 1 to 1000.
        # 
        # Default value: 100.
        self.count = count
        # The description of the activation code.
        self.description = description
        # The name of the activation code. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain digits, colons (:), underscores (_), and hyphens (-).
        self.name = name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # The validity period of the activation code. The activation code can no longer be used to import the information of migration sources after the code expires. Unit: day. Valid values: 1 to 90.
        # 
        # Default value: 30.
        self.time_to_live_in_days = time_to_live_in_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.time_to_live_in_days is not None:
            result['TimeToLiveInDays'] = self.time_to_live_in_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TimeToLiveInDays') is not None:
            self.time_to_live_in_days = m.get('TimeToLiveInDays')
        return self


class CreateAccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token_code: str = None,
        access_token_id: str = None,
        request_id: str = None,
    ):
        # The value of the activation code. The value is returned only once after the CreateAccessToken operation is called and cannot be subsequently queried. Make sure that you properly save the returned value.
        self.access_token_code = access_token_code
        # The ID of the activation code.
        self.access_token_id = access_token_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_code is not None:
            result['AccessTokenCode'] = self.access_token_code
        if self.access_token_id is not None:
            result['AccessTokenId'] = self.access_token_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenCode') is not None:
            self.access_token_code = m.get('AccessTokenCode')
        if m.get('AccessTokenId') is not None:
            self.access_token_id = m.get('AccessTokenId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccessTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCrossZoneMigrationJobRequestDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        disk_id: str = None,
        performance_level: str = None,
    ):
        # The disk category. A value of cloud_essd indicates enhanced SSD (ESSD).
        self.category = category
        # The disk ID.
        self.disk_id = disk_id
        # The performance level of the ESSD. Valid values:
        # 
        # *   PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # *   PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # *   PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        self.performance_level = performance_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        return self


class CreateCrossZoneMigrationJobRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        client_token: str = None,
        disk: List[CreateCrossZoneMigrationJobRequestDisk] = None,
        instance_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        target_instance_type: str = None,
        target_vswitch_id: str = None,
        target_zone_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true** (default): enables automatic payment. Make sure that you have sufficient balance within your account.
        # *   **false**: disables automatic payment. In this case, you must manually pay for the instance. For more information, see [Renew a subscription instance](https://help.aliyun.com/document_detail/85052.html).
        self.auto_pay = auto_pay
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The disk list.
        self.disk = disk
        # The instance ID.
        self.instance_id = instance_id
        self.owner_id = owner_id
        # The ID of the destination Alibaba Cloud region.
        # 
        # For example, if you want to migrate the source server to the China (Hangzhou) region, set this parameter to `cn-hangzhou`. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The type of the new instance.
        self.target_instance_type = target_instance_type
        # The vSwitch ID of the destination Elastic Compute Service (ECS) instance.
        self.target_vswitch_id = target_vswitch_id
        # The ID of the destination zone.
        self.target_zone_id = target_zone_id

    def validate(self):
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.target_instance_type is not None:
            result['TargetInstanceType'] = self.target_instance_type
        if self.target_vswitch_id is not None:
            result['TargetVSwitchId'] = self.target_vswitch_id
        if self.target_zone_id is not None:
            result['TargetZoneId'] = self.target_zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.disk = []
        if m.get('Disk') is not None:
            for k in m.get('Disk'):
                temp_model = CreateCrossZoneMigrationJobRequestDisk()
                self.disk.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TargetInstanceType') is not None:
            self.target_instance_type = m.get('TargetInstanceType')
        if m.get('TargetVSwitchId') is not None:
            self.target_vswitch_id = m.get('TargetVSwitchId')
        if m.get('TargetZoneId') is not None:
            self.target_zone_id = m.get('TargetZoneId')
        return self


class CreateCrossZoneMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the migration job.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCrossZoneMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCrossZoneMigrationJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCrossZoneMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReplicationJobRequestDataDiskPart(TeaModel):
    def __init__(
        self,
        block: bool = None,
        device: str = None,
        size_bytes: int = None,
    ):
        # Specifies whether to enable block replication for partition N in the destination data disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true
        self.block = block
        # The device ID of partition N in the destination data disk. The partitions in the destination data disk are arranged in the same sequential order as those in the source data disk.
        # 
        # >  You must set both the DataDisk.N.Part.N.Device and `DataDisk.N.Part.N.SizeBytes` parameters or leave both parameters empty.
        self.device = device
        # The size of partition N in the destination data disk. Unit: bytes. The default value is equal to the corresponding partition size of the source data disk.
        # 
        # > 
        # 
        # *   The total size of all partitions in a destination data disk cannot exceed the size of the destination data disk.
        # 
        # *   You must set both the `DataDisk.N.Part.N.Device` and DataDisk.N.Part.N.SizeBytes parameters or leave both parameters empty.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class CreateReplicationJobRequestDataDisk(TeaModel):
    def __init__(
        self,
        index: int = None,
        part: List[CreateReplicationJobRequestDataDiskPart] = None,
        size: int = None,
    ):
        # The index of data disk N on the destination ECS instance. Data disks on a destination ECS instance are arranged in a sequential order that starts from 1. Valid values: 1 to 16.
        # 
        # >  To create a destination data disk for a source server, make sure that the source server has data disks.
        self.index = index
        # The data disk partitions.
        self.part = part
        # The size of the data disk on the destination ECS instance. Unit: GiB. Valid values: 20 to 32768.
        # 
        # >  The size of a destination data disk must be larger than the size of data in the source data disk. For example, if the size of the source data disk is 500 GiB and the used space is 100 GiB, you must set this parameter to a value greater than 100.
        self.size = size

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = CreateReplicationJobRequestDataDiskPart()
                self.part.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateReplicationJobRequestDisksDataPart(TeaModel):
    def __init__(
        self,
        block: bool = None,
        path: str = None,
        size_bytes: int = None,
    ):
        # Whether block replication is enabled for the data disk partition. Valid values:
        # 
        # *   true: Block replication is enabled for the data disk partition.
        # *   false: Block replication is disabled for the data disk partition.
        self.block = block
        # The path of the data disk partition.
        self.path = path
        # The size of the data disk partition. Unit: bytes.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.path is not None:
            result['Path'] = self.path
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class CreateReplicationJobRequestDisksData(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        lvm: bool = None,
        part: List[CreateReplicationJobRequestDisksDataPart] = None,
        size: int = None,
    ):
        # The ID of the data disk.
        self.disk_id = disk_id
        # Specifies whether the data disk uses LVM. Valid values:
        # 
        # *   true: Use LVM.
        # *   false: Not use LVM.
        self.lvm = lvm
        # The information about the data disk partition.
        self.part = part
        # The size of the data disk of the migration source. Unit: GiB.
        self.size = size

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.lvm is not None:
            result['LVM'] = self.lvm
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('LVM') is not None:
            self.lvm = m.get('LVM')
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = CreateReplicationJobRequestDisksDataPart()
                self.part.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateReplicationJobRequestDisksSystemPart(TeaModel):
    def __init__(
        self,
        block: bool = None,
        path: str = None,
        size_bytes: int = None,
    ):
        # Specifies whether block replication is enabled for the system disk partition.
        self.block = block
        # The path of the system disk partition.
        self.path = path
        # The size of the system disk partition. Unit: bytes.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.path is not None:
            result['Path'] = self.path
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class CreateReplicationJobRequestDisksSystem(TeaModel):
    def __init__(
        self,
        lvm: bool = None,
        part: List[CreateReplicationJobRequestDisksSystemPart] = None,
        size: int = None,
    ):
        # Specifies whether to use LVM. Valid values:
        # 
        # *   true: Use LVM.
        # *   false: Not use LVM.
        # 
        # LVM is not supported:
        # 
        # *   If your source server runs Windows, LVM is not supported.
        # *   The system disk does not have a boot partition, and LVM is not supported.
        # 
        # After LVM is enabled, this feature does not take effect in the following scenarios:
        # 
        # *   LVM2 is not supported on your source server and the software package is not installed.
        # *   Your source server runs Debian with a kernel version of 3.x or earlier and XFS file systems are mounted.
        self.lvm = lvm
        # The information about the system disk partition.
        self.part = part
        # The size of the source system disk. Unit: GiB. Valid values: 20 to 32768.
        # 
        # >  The parameter value must be greater than the actual used space of the data disk on the source server. For example, if the size of the source disk is 500 GiB but the actual used space is 100 GiB, you must set this parameter to a value greater than 100 GiB.
        self.size = size

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lvm is not None:
            result['LVM'] = self.lvm
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LVM') is not None:
            self.lvm = m.get('LVM')
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = CreateReplicationJobRequestDisksSystemPart()
                self.part.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateReplicationJobRequestDisks(TeaModel):
    def __init__(
        self,
        data: List[CreateReplicationJobRequestDisksData] = None,
        system: CreateReplicationJobRequestDisksSystem = None,
    ):
        # The information about the data disk partition.
        self.data = data
        # The information about the system disk.
        self.system = system

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.system:
            self.system.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.system is not None:
            result['System'] = self.system.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = CreateReplicationJobRequestDisksData()
                self.data.append(temp_model.from_map(k))
        if m.get('System') is not None:
            temp_model = CreateReplicationJobRequestDisksSystem()
            self.system = temp_model.from_map(m['System'])
        return self


class CreateReplicationJobRequestSystemDiskPart(TeaModel):
    def __init__(
        self,
        block: bool = None,
        device: str = None,
        size_bytes: int = None,
    ):
        # Specifies whether to enable block replication for partition N in the destination system disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true
        self.block = block
        # The ID of partition N in the destination system disk. The partitions in the destination system disk are arranged in the same sequential order as those in the source system disk.
        # 
        # >  You must set both the SystemDiskPart.N.Device and `SystemDiskPart.N.SizeBytes` parameters or leave both parameters empty.
        self.device = device
        # The size of the partition N in the destination system disk. Unit: bytes. The default value is equal to the partition size of the source system disk.
        # 
        # > 
        # 
        # *   The total size of all partitions in the destination system disk cannot exceed the size of the destination system disk.
        # 
        # *   You must set both the `SystemDiskPart.N.Device` and SystemDiskPart.N.SizeBytes parameters or leave both parameters empty.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class CreateReplicationJobRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag for the migration job. Valid values of N: 1 to 20.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        self.key = key
        # The value of the tag for the migration job. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateReplicationJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        container_namespace: str = None,
        container_repository: str = None,
        container_tag: str = None,
        data_disk: List[CreateReplicationJobRequestDataDisk] = None,
        description: str = None,
        disks: CreateReplicationJobRequestDisks = None,
        frequency: int = None,
        image_name: str = None,
        instance_id: str = None,
        instance_ram_role: str = None,
        instance_type: str = None,
        job_type: int = None,
        launch_template_id: str = None,
        launch_template_version: str = None,
        license_type: str = None,
        max_number_of_image_to_keep: int = None,
        name: str = None,
        net_mode: int = None,
        owner_id: int = None,
        region_id: str = None,
        replication_parameters: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        run_once: bool = None,
        scheduled_start_time: str = None,
        source_id: str = None,
        system_disk_part: List[CreateReplicationJobRequestSystemDiskPart] = None,
        system_disk_size: int = None,
        tag: List[CreateReplicationJobRequestTag] = None,
        target_type: str = None,
        v_switch_id: str = None,
        valid_time: str = None,
        vpc_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The namespace of the destination Docker container image. For more information about Docker container images, see [Terms](https://help.aliyun.com/document_detail/60744.html).
        self.container_namespace = container_namespace
        # The repository that stores the destination Docker container image. For more information about Docker container images, see [Terms](https://help.aliyun.com/document_detail/60744.html).
        self.container_repository = container_repository
        # The tag of the destination Docker container image. For more information about Docker container images, see [Terms](https://help.aliyun.com/document_detail/60744.html).
        self.container_tag = container_tag
        # The data disks.
        self.data_disk = data_disk
        # The description of the migration job.
        # 
        # The description must be 2 to 128 characters in length, and can contain digits, colons (:), underscores (_), and hyphens (-). The description must start with a letter, but cannot start with `http://` or `https://`.
        self.description = description
        # The information about the disk.
        self.disks = disks
        # The interval at which SMC synchronizes incremental data to Alibaba Cloud. Unit: hour. Valid values: 1 to 168.
        # 
        # This parameter is required if you set the `RunOnce` parameter to false.
        # 
        # By default, this parameter is empty.
        self.frequency = frequency
        # The name of the destination image. The name must meet the following requirements:
        # 
        # *   The name must be unique within an Alibaba Cloud region.
        # *   The name must be 2 to 128 characters in length, and can contain digits, colons (:), underscores (_), and hyphens (-). The name must start with a letter, but cannot start with `http://` or `https://`.
        # 
        # >  If you specify an image name that already exists in the destination region, the migration job ID is appended to the image name as a suffix. Example: ImageName_j-2zexxxxxxxxxxxxx.
        self.image_name = image_name
        # The ID of the destination ECS instance.
        self.instance_id = instance_id
        # The name of the Resource Access Management (RAM) role that is assigned to the instance.
        self.instance_ram_role = instance_ram_role
        # The type of the intermediate instance.
        # 
        # You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to obtain the ECS instance types.
        # 
        # *   If you specify this parameter, SMC creates an intermediate instance of the specified instance type. If the specified instance type is unavailable, you cannot create the migration job.
        # *   If you do not specify this parameter, SMC selects an available instance type in a specific order to create an intermediate instance. For more information, see [SMC FAQ](https://help.aliyun.com/document_detail/121707.html).
        self.instance_type = instance_type
        # The type of the migration job. Valid values:
        # 
        # *   0: server migration.
        # *   1: operating system migration.
        # *   2: cross-zone migration.
        # *   3: agentless migration for a VMware VM.
        self.job_type = job_type
        # The ID of the launch template.
        self.launch_template_id = launch_template_id
        # The version number of the launch template.
        self.launch_template_version = launch_template_version
        # The license type. Valid values:
        # 
        # *   An empty value specifies no license.
        # *   A value of BYOL specifies Bring Your Own License (BYOL).
        # 
        # For more information, see [SMC FAQ](https://help.aliyun.com/document_detail/121707.html).
        self.license_type = license_type
        # The maximum number of images retained for the incremental migration job. Valid values: 1 to 10.
        # 
        # This parameter is required if you set the `RunOnce` parameter to false.
        # 
        # By default, this parameter is empty.
        self.max_number_of_image_to_keep = max_number_of_image_to_keep
        # The name of the migration job. The name must meet the following requirements:
        # 
        # *   The name must be unique.
        # *   The name must be 2 to 128 characters in length, and can contain digits, colons (:), underscores (_), and hyphens (-). The name must start with a letter, but cannot start with `http://` or `https://`.
        self.name = name
        # The network mode for data transmission. Valid values:
        # 
        # *   0: Data is transmitted over the Internet. Make sure that the source server can access the Internet.
        # *   2: Data is transmitted over a VPC. If you specify this value, you must specify the VSwitchId parameter. You do not need to specify the VpcId parameter because the value of the VpcId parameter can be retrieved based on the value of the VSwitchId parameter.
        # 
        # Default value: 0
        self.net_mode = net_mode
        self.owner_id = owner_id
        # The ID of the Alibaba Cloud region to which you want to migrate the source server.
        # 
        # For example, if you want to migrate the source server to the China (Hangzhou) region, set this parameter to `cn-hangzhou`. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the latest regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The parameters of the replication driver. The parameters must be specified as key-value pairs in the JSON format. The keys are fixed for each type of replication driver. The JSON string can be up to 2,048 characters in length.
        # 
        # A replication driver is a tool that is used to migrate a source server to an intermediate instance. The parameters vary based on the replication driver type. If you use a Server Migration Tool (SMT) driver, you can specify the following parameters:
        # 
        # *   bandwidth_limit: the maximum bandwidth for data transmission.
        # *   compress_level: the compression ratio of data to be transmitted.
        # *   checksum: specifies whether to enable checksum verification.
        # 
        # For more information about replication drivers, see the response parameter `SourceServers.ReplicationDriver` of the [DescribeSourceServers](https://help.aliyun.com/document_detail/121818.html) operation.
        self.replication_parameters = replication_parameters
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # Specifies whether to disable incremental migration for the source server. Valid values:
        # 
        # *   true: creates a migration job that runs only once. This is the default value. Incremental data of the source server is not synchronized.
        # *   false: creates an incremental migration job. In this case, you must specify the `Frequency` parameter. SMC synchronizes incremental data of the source server to Alibaba Cloud at the specified frequency. You can use an incremental migration job to synchronize incremental data from the source server to Alibaba Cloud without the need to interrupt your business. A full data image is generated for the source server when the job is running.
        # 
        # >  You can specify this parameter only when you create a migration job. The parameter value cannot be changed after the migration job is created.
        self.run_once = run_once
        # The time when you want to run the migration job. The time must meet the following requirements:
        # 
        # *   The time must be specified in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. For example, 2018-01-01T12:00:00Z specifies 20:00:00 on January 1, 2018 (UTC+8).
        # *   The value must be within 30 days after the current time.
        # 
        # >  If you do not specify this parameter, you must manually start the migration job after the job is created. You can call the [StartReplicationJob](https://help.aliyun.com/document_detail/121823.html) operation to start the migration job.
        self.scheduled_start_time = scheduled_start_time
        # The ID of the source server.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The information about system disk partitions.
        self.system_disk_part = system_disk_part
        # The system disk size of the destination ECS instance. Unit: GiB. Valid values: 20 to 2048.
        # 
        # >  The value must be greater than the used space of the system disk on the source server. For example, if the total size of the source disk is 500 GiB and the used space is 100 GiB, the value of this parameter must be greater than 100 GiB.
        self.system_disk_size = system_disk_size
        # The tags.
        self.tag = tag
        # The type of destination to which you want to migrate the source server. Valid values:
        # 
        # *   Image: After the migration job is complete, SMC generates an Elastic Compute Service (ECS) image for the source server.
        # *   ContainerImage: After the migration job is complete, SMC generates a Docker container image for the source server.
        # *   TargetInstance: After the migration job is completed, SMC migrates the source server to the destination instance. If you set this parameter to TargetInstance, you must set the `InstanceId` parameter.
        self.target_type = target_type
        # The ID of the vSwitch in the specified VPC.
        # 
        # You must set this parameter if you use a VPC to migrate data.
        self.v_switch_id = v_switch_id
        # The time when the migration job expires. You can schedule the migration job to expire 7 to 90 days after the job is created.
        # 
        # *   The time must be specified in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. For example, 2018-01-01T12:00:00Z specifies 20:00:00 on January 1, 2018 (UTC+8).
        # *   If you do not specify this parameter, the migration job does not expire.
        # *   After a migration job expires, the job state changes to Expired. SMC retains the migration job for seven days after the job expires. After the job is retained for seven days, SMC deletes the migration job.
        # 
        # By default, a migration job is valid for 30 days after it is created.
        self.valid_time = valid_time
        # The ID of a VPC for which you have configured an Express Connect circuit or a VPN gateway.
        self.vpc_id = vpc_id

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.disks:
            self.disks.validate()
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.container_namespace is not None:
            result['ContainerNamespace'] = self.container_namespace
        if self.container_repository is not None:
            result['ContainerRepository'] = self.container_repository
        if self.container_tag is not None:
            result['ContainerTag'] = self.container_tag
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.disks is not None:
            result['Disks'] = self.disks.to_map()
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ram_role is not None:
            result['InstanceRamRole'] = self.instance_ram_role
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.license_type is not None:
            result['LicenseType'] = self.license_type
        if self.max_number_of_image_to_keep is not None:
            result['MaxNumberOfImageToKeep'] = self.max_number_of_image_to_keep
        if self.name is not None:
            result['Name'] = self.name
        if self.net_mode is not None:
            result['NetMode'] = self.net_mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replication_parameters is not None:
            result['ReplicationParameters'] = self.replication_parameters
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.run_once is not None:
            result['RunOnce'] = self.run_once
        if self.scheduled_start_time is not None:
            result['ScheduledStartTime'] = self.scheduled_start_time
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.valid_time is not None:
            result['ValidTime'] = self.valid_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContainerNamespace') is not None:
            self.container_namespace = m.get('ContainerNamespace')
        if m.get('ContainerRepository') is not None:
            self.container_repository = m.get('ContainerRepository')
        if m.get('ContainerTag') is not None:
            self.container_tag = m.get('ContainerTag')
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = CreateReplicationJobRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Disks') is not None:
            temp_model = CreateReplicationJobRequestDisks()
            self.disks = temp_model.from_map(m['Disks'])
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRamRole') is not None:
            self.instance_ram_role = m.get('InstanceRamRole')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')
        if m.get('MaxNumberOfImageToKeep') is not None:
            self.max_number_of_image_to_keep = m.get('MaxNumberOfImageToKeep')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetMode') is not None:
            self.net_mode = m.get('NetMode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicationParameters') is not None:
            self.replication_parameters = m.get('ReplicationParameters')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RunOnce') is not None:
            self.run_once = m.get('RunOnce')
        if m.get('ScheduledStartTime') is not None:
            self.scheduled_start_time = m.get('ScheduledStartTime')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = CreateReplicationJobRequestSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateReplicationJobRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ValidTime') is not None:
            self.valid_time = m.get('ValidTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateReplicationJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the migration job.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateReplicationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateReplicationJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkgroupRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of a specified workgroup.
        # 
        # You can specify an empty string as a tag key. The tag key can be up to 64 characters in length and cannot contain http:// or https://.
        self.key = key
        # The tag value of a specified workgroup.
        # 
        # You can specify an empty string as a tag value. The tag value can be up to 64 characters in length and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateWorkgroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        tag: List[CreateWorkgroupRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the workgroup.
        # 
        # The description must be 2 to 128 characters in length. It must start with a letter and cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The name of the workgroup. The name must meet the following requirements:
        # 
        # *   The name must be unique.
        # *   The name must be 2 to 128 characters in length. It must start with a letter and cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.name = name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # The tag information of the workgroup.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateWorkgroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateWorkgroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        workgroup_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The workgroup ID.
        self.workgroup_id = workgroup_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workgroup_id is not None:
            result['WorkgroupId'] = self.workgroup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WorkgroupId') is not None:
            self.workgroup_id = m.get('WorkgroupId')
        return self


class CreateWorkgroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWorkgroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWorkgroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CutOverReplicationJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        sync_data: bool = None,
    ):
        # The ID of the incremental migration job.
        # 
        # This parameter is required.
        self.job_id = job_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # Specifies whether to migrate full data for the last time. Valid Values:
        # 
        # *   true: migrates full data for the last time.
        # *   false: does not migrate full data for the last time.
        # 
        # Default value: false.
        self.sync_data = sync_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.sync_data is not None:
            result['SyncData'] = self.sync_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SyncData') is not None:
            self.sync_data = m.get('SyncData')
        return self


class CutOverReplicationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CutOverReplicationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CutOverReplicationJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CutOverReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessTokenRequest(TeaModel):
    def __init__(
        self,
        access_token_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        # The ID of the activation code.
        # 
        # This parameter is required.
        self.access_token_id = access_token_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_id is not None:
            result['AccessTokenId'] = self.access_token_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenId') is not None:
            self.access_token_id = m.get('AccessTokenId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DeleteAccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccessTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReplicationJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        # The migration job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DeleteReplicationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteReplicationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteReplicationJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSourceServerRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        source_id: str = None,
    ):
        # Specifies whether to forcibly delete the migration source. Valid values:
        # 
        # *   true: forcibly deletes the migration source and the migration job created for the migration source, and releases the intermediate resources of the migration job.
        # *   false: does not delete the migration source if a migration job is created for the migration source.
        self.force = force
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # The migration source ID.
        # 
        # This parameter is required.
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class DeleteSourceServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSourceServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSourceServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSourceServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkgroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        workgroup_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # The workgroup ID.
        # 
        # This parameter is required.
        self.workgroup_id = workgroup_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.workgroup_id is not None:
            result['WorkgroupId'] = self.workgroup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('WorkgroupId') is not None:
            self.workgroup_id = m.get('WorkgroupId')
        return self


class DeleteWorkgroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWorkgroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWorkgroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWorkgroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeReplicationJobsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag N that is added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag key can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.
        self.key = key
        # The value of tag N that is added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.[](http://https://。)
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeReplicationJobsRequest(TeaModel):
    def __init__(
        self,
        business_status: str = None,
        instance_id: List[str] = None,
        job_id: List[str] = None,
        job_type: int = None,
        name: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        source_id: List[str] = None,
        status: str = None,
        tag: List[DescribeReplicationJobsRequestTag] = None,
    ):
        # The business status of the migration job. Valid values:
        # 
        # *   Preparing: The migration is being prepared.
        # *   Syncing: Data is being synchronized.
        # *   Processing: The migration is in progress.
        # *   Cleaning: Intermediate resources are being released.
        self.business_status = business_status
        # The IDs of the destination Elastic Compute Service (ECS) instances.
        self.instance_id = instance_id
        # The IDs of the migration jobs. You can specify a maximum of 50 IDs.
        self.job_id = job_id
        # The type of the migration job. Valid values:
        # 
        # *   0: server migration.
        # *   1: operating system migration.
        # *   2: cross-zone migration.
        # *   3: agentless migration for a VMware VM.
        self.job_type = job_type
        # The name of the migration job.
        self.name = name
        self.owner_id = owner_id
        # The page number. Minimum value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The ID of the Alibaba Cloud region to which you want to migrate the source server.
        # 
        # For example, if you want to migrate a source server to the China (Hangzhou) region, set this parameter to `cn-hangzhou`. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the latest regions.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The IDs of the source servers. You can specify a maximum of 50 IDs.
        self.source_id = source_id
        # The status of the migration job. Valid values:
        # 
        # *   Ready: The migration job is not started.
        # *   Running: The migration job is running.
        # *   Stopped: The migration job is paused.
        # *   InError: An error occurs in the migration job.
        # *   Finished: The migration job is complete.
        # *   Waiting: The migration job is waiting to run.
        # *   Expired: The migration job has expired.
        # *   Deleting: The migration job is being deleted.
        self.status = status
        # The information about tags that are attached to the SMC resource.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.name is not None:
            result['Name'] = self.name
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
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeReplicationJobsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskPartsPart(TeaModel):
    def __init__(
        self,
        block: bool = None,
        device: str = None,
        size_bytes: int = None,
    ):
        # Indicates whether block replication is enabled for the data disk partition.
        self.block = block
        # The device ID of the data disk partition.
        self.device = device
        # The size of the data disk partition. Unit: bytes.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskParts(TeaModel):
    def __init__(
        self,
        part: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskPartsPart] = None,
    ):
        self.part = part

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskPartsPart()
                self.part.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDisk(TeaModel):
    def __init__(
        self,
        index: int = None,
        parts: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskParts = None,
        size: int = None,
    ):
        # The index number of the data disk.
        self.index = index
        # The data disk partitions.
        self.parts = parts
        # The size of the data disk. Unit: GiB.
        self.size = size

    def validate(self):
        if self.parts:
            self.parts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.parts is not None:
            result['Parts'] = self.parts.to_map()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Parts') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDiskParts()
            self.parts = temp_model.from_map(m['Parts'])
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisks(TeaModel):
    def __init__(
        self,
        data_disk: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDisk] = None,
    ):
        self.data_disk = data_disk

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisksDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksDataDataPartsPart(TeaModel):
    def __init__(
        self,
        block: bool = None,
        path: str = None,
        size_bytes: int = None,
    ):
        # Whether block replication is enabled for the data disk partition. Valid values:
        # 
        # *   true: Block replication is enabled for the data disk partition.
        # *   false: Block replication is disabled for the data disk partition.
        self.block = block
        # The path of the data disk partition.
        self.path = path
        # The size of the data disk partition. Unit: bytes.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.path is not None:
            result['Path'] = self.path
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksDataDataParts(TeaModel):
    def __init__(
        self,
        part: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksDataDataPartsPart] = None,
    ):
        self.part = part

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksDataDataPartsPart()
                self.part.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksDataData(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        lvm: bool = None,
        parts: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksDataDataParts = None,
        size: int = None,
    ):
        # The ID of the data disk.
        self.disk_id = disk_id
        # Specifies whether to use LVM. Valid values:
        # 
        # *   true: Use LVM.
        # *   false: Not use LVM.
        self.lvm = lvm
        # The information about the data disk partition.
        self.parts = parts
        # The size of a data disk on the destination ECS instance. Unit: GiB. Valid values: 20 to 32768.
        # 
        # >  The size of a destination data disk must be larger than the size of data in the corresponding source data disk. For example, if the size of the source disk is 500 GiB but the actual used space is 100 GiB, you must set this parameter to a value greater than 100 GiB.
        self.size = size

    def validate(self):
        if self.parts:
            self.parts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.lvm is not None:
            result['LVM'] = self.lvm
        if self.parts is not None:
            result['Parts'] = self.parts.to_map()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('LVM') is not None:
            self.lvm = m.get('LVM')
        if m.get('Parts') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksDataDataParts()
            self.parts = temp_model.from_map(m['Parts'])
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksData(TeaModel):
    def __init__(
        self,
        data: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksDataData()
                self.data.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksSystemPartsPart(TeaModel):
    def __init__(
        self,
        block: bool = None,
        path: str = None,
        size_bytes: int = None,
    ):
        # Specifies whether block replication is enabled for the system disk partition. Valid values:
        # 
        # *   true: Block replication is enabled for the system disk partition.
        # *   false: Block replication is disabled for the system disk partition.
        self.block = block
        # The path of the system disk partition.
        self.path = path
        # The size of the system disk partition. Unit: bytes.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.path is not None:
            result['Path'] = self.path
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksSystemParts(TeaModel):
    def __init__(
        self,
        part: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksSystemPartsPart] = None,
    ):
        self.part = part

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksSystemPartsPart()
                self.part.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksSystem(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        lvm: bool = None,
        parts: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksSystemParts = None,
        size: int = None,
    ):
        # The ID of the system disk.
        self.disk_id = disk_id
        # Specifies whether to use LVM. Valid values:
        # 
        # *   true: Use LVM.
        # *   false: Not use LVM.
        self.lvm = lvm
        # The information about the system disk partition.
        self.parts = parts
        # The size of the source system disk. Unit: GiB. Valid values: 20 to 32768.
        # 
        # >  The parameter value must be greater than the actual used space of the data disk on the source server. For example, if the size of the source disk is 500 GiB but the actual used space is 100 GiB, you must set this parameter to a value greater than 100 GiB.
        self.size = size

    def validate(self):
        if self.parts:
            self.parts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.lvm is not None:
            result['LVM'] = self.lvm
        if self.parts is not None:
            result['Parts'] = self.parts.to_map()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('LVM') is not None:
            self.lvm = m.get('LVM')
        if m.get('Parts') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksSystemParts()
            self.parts = temp_model.from_map(m['Parts'])
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisks(TeaModel):
    def __init__(
        self,
        data: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksData = None,
        system: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksSystem = None,
    ):
        # The information about the data disk.
        self.data = data
        # The information about the system disk.
        self.system = system

    def validate(self):
        if self.data:
            self.data.validate()
        if self.system:
            self.system.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.system is not None:
            result['System'] = self.system.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('System') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisksSystem()
            self.system = temp_model.from_map(m['System'])
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRunsReplicationJobRun(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        image_id: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The time when the migration job ended. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # >  The time displayed in the SMC console is in the format of UTC+8.
        self.end_time = end_time
        # The ID of the destination image.
        self.image_id = image_id
        # The time when the migration job was started. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # >  The time displayed in the SMC console is in the format of UTC+8.
        self.start_time = start_time
        # The method used to run the migration job. Valid values:
        # 
        # *   Manual: The migration job was manually started.
        # *   Schedule: The migration job was started at a scheduled time or at a specific interval.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRuns(TeaModel):
    def __init__(
        self,
        replication_job_run: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRunsReplicationJobRun] = None,
    ):
        self.replication_job_run = replication_job_run

    def validate(self):
        if self.replication_job_run:
            for k in self.replication_job_run:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReplicationJobRun'] = []
        if self.replication_job_run is not None:
            for k in self.replication_job_run:
                result['ReplicationJobRun'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.replication_job_run = []
        if m.get('ReplicationJobRun') is not None:
            for k in m.get('ReplicationJobRun'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRunsReplicationJobRun()
                self.replication_job_run.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskPartsSystemDiskPart(TeaModel):
    def __init__(
        self,
        block: bool = None,
        device: str = None,
        size_bytes: int = None,
    ):
        # Indicates whether block replication is enabled for the system disk partition.
        self.block = block
        # The device ID of the system disk partition.
        self.device = device
        # The size of the system disk partition. Unit: bytes.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskParts(TeaModel):
    def __init__(
        self,
        system_disk_part: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskPartsSystemDiskPart] = None,
    ):
        self.system_disk_part = system_disk_part

    def validate(self):
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskPartsSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag N that is added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag key can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.[](http://https://。)
        self.key = key
        # The value of tag N that is added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.[](http://https://。)
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBodyReplicationJobsReplicationJob(TeaModel):
    def __init__(
        self,
        business_status: str = None,
        container_namespace: str = None,
        container_repository: str = None,
        container_tag: str = None,
        creation_time: str = None,
        data_disks: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisks = None,
        description: str = None,
        disks: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisks = None,
        end_time: str = None,
        error_code: str = None,
        frequency: int = None,
        image_id: str = None,
        image_name: str = None,
        instance_id: str = None,
        instance_ram_role: str = None,
        instance_type: str = None,
        job_id: str = None,
        job_type: int = None,
        launch_template_id: str = None,
        launch_template_version: str = None,
        license_type: str = None,
        max_number_of_image_to_keep: int = None,
        name: str = None,
        net_mode: int = None,
        progress: float = None,
        region_id: str = None,
        replication_job_runs: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRuns = None,
        replication_parameters: str = None,
        resource_group_id: str = None,
        run_once: bool = None,
        scheduled_start_time: str = None,
        source_id: str = None,
        start_time: str = None,
        status: str = None,
        status_info: str = None,
        system_disk_parts: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskParts = None,
        system_disk_size: int = None,
        tags: DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTags = None,
        target_type: str = None,
        transition_instance_id: str = None,
        v_switch_id: str = None,
        valid_time: str = None,
        vpc_id: str = None,
    ):
        # The business status of the migration job. Valid values:
        # 
        # *   Preparing: The migration is being prepared.
        # *   Syncing: Data is being synchronized.
        # *   Processing: The migration is in progress.
        # *   Cleaning: Intermediate resources are being released.
        self.business_status = business_status
        # The namespace of the destination Docker container image.
        self.container_namespace = container_namespace
        # The repository that stores the destination Docker container image.
        self.container_repository = container_repository
        # The tag of the destination Docker container image.
        self.container_tag = container_tag
        # The time when the migration job was created.
        self.creation_time = creation_time
        # The data disks on the destination ECS instance.
        self.data_disks = data_disks
        # The description of the migration job.
        self.description = description
        # The information about the disk.
        self.disks = disks
        # The time when the migration job was complete. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # >  The time displayed in the SMC console is in the format of UTC+8.
        self.end_time = end_time
        # The error code returned if an error occurred in the migration job.
        self.error_code = error_code
        # The interval at which the incremental migration job runs. Unit: hour. Valid values: 1 to 168.
        self.frequency = frequency
        # The ID of the destination image.
        self.image_id = image_id
        # The name of the destination image.
        self.image_name = image_name
        # The ID of the destination ECS instance.
        self.instance_id = instance_id
        # The name of the Resource Access Management (RAM) role that is assigned to the instance.
        self.instance_ram_role = instance_ram_role
        # The instance type of the intermediate instance.
        self.instance_type = instance_type
        # The ID of the migration job.
        self.job_id = job_id
        # The type of the migration job. Valid values:
        # 
        # *   0: server migration.
        # *   1: operating system migration.
        # *   2: cross-zone migration.
        # *   3: agentless migration for a VMware VM.
        self.job_type = job_type
        # The ID of the launch template.
        self.launch_template_id = launch_template_id
        # The versions of the launch template.
        self.launch_template_version = launch_template_version
        # The type of license for the migration job. Valid values:
        # 
        # *   An empty value indicates no license.
        # *   A value of BYOL indicates Bring Your Own License (BYOL).
        self.license_type = license_type
        # The maximum number of images retained for the incremental migration job. Valid values: 1 to 10.
        self.max_number_of_image_to_keep = max_number_of_image_to_keep
        # The name of the migration job.
        self.name = name
        # The type of network used for the migration.
        self.net_mode = net_mode
        # The progress of the migration job.
        self.progress = progress
        # The ID of the Alibaba Cloud region to which the source server is migrated.
        self.region_id = region_id
        # The execution records of the migration job.
        self.replication_job_runs = replication_job_runs
        # The string of key-value pairs configured for the replication driver.
        self.replication_parameters = replication_parameters
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether incremental migration is disabled for the source server. Valid values:
        # 
        # *   true: Incremental migration is disabled. A migration job runs only once after the job is created.
        # *   false: Incremental migration is enabled. For an incremental migration job, SMC synchronizes incremental data to Alibaba Cloud at the interval specified by the `Frequency` parameter.
        self.run_once = run_once
        # The time when the migration job is scheduled to run. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. The time must meet the following requirements:
        # 
        # *   The value must be within 30 days after the current time.
        # *   If you do not specify this parameter, you must manually start the migration job after the migration job is created. You can call the [StartReplicationJob](https://help.aliyun.com/document_detail/121823.html) operation to start the migration job.
        self.scheduled_start_time = scheduled_start_time
        # The ID of the source server.
        self.source_id = source_id
        # The time when the migration job was started. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # >  The time displayed in the SMC console is in the format of UTC+8.
        self.start_time = start_time
        # The status of the migration job. Valid values:
        # 
        # *   Ready: The migration job is not started.
        # *   Running: The migration job is running.
        # *   Stopped: The migration job is paused.
        # *   InError: An error occurs in the migration job.
        # *   Finished: The migration job is complete.
        # *   Waiting: The migration job is waiting to run.
        # *   Expired: The migration job has expired.
        # *   Deleting: The migration job is being deleted.
        self.status = status
        # The status information about the migration job.
        self.status_info = status_info
        # The system disk partitions.
        self.system_disk_parts = system_disk_parts
        # The size of the system disk of the destination ECS instance.
        self.system_disk_size = system_disk_size
        # The information about tags that are attached to the SMC resource.
        self.tags = tags
        # The type of destination to which the source server is migrated. Valid values:
        # 
        # *   Image: After the migration job is complete, SMC generates an ECS image for the source server.
        # *   ContainerImage: After the migration job is complete, SMC generates a Docker container image for the source server.
        # *   TargetInstance: After the migration job is complete, SMC migrates the source server to the destination instance. If you set this parameter to TargetInstance, you must set the InstanceId parameter.
        self.target_type = target_type
        # The ID of the intermediate instance.
        self.transition_instance_id = transition_instance_id
        # The ID of the vSwitch in the specified VPC.
        self.v_switch_id = v_switch_id
        # The time when the migration job expired. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # >  The time displayed in the SMC console is in the format of UTC+8.
        self.valid_time = valid_time
        # The ID of a virtual private cloud (VPC) for which you have configured an Express Connect circuit or a VPN gateway.
        self.vpc_id = vpc_id

    def validate(self):
        if self.data_disks:
            self.data_disks.validate()
        if self.disks:
            self.disks.validate()
        if self.replication_job_runs:
            self.replication_job_runs.validate()
        if self.system_disk_parts:
            self.system_disk_parts.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.container_namespace is not None:
            result['ContainerNamespace'] = self.container_namespace
        if self.container_repository is not None:
            result['ContainerRepository'] = self.container_repository
        if self.container_tag is not None:
            result['ContainerTag'] = self.container_tag
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_disks is not None:
            result['DataDisks'] = self.data_disks.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.disks is not None:
            result['Disks'] = self.disks.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ram_role is not None:
            result['InstanceRamRole'] = self.instance_ram_role
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.license_type is not None:
            result['LicenseType'] = self.license_type
        if self.max_number_of_image_to_keep is not None:
            result['MaxNumberOfImageToKeep'] = self.max_number_of_image_to_keep
        if self.name is not None:
            result['Name'] = self.name
        if self.net_mode is not None:
            result['NetMode'] = self.net_mode
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replication_job_runs is not None:
            result['ReplicationJobRuns'] = self.replication_job_runs.to_map()
        if self.replication_parameters is not None:
            result['ReplicationParameters'] = self.replication_parameters
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.run_once is not None:
            result['RunOnce'] = self.run_once
        if self.scheduled_start_time is not None:
            result['ScheduledStartTime'] = self.scheduled_start_time
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_info is not None:
            result['StatusInfo'] = self.status_info
        if self.system_disk_parts is not None:
            result['SystemDiskParts'] = self.system_disk_parts.to_map()
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.transition_instance_id is not None:
            result['TransitionInstanceId'] = self.transition_instance_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.valid_time is not None:
            result['ValidTime'] = self.valid_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('ContainerNamespace') is not None:
            self.container_namespace = m.get('ContainerNamespace')
        if m.get('ContainerRepository') is not None:
            self.container_repository = m.get('ContainerRepository')
        if m.get('ContainerTag') is not None:
            self.container_tag = m.get('ContainerTag')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataDisks') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDataDisks()
            self.data_disks = temp_model.from_map(m['DataDisks'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Disks') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobDisks()
            self.disks = temp_model.from_map(m['Disks'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRamRole') is not None:
            self.instance_ram_role = m.get('InstanceRamRole')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')
        if m.get('MaxNumberOfImageToKeep') is not None:
            self.max_number_of_image_to_keep = m.get('MaxNumberOfImageToKeep')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetMode') is not None:
            self.net_mode = m.get('NetMode')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicationJobRuns') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobReplicationJobRuns()
            self.replication_job_runs = temp_model.from_map(m['ReplicationJobRuns'])
        if m.get('ReplicationParameters') is not None:
            self.replication_parameters = m.get('ReplicationParameters')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RunOnce') is not None:
            self.run_once = m.get('RunOnce')
        if m.get('ScheduledStartTime') is not None:
            self.scheduled_start_time = m.get('ScheduledStartTime')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusInfo') is not None:
            self.status_info = m.get('StatusInfo')
        if m.get('SystemDiskParts') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobSystemDiskParts()
            self.system_disk_parts = temp_model.from_map(m['SystemDiskParts'])
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('Tags') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJobTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TransitionInstanceId') is not None:
            self.transition_instance_id = m.get('TransitionInstanceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ValidTime') is not None:
            self.valid_time = m.get('ValidTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeReplicationJobsResponseBodyReplicationJobs(TeaModel):
    def __init__(
        self,
        replication_job: List[DescribeReplicationJobsResponseBodyReplicationJobsReplicationJob] = None,
    ):
        self.replication_job = replication_job

    def validate(self):
        if self.replication_job:
            for k in self.replication_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReplicationJob'] = []
        if self.replication_job is not None:
            for k in self.replication_job:
                result['ReplicationJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.replication_job = []
        if m.get('ReplicationJob') is not None:
            for k in m.get('ReplicationJob'):
                temp_model = DescribeReplicationJobsResponseBodyReplicationJobsReplicationJob()
                self.replication_job.append(temp_model.from_map(k))
        return self


class DescribeReplicationJobsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        replication_jobs: DescribeReplicationJobsResponseBodyReplicationJobs = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The details of migration jobs.
        self.replication_jobs = replication_jobs
        # The request ID.
        self.request_id = request_id
        # The total number of migration jobs returned.
        self.total_count = total_count

    def validate(self):
        if self.replication_jobs:
            self.replication_jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.replication_jobs is not None:
            result['ReplicationJobs'] = self.replication_jobs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReplicationJobs') is not None:
            temp_model = DescribeReplicationJobsResponseBodyReplicationJobs()
            self.replication_jobs = temp_model.from_map(m['ReplicationJobs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeReplicationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeReplicationJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeReplicationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSourceServersRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N that is attached to the SMC resource. Valid values of N: 1 to 20.
        # 
        # You cannot specify an empty string as a tag key. The tag key can be up to 64 characters in length and cannot contain http:// or https://. The tag key cannot start with acs: or aliyun.
        self.key = key
        # The value of tag N that is attached to the SMC resource. Valid values of N: 1 to 20.
        # 
        # You can specify an empty string as a tag key. The tag value can be up to 64 characters in length and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeSourceServersRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        name: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        related_job_type: List[str] = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        source_id: List[str] = None,
        state: str = None,
        tag: List[DescribeSourceServersRequestTag] = None,
        workgroup_id: str = None,
    ):
        # The ID of the migration job.
        self.job_id = job_id
        # The name of the migration source. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https://. It can contain digits, colons (:), underscores (_), and hyphens (-).
        # 
        # This parameter is empty by default.
        self.name = name
        self.owner_id = owner_id
        # The page number. Minimum value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The type of migration job that is associated with the migration source.
        self.related_job_type = related_job_type
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The migration source ID. You can specify multiple IDs.
        self.source_id = source_id
        # The state of the migration source. Valid values:
        # 
        # *   Unavailable: The migration source is inactive, or an error occurs in the migration source.
        # *   Available: The migration source is active.
        # *   InUse: The migration source is being migrated.
        # *   Deleting: The migration source is being deleted from Server Migration Center (SMC).
        self.state = state
        # The tag.
        self.tag = tag
        # The workgroup ID.
        self.workgroup_id = workgroup_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.related_job_type is not None:
            result['RelatedJobType'] = self.related_job_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.state is not None:
            result['State'] = self.state
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.workgroup_id is not None:
            result['WorkgroupId'] = self.workgroup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RelatedJobType') is not None:
            self.related_job_type = m.get('RelatedJobType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeSourceServersRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('WorkgroupId') is not None:
            self.workgroup_id = m.get('WorkgroupId')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskPartsPart(TeaModel):
    def __init__(
        self,
        can_block: bool = None,
        device: str = None,
        need: bool = None,
        path: str = None,
        size_bytes: int = None,
    ):
        # Indicates whether block replication is enabled for the data disk partition.
        self.can_block = can_block
        # The device ID of the data disk partition.
        self.device = device
        # Indicates whether the data disk partition must be selected.
        self.need = need
        # The path of the data disk partition.
        self.path = path
        # The size of the data disk partition. Unit: bytes.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_block is not None:
            result['CanBlock'] = self.can_block
        if self.device is not None:
            result['Device'] = self.device
        if self.need is not None:
            result['Need'] = self.need
        if self.path is not None:
            result['Path'] = self.path
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanBlock') is not None:
            self.can_block = m.get('CanBlock')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('Need') is not None:
            self.need = m.get('Need')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskParts(TeaModel):
    def __init__(
        self,
        part: List[DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskPartsPart] = None,
    ):
        self.part = part

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskPartsPart()
                self.part.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDisk(TeaModel):
    def __init__(
        self,
        index: int = None,
        parts: DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskParts = None,
        path: str = None,
        size: int = None,
    ):
        # The index number of the data disk.
        self.index = index
        # The information about the data disk partition.
        self.parts = parts
        # The path of data disk N.
        self.path = path
        # The size of data disk N. Unit: GiB.
        self.size = size

    def validate(self):
        if self.parts:
            self.parts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.parts is not None:
            result['Parts'] = self.parts.to_map()
        if self.path is not None:
            result['Path'] = self.path
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Parts') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDiskParts()
            self.parts = temp_model.from_map(m['Parts'])
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDataDisks(TeaModel):
    def __init__(
        self,
        data_disk: List[DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDisk] = None,
    ):
        self.data_disk = data_disk

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisksDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDisksDataDataPartsPart(TeaModel):
    def __init__(
        self,
        can_block: bool = None,
        path: str = None,
        size_bytes: int = None,
        type: str = None,
    ):
        # Whether block replication is enabled for the data disk partition. Valid values:
        # 
        # *   true: Block replication is enabled for the data disk partition.
        # *   false: Block replication is disabled for the data disk partition.
        self.can_block = can_block
        # The path of the data disk partition.
        self.path = path
        # The size of the data disk partition. Unit: bytes.
        self.size_bytes = size_bytes
        # The type of the data disk partition. Valid values:
        # 
        # *   Normal: normal partition.
        # *   System: system partition.
        # *   Boot: boot partition.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_block is not None:
            result['CanBlock'] = self.can_block
        if self.path is not None:
            result['Path'] = self.path
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanBlock') is not None:
            self.can_block = m.get('CanBlock')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDisksDataDataParts(TeaModel):
    def __init__(
        self,
        part: List[DescribeSourceServersResponseBodySourceServersSourceServerDisksDataDataPartsPart] = None,
    ):
        self.part = part

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDisksDataDataPartsPart()
                self.part.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDisksDataData(TeaModel):
    def __init__(
        self,
        offset: int = None,
        parts: DescribeSourceServersResponseBodySourceServersSourceServerDisksDataDataParts = None,
        size: int = None,
    ):
        # The start offset of the first partition of the data disk. Unit: bytes.
        self.offset = offset
        # The information about the data disk partition.
        self.parts = parts
        # The data disk size of the migration source. Unit: GiB.
        self.size = size

    def validate(self):
        if self.parts:
            self.parts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.parts is not None:
            result['Parts'] = self.parts.to_map()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Parts') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDisksDataDataParts()
            self.parts = temp_model.from_map(m['Parts'])
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDisksData(TeaModel):
    def __init__(
        self,
        data: List[DescribeSourceServersResponseBodySourceServersSourceServerDisksDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDisksDataData()
                self.data.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDisksSystemPartsPart(TeaModel):
    def __init__(
        self,
        can_block: bool = None,
        path: str = None,
        size_bytes: int = None,
        type: str = None,
    ):
        # Indicates whether block replication is enabled for the system disk partition. Valid values:
        # 
        # *   true: Block replication is enabled for the system disk partition.
        # *   false: Block replication is disabled for the system disk partition.
        self.can_block = can_block
        # The path of the system disk partition.
        self.path = path
        # The size of the system disk partition. Unit: bytes.
        self.size_bytes = size_bytes
        # The type of the system disk partition. Valid values:
        # 
        # *   Normal: normal partition.
        # *   System: system partition.
        # *   Boot: boot partition.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_block is not None:
            result['CanBlock'] = self.can_block
        if self.path is not None:
            result['Path'] = self.path
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanBlock') is not None:
            self.can_block = m.get('CanBlock')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDisksSystemParts(TeaModel):
    def __init__(
        self,
        part: List[DescribeSourceServersResponseBodySourceServersSourceServerDisksSystemPartsPart] = None,
    ):
        self.part = part

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDisksSystemPartsPart()
                self.part.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDisksSystem(TeaModel):
    def __init__(
        self,
        offset: int = None,
        parts: DescribeSourceServersResponseBodySourceServersSourceServerDisksSystemParts = None,
        size: int = None,
    ):
        # The start offset of the first partition of the system disk. Unit: bytes.
        self.offset = offset
        # The information about the system disk partition.
        self.parts = parts
        # The size of the source system disk. Unit: GiB. Valid values: 20 to 32768.
        # 
        # >  The parameter value must be greater than the actual used space of the data disk on the source server. For example, if the size of the source disk is 500 GiB but the actual used space is 100 GiB, you must set this parameter to a value greater than 100 GiB.
        self.size = size

    def validate(self):
        if self.parts:
            self.parts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.parts is not None:
            result['Parts'] = self.parts.to_map()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Parts') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDisksSystemParts()
            self.parts = temp_model.from_map(m['Parts'])
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerDisks(TeaModel):
    def __init__(
        self,
        data: DescribeSourceServersResponseBodySourceServersSourceServerDisksData = None,
        system: DescribeSourceServersResponseBodySourceServersSourceServerDisksSystem = None,
    ):
        # The list of data disk information.
        self.data = data
        # The information about the system disk.
        self.system = system

    def validate(self):
        if self.data:
            self.data.validate()
        if self.system:
            self.system.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.system is not None:
            result['System'] = self.system.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDisksData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('System') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDisksSystem()
            self.system = temp_model.from_map(m['System'])
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskPartsSystemDiskPart(TeaModel):
    def __init__(
        self,
        can_block: bool = None,
        device: str = None,
        need: bool = None,
        path: str = None,
        size_bytes: int = None,
    ):
        # Indicates whether block replication is enabled for the system disk partition.
        self.can_block = can_block
        # The device ID of the system disk partition.
        self.device = device
        # Indicates whether the system disk partition must be selected.
        self.need = need
        # The path of the system disk partition.
        self.path = path
        # The size of the system disk partition. Unit: bytes.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_block is not None:
            result['CanBlock'] = self.can_block
        if self.device is not None:
            result['Device'] = self.device
        if self.need is not None:
            result['Need'] = self.need
        if self.path is not None:
            result['Path'] = self.path
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanBlock') is not None:
            self.can_block = m.get('CanBlock')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('Need') is not None:
            self.need = m.get('Need')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskParts(TeaModel):
    def __init__(
        self,
        system_disk_part: List[DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskPartsSystemDiskPart] = None,
    ):
        self.system_disk_part = system_disk_part

    def validate(self):
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskPartsSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServerTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N that is attached to the SMC resource. Valid values of N: 1 to 20.
        # 
        # You cannot specify an empty string as a tag key. The tag key can be up to 64 characters in length and cannot contain http:// or https://. The tag key cannot start with acs: or aliyun.
        self.key = key
        # The value of tag N that is attached to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag key can be an empty string. The tag value can be up to 64 characters in length and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeSourceServersResponseBodySourceServersSourceServerTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeSourceServersResponseBodySourceServersSourceServerTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServerTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBodySourceServersSourceServer(TeaModel):
    def __init__(
        self,
        agent_version: str = None,
        architecture: str = None,
        creation_time: str = None,
        data_disks: DescribeSourceServersResponseBodySourceServersSourceServerDataDisks = None,
        description: str = None,
        disks: DescribeSourceServersResponseBodySourceServersSourceServerDisks = None,
        error_code: str = None,
        heartbeat_rate: int = None,
        job_id: str = None,
        kernel_level: int = None,
        name: str = None,
        platform: str = None,
        replication_driver: str = None,
        resource_group_id: str = None,
        source_id: str = None,
        state: str = None,
        status_info: str = None,
        system_disk_parts: DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskParts = None,
        system_disk_size: int = None,
        system_info: str = None,
        tags: DescribeSourceServersResponseBodySourceServersSourceServerTags = None,
        workgroup_id: str = None,
    ):
        # The version number of the SMC client.
        self.agent_version = agent_version
        # The system architecture of the migration source.
        self.architecture = architecture
        # The time when the migration source was created.
        self.creation_time = creation_time
        # The data disks on the migration source.
        self.data_disks = data_disks
        # The description of the migration source.
        self.description = description
        # The information about the disk.
        self.disks = disks
        # The error code of the migration source.
        self.error_code = error_code
        # The interval at which heartbeats are sent from the SMC client. Unit: seconds.
        self.heartbeat_rate = heartbeat_rate
        # The ID of the last migration job.
        self.job_id = job_id
        # The kernel level of the migration source.
        self.kernel_level = kernel_level
        # The name of the migration source.
        self.name = name
        # The operating system of the migration source.
        self.platform = platform
        # The replication driver used for migration. Default value: SMT.
        self.replication_driver = replication_driver
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the migration source.
        self.source_id = source_id
        # The state of the migration source.
        self.state = state
        # The status information of the migration source. This parameter is returned if the migration source is in the Unavailable state. The value of this parameter consists of key-value pairs in the JSON format. Sample keys:
        # 
        #     error_code: The error code.
        #     error_msg: the error message.
        self.status_info = status_info
        # The information about the system disk partition.
        self.system_disk_parts = system_disk_parts
        # The system disk size of the migration source. Unit: GiB
        self.system_disk_size = system_disk_size
        # The system information of the migration source. The parameter must be specified as key-value pairs in the JSON format. The key-value pairs are extensible and have fixed keys. Maximum value: 1 KB. Example:
        # 
        #     agent_mode: the running mode.
        #     agent_type: the type of the run.
        #     client_type: the type of the client.
        #     hostname : the hostname.
        #     ipv4:IPv4 address
        #     ipv6: IPv6 address
        #     cores: the number of CPU cores.
        #     cpu_usage: the CPU utilization.
        #     memory: the memory size.
        #     memory_usage: the memory usage.
        self.system_info = system_info
        # The tag details.
        self.tags = tags
        # The workgroup ID.
        self.workgroup_id = workgroup_id

    def validate(self):
        if self.data_disks:
            self.data_disks.validate()
        if self.disks:
            self.disks.validate()
        if self.system_disk_parts:
            self.system_disk_parts.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_disks is not None:
            result['DataDisks'] = self.data_disks.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.disks is not None:
            result['Disks'] = self.disks.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.heartbeat_rate is not None:
            result['HeartbeatRate'] = self.heartbeat_rate
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.kernel_level is not None:
            result['KernelLevel'] = self.kernel_level
        if self.name is not None:
            result['Name'] = self.name
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.replication_driver is not None:
            result['ReplicationDriver'] = self.replication_driver
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.state is not None:
            result['State'] = self.state
        if self.status_info is not None:
            result['StatusInfo'] = self.status_info
        if self.system_disk_parts is not None:
            result['SystemDiskParts'] = self.system_disk_parts.to_map()
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_info is not None:
            result['SystemInfo'] = self.system_info
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.workgroup_id is not None:
            result['WorkgroupId'] = self.workgroup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataDisks') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDataDisks()
            self.data_disks = temp_model.from_map(m['DataDisks'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Disks') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerDisks()
            self.disks = temp_model.from_map(m['Disks'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HeartbeatRate') is not None:
            self.heartbeat_rate = m.get('HeartbeatRate')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('KernelLevel') is not None:
            self.kernel_level = m.get('KernelLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ReplicationDriver') is not None:
            self.replication_driver = m.get('ReplicationDriver')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StatusInfo') is not None:
            self.status_info = m.get('StatusInfo')
        if m.get('SystemDiskParts') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerSystemDiskParts()
            self.system_disk_parts = temp_model.from_map(m['SystemDiskParts'])
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemInfo') is not None:
            self.system_info = m.get('SystemInfo')
        if m.get('Tags') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServersSourceServerTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('WorkgroupId') is not None:
            self.workgroup_id = m.get('WorkgroupId')
        return self


class DescribeSourceServersResponseBodySourceServers(TeaModel):
    def __init__(
        self,
        source_server: List[DescribeSourceServersResponseBodySourceServersSourceServer] = None,
    ):
        self.source_server = source_server

    def validate(self):
        if self.source_server:
            for k in self.source_server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceServer'] = []
        if self.source_server is not None:
            for k in self.source_server:
                result['SourceServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_server = []
        if m.get('SourceServer') is not None:
            for k in m.get('SourceServer'):
                temp_model = DescribeSourceServersResponseBodySourceServersSourceServer()
                self.source_server.append(temp_model.from_map(k))
        return self


class DescribeSourceServersResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        source_servers: DescribeSourceServersResponseBodySourceServers = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The information about the migration source.
        self.source_servers = source_servers
        # The total number of migration sources returned.
        self.total_count = total_count

    def validate(self):
        if self.source_servers:
            self.source_servers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_servers is not None:
            result['SourceServers'] = self.source_servers.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceServers') is not None:
            temp_model = DescribeSourceServersResponseBodySourceServers()
            self.source_servers = temp_model.from_map(m['SourceServers'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSourceServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSourceServersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSourceServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWorkgroupsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the workgroup. Valid values of N: 1 to 20.
        # 
        # You cannot specify an empty string as a tag key. The tag key can be up to 64 characters in length and cannot contain http:// or https://. The tag key cannot start with acs: or aliyun.
        self.key = key
        # The tag value of the workgroup. Valid values of N: 1 to 20.
        # 
        # You can specify an empty string as a tag value. The tag value can be up to 64 characters in length and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeWorkgroupsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        status: str = None,
        tag: List[DescribeWorkgroupsRequestTag] = None,
        workgroup_id: List[str] = None,
    ):
        # The name of the workgroup.
        self.name = name
        self.owner_id = owner_id
        # The page number. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50. Default value: 10.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        # The state of the workgroup. Valid values:
        # 
        # *   NotStarted
        # *   InProgress
        # *   Cutover
        # *   Completed
        self.status = status
        # The list of tag information of workgroups.
        self.tag = tag
        # The workgroup IDs. You can specify up to 50 workgroup IDs.
        self.workgroup_id = workgroup_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.workgroup_id is not None:
            result['WorkgroupId'] = self.workgroup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeWorkgroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('WorkgroupId') is not None:
            self.workgroup_id = m.get('WorkgroupId')
        return self


class DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the workgroup.
        # 
        # You can specify an empty string as a tag key. The tag key can be up to 64 characters in length and cannot contain http:// or https://.
        self.key = key
        # The tag value of the workgroup. Valid values of N: 1 to 20.
        # 
        # You can specify an empty string as a tag value. The tag value can be up to 64 characters in length and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupWarningsWarningSourceIds(TeaModel):
    def __init__(
        self,
        source_id: List[str] = None,
    ):
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupWarningsWarning(TeaModel):
    def __init__(
        self,
        source_ids: DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupWarningsWarningSourceIds = None,
        warning_type: str = None,
    ):
        # The migration sources for which alerts are generated.
        self.source_ids = source_ids
        # The type of the alert. Valid values:
        # 
        # *   InError: A migration job failed.
        # *   UnRelated: No migration job is created for a migration source.
        # *   NotPassed: A migration job failed to pass the migration test.
        self.warning_type = warning_type

    def validate(self):
        if self.source_ids:
            self.source_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ids is not None:
            result['SourceIds'] = self.source_ids.to_map()
        if self.warning_type is not None:
            result['WarningType'] = self.warning_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIds') is not None:
            temp_model = DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupWarningsWarningSourceIds()
            self.source_ids = temp_model.from_map(m['SourceIds'])
        if m.get('WarningType') is not None:
            self.warning_type = m.get('WarningType')
        return self


class DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupWarnings(TeaModel):
    def __init__(
        self,
        warning: List[DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupWarningsWarning] = None,
    ):
        self.warning = warning

    def validate(self):
        if self.warning:
            for k in self.warning:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Warning'] = []
        if self.warning is not None:
            for k in self.warning:
                result['Warning'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.warning = []
        if m.get('Warning') is not None:
            for k in m.get('Warning'):
                temp_model = DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupWarningsWarning()
                self.warning.append(temp_model.from_map(k))
        return self


class DescribeWorkgroupsResponseBodyWorkgroupsWorkgroup(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        status: str = None,
        tags: DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupTags = None,
        warnings: DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupWarnings = None,
        workgroup_id: str = None,
    ):
        # The description of the workgroup.
        self.description = description
        # The name of the workgroup.
        self.name = name
        # The state of the workgroup. Valid values:
        # 
        # *   NotStarted
        # *   InProgress
        # *   Cutover
        # *   Completed
        self.status = status
        # The tag information of the workgroup.
        self.tags = tags
        # The alert information of the workgroup, which can contain multiple types of alerts.
        self.warnings = warnings
        # The workgroup ID.
        self.workgroup_id = workgroup_id

    def validate(self):
        if self.tags:
            self.tags.validate()
        if self.warnings:
            self.warnings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.warnings is not None:
            result['Warnings'] = self.warnings.to_map()
        if self.workgroup_id is not None:
            result['WorkgroupId'] = self.workgroup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Warnings') is not None:
            temp_model = DescribeWorkgroupsResponseBodyWorkgroupsWorkgroupWarnings()
            self.warnings = temp_model.from_map(m['Warnings'])
        if m.get('WorkgroupId') is not None:
            self.workgroup_id = m.get('WorkgroupId')
        return self


class DescribeWorkgroupsResponseBodyWorkgroups(TeaModel):
    def __init__(
        self,
        workgroup: List[DescribeWorkgroupsResponseBodyWorkgroupsWorkgroup] = None,
    ):
        self.workgroup = workgroup

    def validate(self):
        if self.workgroup:
            for k in self.workgroup:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Workgroup'] = []
        if self.workgroup is not None:
            for k in self.workgroup:
                result['Workgroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.workgroup = []
        if m.get('Workgroup') is not None:
            for k in m.get('Workgroup'):
                temp_model = DescribeWorkgroupsResponseBodyWorkgroupsWorkgroup()
                self.workgroup.append(temp_model.from_map(k))
        return self


class DescribeWorkgroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        workgroups: DescribeWorkgroupsResponseBodyWorkgroups = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of workgroups.
        self.total_count = total_count
        # The queried workgroups.
        self.workgroups = workgroups

    def validate(self):
        if self.workgroups:
            self.workgroups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.workgroups is not None:
            result['Workgroups'] = self.workgroups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Workgroups') is not None:
            temp_model = DescribeWorkgroupsResponseBodyWorkgroups()
            self.workgroups = temp_model.from_map(m['Workgroups'])
        return self


class DescribeWorkgroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWorkgroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWorkgroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAccessTokenRequest(TeaModel):
    def __init__(
        self,
        access_token_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        # The ID of the activation code.
        # 
        # This parameter is required.
        self.access_token_id = access_token_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_id is not None:
            result['AccessTokenId'] = self.access_token_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenId') is not None:
            self.access_token_id = m.get('AccessTokenId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DisableAccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAccessTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateSourceServersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        source_id: List[str] = None,
        workgroup_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # The IDs of migration sources that you want to disassociate from the workgroup. You can specify up to 50 migration sources.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The ID of the workgroup.
        # 
        # This parameter is required.
        self.workgroup_id = workgroup_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.workgroup_id is not None:
            result['WorkgroupId'] = self.workgroup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('WorkgroupId') is not None:
            self.workgroup_id = m.get('WorkgroupId')
        return self


class DisassociateSourceServersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociateSourceServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisassociateSourceServersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociateSourceServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessTokensRequest(TeaModel):
    def __init__(
        self,
        access_token_id: List[str] = None,
        name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        status: str = None,
    ):
        # The information about activation codes.
        self.access_token_id = access_token_id
        # The name of the activation code.
        self.name = name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # The status of the activation code. Valid values:
        # 
        # *   activated
        # *   unactivated
        # *   expired
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_id is not None:
            result['AccessTokenId'] = self.access_token_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenId') is not None:
            self.access_token_id = m.get('AccessTokenId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAccessTokensResponseBodyAccessTokensAccessToken(TeaModel):
    def __init__(
        self,
        access_token_id: str = None,
        count: str = None,
        creation_time: str = None,
        description: str = None,
        name: str = None,
        registered_count: str = None,
        status: str = None,
        time_to_live_in_days: str = None,
    ):
        # The ID of the activation code.
        self.access_token_id = access_token_id
        # The maximum number of times that the activation code can be used. Valid values: 1 to 1000.
        # 
        # Default value: 100.
        self.count = count
        # The time when the activation code was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the activation code.
        self.description = description
        # The name of the activation code.
        self.name = name
        # The number of migration sources whose information has been imported to Server Migration Center (SMC) by using the activation code.
        self.registered_count = registered_count
        # The status of the activation code. Valid values:
        # 
        # *   activated
        # *   unactivated
        # *   expired
        self.status = status
        # The validity period of the activation code. Unit: day. Valid values: 1 to 90. Default value: 30.
        self.time_to_live_in_days = time_to_live_in_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_id is not None:
            result['AccessTokenId'] = self.access_token_id
        if self.count is not None:
            result['Count'] = self.count
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.registered_count is not None:
            result['RegisteredCount'] = self.registered_count
        if self.status is not None:
            result['Status'] = self.status
        if self.time_to_live_in_days is not None:
            result['TimeToLiveInDays'] = self.time_to_live_in_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenId') is not None:
            self.access_token_id = m.get('AccessTokenId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegisteredCount') is not None:
            self.registered_count = m.get('RegisteredCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeToLiveInDays') is not None:
            self.time_to_live_in_days = m.get('TimeToLiveInDays')
        return self


class ListAccessTokensResponseBodyAccessTokens(TeaModel):
    def __init__(
        self,
        access_token: List[ListAccessTokensResponseBodyAccessTokensAccessToken] = None,
    ):
        self.access_token = access_token

    def validate(self):
        if self.access_token:
            for k in self.access_token:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessToken'] = []
        if self.access_token is not None:
            for k in self.access_token:
                result['AccessToken'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_token = []
        if m.get('AccessToken') is not None:
            for k in m.get('AccessToken'):
                temp_model = ListAccessTokensResponseBodyAccessTokensAccessToken()
                self.access_token.append(temp_model.from_map(k))
        return self


class ListAccessTokensResponseBody(TeaModel):
    def __init__(
        self,
        access_tokens: ListAccessTokensResponseBodyAccessTokens = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The activation codes returned.
        self.access_tokens = access_tokens
        # The number of entries per page. Valid values:
        # 
        # *   10
        # *   20
        # *   50
        # 
        # Default value: 20.
        self.page_number = page_number
        # The page number.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of migration sources returned.
        self.total_count = total_count

    def validate(self):
        if self.access_tokens:
            self.access_tokens.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_tokens is not None:
            result['AccessTokens'] = self.access_tokens.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokens') is not None:
            temp_model = ListAccessTokensResponseBodyAccessTokens()
            self.access_tokens = temp_model.from_map(m['AccessTokens'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccessTokensResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccessTokensResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccessTokensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. The tag key must be 1 to 64 characters in length. Valid values of N: 1 to 20.
        # 
        # Tag.N is used for exact match of SMC resources to which the tag is attached. Tag N consists of a key-value pair.
        # 
        # *   Tag keys and values are case-sensitive.
        # *   If you set only the Tag.N.Key parameter, all resources to which the specified tags are attached are returned.
        # *   If you set only the Tag.N.Value parameter, the error message InvalidParameter.TagValue is returned.
        # *   If you specify multiple tag key-value pairs at a time, only SMC resources that match all tag key-value pairs are returned.
        self.key = key
        # The value of tag N. The value must be 1 to 64 characters in length. Valid values of N: 1 to 20.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        owner_id: int = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        self.owner_id = owner_id
        # The IDs of SMC resources. SMC resources include migration sources and migration jobs. You can specify a maximum of 50 SMC resource IDs.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        # The type of the SMC resource. Valid values:
        # 
        # *   sourceserver: migration source.
        # *   replicationjob: migration job.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that are attached to SMC resources.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The resource ID.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type
        # The key of the tag that is attached to the resource.
        self.tag_key = tag_key
        # The value of the tag that is attached to the resource.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about SMC resources and tags, such as the IDs, types, and tag key-value pairs of the resources.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyReplicationJobAttributeRequestDataDiskPart(TeaModel):
    def __init__(
        self,
        block: bool = None,
        device: str = None,
        size_bytes: int = None,
    ):
        # Specifies whether to enable block replication for partition N in the destination data disk. Valid values:
        # 
        # *   true
        # *   false
        self.block = block
        # The ID of partition N in the destination data disk.
        # 
        # >  The partitions in the destination data disk are arranged in the same sequential order as those in the source data disk.
        self.device = device
        # The size of partition N in the destination data disk. Unit: bytes. The default value is equal to the corresponding size of the partition in the source data disk.
        # 
        # >  The total size of all partitions in the destination data disk cannot exceed the size of the destination data disk.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class ModifyReplicationJobAttributeRequestDataDisk(TeaModel):
    def __init__(
        self,
        index: int = None,
        part: List[ModifyReplicationJobAttributeRequestDataDiskPart] = None,
        size: int = None,
    ):
        # The index of data disk N on the destination ECS instance. Valid values of N: 1 to 16.
        # 
        # Data disks on a destination ECS instance are arranged in a sequential order that starts from 1.
        # 
        # >  You can create a destination data disk only for a source server that has data disks.
        self.index = index
        # The information about partitions.
        self.part = part
        # The size of the data disk on the destination ECS instance. Unit: GiB. Valid values: 20 to 32768.
        # 
        # >  The size of a destination data disk must be greater than the size of data in the source data disk. For example, if the source data disk has 500 GiB of storage space and 100 GiB of data, you must set this parameter to a value greater than 100.
        self.size = size

    def validate(self):
        if self.part:
            for k in self.part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        result['Part'] = []
        if self.part is not None:
            for k in self.part:
                result['Part'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        self.part = []
        if m.get('Part') is not None:
            for k in m.get('Part'):
                temp_model = ModifyReplicationJobAttributeRequestDataDiskPart()
                self.part.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ModifyReplicationJobAttributeRequestSystemDiskPart(TeaModel):
    def __init__(
        self,
        block: bool = None,
        device: str = None,
        size_bytes: int = None,
    ):
        # Specifies whether to enable block replication for partition N in the destination system disk. Valid values:
        # 
        # *   true
        # *   false
        self.block = block
        # The ID of partition N in the destination system disk.
        # 
        # >  The partitions in the destination system disk are arranged in the same sequential order as those in the source system disk.
        self.device = device
        # The size of partition N in the destination system disk. Unit: bytes. The default value is equal to the partition size of the source system disk.
        # 
        # >  The total size of all partitions in the destination system disk cannot exceed the size of the destination system disk.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.device is not None:
            result['Device'] = self.device
        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')
        return self


class ModifyReplicationJobAttributeRequest(TeaModel):
    def __init__(
        self,
        container_namespace: str = None,
        container_repository: str = None,
        container_tag: str = None,
        data_disk: List[ModifyReplicationJobAttributeRequestDataDisk] = None,
        description: str = None,
        frequency: int = None,
        image_name: str = None,
        instance_id: str = None,
        instance_ram_role: str = None,
        instance_type: str = None,
        job_id: str = None,
        launch_template_id: str = None,
        launch_template_version: str = None,
        max_number_of_image_to_keep: int = None,
        name: str = None,
        net_mode: int = None,
        owner_id: int = None,
        replication_parameters: str = None,
        resource_owner_account: str = None,
        scheduled_start_time: str = None,
        system_disk_part: List[ModifyReplicationJobAttributeRequestSystemDiskPart] = None,
        system_disk_size: int = None,
        target_type: str = None,
        v_switch_id: str = None,
        valid_time: str = None,
        vpc_id: str = None,
    ):
        # The namespace of the destination Docker container image. For more information about Docker container images, see [Terms](https://help.aliyun.com/document_detail/60744.html).
        self.container_namespace = container_namespace
        # The repository that stores the destination Docker container image. For more information about Docker container images, see [Terms](https://help.aliyun.com/document_detail/60744.html).
        self.container_repository = container_repository
        # The tag of the destination Docker container image. For more information about Docker container images, see [Terms](https://help.aliyun.com/document_detail/60744.html).
        self.container_tag = container_tag
        # The information about the data disk.
        self.data_disk = data_disk
        # The description of the migration job.
        # 
        # The description must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        self.description = description
        # The interval at which an incremental migration job runs. Unit: hour. Valid values: 1 to 168.
        # 
        # This parameter is required if you set the `RunOnce` parameter to false.
        self.frequency = frequency
        # The name of the destination image. The name must meet the following requirements:
        # 
        # *   The name must be unique within an Alibaba Cloud region.
        # *   The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        # 
        # >  If an image whose name is the same as that of the destination image already exists in the current region when the migration job is in progress, the system adds the migration job ID to the end of the image name by default. Example: ImageName-JobId.
        self.image_name = image_name
        # The destination instance ID.
        self.instance_id = instance_id
        # The name of the Resource Access Management (RAM) role that is attached to the intermediate instance.
        self.instance_ram_role = instance_ram_role
        # The type of the intermediate instance.
        # 
        # You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the ECS instance types.
        # 
        # *   If you specify this parameter, SMC creates an intermediate instance of the specified instance type. If the specified instance type is unavailable, you cannot create the migration job.
        # *   If you do not specify this parameter, SMC selects an available instance type in a specific order to create an intermediate instance. For more information,
        # 
        # see the "How does SMC create an intermediate instance?" section of the "FAQ" topic.
        self.instance_type = instance_type
        # The migration job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The launch template ID.
        self.launch_template_id = launch_template_id
        # The version number of the launch template.
        self.launch_template_version = launch_template_version
        # The maximum number of images that are retained for an incremental migration job. Valid values: 1 to 10.
        # 
        # This parameter is required if you set the `RunOnce` parameter to false.
        self.max_number_of_image_to_keep = max_number_of_image_to_keep
        # The name of the migration job. The name must meet the following requirements:
        # 
        # *   The name must be unique.
        # *   The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        self.name = name
        # The network mode for data transmission. Valid values:
        # 
        # *   0: Data is transmitted over the Internet. Make sure that the source server can access the Internet.
        # *   2: Data is transmitted over a virtual private cloud (VPC). If you set this parameter to 2, you must specify the VSwitchId parameter. You can leave the VpcId parameter empty, the VPC ID can be queried by calling an operation.
        self.net_mode = net_mode
        self.owner_id = owner_id
        # The parameters of the replication driver. The parameters are fixed key-value pairs of the JSON format. The value can be up to 2,048 characters in length.
        # 
        # A replication driver is a tool that is used to replicate the data of a source server to an intermediate instance. The parameters vary based on the replication driver type. If you use a Server Migration Tool (SMT) driver, you can set the following parameters:
        # 
        # *   bandwidth_limit: the maximum bandwidth for data transmission.
        # *   compress_level: the compression ratio of data to be transmitted.
        # *   checksum: specifies whether to enable checksum verification
        # 
        # For more information about the replication driver, see the response parameter `SourceServers.ReplicationDriver` of the [DescribeSourceServers](https://help.aliyun.com/document_detail/2402126.html) operation.
        self.replication_parameters = replication_parameters
        self.resource_owner_account = resource_owner_account
        # The time when the migration job is executed. SMC starts the migration job at the specified time.
        # 
        # Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2018-01-01T12:00:00Z indicates 20:00:00 on January 1, 2018 (UTC+8).
        # 
        # >  If ScheduledStartTime is left empty, SMC does not automatically start the migration job. In this case, you must call the [StartReplicationJob](https://help.aliyun.com/document_detail/121823.html) operation to start the migration job.
        self.scheduled_start_time = scheduled_start_time
        # The partition information of the system disk.
        self.system_disk_part = system_disk_part
        # The system disk size of the destination ECS instance. Unit: GiB. Valid values: 20 to 500.
        # 
        # >  The size of a destination data disk must be greater than the size of data in the source data disk. For example, if the source data disk has 500 GiB of storage space and 100 GiB of data, you must set this parameter to a value greater than 100.
        self.system_disk_size = system_disk_size
        # The type of destination to which the source server is migrated. You can modify the value only before the migration job starts. Valid values:
        # 
        # *   Image: After the migration job is complete, Server Migration Center (SMC) generates a destination Elastic Compute Service (ECS) image for the source server. You can use the image to create an ECS instance.
        # *   ContainerImage: After the migration job is complete, SMC generates a container image for the source server. You can use the container image in Container Registry.
        # *   TargetInstance: After the migration job is complete, SMC migrates the source server to the destination instance. If you set this parameter to TargetInstance, you must set the `InstanceId` parameter.
        # 
        # > 
        # 
        # *   The value of this parameter is not case-sensitive.
        # 
        # *   SMC does not allow you to migrate Windows servers or servers that run operating systems on the ARM architecture to Container Registry.
        self.target_type = target_type
        # The ID of the vSwitch in the VPC.
        self.v_switch_id = v_switch_id
        # The time when the migration job expires. You can schedule the migration job to expire 7 to 90 days after the job is created.
        # 
        # *   This parameter can be modified only if the migration job is in the Ready, Running, Stopped, InError, or Waiting state.
        # *   Specify the time in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC. For example, 2018-01-01T12:00:00Z indicates 20:00:00 on January 1, 2018 (UTC+8).
        # *   If you do not specify this parameter, the migration job does not expire.
        # *   After a migration job expires, the job state changes to Expired. SMC retains the migration job for seven days after the job expires. After the job is retained for seven days, SMC deletes the migration job.
        # 
        # By default, a migration job is valid for 30 days after it is created.
        self.valid_time = valid_time
        # The ID of the VPC for which an Express Connect circuit or VPN gateway is configured.
        self.vpc_id = vpc_id

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk_part:
            for k in self.system_disk_part:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_namespace is not None:
            result['ContainerNamespace'] = self.container_namespace
        if self.container_repository is not None:
            result['ContainerRepository'] = self.container_repository
        if self.container_tag is not None:
            result['ContainerTag'] = self.container_tag
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ram_role is not None:
            result['InstanceRamRole'] = self.instance_ram_role
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.max_number_of_image_to_keep is not None:
            result['MaxNumberOfImageToKeep'] = self.max_number_of_image_to_keep
        if self.name is not None:
            result['Name'] = self.name
        if self.net_mode is not None:
            result['NetMode'] = self.net_mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.replication_parameters is not None:
            result['ReplicationParameters'] = self.replication_parameters
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scheduled_start_time is not None:
            result['ScheduledStartTime'] = self.scheduled_start_time
        result['SystemDiskPart'] = []
        if self.system_disk_part is not None:
            for k in self.system_disk_part:
                result['SystemDiskPart'].append(k.to_map() if k else None)
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.valid_time is not None:
            result['ValidTime'] = self.valid_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerNamespace') is not None:
            self.container_namespace = m.get('ContainerNamespace')
        if m.get('ContainerRepository') is not None:
            self.container_repository = m.get('ContainerRepository')
        if m.get('ContainerTag') is not None:
            self.container_tag = m.get('ContainerTag')
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = ModifyReplicationJobAttributeRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRamRole') is not None:
            self.instance_ram_role = m.get('InstanceRamRole')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('MaxNumberOfImageToKeep') is not None:
            self.max_number_of_image_to_keep = m.get('MaxNumberOfImageToKeep')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetMode') is not None:
            self.net_mode = m.get('NetMode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReplicationParameters') is not None:
            self.replication_parameters = m.get('ReplicationParameters')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScheduledStartTime') is not None:
            self.scheduled_start_time = m.get('ScheduledStartTime')
        self.system_disk_part = []
        if m.get('SystemDiskPart') is not None:
            for k in m.get('SystemDiskPart'):
                temp_model = ModifyReplicationJobAttributeRequestSystemDiskPart()
                self.system_disk_part.append(temp_model.from_map(k))
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ValidTime') is not None:
            self.valid_time = m.get('ValidTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ModifyReplicationJobAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyReplicationJobAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyReplicationJobAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyReplicationJobAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySourceServerAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        source_id: str = None,
    ):
        # The description of the migration source. The description can be up to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the migration source. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.name = name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # The migration source ID.
        # 
        # This parameter is required.
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class ModifySourceServerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySourceServerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySourceServerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifySourceServerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWorkgroupAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        workgroup_id: str = None,
    ):
        # The new description of the workgroup.
        # 
        # The description must be 2 to 128 characters in length. It must start with a letter but cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The new name of the workgroup. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.name = name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # The workgroup ID.
        # 
        # This parameter is required.
        self.workgroup_id = workgroup_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.workgroup_id is not None:
            result['WorkgroupId'] = self.workgroup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('WorkgroupId') is not None:
            self.workgroup_id = m.get('WorkgroupId')
        return self


class ModifyWorkgroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWorkgroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyWorkgroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyWorkgroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartReplicationJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        # The migration job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class StartReplicationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartReplicationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartReplicationJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopReplicationJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        # The migration job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class StopReplicationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopReplicationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopReplicationJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopReplicationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to be added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag key cannot be an empty string. It can be up to 64 characters in length and cannot start with acs: or aliyun. It cannot contain http:// or https://.
        self.key = key
        # The value of tag N to be added to the SMC resource. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        # The IDs of N SMC resources. SMC resources include migration sources and jobs. Valid values of N: 1 to 50.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        # The type of the SMC resource. Valid values:
        # 
        # *   sourceserver: migration source.
        # *   replicationjob: migration job.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        owner_id: int = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags that are added to the specified SMC resource. This parameter is valid only if you do not set `TagKey.N`. Valid values:
        # 
        # *   true: removes all tags that are added to the specified SMC resource. If no tags are added to the specified SMC resource, no operation is performed.
        # *   false: does not remove tags that are added to the specified SMC resource.
        # 
        # Default value: false.
        self.all = all
        self.owner_id = owner_id
        # The IDs of N SMC resources. SMC resources include migration sources and jobs. Valid values of N: 1 to 50.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        # The type of the SMC resource. Valid values:
        # 
        # *   sourceserver: migration source.
        # *   replicationjob: migration job.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The key of tag N that is added to the SMC resource. Tag keys are case-sensitive. Valid values of N: 1 to 20.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


