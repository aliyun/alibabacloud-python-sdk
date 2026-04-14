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
        tag: List[main_models.CreateApplicationRequestTag] = None,
        target_version: str = None,
        used_time: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.aidbcluster_id = aidbcluster_id
        # This parameter is required.
        self.application_type = application_type
        # This parameter is required.
        self.architecture = architecture
        self.auth_provider = auth_provider
        self.auth_provider_config = auth_provider_config
        self.auto_allocate_public_eip = auto_allocate_public_eip
        self.auto_create_polar_fs = auto_create_polar_fs
        self.auto_renew = auto_renew
        self.auto_use_coupon = auto_use_coupon
        self.components = components
        self.dbcluster_id = dbcluster_id
        self.description = description
        self.dry_run = dry_run
        self.endpoints = endpoints
        self.knowledge_application_spec = knowledge_application_spec
        self.mem_application_spec = mem_application_spec
        self.model_api = model_api
        self.model_api_key = model_api_key
        self.model_base_url = model_base_url
        self.model_from = model_from
        self.model_name = model_name
        self.parameters = parameters
        self.pay_type = pay_type
        self.period = period
        self.polar_fsinstance_id = polar_fsinstance_id
        self.promotion_code = promotion_code
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id
        self.security_iparray_name = security_iparray_name
        self.security_iplist = security_iplist
        self.security_iptype = security_iptype
        self.skill_template_id = skill_template_id
        self.tag = tag
        self.target_version = target_version
        self.used_time = used_time
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
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
        if self.knowledge_application_spec:
            self.knowledge_application_spec.validate()
        if self.mem_application_spec:
            self.mem_application_spec.validate()
        if self.parameters:
            for v1 in self.parameters:
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

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIDBClusterId') is not None:
            self.aidbcluster_id = m.get('AIDBClusterId')

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

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateApplicationRequestTag(DaraModel):
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

class CreateApplicationRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_name = parameter_name
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
        self.db_name = db_name
        self.db_password = db_password
        self.db_user = db_user
        self.embedder_model = embedder_model
        self.embedder_model_dimension = embedder_model_dimension
        self.graph_llm_model = graph_llm_model
        self.llm_model = llm_model
        self.project_name = project_name
        self.reranker_model = reranker_model
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
        self.dashboard_password = dashboard_password
        self.db_password = db_password
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
        self.description = description
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
        self.component_class = component_class
        self.component_max_replica = component_max_replica
        self.component_replica = component_replica
        self.component_type = component_type
        self.scale_max = scale_max
        self.scale_min = scale_min
        self.security_groups = security_groups
        self.security_iparray_name = security_iparray_name
        self.security_iplist = security_iplist
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

