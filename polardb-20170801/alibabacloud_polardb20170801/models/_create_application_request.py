# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationRequest(DaraModel):
    def __init__(
        self,
        aidbcluster_id: str = None,
        agentic_dbbranch_spec: main_models.CreateApplicationRequestAgenticDBBranchSpec = None,
        application_type: str = None,
        architecture: str = None,
        auth_provider: str = None,
        auth_provider_config: str = None,
        auto_allocate_public_eip: bool = None,
        auto_create_polar_fs: bool = None,
        auto_renew: bool = None,
        auto_use_coupon: bool = None,
        components: List[main_models.CreateApplicationRequestComponents] = None,
        dbcluster_id: str = None,
        description: str = None,
        dnat_entries: List[main_models.CreateApplicationRequestDnatEntries] = None,
        dnat_ip_address: str = None,
        dry_run: bool = None,
        endpoints: List[main_models.CreateApplicationRequestEndpoints] = None,
        knowledge_application_spec: main_models.CreateApplicationRequestKnowledgeApplicationSpec = None,
        mem_application_spec: main_models.CreateApplicationRequestMemApplicationSpec = None,
        model_api: str = None,
        model_api_key: str = None,
        model_base_url: str = None,
        model_from: str = None,
        model_name: str = None,
        parameters: List[main_models.CreateApplicationRequestParameters] = None,
        pay_type: str = None,
        period: str = None,
        polar_fsinstance_id: str = None,
        promotion_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        security_iparray_name: str = None,
        security_iplist: str = None,
        security_iptype: str = None,
        skill_template_id: str = None,
        storages: List[main_models.CreateApplicationRequestStorages] = None,
        tag: List[main_models.CreateApplicationRequestTag] = None,
        target_version: str = None,
        used_time: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_nat_gateway_id: str = None,
        zone_id: str = None,
    ):
        # The ID of an existing model operator instance to associate. This parameter takes effect only when ApplicationType is set to polarclaw.
        self.aidbcluster_id = aidbcluster_id
        # The AgenticDB branch specification.
        self.agentic_dbbranch_spec = agentic_dbbranch_spec
        # The application type. Valid values:
        # 
        # - supabase: Set this value to create a managed Supabase application.
        # - raycluster: Set this value to create a managed Ray Cluster application.
        # - polarclaw: Set this value to create a managed PolarClaw application.
        # 
        # This parameter is required.
        self.application_type = application_type
        # The CPU architecture. Valid values:
        # 
        # - x86
        # 
        # This parameter is required.
        self.architecture = architecture
        # The authentication service provider.
        self.auth_provider = auth_provider
        # The authentication provider configuration.
        self.auth_provider_config = auth_provider_config
        # Specifies whether to enable automatic creation of an elastic IP address (EIP) and attach it to the instance. This is equivalent to associate with an EIP.
        self.auto_allocate_public_eip = auto_allocate_public_eip
        # Specifies whether to enable automatic creation of a cold storage Polarlakebase instance. Valid values:
        # * false (default): Automatic creation is disabled.
        # * true: Automatic creation is enabled.
        self.auto_create_polar_fs = auto_create_polar_fs
        # Specifies whether to enable auto-renewal.
        self.auto_renew = auto_renew
        # Specifies whether to automatically use coupons. Valid values:
        # * true (default): Use coupons.
        # * false: Do not use coupons.
        self.auto_use_coupon = auto_use_coupon
        # The list of user-defined application subcomponents.
        self.components = components
        # The instance ID of the PolarDB instance on which the application depends.
        self.dbcluster_id = dbcluster_id
        # The description of the application.
        self.description = description
        # The list of expected DNAT entries for NAT mapping. Specify this parameter together with VpcNatGatewayId. This parameter can be left empty, which indicates that no DNAT entries are created.
        self.dnat_entries = dnat_entries
        # The DNAT-dedicated NAT IP address that has been allocated (separate from the SNAT IP address) for NAT mapping. The IP address must belong to the specified gateway and be in an available state. The vSwitch of the gateway must belong to a primary CIDR block that is reachable from the office network. Specify this parameter together with VpcNatGatewayId. Prerequisite: An SNAT entry has been bound to the vSwitch where the application resides.
        self.dnat_ip_address = dnat_ip_address
        # Default value: `false`. If you set this parameter to `true`, only parameter and resource validation is performed without actually creating the resource.
        self.dry_run = dry_run
        # The list of user-defined service endpoints. By default, a VPC endpoint is created.
        self.endpoints = endpoints
        # Required for knowledge applications.
        self.knowledge_application_spec = knowledge_application_spec
        # Required for mem0 applications.
        self.mem_application_spec = mem_application_spec
        # The model API. This parameter takes effect only when ApplicationType is set to polarclaw.
        self.model_api = model_api
        # The model API key. This parameter takes effect only when ApplicationType is set to polarclaw.
        self.model_api_key = model_api_key
        # The model base URL. This parameter takes effect only when ApplicationType is set to polarclaw.
        self.model_base_url = model_base_url
        # The model source. Valid values:
        # 
        # * bailian: Alibaba Cloud Model Studio model.
        # * custom: Custom model.
        # * maas: PolarDB model operator.
        self.model_from = model_from
        # The model name. This parameter takes effect only when ApplicationType is set to polarclaw.
        self.model_name = model_name
        # The list of parameters.
        self.parameters = parameters
        # The billing type.
        self.pay_type = pay_type
        # The subscription type (yearly or monthly).
        self.period = period
        # The instance ID of the Polarlakebase cold storage or high-performance edition. Default value: empty. If specified, the corresponding storage is mounted to the application.
        # 
        # Currently, only the following applications support this parameter:
        # - supabase
        # - raycluster
        self.polar_fsinstance_id = polar_fsinstance_id
        # The coupon code. If you do not specify this parameter, the default coupon is used.
        self.promotion_code = promotion_code
        # The region. Default value: the region of the instance.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The name of the IP whitelist group. Default value: `default`.
        self.security_iparray_name = security_iparray_name
        # The IP whitelist. If you do not specify this parameter, the default value is `127.0.0.1`.
        self.security_iplist = security_iplist
        # The type of the IP address.
        self.security_iptype = security_iptype
        # The skill template ID.
        self.skill_template_id = skill_template_id
        # The list of application storages.
        self.storages = storages
        # The tags.
        self.tag = tag
        # The target version.
        self.target_version = target_version
        # The subscription duration.
        self.used_time = used_time
        # The vSwitch. Default value: the vSwitch in the primary zone of the instance.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The VPC NAT gateway ID for NAT mapping. If specified, NAT mapping is enabled when the instance is created. The NAT gateway must be in the same VPC as the application, use the private network type (intranet), and be in an active state.
        self.vpc_nat_gateway_id = vpc_nat_gateway_id
        # The zone. Default value: the primary zone of the instance.
        self.zone_id = zone_id

    def validate(self):
        if self.agentic_dbbranch_spec:
            self.agentic_dbbranch_spec.validate()
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()
        if self.dnat_entries:
            for v1 in self.dnat_entries:
                 if v1:
                    v1.validate()
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.knowledge_application_spec:
            self.knowledge_application_spec.validate()
        if self.mem_application_spec:
            self.mem_application_spec.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.storages:
            for v1 in self.storages:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aidbcluster_id is not None:
            result['AIDBClusterId'] = self.aidbcluster_id

        if self.agentic_dbbranch_spec is not None:
            result['AgenticDBBranchSpec'] = self.agentic_dbbranch_spec.to_map()

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.auth_provider is not None:
            result['AuthProvider'] = self.auth_provider

        if self.auth_provider_config is not None:
            result['AuthProviderConfig'] = self.auth_provider_config

        if self.auto_allocate_public_eip is not None:
            result['AutoAllocatePublicEip'] = self.auto_allocate_public_eip

        if self.auto_create_polar_fs is not None:
            result['AutoCreatePolarFs'] = self.auto_create_polar_fs

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        result['DnatEntries'] = []
        if self.dnat_entries is not None:
            for k1 in self.dnat_entries:
                result['DnatEntries'].append(k1.to_map() if k1 else None)

        if self.dnat_ip_address is not None:
            result['DnatIpAddress'] = self.dnat_ip_address

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.knowledge_application_spec is not None:
            result['KnowledgeApplicationSpec'] = self.knowledge_application_spec.to_map()

        if self.mem_application_spec is not None:
            result['MemApplicationSpec'] = self.mem_application_spec.to_map()

        if self.model_api is not None:
            result['ModelApi'] = self.model_api

        if self.model_api_key is not None:
            result['ModelApiKey'] = self.model_api_key

        if self.model_base_url is not None:
            result['ModelBaseUrl'] = self.model_base_url

        if self.model_from is not None:
            result['ModelFrom'] = self.model_from

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.polar_fsinstance_id is not None:
            result['PolarFSInstanceId'] = self.polar_fsinstance_id

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_iparray_name is not None:
            result['SecurityIPArrayName'] = self.security_iparray_name

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype

        if self.skill_template_id is not None:
            result['SkillTemplateId'] = self.skill_template_id

        result['Storages'] = []
        if self.storages is not None:
            for k1 in self.storages:
                result['Storages'].append(k1.to_map() if k1 else None)

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.target_version is not None:
            result['TargetVersion'] = self.target_version

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_nat_gateway_id is not None:
            result['VpcNatGatewayId'] = self.vpc_nat_gateway_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIDBClusterId') is not None:
            self.aidbcluster_id = m.get('AIDBClusterId')

        if m.get('AgenticDBBranchSpec') is not None:
            temp_model = main_models.CreateApplicationRequestAgenticDBBranchSpec()
            self.agentic_dbbranch_spec = temp_model.from_map(m.get('AgenticDBBranchSpec'))

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('AuthProvider') is not None:
            self.auth_provider = m.get('AuthProvider')

        if m.get('AuthProviderConfig') is not None:
            self.auth_provider_config = m.get('AuthProviderConfig')

        if m.get('AutoAllocatePublicEip') is not None:
            self.auto_allocate_public_eip = m.get('AutoAllocatePublicEip')

        if m.get('AutoCreatePolarFs') is not None:
            self.auto_create_polar_fs = m.get('AutoCreatePolarFs')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.CreateApplicationRequestComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.dnat_entries = []
        if m.get('DnatEntries') is not None:
            for k1 in m.get('DnatEntries'):
                temp_model = main_models.CreateApplicationRequestDnatEntries()
                self.dnat_entries.append(temp_model.from_map(k1))

        if m.get('DnatIpAddress') is not None:
            self.dnat_ip_address = m.get('DnatIpAddress')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.CreateApplicationRequestEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('KnowledgeApplicationSpec') is not None:
            temp_model = main_models.CreateApplicationRequestKnowledgeApplicationSpec()
            self.knowledge_application_spec = temp_model.from_map(m.get('KnowledgeApplicationSpec'))

        if m.get('MemApplicationSpec') is not None:
            temp_model = main_models.CreateApplicationRequestMemApplicationSpec()
            self.mem_application_spec = temp_model.from_map(m.get('MemApplicationSpec'))

        if m.get('ModelApi') is not None:
            self.model_api = m.get('ModelApi')

        if m.get('ModelApiKey') is not None:
            self.model_api_key = m.get('ModelApiKey')

        if m.get('ModelBaseUrl') is not None:
            self.model_base_url = m.get('ModelBaseUrl')

        if m.get('ModelFrom') is not None:
            self.model_from = m.get('ModelFrom')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.CreateApplicationRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PolarFSInstanceId') is not None:
            self.polar_fsinstance_id = m.get('PolarFSInstanceId')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityIPArrayName') is not None:
            self.security_iparray_name = m.get('SecurityIPArrayName')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')

        if m.get('SkillTemplateId') is not None:
            self.skill_template_id = m.get('SkillTemplateId')

        self.storages = []
        if m.get('Storages') is not None:
            for k1 in m.get('Storages'):
                temp_model = main_models.CreateApplicationRequestStorages()
                self.storages.append(temp_model.from_map(k1))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateApplicationRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcNatGatewayId') is not None:
            self.vpc_nat_gateway_id = m.get('VpcNatGatewayId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateApplicationRequestTag(DaraModel):
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

class CreateApplicationRequestStorages(DaraModel):
    def __init__(
        self,
        container_mount_path: str = None,
        endpoint_id: str = None,
        mount_path: str = None,
        storage_capacity: str = None,
        storage_endpoint: str = None,
        storage_instance_id: str = None,
        storage_performance_level: str = None,
        storage_type: str = None,
    ):
        # The mount path inside the container.
        self.container_mount_path = container_mount_path
        # The storage endpoint ID.
        self.endpoint_id = endpoint_id
        # The storage mount path.
        self.mount_path = mount_path
        # The storage capacity.
        self.storage_capacity = storage_capacity
        # The storage access endpoint.
        self.storage_endpoint = storage_endpoint
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
        if self.container_mount_path is not None:
            result['ContainerMountPath'] = self.container_mount_path

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.storage_capacity is not None:
            result['StorageCapacity'] = self.storage_capacity

        if self.storage_endpoint is not None:
            result['StorageEndpoint'] = self.storage_endpoint

        if self.storage_instance_id is not None:
            result['StorageInstanceId'] = self.storage_instance_id

        if self.storage_performance_level is not None:
            result['StoragePerformanceLevel'] = self.storage_performance_level

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerMountPath') is not None:
            self.container_mount_path = m.get('ContainerMountPath')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('StorageCapacity') is not None:
            self.storage_capacity = m.get('StorageCapacity')

        if m.get('StorageEndpoint') is not None:
            self.storage_endpoint = m.get('StorageEndpoint')

        if m.get('StorageInstanceId') is not None:
            self.storage_instance_id = m.get('StorageInstanceId')

        if m.get('StoragePerformanceLevel') is not None:
            self.storage_performance_level = m.get('StoragePerformanceLevel')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class CreateApplicationRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        # The parameter name.
        self.parameter_name = parameter_name
        # The parameter value.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

class CreateApplicationRequestMemApplicationSpec(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        db_password: str = None,
        db_user: str = None,
        embedder_model: str = None,
        embedder_model_dimension: int = None,
        graph_llm_model: str = None,
        llm_model: str = None,
        project_name: str = None,
        reranker_model: str = None,
        shard: int = None,
    ):
        # The database name.
        self.db_name = db_name
        # The password.
        self.db_password = db_password
        # The username.
        self.db_user = db_user
        # Required for mem0 applications. The embedder model name, such as text-embedding-v4.
        self.embedder_model = embedder_model
        # The vector dimensions.
        self.embedder_model_dimension = embedder_model_dimension
        # The graph LLM model.
        self.graph_llm_model = graph_llm_model
        # Required for mem0 applications. The LLM model name, such as qwen3-max.
        self.llm_model = llm_model
        # The project name, which corresponds to the database schema that stores project data.
        self.project_name = project_name
        # Required for mem0 applications. The reranker model name, such as qwen3-rerank.
        self.reranker_model = reranker_model
        # The number of table shards.
        self.shard = shard

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.db_password is not None:
            result['DbPassword'] = self.db_password

        if self.db_user is not None:
            result['DbUser'] = self.db_user

        if self.embedder_model is not None:
            result['EmbedderModel'] = self.embedder_model

        if self.embedder_model_dimension is not None:
            result['EmbedderModelDimension'] = self.embedder_model_dimension

        if self.graph_llm_model is not None:
            result['GraphLlmModel'] = self.graph_llm_model

        if self.llm_model is not None:
            result['LlmModel'] = self.llm_model

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.reranker_model is not None:
            result['RerankerModel'] = self.reranker_model

        if self.shard is not None:
            result['Shard'] = self.shard

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')

        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')

        if m.get('EmbedderModel') is not None:
            self.embedder_model = m.get('EmbedderModel')

        if m.get('EmbedderModelDimension') is not None:
            self.embedder_model_dimension = m.get('EmbedderModelDimension')

        if m.get('GraphLlmModel') is not None:
            self.graph_llm_model = m.get('GraphLlmModel')

        if m.get('LlmModel') is not None:
            self.llm_model = m.get('LlmModel')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RerankerModel') is not None:
            self.reranker_model = m.get('RerankerModel')

        if m.get('Shard') is not None:
            self.shard = m.get('Shard')

        return self

class CreateApplicationRequestKnowledgeApplicationSpec(DaraModel):
    def __init__(
        self,
        dashboard_password: str = None,
        db_password: str = None,
        llm_model: str = None,
    ):
        # The dashboard password.
        self.dashboard_password = dashboard_password
        # The password.
        self.db_password = db_password
        # Required for knowledge applications. The LLM model name, such as qwen3-max.
        self.llm_model = llm_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password

        if self.db_password is not None:
            result['DbPassword'] = self.db_password

        if self.llm_model is not None:
            result['LlmModel'] = self.llm_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')

        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')

        if m.get('LlmModel') is not None:
            self.llm_model = m.get('LlmModel')

        return self

class CreateApplicationRequestEndpoints(DaraModel):
    def __init__(
        self,
        description: str = None,
        endpoint_type: str = None,
    ):
        # The description of the service endpoint.
        self.description = description
        # The type of the service endpoint. The value is fixed as Primary.
        self.endpoint_type = endpoint_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        return self

class CreateApplicationRequestDnatEntries(DaraModel):
    def __init__(
        self,
        front_port: int = None,
        port_name: str = None,
    ):
        # The frontend port. This parameter is optional. If not specified, the system automatically assigns a port that does not conflict with ports already in use on the gateway. You can query the assignment result by calling the DescribeApplicationAttribute operation.
        self.front_port = front_port
        # The port name. Valid values: webui, hermesagent, dashboard, and ssh.
        self.port_name = port_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.front_port is not None:
            result['FrontPort'] = self.front_port

        if self.port_name is not None:
            result['PortName'] = self.port_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        return self

class CreateApplicationRequestComponents(DaraModel):
    def __init__(
        self,
        component_class: str = None,
        component_max_replica: int = None,
        component_replica: int = None,
        component_type: str = None,
        scale_max: str = None,
        scale_min: str = None,
        security_groups: str = None,
        security_iparray_name: str = None,
        security_iplist: str = None,
        security_iptype: str = None,
    ):
        # The specification of the application subcomponent.
        self.component_class = component_class
        # The maximum number of replicas for the application subcomponent with the same specification. Default value: the value of ComponentReplica.
        # 
        # - Only raycluster supports this parameter.
        self.component_max_replica = component_max_replica
        # The number of replicas for the application subcomponent. Default value: 1.
        self.component_replica = component_replica
        # The type of the application subcomponent.
        # 
        # For supabase, valid values:
        # 
        # - gateway
        # - backend
        # 
        # For raycluster, valid values:
        # 
        # - head
        # - worker
        # - gpuworker
        self.component_type = component_type
        # The maximum number of replicas for component scaling.
        self.scale_max = scale_max
        # The minimum number of replicas for component scaling.
        self.scale_min = scale_min
        # The list of security groups for the application subcomponent, separated by commas (,).
        self.security_groups = security_groups
        # The name of the whitelist IP address group for the application subcomponent. Default value: default.
        self.security_iparray_name = security_iparray_name
        # The whitelist IP addresses of the application subcomponent, separated by commas (,).
        self.security_iplist = security_iplist
        # The type of the whitelist IP addresses for the application subcomponent. Default value: ipv4.
        self.security_iptype = security_iptype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_class is not None:
            result['ComponentClass'] = self.component_class

        if self.component_max_replica is not None:
            result['ComponentMaxReplica'] = self.component_max_replica

        if self.component_replica is not None:
            result['ComponentReplica'] = self.component_replica

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups

        if self.security_iparray_name is not None:
            result['SecurityIPArrayName'] = self.security_iparray_name

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentClass') is not None:
            self.component_class = m.get('ComponentClass')

        if m.get('ComponentMaxReplica') is not None:
            self.component_max_replica = m.get('ComponentMaxReplica')

        if m.get('ComponentReplica') is not None:
            self.component_replica = m.get('ComponentReplica')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('SecurityGroups') is not None:
            self.security_groups = m.get('SecurityGroups')

        if m.get('SecurityIPArrayName') is not None:
            self.security_iparray_name = m.get('SecurityIPArrayName')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')

        return self

class CreateApplicationRequestAgenticDBBranchSpec(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        dbcluster_id: str = None,
        fork_from_application_id: str = None,
        fork_from_branch: bool = None,
        project_id: str = None,
        tenant_id: str = None,
    ):
        # The AgenticDB branch ID.
        self.branch_id = branch_id
        # The AgenticDB cluster ID.
        self.dbcluster_id = dbcluster_id
        # The ID of the source application.
        self.fork_from_application_id = fork_from_application_id
        # Specifies whether to create the application based on a specified AgenticDB branch.
        self.fork_from_branch = fork_from_branch
        # The AgenticDB project ID.
        self.project_id = project_id
        # The AgenticDB tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.fork_from_application_id is not None:
            result['ForkFromApplicationId'] = self.fork_from_application_id

        if self.fork_from_branch is not None:
            result['ForkFromBranch'] = self.fork_from_branch

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ForkFromApplicationId') is not None:
            self.fork_from_application_id = m.get('ForkFromApplicationId')

        if m.get('ForkFromBranch') is not None:
            self.fork_from_branch = m.get('ForkFromBranch')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

