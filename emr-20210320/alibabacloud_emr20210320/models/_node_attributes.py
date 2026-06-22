# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NodeAttributes(DaraModel):
    def __init__(
        self,
        data_disk_encrypted: bool = None,
        data_disk_kmskey_id: str = None,
        key_pair_name: str = None,
        master_root_password: str = None,
        ram_role: str = None,
        security_group_id: str = None,
        system_disk_encrypted: bool = None,
        system_disk_kmskey_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable encryption for the data disk. For more information, see <props="china">[Encrypt a data disk](https://help.aliyun.com/zh/ecs/user-guide/encrypt-a-data-disk)<props="intl">[Encrypt a data disk](https://www.alibabacloud.com/help/en/ecs/user-guide/encryption-overview). Valid values:
        # 
        # - true: Enables encryption.
        # 
        # - false (default): Disables encryption.
        self.data_disk_encrypted = data_disk_encrypted
        # The ID of the KMS key for the data disk.
        self.data_disk_kmskey_id = data_disk_kmskey_id
        # The SSH key pair for logging on to the ECS instances.
        self.key_pair_name = key_pair_name
        # The password of the root user for the master node. This parameter is left empty in the response of an API call.
        self.master_root_password = master_root_password
        # The RAM role that is attached to the ECS instances to access other cloud resources.
        # Default value: AliyunECSInstanceForEMRRole.
        self.ram_role = ram_role
        # The ID of the security group. EMR supports only basic security groups and does not support enterprise security groups.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # Specifies whether to enable disk encryption for the system disk. Valid values:
        # 
        # - true: Enables encryption.
        # 
        # - false (default): Disables encryption.
        self.system_disk_encrypted = system_disk_encrypted
        # The ID of the KMS key.
        self.system_disk_kmskey_id = system_disk_kmskey_id
        # The ID of the VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the zone.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_encrypted is not None:
            result['DataDiskEncrypted'] = self.data_disk_encrypted

        if self.data_disk_kmskey_id is not None:
            result['DataDiskKMSKeyId'] = self.data_disk_kmskey_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.master_root_password is not None:
            result['MasterRootPassword'] = self.master_root_password

        if self.ram_role is not None:
            result['RamRole'] = self.ram_role

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.system_disk_encrypted is not None:
            result['SystemDiskEncrypted'] = self.system_disk_encrypted

        if self.system_disk_kmskey_id is not None:
            result['SystemDiskKMSKeyId'] = self.system_disk_kmskey_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskEncrypted') is not None:
            self.data_disk_encrypted = m.get('DataDiskEncrypted')

        if m.get('DataDiskKMSKeyId') is not None:
            self.data_disk_kmskey_id = m.get('DataDiskKMSKeyId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('MasterRootPassword') is not None:
            self.master_root_password = m.get('MasterRootPassword')

        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SystemDiskEncrypted') is not None:
            self.system_disk_encrypted = m.get('SystemDiskEncrypted')

        if m.get('SystemDiskKMSKeyId') is not None:
            self.system_disk_kmskey_id = m.get('SystemDiskKMSKeyId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

