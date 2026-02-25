# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeInstancesResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        architecture: str = None,
        begin_time: int = None,
        enable_auto_minor_version_upgrade: bool = None,
        enable_ssl: bool = None,
        enabled_audit_loader: bool = None,
        encrypted: bool = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        isolate_leader: bool = None,
        kms_key_id: str = None,
        maintainable_period: str = None,
        minor_version: str = None,
        monitor_type: str = None,
        oss_location: str = None,
        package_type: str = None,
        pay_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        run_mode: str = None,
        running_time: int = None,
        security_group_managed: bool = None,
        sg_id: str = None,
        tags: List[main_models.DescribeInstancesResponseBodyDataTags] = None,
        v_switches: List[main_models.DescribeInstancesResponseBodyDataVSwitches] = None,
        version: str = None,
        vpc_id: str = None,
    ):
        self.acl_id = acl_id
        self.architecture = architecture
        self.begin_time = begin_time
        self.enable_auto_minor_version_upgrade = enable_auto_minor_version_upgrade
        self.enable_ssl = enable_ssl
        self.enabled_audit_loader = enabled_audit_loader
        self.encrypted = encrypted
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.isolate_leader = isolate_leader
        self.kms_key_id = kms_key_id
        self.maintainable_period = maintainable_period
        self.minor_version = minor_version
        self.monitor_type = monitor_type
        self.oss_location = oss_location
        self.package_type = package_type
        self.pay_type = pay_type
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.run_mode = run_mode
        self.running_time = running_time
        self.security_group_managed = security_group_managed
        self.sg_id = sg_id
        self.tags = tags
        self.v_switches = v_switches
        self.version = version
        # VPC ID。
        self.vpc_id = vpc_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.v_switches:
            for v1 in self.v_switches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.enable_auto_minor_version_upgrade is not None:
            result['EnableAutoMinorVersionUpgrade'] = self.enable_auto_minor_version_upgrade

        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl

        if self.enabled_audit_loader is not None:
            result['EnabledAuditLoader'] = self.enabled_audit_loader

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.isolate_leader is not None:
            result['IsolateLeader'] = self.isolate_leader

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.maintainable_period is not None:
            result['MaintainablePeriod'] = self.maintainable_period

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type

        if self.oss_location is not None:
            result['OssLocation'] = self.oss_location

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.running_time is not None:
            result['RunningTime'] = self.running_time

        if self.security_group_managed is not None:
            result['SecurityGroupManaged'] = self.security_group_managed

        if self.sg_id is not None:
            result['SgId'] = self.sg_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        result['VSwitches'] = []
        if self.v_switches is not None:
            for k1 in self.v_switches:
                result['VSwitches'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EnableAutoMinorVersionUpgrade') is not None:
            self.enable_auto_minor_version_upgrade = m.get('EnableAutoMinorVersionUpgrade')

        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')

        if m.get('EnabledAuditLoader') is not None:
            self.enabled_audit_loader = m.get('EnabledAuditLoader')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('IsolateLeader') is not None:
            self.isolate_leader = m.get('IsolateLeader')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('MaintainablePeriod') is not None:
            self.maintainable_period = m.get('MaintainablePeriod')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')

        if m.get('OssLocation') is not None:
            self.oss_location = m.get('OssLocation')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')

        if m.get('SecurityGroupManaged') is not None:
            self.security_group_managed = m.get('SecurityGroupManaged')

        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeInstancesResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k1 in m.get('VSwitches'):
                temp_model = main_models.DescribeInstancesResponseBodyDataVSwitches()
                self.v_switches.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeInstancesResponseBodyDataVSwitches(DaraModel):
    def __init__(
        self,
        primary: bool = None,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        self.primary = primary
        self.vsw_id = vsw_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.primary is not None:
            result['Primary'] = self.primary

        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeInstancesResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

