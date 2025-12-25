# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceDetailsResponseBody(DaraModel):
    def __init__(
        self,
        backup_data_size: int = None,
        backup_log_size: int = None,
        backup_size: int = None,
        db_instance_storage: int = None,
        db_proxy_instance_name: str = None,
        disk_used: int = None,
        instance_storage_type: str = None,
        rds_ecs_security_group_rel: List[main_models.DescribeResourceDetailsResponseBodyRdsEcsSecurityGroupRel] = None,
        region: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        security_iplist: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The storage that is occupied by data backup files, excluding archived backup files, on the instance. Unit: bytes.
        self.backup_data_size = backup_data_size
        # The size of the backup log. Unit: bytes.
        self.backup_log_size = backup_log_size
        # The size of the backup data. Unit: MB.
        self.backup_size = backup_size
        # The disk capacity of the instance.
        self.db_instance_storage = db_instance_storage
        # The name of the proxy instance.
        self.db_proxy_instance_name = db_proxy_instance_name
        # The total storage used. The value is the sum of the DataSize and LogSize values. Unit: bytes. The value -1 indicates that no data files or log files are stored.
        self.disk_used = disk_used
        # The storage type of the instance.
        self.instance_storage_type = instance_storage_type
        # The rule for the IP address whitelist of the instance.
        self.rds_ecs_security_group_rel = rds_ecs_security_group_rel
        # The region ID.
        self.region = region
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The IP address whitelist of the instance. For more information, see [Configure IP address whitelists](https://help.aliyun.com/document_detail/43185.html). If the returned IP address whitelist contains more than one entry, these entries are separated with commas (,). Each entry is unique and up to 1,000 entries are returned. The entries in the IP address whitelist must be in one of the following formats:
        # 
        # *   IP addresses, such as 10.10.XX.XX.
        # *   CIDR blocks, such as 10.10.XX.XX/24. In this example, 24 indicates that the prefix of each IP address in the IP address whitelist is 24 bits in length. You can replace 24 with a value within the range of 1 to 32.
        # 
        # If this parameter is not specified, the default IP address whitelist is used.
        self.security_iplist = security_iplist
        # The vSwitch ID.
        # 
        # >  The vSwitch must belong to the same zone as the instance.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        if self.rds_ecs_security_group_rel:
            for v1 in self.rds_ecs_security_group_rel:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_data_size is not None:
            result['BackupDataSize'] = self.backup_data_size

        if self.backup_log_size is not None:
            result['BackupLogSize'] = self.backup_log_size

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.db_instance_storage is not None:
            result['DbInstanceStorage'] = self.db_instance_storage

        if self.db_proxy_instance_name is not None:
            result['DbProxyInstanceName'] = self.db_proxy_instance_name

        if self.disk_used is not None:
            result['DiskUsed'] = self.disk_used

        if self.instance_storage_type is not None:
            result['InstanceStorageType'] = self.instance_storage_type

        result['RdsEcsSecurityGroupRel'] = []
        if self.rds_ecs_security_group_rel is not None:
            for k1 in self.rds_ecs_security_group_rel:
                result['RdsEcsSecurityGroupRel'].append(k1.to_map() if k1 else None)

        if self.region is not None:
            result['Region'] = self.region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupDataSize') is not None:
            self.backup_data_size = m.get('BackupDataSize')

        if m.get('BackupLogSize') is not None:
            self.backup_log_size = m.get('BackupLogSize')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('DbInstanceStorage') is not None:
            self.db_instance_storage = m.get('DbInstanceStorage')

        if m.get('DbProxyInstanceName') is not None:
            self.db_proxy_instance_name = m.get('DbProxyInstanceName')

        if m.get('DiskUsed') is not None:
            self.disk_used = m.get('DiskUsed')

        if m.get('InstanceStorageType') is not None:
            self.instance_storage_type = m.get('InstanceStorageType')

        self.rds_ecs_security_group_rel = []
        if m.get('RdsEcsSecurityGroupRel') is not None:
            for k1 in m.get('RdsEcsSecurityGroupRel'):
                temp_model = main_models.DescribeResourceDetailsResponseBodyRdsEcsSecurityGroupRel()
                self.rds_ecs_security_group_rel.append(temp_model.from_map(k1))

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeResourceDetailsResponseBodyRdsEcsSecurityGroupRel(DaraModel):
    def __init__(
        self,
        security_group_name: str = None,
    ):
        # The name of the security group.
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

