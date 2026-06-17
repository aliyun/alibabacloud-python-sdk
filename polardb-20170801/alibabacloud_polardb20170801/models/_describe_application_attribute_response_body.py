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
        pay_type: str = None,
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
        zone_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The application type.
        self.application_type = application_type
        # The CPU architecture. The value is:
        # 
        # - `x86`
        self.architecture = architecture
        # Indicates whether SNAT can be disabled.
        self.can_disable_snat = can_disable_snat
        # The child components.
        self.components = components
        # The creation time.
        self.creation_time = creation_time
        # The ID of the PolarDB instance that the application depends on.
        self.dbcluster_id = dbcluster_id
        # The application description.
        self.description = description
        # The application endpoints.
        self.endpoints = endpoints
        # The expiration time.
        # 
        # This parameter is not returned for Postpaid instances.
        self.expire_time = expire_time
        # Indicates whether the application has expired.
        self.expired = expired
        # Indicates whether the application is the latest version.
        self.is_latest_version = is_latest_version
        # The latest version number.
        self.latest_version = latest_version
        # The lock mode. Valid values:
        # 
        # - Unlock: The application is not locked.
        # 
        # - Lock: The application is locked.
        self.lock_mode = lock_mode
        # The maintenance end time.
        self.maintain_end_time = maintain_end_time
        # The maintenance start time.
        self.maintain_start_time = maintain_start_time
        # The attributes of the Mem0 application.
        self.mem_application_attribute = mem_application_attribute
        # The minor version number.
        self.minor_version = minor_version
        # The ID of the NAT Gateway.
        self.nat_gateway_id = nat_gateway_id
        # The billing method.
        self.pay_type = pay_type
        # The attributes of the PolarClaw SaaS application.
        self.polar_claw_saa_sapplication_attribute = polar_claw_saa_sapplication_attribute
        # The ID of the PolarFS Cold Storage or PolarFS High-performance instance.
        self.polar_fsinstance_id = polar_fsinstance_id
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The application-level security groups.
        self.security_groups = security_groups
        # The application-level whitelists.
        self.security_iparrays = security_iparrays
        # The Serverless type. Valid values:
        # 
        # - 2: Agile
        # 
        # - 3: Stable
        self.serverless_type = serverless_type
        # The SNAT status.
        self.snat_status = snat_status
        # The application status. Valid values:
        # 
        # - Creating: The application is being created.
        # 
        # - Activated: The application is running.
        # 
        # - Maintaining: The application is being maintained.
        # 
        # - ClassChanging: The application configuration is being changed.
        # 
        # - Transing: The application is being migrated.
        # 
        # - MinorVersionUpgrading: The minor version of the application is being upgraded.
        # 
        # - NetCreating: The endpoint is being created.
        # 
        # - NetDeleting: The endpoint is being deleted.
        # 
        # - NetModifying: The endpoint is being modified.
        # 
        # - Restarting: The application is restarting.
        # 
        # - Locking: The application is being locked.
        # 
        # - Locked: The application is locked.
        # 
        # - Unlocking: The application is being unlocked.
        # 
        # - Deleting: The application is being deleted.
        self.status = status
        # The details of the storage resources.
        self.storages = storages
        # Indicates whether an upgrade is available.
        self.upgrade_available = upgrade_available
        # The VPC ID.
        self.vpcid = vpcid
        # The VSwitch ID.
        self.v_switch_id = v_switch_id
        # The application version.
        self.version = version
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.mem_application_attribute:
            self.mem_application_attribute.validate()
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

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

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

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

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
        # The storage performance level.
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
        # The name of the IP address group. The default value is `default`.
        self.security_iparray_name = security_iparray_name
        # The tag of the IP address group.
        self.security_iparray_tag = security_iparray_tag
        # The whitelisted IP addresses, separated by commas.
        self.security_iplist = security_iplist
        # The network type of the whitelisted IP addresses. The default value is `mix`.
        self.security_ipnet_type = security_ipnet_type
        # The IP address type.
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
        # The network type. The value is:
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
        # The enabled authentication providers.
        self.auth_providers = auth_providers
        # The Supabase cluster ID.
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

class DescribeApplicationAttributeResponseBodyMemApplicationAttribute(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        embedder_model_name: str = None,
        graph_llm_model_name: str = None,
        llm_model_name: str = None,
        project_name: str = None,
        reranker_model_name: str = None,
        user_name: str = None,
    ):
        # The database name.
        self.db_name = db_name
        # The name of the embedder model.
        self.embedder_model_name = embedder_model_name
        # The name of the graph LLM model.
        self.graph_llm_model_name = graph_llm_model_name
        # The name of the LLM model.
        self.llm_model_name = llm_model_name
        # The project name. It corresponds to the database schema where project data is stored.
        self.project_name = project_name
        # The name of the reranker model.
        self.reranker_model_name = reranker_model_name
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

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

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.reranker_model_name is not None:
            result['RerankerModelName'] = self.reranker_model_name

        if self.user_name is not None:
            result['UserName'] = self.user_name

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

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RerankerModelName') is not None:
            self.reranker_model_name = m.get('RerankerModelName')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeApplicationAttributeResponseBodyEndpoints(DaraModel):
    def __init__(
        self,
        description: str = None,
        endpoint_id: str = None,
        ip: str = None,
        net_type: str = None,
        port: str = None,
        port_description: str = None,
    ):
        # The endpoint description.
        self.description = description
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The IP address.
        self.ip = ip
        # The endpoint type. Valid values:
        # 
        # - Private: a VPC endpoint
        # 
        # - Public: a public endpoint
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
        # The class of the child component.
        self.component_class = component_class
        # The description of the child component\\"s class.
        self.component_class_description = component_class_description
        # The child component ID.
        self.component_id = component_id
        # The maximum number of replicas for the child component.
        self.component_max_replica = component_max_replica
        # The number of replicas of the child component.
        self.component_replica = component_replica
        # The group name of the child component replicas.
        self.component_replica_group_name = component_replica_group_name
        # The type of the child component.
        self.component_type = component_type
        # The component-level security groups.
        # 
        # This parameter is not returned if the component-level security groups are the same as the application-level security groups.
        self.security_groups = security_groups
        # The component-level whitelists.
        # 
        # This parameter is not returned if the component-level whitelists are the same as the application-level whitelists.
        self.security_iparrays = security_iparrays
        # The component status. The valid values are the same as those for the application status.
        self.status = status
        # The topology of the child component.
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
        # The IDs or component types of the child nodes for this child component.
        self.children = children
        # The topology layer of the child component.
        self.layer = layer
        # The IDs or component types of the parent nodes for this child component.
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
        # The name of the IP address group. The default value is `default`.
        self.security_iparray_name = security_iparray_name
        # The tag of the IP address group.
        self.security_iparray_tag = security_iparray_tag
        # The whitelisted IP addresses, separated by commas.
        self.security_iplist = security_iplist
        # The network type of the whitelisted IP addresses. The default value is `mix`.
        self.security_ipnet_type = security_ipnet_type
        # The IP address type.
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
        # The network type. The value is:
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

