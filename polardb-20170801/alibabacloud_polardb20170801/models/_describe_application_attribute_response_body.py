# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationAttributeResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        architecture: str = None,
        can_disable_snat: bool = None,
        components: List[main_models.DescribeApplicationAttributeResponseBodyComponents] = None,
        creation_time: str = None,
        dbcluster_id: str = None,
        description: str = None,
        dnat_mappings: List[main_models.DescribeApplicationAttributeResponseBodyDnatMappings] = None,
        endpoints: List[main_models.DescribeApplicationAttributeResponseBodyEndpoints] = None,
        expire_time: str = None,
        expired: bool = None,
        is_latest_version: bool = None,
        latest_version: str = None,
        lock_mode: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        mem_application_attribute: main_models.DescribeApplicationAttributeResponseBodyMemApplicationAttribute = None,
        minor_version: str = None,
        nat_gateway_id: str = None,
        nat_mapping_snat_ip_address: str = None,
        pay_type: str = None,
        polar_claw_application_attribute: main_models.DescribeApplicationAttributeResponseBodyPolarClawApplicationAttribute = None,
        polar_claw_saa_sapplication_attribute: main_models.DescribeApplicationAttributeResponseBodyPolarClawSaaSApplicationAttribute = None,
        polar_fsinstance_id: str = None,
        region_id: str = None,
        request_id: str = None,
        security_groups: List[main_models.DescribeApplicationAttributeResponseBodySecurityGroups] = None,
        security_iparrays: List[main_models.DescribeApplicationAttributeResponseBodySecurityIPArrays] = None,
        serverless_type: str = None,
        snat_status: str = None,
        status: str = None,
        storages: List[main_models.DescribeApplicationAttributeResponseBodyStorages] = None,
        upgrade_available: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        version: str = None,
        vpc_nat_gateway_id: str = None,
        zone_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The application type.
        self.application_type = application_type
        # The CPU architecture. Valid values:
        # - `x86`
        self.architecture = architecture
        # Indicates whether SNAT can be disabled.
        self.can_disable_snat = can_disable_snat
        # The list of subcomponents.
        self.components = components
        # The creation time.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The PolarDB instance ID on which the application depends.
        self.dbcluster_id = dbcluster_id
        # The description of the application.
        self.description = description
        # The NAT mapping: the list of DNAT mapping entries.
        self.dnat_mappings = dnat_mappings
        # The list of endpoints for the application.
        self.endpoints = endpoints
        # The expiration time.
        # 
        # This parameter is empty when the billing method is pay-as-you-go.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.expire_time = expire_time
        # Indicates whether the application has expired.
        self.expired = expired
        # Indicates whether the application is of the latest version.
        self.is_latest_version = is_latest_version
        # The latest version number.
        self.latest_version = latest_version
        # The lock mode. Valid values:
        # 
        # - Unlock: unlocked.
        # - Lock: locked.
        self.lock_mode = lock_mode
        # The end time of the maintenance window.
        # 
        # The time is displayed in UTC in the HH:mmZ format.
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window.
        # 
        # The time is displayed in UTC in the HH:mmZ format.
        self.maintain_start_time = maintain_start_time
        # The Mem0 application attributes.
        self.mem_application_attribute = mem_application_attribute
        # The minor version number.
        self.minor_version = minor_version
        # The NAT gateway ID.
        self.nat_gateway_id = nat_gateway_id
        # The NAT mapping: the SNAT IP address bound to the vSwitch where the application resides. This refers to a customer-managed SNAT entry that is discovered and returned in real time by the control plane, and is unrelated to the SNAT of the Internet NAT gateway.
        self.nat_mapping_snat_ip_address = nat_mapping_snat_ip_address
        # The billing method.
        self.pay_type = pay_type
        # The PolarClaw application attributes.
        self.polar_claw_application_attribute = polar_claw_application_attribute
        # The PolarClaw SaaS application attributes.
        self.polar_claw_saa_sapplication_attribute = polar_claw_saa_sapplication_attribute
        # The instance ID of the PolarFS Cold Storage Edition or High-performance Edition.
        self.polar_fsinstance_id = polar_fsinstance_id
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The list of application-level security groups.
        self.security_groups = security_groups
        # The list of application-level whitelists.
        self.security_iparrays = security_iparrays
        # The Serverless type. Valid values:
        # - 2: Agile.
        # - 3: Stable.
        self.serverless_type = serverless_type
        # The SNAT status. Valid values: on, off.
        self.snat_status = snat_status
        # The application status. Valid values:
        # - Creating: The application is being created.
        # - Activated: The application is running.
        # - Maintaining: The application is under maintenance.
        # - ClassChanging: The application configuration is being changed.
        # - Transing: The application is being migrated.
        # - MinorVersionUpgrading: The minor version of the application is being upgraded.
        # - NetCreating: The endpoint of the application is being created.
        # - NetDeleting: The endpoint of the application is being deleted.
        # - NetModifying: The endpoint of the application is being modified.
        # - Restarting: The application is being restarted.
        # - Locking: The application is being locked.
        # - Locked: The application is locked.
        # - Unlocking: The application is being unlocked.
        # - Deleting: The application is being deleted.
        self.status = status
        # The storage resource description.
        self.storages = storages
        # Indicates whether an upgrade is available.
        self.upgrade_available = upgrade_available
        # VPC ID
        self.vpcid = vpcid
        # VSwitch ID
        self.v_switch_id = v_switch_id
        # The application version.
        self.version = version
        # The NAT mapping: the customer-managed VPC NAT gateway ID.
        self.vpc_nat_gateway_id = vpc_nat_gateway_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()
        if self.dnat_mappings:
            for v1 in self.dnat_mappings:
                 if v1:
                    v1.validate()
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.mem_application_attribute:
            self.mem_application_attribute.validate()
        if self.polar_claw_application_attribute:
            self.polar_claw_application_attribute.validate()
        if self.polar_claw_saa_sapplication_attribute:
            self.polar_claw_saa_sapplication_attribute.validate()
        if self.security_groups:
            for v1 in self.security_groups:
                 if v1:
                    v1.validate()
        if self.security_iparrays:
            for v1 in self.security_iparrays:
                 if v1:
                    v1.validate()
        if self.storages:
            for v1 in self.storages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.can_disable_snat is not None:
            result['CanDisableSnat'] = self.can_disable_snat

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        result['DnatMappings'] = []
        if self.dnat_mappings is not None:
            for k1 in self.dnat_mappings:
                result['DnatMappings'].append(k1.to_map() if k1 else None)

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.mem_application_attribute is not None:
            result['MemApplicationAttribute'] = self.mem_application_attribute.to_map()

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_mapping_snat_ip_address is not None:
            result['NatMappingSnatIpAddress'] = self.nat_mapping_snat_ip_address

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.polar_claw_application_attribute is not None:
            result['PolarClawApplicationAttribute'] = self.polar_claw_application_attribute.to_map()

        if self.polar_claw_saa_sapplication_attribute is not None:
            result['PolarClawSaaSApplicationAttribute'] = self.polar_claw_saa_sapplication_attribute.to_map()

        if self.polar_fsinstance_id is not None:
            result['PolarFSInstanceId'] = self.polar_fsinstance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SecurityGroups'] = []
        if self.security_groups is not None:
            for k1 in self.security_groups:
                result['SecurityGroups'].append(k1.to_map() if k1 else None)

        result['SecurityIPArrays'] = []
        if self.security_iparrays is not None:
            for k1 in self.security_iparrays:
                result['SecurityIPArrays'].append(k1.to_map() if k1 else None)

        if self.serverless_type is not None:
            result['ServerlessType'] = self.serverless_type

        if self.snat_status is not None:
            result['SnatStatus'] = self.snat_status

        if self.status is not None:
            result['Status'] = self.status

        result['Storages'] = []
        if self.storages is not None:
            for k1 in self.storages:
                result['Storages'].append(k1.to_map() if k1 else None)

        if self.upgrade_available is not None:
            result['UpgradeAvailable'] = self.upgrade_available

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_nat_gateway_id is not None:
            result['VpcNatGatewayId'] = self.vpc_nat_gateway_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('CanDisableSnat') is not None:
            self.can_disable_snat = m.get('CanDisableSnat')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodyComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.dnat_mappings = []
        if m.get('DnatMappings') is not None:
            for k1 in m.get('DnatMappings'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodyDnatMappings()
                self.dnat_mappings.append(temp_model.from_map(k1))

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('MemApplicationAttribute') is not None:
            temp_model = main_models.DescribeApplicationAttributeResponseBodyMemApplicationAttribute()
            self.mem_application_attribute = temp_model.from_map(m.get('MemApplicationAttribute'))

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatMappingSnatIpAddress') is not None:
            self.nat_mapping_snat_ip_address = m.get('NatMappingSnatIpAddress')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PolarClawApplicationAttribute') is not None:
            temp_model = main_models.DescribeApplicationAttributeResponseBodyPolarClawApplicationAttribute()
            self.polar_claw_application_attribute = temp_model.from_map(m.get('PolarClawApplicationAttribute'))

        if m.get('PolarClawSaaSApplicationAttribute') is not None:
            temp_model = main_models.DescribeApplicationAttributeResponseBodyPolarClawSaaSApplicationAttribute()
            self.polar_claw_saa_sapplication_attribute = temp_model.from_map(m.get('PolarClawSaaSApplicationAttribute'))

        if m.get('PolarFSInstanceId') is not None:
            self.polar_fsinstance_id = m.get('PolarFSInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_groups = []
        if m.get('SecurityGroups') is not None:
            for k1 in m.get('SecurityGroups'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodySecurityGroups()
                self.security_groups.append(temp_model.from_map(k1))

        self.security_iparrays = []
        if m.get('SecurityIPArrays') is not None:
            for k1 in m.get('SecurityIPArrays'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodySecurityIPArrays()
                self.security_iparrays.append(temp_model.from_map(k1))

        if m.get('ServerlessType') is not None:
            self.serverless_type = m.get('ServerlessType')

        if m.get('SnatStatus') is not None:
            self.snat_status = m.get('SnatStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.storages = []
        if m.get('Storages') is not None:
            for k1 in m.get('Storages'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodyStorages()
                self.storages.append(temp_model.from_map(k1))

        if m.get('UpgradeAvailable') is not None:
            self.upgrade_available = m.get('UpgradeAvailable')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcNatGatewayId') is not None:
            self.vpc_nat_gateway_id = m.get('VpcNatGatewayId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeApplicationAttributeResponseBodyStorages(DaraModel):
    def __init__(
        self,
        storage_capacity: str = None,
        storage_instance_id: str = None,
        storage_performance_level: str = None,
        storage_type: str = None,
    ):
        # The storage capacity.
        self.storage_capacity = storage_capacity
        # The storage instance ID.
        self.storage_instance_id = storage_instance_id
        # The storage performance level (PL).
        self.storage_performance_level = storage_performance_level
        # The storage type.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.storage_capacity is not None:
            result['StorageCapacity'] = self.storage_capacity

        if self.storage_instance_id is not None:
            result['StorageInstanceId'] = self.storage_instance_id

        if self.storage_performance_level is not None:
            result['StoragePerformanceLevel'] = self.storage_performance_level

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageCapacity') is not None:
            self.storage_capacity = m.get('StorageCapacity')

        if m.get('StorageInstanceId') is not None:
            self.storage_instance_id = m.get('StorageInstanceId')

        if m.get('StoragePerformanceLevel') is not None:
            self.storage_performance_level = m.get('StoragePerformanceLevel')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class DescribeApplicationAttributeResponseBodySecurityIPArrays(DaraModel):
    def __init__(
        self,
        security_iparray_name: str = None,
        security_iparray_tag: str = None,
        security_iplist: str = None,
        security_ipnet_type: str = None,
        security_iptype: str = None,
    ):
        # The name of the IP address group. Default value: `default`.
        self.security_iparray_name = security_iparray_name
        # The tag of the IP address group.
        self.security_iparray_tag = security_iparray_tag
        # The whitelist IP addresses, separated by commas.
        self.security_iplist = security_iplist
        # The network type of the whitelist IP addresses. Default value: `mix`.
        self.security_ipnet_type = security_ipnet_type
        # The type of the IP address.
        self.security_iptype = security_iptype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_iparray_name is not None:
            result['SecurityIPArrayName'] = self.security_iparray_name

        if self.security_iparray_tag is not None:
            result['SecurityIPArrayTag'] = self.security_iparray_tag

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.security_ipnet_type is not None:
            result['SecurityIPNetType'] = self.security_ipnet_type

        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityIPArrayName') is not None:
            self.security_iparray_name = m.get('SecurityIPArrayName')

        if m.get('SecurityIPArrayTag') is not None:
            self.security_iparray_tag = m.get('SecurityIPArrayTag')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SecurityIPNetType') is not None:
            self.security_ipnet_type = m.get('SecurityIPNetType')

        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')

        return self

class DescribeApplicationAttributeResponseBodySecurityGroups(DaraModel):
    def __init__(
        self,
        net_type: str = None,
        region_id: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        # The network type. Valid values: 
        # 
        # - vpc
        self.net_type = net_type
        # The region ID.
        self.region_id = region_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The security group name.
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

class DescribeApplicationAttributeResponseBodyPolarClawSaaSApplicationAttribute(DaraModel):
    def __init__(
        self,
        auth_callback_url: str = None,
        auth_providers: List[str] = None,
        supabase_cluster_id: str = None,
    ):
        # The authentication callback URL.
        self.auth_callback_url = auth_callback_url
        # The list of authentication providers for the application.
        self.auth_providers = auth_providers
        # The Supabase cluster identifier.
        self.supabase_cluster_id = supabase_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_callback_url is not None:
            result['AuthCallbackURL'] = self.auth_callback_url

        if self.auth_providers is not None:
            result['AuthProviders'] = self.auth_providers

        if self.supabase_cluster_id is not None:
            result['SupabaseClusterId'] = self.supabase_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCallbackURL') is not None:
            self.auth_callback_url = m.get('AuthCallbackURL')

        if m.get('AuthProviders') is not None:
            self.auth_providers = m.get('AuthProviders')

        if m.get('SupabaseClusterId') is not None:
            self.supabase_cluster_id = m.get('SupabaseClusterId')

        return self

class DescribeApplicationAttributeResponseBodyPolarClawApplicationAttribute(DaraModel):
    def __init__(
        self,
        langfuse_binding: main_models.DescribeApplicationAttributeResponseBodyPolarClawApplicationAttributeLangfuseBinding = None,
    ):
        # The Langfuse binding information.
        self.langfuse_binding = langfuse_binding

    def validate(self):
        if self.langfuse_binding:
            self.langfuse_binding.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.langfuse_binding is not None:
            result['LangfuseBinding'] = self.langfuse_binding.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LangfuseBinding') is not None:
            temp_model = main_models.DescribeApplicationAttributeResponseBodyPolarClawApplicationAttributeLangfuseBinding()
            self.langfuse_binding = temp_model.from_map(m.get('LangfuseBinding'))

        return self

class DescribeApplicationAttributeResponseBodyPolarClawApplicationAttributeLangfuseBinding(DaraModel):
    def __init__(
        self,
        activated_at: int = None,
        api_key_id: str = None,
        binding_task_id: int = None,
        langfuse_application_id: str = None,
        phase: str = None,
        project_id: str = None,
    ):
        # The effective period of the attachment. The value is a UNIX timestamp.
        self.activated_at = activated_at
        # Langfuse API Key ID
        self.api_key_id = api_key_id
        # The ID of the binding task.
        self.binding_task_id = binding_task_id
        # The Langfuse application ID.
        self.langfuse_application_id = langfuse_application_id
        # The binding phase.
        self.phase = phase
        # The Langfuse project ID.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activated_at is not None:
            result['ActivatedAt'] = self.activated_at

        if self.api_key_id is not None:
            result['ApiKeyId'] = self.api_key_id

        if self.binding_task_id is not None:
            result['BindingTaskId'] = self.binding_task_id

        if self.langfuse_application_id is not None:
            result['LangfuseApplicationId'] = self.langfuse_application_id

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivatedAt') is not None:
            self.activated_at = m.get('ActivatedAt')

        if m.get('ApiKeyId') is not None:
            self.api_key_id = m.get('ApiKeyId')

        if m.get('BindingTaskId') is not None:
            self.binding_task_id = m.get('BindingTaskId')

        if m.get('LangfuseApplicationId') is not None:
            self.langfuse_application_id = m.get('LangfuseApplicationId')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class DescribeApplicationAttributeResponseBodyMemApplicationAttribute(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        embedder_model_name: str = None,
        graph_llm_model_name: str = None,
        llm_model_name: str = None,
        memory_type: str = None,
        multimodal_enabled: bool = None,
        project_name: str = None,
        reranker_model_name: str = None,
        session_store: main_models.DescribeApplicationAttributeResponseBodyMemApplicationAttributeSessionStore = None,
        user_name: str = None,
        visual_embedder_dimensions: int = None,
        visual_embedder_model_name: str = None,
        visual_llm_modalities: List[str] = None,
        visual_llm_model_name: str = None,
    ):
        # The database name.
        self.db_name = db_name
        # The embedder model name.
        self.embedder_model_name = embedder_model_name
        # The graph LLM model support.
        self.graph_llm_model_name = graph_llm_model_name
        # The LLM model name.
        self.llm_model_name = llm_model_name
        # The currently active memory type.
        self.memory_type = memory_type
        # Indicates whether multimodal capabilities are currently enabled.
        self.multimodal_enabled = multimodal_enabled
        # The project name, which corresponds to the schema where project data is stored in the database.
        self.project_name = project_name
        # The name of the Reranker model.
        self.reranker_model_name = reranker_model_name
        # The Mem0 full session information storage configuration.
        self.session_store = session_store
        # The username.
        self.user_name = user_name
        # The current VisualEmbedder dimensions.
        self.visual_embedder_dimensions = visual_embedder_dimensions
        # The current VisualEmbedder model.
        self.visual_embedder_model_name = visual_embedder_model_name
        # The currently enabled understanding modalities.
        self.visual_llm_modalities = visual_llm_modalities
        # The current VisualLLM model.
        self.visual_llm_model_name = visual_llm_model_name

    def validate(self):
        if self.session_store:
            self.session_store.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.embedder_model_name is not None:
            result['EmbedderModelName'] = self.embedder_model_name

        if self.graph_llm_model_name is not None:
            result['GraphLlmModelName'] = self.graph_llm_model_name

        if self.llm_model_name is not None:
            result['LlmModelName'] = self.llm_model_name

        if self.memory_type is not None:
            result['MemoryType'] = self.memory_type

        if self.multimodal_enabled is not None:
            result['MultimodalEnabled'] = self.multimodal_enabled

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.reranker_model_name is not None:
            result['RerankerModelName'] = self.reranker_model_name

        if self.session_store is not None:
            result['SessionStore'] = self.session_store.to_map()

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.visual_embedder_dimensions is not None:
            result['VisualEmbedderDimensions'] = self.visual_embedder_dimensions

        if self.visual_embedder_model_name is not None:
            result['VisualEmbedderModelName'] = self.visual_embedder_model_name

        if self.visual_llm_modalities is not None:
            result['VisualLlmModalities'] = self.visual_llm_modalities

        if self.visual_llm_model_name is not None:
            result['VisualLlmModelName'] = self.visual_llm_model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('EmbedderModelName') is not None:
            self.embedder_model_name = m.get('EmbedderModelName')

        if m.get('GraphLlmModelName') is not None:
            self.graph_llm_model_name = m.get('GraphLlmModelName')

        if m.get('LlmModelName') is not None:
            self.llm_model_name = m.get('LlmModelName')

        if m.get('MemoryType') is not None:
            self.memory_type = m.get('MemoryType')

        if m.get('MultimodalEnabled') is not None:
            self.multimodal_enabled = m.get('MultimodalEnabled')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RerankerModelName') is not None:
            self.reranker_model_name = m.get('RerankerModelName')

        if m.get('SessionStore') is not None:
            temp_model = main_models.DescribeApplicationAttributeResponseBodyMemApplicationAttributeSessionStore()
            self.session_store = temp_model.from_map(m.get('SessionStore'))

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VisualEmbedderDimensions') is not None:
            self.visual_embedder_dimensions = m.get('VisualEmbedderDimensions')

        if m.get('VisualEmbedderModelName') is not None:
            self.visual_embedder_model_name = m.get('VisualEmbedderModelName')

        if m.get('VisualLlmModalities') is not None:
            self.visual_llm_modalities = m.get('VisualLlmModalities')

        if m.get('VisualLlmModelName') is not None:
            self.visual_llm_model_name = m.get('VisualLlmModelName')

        return self

class DescribeApplicationAttributeResponseBodyMemApplicationAttributeSessionStore(DaraModel):
    def __init__(
        self,
        account_mode: str = None,
        dbcluster_id: str = None,
        dbname: str = None,
        status: str = None,
    ):
        # The account source. Valid values: reuse_vector, existing. This parameter is returned only when the status is ENABLED.
        self.account_mode = account_mode
        # The ID of the PolarDB cluster used for session storage. This parameter is returned only when the status is ENABLED.
        self.dbcluster_id = dbcluster_id
        # The name of the session database. This parameter is returned only when the status is ENABLED.
        self.dbname = dbname
        # The session storage status. Valid values: DISABLED, ENABLING, ENABLED, DISABLING.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_mode is not None:
            result['AccountMode'] = self.account_mode

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountMode') is not None:
            self.account_mode = m.get('AccountMode')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeApplicationAttributeResponseBodyEndpoints(DaraModel):
    def __init__(
        self,
        description: str = None,
        domain: str = None,
        endpoint_id: str = None,
        ip: str = None,
        net_type: str = None,
        port: str = None,
        port_description: str = None,
    ):
        # The description of the endpoint.
        self.description = description
        # The domain name of the application endpoint.
        self.domain = domain
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The IP address.
        self.ip = ip
        # The endpoint type. Valid values:
        # - Private: VPC address.
        # - Public: Internet address.
        self.net_type = net_type
        # The port.
        self.port = port
        # The port description.
        self.port_description = port_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.ip is not None:
            result['IP'] = self.ip

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        if self.port_description is not None:
            result['PortDescription'] = self.port_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PortDescription') is not None:
            self.port_description = m.get('PortDescription')

        return self

class DescribeApplicationAttributeResponseBodyDnatMappings(DaraModel):
    def __init__(
        self,
        access_address: str = None,
        backend_port: int = None,
        entry_id: str = None,
        front_port: int = None,
        port_name: str = None,
        status: str = None,
    ):
        # The access address in the NatIp:FrontPort format, which can be directly used on the office network.
        self.access_address = access_address
        # The backend service port.
        self.backend_port = backend_port
        # The DNAT entry ID.
        self.entry_id = entry_id
        # The frontend port.
        self.front_port = front_port
        # The port name. Valid values: webui, hermesagent, dashboard, and ssh.
        self.port_name = port_name
        # The entry status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_address is not None:
            result['AccessAddress'] = self.access_address

        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port

        if self.entry_id is not None:
            result['EntryId'] = self.entry_id

        if self.front_port is not None:
            result['FrontPort'] = self.front_port

        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessAddress') is not None:
            self.access_address = m.get('AccessAddress')

        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')

        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')

        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeApplicationAttributeResponseBodyComponents(DaraModel):
    def __init__(
        self,
        component_class: str = None,
        component_class_description: str = None,
        component_id: str = None,
        component_max_replica: int = None,
        component_replica: int = None,
        component_replica_group_name: str = None,
        component_type: str = None,
        security_groups: List[main_models.DescribeApplicationAttributeResponseBodyComponentsSecurityGroups] = None,
        security_iparrays: List[main_models.DescribeApplicationAttributeResponseBodyComponentsSecurityIPArrays] = None,
        status: str = None,
        topology: main_models.DescribeApplicationAttributeResponseBodyComponentsTopology = None,
    ):
        # The specifications of the application subcomponent.
        self.component_class = component_class
        # The description of the application subcomponent specifications.
        self.component_class_description = component_class_description
        # The subcomponent ID.
        self.component_id = component_id
        # The maximum number of replicas for the application subcomponent.
        self.component_max_replica = component_max_replica
        # The number of replicas for the application subcomponent.
        self.component_replica = component_replica
        # The replica group name of the application subcomponent.
        self.component_replica_group_name = component_replica_group_name
        # The type of the application subcomponent.
        self.component_type = component_type
        # The list of security groups at the subcomponent level.
        # 
        # If the security groups at the subcomponent level are the same as those at the application level, this return value is omitted.
        self.security_groups = security_groups
        # The list of whitelist IP addresses at the subcomponent level.
        # 
        # If the whitelist at the subcomponent level is the same as that at the application level, this return value is omitted.
        self.security_iparrays = security_iparrays
        # The component status. The valid values are the same as the application status.
        self.status = status
        # The topology information of the application subcomponent.
        self.topology = topology

    def validate(self):
        if self.security_groups:
            for v1 in self.security_groups:
                 if v1:
                    v1.validate()
        if self.security_iparrays:
            for v1 in self.security_iparrays:
                 if v1:
                    v1.validate()
        if self.topology:
            self.topology.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_class is not None:
            result['ComponentClass'] = self.component_class

        if self.component_class_description is not None:
            result['ComponentClassDescription'] = self.component_class_description

        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.component_max_replica is not None:
            result['ComponentMaxReplica'] = self.component_max_replica

        if self.component_replica is not None:
            result['ComponentReplica'] = self.component_replica

        if self.component_replica_group_name is not None:
            result['ComponentReplicaGroupName'] = self.component_replica_group_name

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        result['SecurityGroups'] = []
        if self.security_groups is not None:
            for k1 in self.security_groups:
                result['SecurityGroups'].append(k1.to_map() if k1 else None)

        result['SecurityIPArrays'] = []
        if self.security_iparrays is not None:
            for k1 in self.security_iparrays:
                result['SecurityIPArrays'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.topology is not None:
            result['Topology'] = self.topology.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentClass') is not None:
            self.component_class = m.get('ComponentClass')

        if m.get('ComponentClassDescription') is not None:
            self.component_class_description = m.get('ComponentClassDescription')

        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ComponentMaxReplica') is not None:
            self.component_max_replica = m.get('ComponentMaxReplica')

        if m.get('ComponentReplica') is not None:
            self.component_replica = m.get('ComponentReplica')

        if m.get('ComponentReplicaGroupName') is not None:
            self.component_replica_group_name = m.get('ComponentReplicaGroupName')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        self.security_groups = []
        if m.get('SecurityGroups') is not None:
            for k1 in m.get('SecurityGroups'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodyComponentsSecurityGroups()
                self.security_groups.append(temp_model.from_map(k1))

        self.security_iparrays = []
        if m.get('SecurityIPArrays') is not None:
            for k1 in m.get('SecurityIPArrays'):
                temp_model = main_models.DescribeApplicationAttributeResponseBodyComponentsSecurityIPArrays()
                self.security_iparrays.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Topology') is not None:
            temp_model = main_models.DescribeApplicationAttributeResponseBodyComponentsTopology()
            self.topology = temp_model.from_map(m.get('Topology'))

        return self

class DescribeApplicationAttributeResponseBodyComponentsTopology(DaraModel):
    def __init__(
        self,
        children: List[str] = None,
        layer: str = None,
        parents: List[str] = None,
    ):
        # The list of topology child node IDs for the current application subcomponent, or the list of subcomponent types of the child nodes.
        self.children = children
        # The topology layer of the topology information for the current application subcomponent.
        self.layer = layer
        # The list of topology parent node IDs for the current application subcomponent, or the list of subcomponent types of the parent nodes.
        self.parents = parents

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.children is not None:
            result['Children'] = self.children

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.parents is not None:
            result['Parents'] = self.parents

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Children') is not None:
            self.children = m.get('Children')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('Parents') is not None:
            self.parents = m.get('Parents')

        return self

class DescribeApplicationAttributeResponseBodyComponentsSecurityIPArrays(DaraModel):
    def __init__(
        self,
        security_iparray_name: str = None,
        security_iparray_tag: str = None,
        security_iplist: str = None,
        security_ipnet_type: str = None,
        security_iptype: str = None,
    ):
        # The name of the IP address group. Default value: `default`.
        self.security_iparray_name = security_iparray_name
        # The tag of the IP address group.
        self.security_iparray_tag = security_iparray_tag
        # The whitelist IP addresses, separated by commas.
        self.security_iplist = security_iplist
        # The network type of the whitelist IP addresses. Default value: `mix`.
        self.security_ipnet_type = security_ipnet_type
        # The type of the IP address.
        self.security_iptype = security_iptype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_iparray_name is not None:
            result['SecurityIPArrayName'] = self.security_iparray_name

        if self.security_iparray_tag is not None:
            result['SecurityIPArrayTag'] = self.security_iparray_tag

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.security_ipnet_type is not None:
            result['SecurityIPNetType'] = self.security_ipnet_type

        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityIPArrayName') is not None:
            self.security_iparray_name = m.get('SecurityIPArrayName')

        if m.get('SecurityIPArrayTag') is not None:
            self.security_iparray_tag = m.get('SecurityIPArrayTag')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SecurityIPNetType') is not None:
            self.security_ipnet_type = m.get('SecurityIPNetType')

        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')

        return self

class DescribeApplicationAttributeResponseBodyComponentsSecurityGroups(DaraModel):
    def __init__(
        self,
        net_type: str = None,
        region_id: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        # The network type. Valid values: 
        # 
        # - vpc
        self.net_type = net_type
        # The region ID.
        self.region_id = region_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The security group name.
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

