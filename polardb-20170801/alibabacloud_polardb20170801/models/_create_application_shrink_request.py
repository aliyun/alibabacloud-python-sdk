# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationShrinkRequest(DaraModel):
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
        components_shrink: str = None,
        dbcluster_id: str = None,
        description: str = None,
        dry_run: bool = None,
        endpoints_shrink: str = None,
        knowledge_application_spec_shrink: str = None,
        mem_application_spec_shrink: str = None,
        model_api: str = None,
        model_api_key: str = None,
        model_base_url: str = None,
        model_from: str = None,
        model_name: str = None,
        parameters_shrink: str = None,
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
        tag: List[main_models.CreateApplicationShrinkRequestTag] = None,
        target_version: str = None,
        used_time: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The ID of an existing model operator instance to associate. This parameter is effective only when ApplicationType is set to polarclaw.
        self.aidbcluster_id = aidbcluster_id
        # The type of the application. Valid values:
        # 
        # - supabase: Creates a managed Supabase application.
        # 
        # - raycluster: Creates a managed Ray Cluster application.
        # 
        # - polarclaw: Creates a managed PolarClaw application.
        # 
        # This parameter is required.
        self.application_type = application_type
        # The CPU architecture. Valid value:
        # 
        # - x86
        # 
        # This parameter is required.
        self.architecture = architecture
        # The authentication service provider.
        self.auth_provider = auth_provider
        # The configuration of the authentication provider.
        self.auth_provider_config = auth_provider_config
        # Specifies whether to automatically create and bind an Elastic IP Address (EIP).
        self.auto_allocate_public_eip = auto_allocate_public_eip
        # Specifies whether to automatically create a PolarFS cold storage instance. Valid values:
        # 
        # - false (default): Does not automatically create the instance.
        # 
        # - true: Automatically creates the instance.
        self.auto_create_polar_fs = auto_create_polar_fs
        # Specifies whether to enable auto-renewal.
        self.auto_renew = auto_renew
        # Specifies whether to automatically use a coupon. Valid values:
        # 
        # - true (default): Uses a coupon.
        # 
        # - false: Does not use a coupon.
        self.auto_use_coupon = auto_use_coupon
        # A list of custom child components for the application.
        self.components_shrink = components_shrink
        # The ID of the PolarDB instance that the application depends on.
        self.dbcluster_id = dbcluster_id
        # The description of the application.
        self.description = description
        # The default value is `false`. If you set this parameter to `true`, the system only checks the parameters and resources without creating the actual resources.
        self.dry_run = dry_run
        # A list of custom server-side endpoints. By default, a VPC Endpoint is created.
        self.endpoints_shrink = endpoints_shrink
        # This parameter is required for knowledge applications.
        self.knowledge_application_spec_shrink = knowledge_application_spec_shrink
        # This parameter is required for mem0 applications.
        self.mem_application_spec_shrink = mem_application_spec_shrink
        # The model API. This parameter is effective only when ApplicationType is set to polarclaw.
        self.model_api = model_api
        # The API key for the model. This parameter is effective only when ApplicationType is set to polarclaw.
        self.model_api_key = model_api_key
        # The URL of the model. This parameter is effective only when ApplicationType is set to polarclaw.
        self.model_base_url = model_base_url
        # The source of the model. Valid values:
        # 
        # - bailian: Alibaba Cloud Model Studio model.
        # 
        # - custom: A custom model.
        # 
        # - maas: PolarDB model operator.
        self.model_from = model_from
        # The name of the model. This parameter is effective only when ApplicationType is set to polarclaw.
        self.model_name = model_name
        # A list of parameters.
        self.parameters_shrink = parameters_shrink
        # The billing method.
        self.pay_type = pay_type
        # The subscription period type.
        self.period = period
        # The ID of the PolarFileSystem (PolarFS) cold storage or high-performance instance. This parameter is empty by default. If you specify this parameter, the corresponding storage is mounted to the application.
        # 
        # This feature is currently supported only by the following applications:
        # 
        # - supabase
        # 
        # - raycluster
        self.polar_fsinstance_id = polar_fsinstance_id
        # The coupon code. If you do not specify this parameter, the default coupon is used.
        self.promotion_code = promotion_code
        # The region. The default value is the region of the instance.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The name of the IP address whitelist group. The default value is `default`.
        self.security_iparray_name = security_iparray_name
        # The IP address whitelist. If you do not specify this parameter, the default value `127.0.0.1` is used.
        self.security_iplist = security_iplist
        # The type of the IP address.
        self.security_iptype = security_iptype
        # The ID of the skill template.
        self.skill_template_id = skill_template_id
        # The tag.
        self.tag = tag
        # The target version.
        self.target_version = target_version
        # The subscription duration.
        self.used_time = used_time
        # The vSwitch. The default value is the current vSwitch in the primary zone of the instance.
        self.v_switch_id = v_switch_id
        # The ID of the Virtual Private Cloud (VPC).
        self.vpc_id = vpc_id
        # The zone. The default value is the primary zone of the instance.
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

        if self.components_shrink is not None:
            result['Components'] = self.components_shrink

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.endpoints_shrink is not None:
            result['Endpoints'] = self.endpoints_shrink

        if self.knowledge_application_spec_shrink is not None:
            result['KnowledgeApplicationSpec'] = self.knowledge_application_spec_shrink

        if self.mem_application_spec_shrink is not None:
            result['MemApplicationSpec'] = self.mem_application_spec_shrink

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

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

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

        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Endpoints') is not None:
            self.endpoints_shrink = m.get('Endpoints')

        if m.get('KnowledgeApplicationSpec') is not None:
            self.knowledge_application_spec_shrink = m.get('KnowledgeApplicationSpec')

        if m.get('MemApplicationSpec') is not None:
            self.mem_application_spec_shrink = m.get('MemApplicationSpec')

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

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

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
                temp_model = main_models.CreateApplicationShrinkRequestTag()
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

class CreateApplicationShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

