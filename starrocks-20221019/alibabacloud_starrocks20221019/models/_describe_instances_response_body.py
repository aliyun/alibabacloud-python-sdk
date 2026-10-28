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
        # The query results.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of instances.
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
        ai_function_cluster_id: str = None,
        ai_function_endpoint: str = None,
        ai_function_instance_id: str = None,
        architecture: str = None,
        begin_time: int = None,
        compute_free: bool = None,
        enable_ai_function: bool = None,
        enable_auto_minor_version_upgrade: bool = None,
        enable_multi_az: bool = None,
        enable_ssl: bool = None,
        enabled_audit_loader: bool = None,
        encrypted: bool = None,
        eos_date: str = None,
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
        version_lifecycle_status: str = None,
        vpc_id: str = None,
    ):
        # The network access control list (ACL) ID.
        self.acl_id = acl_id
        # The AI dedicated cluster ID. The ID has an af- prefix. This parameter is returned if an unreleased dedicated cluster exists, including those being created. If no dedicated cluster is created, this parameter is empty.
        self.ai_function_cluster_id = ai_function_cluster_id
        # The internal network endpoint of the AI dedicated cluster. The format is fe-{AiFunctionClusterId}-internal.starrocks.aliyuncs.com. This parameter is returned only after the dedicated cluster is created. If no dedicated cluster is created, this parameter is empty.
        self.ai_function_endpoint = ai_function_endpoint
        # The AI function billing instance ID.
        self.ai_function_instance_id = ai_function_instance_id
        # The instance architecture. Valid values:
        # 
        # - onEci: Deployed based on Elastic Container Instance (ECI).
        # - onECS: Deployed based on Elastic Compute Service (ECS).
        # - onBareMetal: Deployed based on bare metal resource pools.
        self.architecture = architecture
        # The time when the cluster was created.
        self.begin_time = begin_time
        self.compute_free = compute_free
        # Indicates whether the AI center is enabled. Default value: false.
        self.enable_ai_function = enable_ai_function
        # Indicates whether automatic minor version upgrades are allowed.
        self.enable_auto_minor_version_upgrade = enable_auto_minor_version_upgrade
        # Indicates whether disaster recovery is enabled.
        self.enable_multi_az = enable_multi_az
        # Indicates whether SSL is enabled.
        self.enable_ssl = enable_ssl
        # Indicates whether the audit plug-in is enabled.
        self.enabled_audit_loader = enabled_audit_loader
        # Indicates whether encryption is enabled.
        self.encrypted = encrypted
        # The end-of-support date for the cluster version.
        self.eos_date = eos_date
        # The expiration time of the cluster.
        self.expire_time = expire_time
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The instance status. Valid values:
        # 
        # - not_init: Not initialized.
        # - unpaid: Unpaid.
        # - paid: Paid.
        # - creating: Creating.
        # - creating_failed: Creation failed.
        # - created: Created.
        # - running: Running.
        # - updating: Upgrading.
        # - agent_creating: Creating the agent.
        # - agent_scaling_up: Scaling up the agent.
        # - modifying_config: Updating configurations.
        # - scaling_out: Scaling out.
        # - restarting: Restarting.
        # - scaling_in: Scaling in.
        # - scaling_up: Scaling up.
        # - scaling_down: Scaling down.
        # - upgrading: Upgrading the version.
        # - enable_public_network: Enabling the public network.
        # - disable_public_network: Disabling the public network.
        # - convert_from_trial_to_official: Converting the edition.
        # - migration_cluster_to_serverless: Migrating the cluster.
        # - modifying_timezone: Modifying the time zone.
        # - switch_az: Switching the primary and secondary zones.
        # - enabling: Recovering.
        # - disable: Unavailable.
        # - actively_disabled: Unavailable.
        # - deleting: Deleting.
        # - deleting_failed: Deletion failed.
        # - deleted_with_error: Ended due to creation failure.
        # - deleted: Deleted.
        self.instance_status = instance_status
        # Indicates whether read/write splitting is enabled. If enabled, the leader FE node processes write requests and other nodes process read requests.
        self.isolate_leader = isolate_leader
        # The KMS key ID.
        self.kms_key_id = kms_key_id
        # The maintenance window of the instance. Valid values:
        # 
        # - 00:00-06:00
        # - 06:00-07:00
        # - 07:00-08:00
        # - 08:00-09:00
        # - 09:00-10:00
        # - 10:00-11:00
        # - 11:00-12:00
        # - 12:00-13:00
        # - 13:00-14:00
        # - 14:00-15:00
        # - 15:00-16:00
        # - 16:00-17:00
        # - 17:00-18:00
        # - 18:00-19:00
        # - 19:00-20:00
        # - 20:00-21:00
        # - 21:00-22:00
        # - 22:00-23:00
        # - 23:00-24:00
        self.maintainable_period = maintainable_period
        # The minor version number.
        self.minor_version = minor_version
        # The monitoring service type.
        self.monitor_type = monitor_type
        # The OSS address.
        self.oss_location = oss_location
        # The instance edition. Valid values:
        # - trial: Trial Edition.
        # - official: Standard Edition.
        self.package_type = package_type
        # The billing method. Valid values:
        # - prePaid: Subscription.
        # - postPaid: Pay-as-you-go.
        self.pay_type = pay_type
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The running mode of the cluster. Valid values:
        # - shared_nothing: Shared-nothing.
        # - shared_data: Shared-data.
        # - lakehouse: Lakehouse.
        self.run_mode = run_mode
        # The running time of the cluster. Unit: seconds.
        self.running_time = running_time
        # Indicates whether the managed security group is used.
        self.security_group_managed = security_group_managed
        # The security group ID.
        self.sg_id = sg_id
        # The tags bound to the instance.
        self.tags = tags
        # The vSwitches.
        self.v_switches = v_switches
        # The cluster version.
        self.version = version
        # The version lifecycle status.
        self.version_lifecycle_status = version_lifecycle_status
        # The VPC ID.
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

        if self.ai_function_cluster_id is not None:
            result['AiFunctionClusterId'] = self.ai_function_cluster_id

        if self.ai_function_endpoint is not None:
            result['AiFunctionEndpoint'] = self.ai_function_endpoint

        if self.ai_function_instance_id is not None:
            result['AiFunctionInstanceId'] = self.ai_function_instance_id

        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.compute_free is not None:
            result['ComputeFree'] = self.compute_free

        if self.enable_ai_function is not None:
            result['EnableAiFunction'] = self.enable_ai_function

        if self.enable_auto_minor_version_upgrade is not None:
            result['EnableAutoMinorVersionUpgrade'] = self.enable_auto_minor_version_upgrade

        if self.enable_multi_az is not None:
            result['EnableMultiAz'] = self.enable_multi_az

        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl

        if self.enabled_audit_loader is not None:
            result['EnabledAuditLoader'] = self.enabled_audit_loader

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.eos_date is not None:
            result['EosDate'] = self.eos_date

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

        if self.version_lifecycle_status is not None:
            result['VersionLifecycleStatus'] = self.version_lifecycle_status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AiFunctionClusterId') is not None:
            self.ai_function_cluster_id = m.get('AiFunctionClusterId')

        if m.get('AiFunctionEndpoint') is not None:
            self.ai_function_endpoint = m.get('AiFunctionEndpoint')

        if m.get('AiFunctionInstanceId') is not None:
            self.ai_function_instance_id = m.get('AiFunctionInstanceId')

        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('ComputeFree') is not None:
            self.compute_free = m.get('ComputeFree')

        if m.get('EnableAiFunction') is not None:
            self.enable_ai_function = m.get('EnableAiFunction')

        if m.get('EnableAutoMinorVersionUpgrade') is not None:
            self.enable_auto_minor_version_upgrade = m.get('EnableAutoMinorVersionUpgrade')

        if m.get('EnableMultiAz') is not None:
            self.enable_multi_az = m.get('EnableMultiAz')

        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')

        if m.get('EnabledAuditLoader') is not None:
            self.enabled_audit_loader = m.get('EnabledAuditLoader')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('EosDate') is not None:
            self.eos_date = m.get('EosDate')

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

        if m.get('VersionLifecycleStatus') is not None:
            self.version_lifecycle_status = m.get('VersionLifecycleStatus')

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
        # Indicates whether the vSwitch is the primary vSwitch.
        self.primary = primary
        # The vSwitch ID.
        self.vsw_id = vsw_id
        # The zone ID.
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
        # The tag key.
        self.key = key
        # The tag value.
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

