# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_waf_openapi20211001 import models as waf_openapi_20211001_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-chengdu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-huhehaote': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-heyuan': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-wulanchabu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'cn-shanghai-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-north-2-gov-1': 'wafopenapi.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('waf-openapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def clear_major_protection_black_ip_with_options(
        self,
        request: waf_openapi_20211001_models.ClearMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_major_protection_black_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.ClearMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_major_protection_black_ip(
        self,
        request: waf_openapi_20211001_models.ClearMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_major_protection_black_ip_with_options(request, runtime)

    async def clear_major_protection_black_ip_async(
        self,
        request: waf_openapi_20211001_models.ClearMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_major_protection_black_ip_with_options_async(request, runtime)

    def create_defense_resource_group_with_options(
        self,
        request: waf_openapi_20211001_models.CreateDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_list):
            query['AddList'] = request.add_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_defense_resource_group_with_options_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_list):
            query['AddList'] = request.add_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_defense_resource_group(
        self,
        request: waf_openapi_20211001_models.CreateDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_defense_resource_group_with_options(request, runtime)

    async def create_defense_resource_group_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_defense_resource_group_with_options_async(request, runtime)

    def create_defense_rule_with_options(
        self,
        request: waf_openapi_20211001_models.CreateDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_defense_rule_with_options_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_defense_rule(
        self,
        request: waf_openapi_20211001_models.CreateDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_defense_rule_with_options(request, runtime)

    async def create_defense_rule_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_defense_rule_with_options_async(request, runtime)

    def create_defense_template_with_options(
        self,
        request: waf_openapi_20211001_models.CreateDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_origin):
            query['TemplateOrigin'] = request.template_origin
        if not UtilClient.is_unset(request.template_status):
            query['TemplateStatus'] = request.template_status
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_defense_template_with_options_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDefenseTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_origin):
            query['TemplateOrigin'] = request.template_origin
        if not UtilClient.is_unset(request.template_status):
            query['TemplateStatus'] = request.template_status
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_defense_template(
        self,
        request: waf_openapi_20211001_models.CreateDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_defense_template_with_options(request, runtime)

    async def create_defense_template_async(
        self,
        request: waf_openapi_20211001_models.CreateDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.CreateDefenseTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_defense_template_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        tmp_req: waf_openapi_20211001_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDomainResponse:
        UtilClient.validate_model(tmp_req)
        request = waf_openapi_20211001_models.CreateDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.listen):
            request.listen_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not UtilClient.is_unset(tmp_req.redirect):
            request.redirect_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not UtilClient.is_unset(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        tmp_req: waf_openapi_20211001_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateDomainResponse:
        UtilClient.validate_model(tmp_req)
        request = waf_openapi_20211001_models.CreateDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.listen):
            request.listen_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not UtilClient.is_unset(tmp_req.redirect):
            request.redirect_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not UtilClient.is_unset(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: waf_openapi_20211001_models.CreateDomainRequest,
    ) -> waf_openapi_20211001_models.CreateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: waf_openapi_20211001_models.CreateDomainRequest,
    ) -> waf_openapi_20211001_models.CreateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_major_protection_black_ip_with_options(
        self,
        request: waf_openapi_20211001_models.CreateMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse:
        """
        This operation is available only on the China site (aliyun.com).
        
        @param request: CreateMajorProtectionBlackIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMajorProtectionBlackIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_major_protection_black_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.CreateMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse:
        """
        This operation is available only on the China site (aliyun.com).
        
        @param request: CreateMajorProtectionBlackIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMajorProtectionBlackIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_major_protection_black_ip(
        self,
        request: waf_openapi_20211001_models.CreateMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse:
        """
        This operation is available only on the China site (aliyun.com).
        
        @param request: CreateMajorProtectionBlackIpRequest
        @return: CreateMajorProtectionBlackIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_major_protection_black_ip_with_options(request, runtime)

    async def create_major_protection_black_ip_async(
        self,
        request: waf_openapi_20211001_models.CreateMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse:
        """
        This operation is available only on the China site (aliyun.com).
        
        @param request: CreateMajorProtectionBlackIpRequest
        @return: CreateMajorProtectionBlackIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_major_protection_black_ip_with_options_async(request, runtime)

    def create_member_accounts_with_options(
        self,
        request: waf_openapi_20211001_models.CreateMemberAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateMemberAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_ids):
            query['MemberAccountIds'] = request.member_account_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMemberAccounts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateMemberAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_member_accounts_with_options_async(
        self,
        request: waf_openapi_20211001_models.CreateMemberAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateMemberAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_ids):
            query['MemberAccountIds'] = request.member_account_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMemberAccounts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateMemberAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_member_accounts(
        self,
        request: waf_openapi_20211001_models.CreateMemberAccountsRequest,
    ) -> waf_openapi_20211001_models.CreateMemberAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_member_accounts_with_options(request, runtime)

    async def create_member_accounts_async(
        self,
        request: waf_openapi_20211001_models.CreateMemberAccountsRequest,
    ) -> waf_openapi_20211001_models.CreateMemberAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_member_accounts_with_options_async(request, runtime)

    def delete_defense_resource_group_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_defense_resource_group_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_defense_resource_group(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_defense_resource_group_with_options(request, runtime)

    async def delete_defense_resource_group_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_defense_resource_group_with_options_async(request, runtime)

    def delete_defense_rule_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_defense_rule_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_defense_rule(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_defense_rule_with_options(request, runtime)

    async def delete_defense_rule_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_defense_rule_with_options_async(request, runtime)

    def delete_defense_template_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_defense_template_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDefenseTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_defense_template(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_defense_template_with_options(request, runtime)

    async def delete_defense_template_async(
        self,
        request: waf_openapi_20211001_models.DeleteDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.DeleteDefenseTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_defense_template_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: waf_openapi_20211001_models.DeleteDomainRequest,
    ) -> waf_openapi_20211001_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: waf_openapi_20211001_models.DeleteDomainRequest,
    ) -> waf_openapi_20211001_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_major_protection_black_ip_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_major_protection_black_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_major_protection_black_ip(
        self,
        request: waf_openapi_20211001_models.DeleteMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_major_protection_black_ip_with_options(request, runtime)

    async def delete_major_protection_black_ip_async(
        self,
        request: waf_openapi_20211001_models.DeleteMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_major_protection_black_ip_with_options_async(request, runtime)

    def delete_member_account_with_options(
        self,
        request: waf_openapi_20211001_models.DeleteMemberAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteMemberAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMemberAccount',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteMemberAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_member_account_with_options_async(
        self,
        request: waf_openapi_20211001_models.DeleteMemberAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DeleteMemberAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMemberAccount',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteMemberAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_member_account(
        self,
        request: waf_openapi_20211001_models.DeleteMemberAccountRequest,
    ) -> waf_openapi_20211001_models.DeleteMemberAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_member_account_with_options(request, runtime)

    async def delete_member_account_async(
        self,
        request: waf_openapi_20211001_models.DeleteMemberAccountRequest,
    ) -> waf_openapi_20211001_models.DeleteMemberAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_member_account_with_options_async(request, runtime)

    def describe_account_delegated_status_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeAccountDelegatedStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountDelegatedStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_delegated_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeAccountDelegatedStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountDelegatedStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_delegated_status(
        self,
        request: waf_openapi_20211001_models.DescribeAccountDelegatedStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_delegated_status_with_options(request, runtime)

    async def describe_account_delegated_status_async(
        self,
        request: waf_openapi_20211001_models.DescribeAccountDelegatedStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeAccountDelegatedStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_delegated_status_with_options_async(request, runtime)

    def describe_certs_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeCertsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCerts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certs_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeCertsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCerts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certs(
        self,
        request: waf_openapi_20211001_models.DescribeCertsRequest,
    ) -> waf_openapi_20211001_models.DescribeCertsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_certs_with_options(request, runtime)

    async def describe_certs_async(
        self,
        request: waf_openapi_20211001_models.DescribeCertsRequest,
    ) -> waf_openapi_20211001_models.DescribeCertsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_certs_with_options_async(request, runtime)

    def describe_defense_resource_group_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_group_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_group(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resource_group_with_options(request, runtime)

    async def describe_defense_resource_group_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_resource_group_with_options_async(request, runtime)

    def describe_defense_resource_templates_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceTemplates',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_templates_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceTemplates',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_templates(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceTemplatesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resource_templates_with_options(request, runtime)

    async def describe_defense_resource_templates_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourceTemplatesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourceTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_resource_templates_with_options_async(request, runtime)

    def describe_defense_resources_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resources(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resources_with_options(request, runtime)

    async def describe_defense_resources_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_resources_with_options_async(request, runtime)

    def describe_defense_rule_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_rule_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_rule(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_rule_with_options(request, runtime)

    async def describe_defense_rule_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_rule_with_options_async(request, runtime)

    def describe_defense_rules_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRules',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_rules_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRules',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_rules(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRulesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_rules_with_options(request, runtime)

    async def describe_defense_rules_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseRulesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_rules_with_options_async(request, runtime)

    def describe_defense_template_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_template_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_template(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_template_with_options(request, runtime)

    async def describe_defense_template_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_template_with_options_async(request, runtime)

    def describe_defense_templates_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.defense_sub_scene):
            query['DefenseSubScene'] = request.defense_sub_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseTemplates',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_templates_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.defense_sub_scene):
            query['DefenseSubScene'] = request.defense_sub_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseTemplates',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_templates(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplatesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_templates_with_options(request, runtime)

    async def describe_defense_templates_async(
        self,
        request: waf_openapi_20211001_models.DescribeDefenseTemplatesRequest,
    ) -> waf_openapi_20211001_models.DescribeDefenseTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_templates_with_options_async(request, runtime)

    def describe_domain_dnsrecord_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDNSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainDNSRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDNSRecord',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainDNSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_dnsrecord_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDNSRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainDNSRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDNSRecord',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainDNSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_dnsrecord(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDNSRecordRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainDNSRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_dnsrecord_with_options(request, runtime)

    async def describe_domain_dnsrecord_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDNSRecordRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainDNSRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_dnsrecord_with_options_async(request, runtime)

    def describe_domain_detail_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDetail',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_detail_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDetail',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_detail(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDetailRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_detail_with_options(request, runtime)

    async def describe_domain_detail_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainDetailRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_detail_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend):
            query['Backend'] = request.backend
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend):
            query['Backend'] = request.backend
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains(
        self,
        request: waf_openapi_20211001_models.DescribeDomainsRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: waf_openapi_20211001_models.DescribeDomainsRequest,
    ) -> waf_openapi_20211001_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_flow_chart_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeFlowChartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowChartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowChart',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_chart_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowChartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowChartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowChart',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_chart(
        self,
        request: waf_openapi_20211001_models.DescribeFlowChartRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowChartResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_chart_with_options(request, runtime)

    async def describe_flow_chart_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowChartRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowChartResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_chart_with_options_async(request, runtime)

    def describe_flow_top_resource_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowTopResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowTopResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowTopResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_top_resource_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowTopResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowTopResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowTopResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_top_resource(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopResourceRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowTopResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_top_resource_with_options(request, runtime)

    async def describe_flow_top_resource_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopResourceRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowTopResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_top_resource_with_options_async(request, runtime)

    def describe_flow_top_url_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowTopUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowTopUrl',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_top_url_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeFlowTopUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowTopUrl',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowTopUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_top_url(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopUrlRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowTopUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_top_url_with_options(request, runtime)

    async def describe_flow_top_url_async(
        self,
        request: waf_openapi_20211001_models.DescribeFlowTopUrlRequest,
    ) -> waf_openapi_20211001_models.DescribeFlowTopUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_top_url_with_options_async(request, runtime)

    def describe_hybrid_cloud_groups_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_proxy_type):
            query['ClusterProxyType'] = request.cluster_proxy_type
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_groups_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_proxy_type):
            query['ClusterProxyType'] = request.cluster_proxy_type
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_groups(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_cloud_groups_with_options(request, runtime)

    async def describe_hybrid_cloud_groups_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hybrid_cloud_groups_with_options_async(request, runtime)

    def describe_hybrid_cloud_resources_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend):
            query['Backend'] = request.backend
        if not UtilClient.is_unset(request.cname_enabled):
            query['CnameEnabled'] = request.cname_enabled
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend):
            query['Backend'] = request.backend
        if not UtilClient.is_unset(request.cname_enabled):
            query['CnameEnabled'] = request.cname_enabled
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_resources(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_cloud_resources_with_options(request, runtime)

    async def describe_hybrid_cloud_resources_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hybrid_cloud_resources_with_options_async(request, runtime)

    def describe_hybrid_cloud_user_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudUser',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_user_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridCloudUser',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeHybridCloudUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_user(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudUserRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_cloud_user_with_options(request, runtime)

    async def describe_hybrid_cloud_user_async(
        self,
        request: waf_openapi_20211001_models.DescribeHybridCloudUserRequest,
    ) -> waf_openapi_20211001_models.DescribeHybridCloudUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hybrid_cloud_user_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceRequest,
    ) -> waf_openapi_20211001_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceRequest,
    ) -> waf_openapi_20211001_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_major_protection_black_ips_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_like):
            query['IpLike'] = request.ip_like
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMajorProtectionBlackIps',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_major_protection_black_ips_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_like):
            query['IpLike'] = request.ip_like
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMajorProtectionBlackIps',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_major_protection_black_ips(
        self,
        request: waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsRequest,
    ) -> waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_major_protection_black_ips_with_options(request, runtime)

    async def describe_major_protection_black_ips_async(
        self,
        request: waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsRequest,
    ) -> waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_major_protection_black_ips_with_options_async(request, runtime)

    def describe_member_accounts_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeMemberAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeMemberAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_status):
            query['AccountStatus'] = request.account_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMemberAccounts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeMemberAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_member_accounts_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeMemberAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeMemberAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_status):
            query['AccountStatus'] = request.account_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMemberAccounts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeMemberAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_member_accounts(
        self,
        request: waf_openapi_20211001_models.DescribeMemberAccountsRequest,
    ) -> waf_openapi_20211001_models.DescribeMemberAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_member_accounts_with_options(request, runtime)

    async def describe_member_accounts_async(
        self,
        request: waf_openapi_20211001_models.DescribeMemberAccountsRequest,
    ) -> waf_openapi_20211001_models.DescribeMemberAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_member_accounts_with_options_async(request, runtime)

    def describe_peak_trend_with_options(
        self,
        request: waf_openapi_20211001_models.DescribePeakTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribePeakTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePeakTrend',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribePeakTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_peak_trend_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribePeakTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribePeakTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePeakTrend',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribePeakTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_peak_trend(
        self,
        request: waf_openapi_20211001_models.DescribePeakTrendRequest,
    ) -> waf_openapi_20211001_models.DescribePeakTrendResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_peak_trend_with_options(request, runtime)

    async def describe_peak_trend_async(
        self,
        request: waf_openapi_20211001_models.DescribePeakTrendRequest,
    ) -> waf_openapi_20211001_models.DescribePeakTrendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_peak_trend_with_options_async(request, runtime)

    def describe_resource_instance_certs_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResourceInstanceCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceInstanceCerts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_instance_certs_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceInstanceCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceInstanceCerts',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_instance_certs(
        self,
        request: waf_openapi_20211001_models.DescribeResourceInstanceCertsRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_instance_certs_with_options(request, runtime)

    async def describe_resource_instance_certs_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceInstanceCertsRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceInstanceCertsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_instance_certs_with_options_async(request, runtime)

    def describe_resource_log_status_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResourceLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceLogStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_log_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceLogStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_log_status(
        self,
        request: waf_openapi_20211001_models.DescribeResourceLogStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceLogStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_log_status_with_options(request, runtime)

    async def describe_resource_log_status_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceLogStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceLogStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_log_status_with_options_async(request, runtime)

    def describe_resource_port_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResourcePortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourcePortResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourcePort',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourcePortResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_port_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourcePortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourcePortResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourcePort',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourcePortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_port(
        self,
        request: waf_openapi_20211001_models.DescribeResourcePortRequest,
    ) -> waf_openapi_20211001_models.DescribeResourcePortResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_port_with_options(request, runtime)

    async def describe_resource_port_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourcePortRequest,
    ) -> waf_openapi_20211001_models.DescribeResourcePortResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_port_with_options_async(request, runtime)

    def describe_resource_region_id_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResourceRegionIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceRegionIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceRegionId',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceRegionIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_region_id_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceRegionIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceRegionIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceRegionId',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceRegionIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_region_id(
        self,
        request: waf_openapi_20211001_models.DescribeResourceRegionIdRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceRegionIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_region_id_with_options(request, runtime)

    async def describe_resource_region_id_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceRegionIdRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceRegionIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_region_id_with_options_async(request, runtime)

    def describe_resource_support_regions_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResourceSupportRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceSupportRegions',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_support_regions_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceSupportRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceSupportRegions',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_support_regions(
        self,
        request: waf_openapi_20211001_models.DescribeResourceSupportRegionsRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_support_regions_with_options(request, runtime)

    async def describe_resource_support_regions_async(
        self,
        request: waf_openapi_20211001_models.DescribeResourceSupportRegionsRequest,
    ) -> waf_openapi_20211001_models.DescribeResourceSupportRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_support_regions_with_options_async(request, runtime)

    def describe_response_code_trend_graph_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeResponseCodeTrendGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResponseCodeTrendGraph',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_response_code_trend_graph_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeResponseCodeTrendGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResponseCodeTrendGraph',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_response_code_trend_graph(
        self,
        request: waf_openapi_20211001_models.DescribeResponseCodeTrendGraphRequest,
    ) -> waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_response_code_trend_graph_with_options(request, runtime)

    async def describe_response_code_trend_graph_async(
        self,
        request: waf_openapi_20211001_models.DescribeResponseCodeTrendGraphRequest,
    ) -> waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_response_code_trend_graph_with_options_async(request, runtime)

    def describe_rule_groups_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.search_type):
            query['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_groups_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.search_type):
            query['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_groups(
        self,
        request: waf_openapi_20211001_models.DescribeRuleGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_groups_with_options(request, runtime)

    async def describe_rule_groups_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleGroupsRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_groups_with_options_async(request, runtime)

    def describe_rule_hits_top_client_ip_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopClientIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopClientIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_client_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopClientIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopClientIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_client_ip(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopClientIpRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_client_ip_with_options(request, runtime)

    async def describe_rule_hits_top_client_ip_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopClientIpRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_client_ip_with_options_async(request, runtime)

    def describe_rule_hits_top_resource_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_resource_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_resource(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopResourceRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_resource_with_options(request, runtime)

    async def describe_rule_hits_top_resource_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopResourceRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_resource_with_options_async(request, runtime)

    def describe_rule_hits_top_rule_id_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_group_resource):
            query['IsGroupResource'] = request.is_group_resource
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopRuleId',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_rule_id_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_group_resource):
            query['IsGroupResource'] = request.is_group_resource
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopRuleId',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_rule_id(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_rule_id_with_options(request, runtime)

    async def describe_rule_hits_top_rule_id_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_rule_id_with_options_async(request, runtime)

    def describe_rule_hits_top_tule_type_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopTuleType',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_tule_type_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopTuleType',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_tule_type(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_tule_type_with_options(request, runtime)

    async def describe_rule_hits_top_tule_type_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_tule_type_with_options_async(request, runtime)

    def describe_rule_hits_top_ua_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopUa',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_ua_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopUa',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_ua(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUaRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_ua_with_options(request, runtime)

    async def describe_rule_hits_top_ua_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUaRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_ua_with_options_async(request, runtime)

    def describe_rule_hits_top_url_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopUrl',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_url_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopUrl',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_url(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUrlRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_url_with_options(request, runtime)

    async def describe_rule_hits_top_url_async(
        self,
        request: waf_openapi_20211001_models.DescribeRuleHitsTopUrlRequest,
    ) -> waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_hits_top_url_with_options_async(request, runtime)

    def describe_sls_auth_status_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsAuthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsAuthStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_auth_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsAuthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsAuthStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsAuthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_auth_status(
        self,
        request: waf_openapi_20211001_models.DescribeSlsAuthStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsAuthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    async def describe_sls_auth_status_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsAuthStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsAuthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_auth_status_with_options_async(request, runtime)

    def describe_sls_log_store_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogStore',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_log_store_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogStore',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_log_store(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_log_store_with_options(request, runtime)

    async def describe_sls_log_store_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_log_store_with_options_async(request, runtime)

    def describe_sls_log_store_status_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogStoreStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_log_store_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogStoreStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_log_store_status(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_log_store_status_with_options(request, runtime)

    async def describe_sls_log_store_status_async(
        self,
        request: waf_openapi_20211001_models.DescribeSlsLogStoreStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeSlsLogStoreStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_log_store_status_with_options_async(request, runtime)

    def describe_template_resources_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeTemplateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeTemplateResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_resources(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_template_resources_with_options(request, runtime)

    async def describe_template_resources_async(
        self,
        request: waf_openapi_20211001_models.DescribeTemplateResourcesRequest,
    ) -> waf_openapi_20211001_models.DescribeTemplateResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_template_resources_with_options_async(request, runtime)

    def describe_user_sls_log_regions_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeUserSlsLogRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserSlsLogRegions',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_sls_log_regions_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeUserSlsLogRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserSlsLogRegions',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_sls_log_regions(
        self,
        request: waf_openapi_20211001_models.DescribeUserSlsLogRegionsRequest,
    ) -> waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_sls_log_regions_with_options(request, runtime)

    async def describe_user_sls_log_regions_async(
        self,
        request: waf_openapi_20211001_models.DescribeUserSlsLogRegionsRequest,
    ) -> waf_openapi_20211001_models.DescribeUserSlsLogRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_sls_log_regions_with_options_async(request, runtime)

    def describe_user_waf_log_status_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeUserWafLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeUserWafLogStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserWafLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeUserWafLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_waf_log_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeUserWafLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeUserWafLogStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserWafLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeUserWafLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_waf_log_status(
        self,
        request: waf_openapi_20211001_models.DescribeUserWafLogStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeUserWafLogStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_waf_log_status_with_options(request, runtime)

    async def describe_user_waf_log_status_async(
        self,
        request: waf_openapi_20211001_models.DescribeUserWafLogStatusRequest,
    ) -> waf_openapi_20211001_models.DescribeUserWafLogStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_waf_log_status_with_options_async(request, runtime)

    def describe_visit_top_ip_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeVisitTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeVisitTopIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVisitTopIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeVisitTopIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_visit_top_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeVisitTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeVisitTopIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVisitTopIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeVisitTopIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_visit_top_ip(
        self,
        request: waf_openapi_20211001_models.DescribeVisitTopIpRequest,
    ) -> waf_openapi_20211001_models.DescribeVisitTopIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_visit_top_ip_with_options(request, runtime)

    async def describe_visit_top_ip_async(
        self,
        request: waf_openapi_20211001_models.DescribeVisitTopIpRequest,
    ) -> waf_openapi_20211001_models.DescribeVisitTopIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_visit_top_ip_with_options_async(request, runtime)

    def describe_visit_uas_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeVisitUasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeVisitUasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVisitUas',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeVisitUasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_visit_uas_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeVisitUasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeVisitUasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVisitUas',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeVisitUasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_visit_uas(
        self,
        request: waf_openapi_20211001_models.DescribeVisitUasRequest,
    ) -> waf_openapi_20211001_models.DescribeVisitUasResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_visit_uas_with_options(request, runtime)

    async def describe_visit_uas_async(
        self,
        request: waf_openapi_20211001_models.DescribeVisitUasRequest,
    ) -> waf_openapi_20211001_models.DescribeVisitUasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_visit_uas_with_options_async(request, runtime)

    def describe_waf_source_ip_segment_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeWafSourceIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWafSourceIpSegment',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_waf_source_ip_segment_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeWafSourceIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWafSourceIpSegment',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_waf_source_ip_segment(
        self,
        request: waf_openapi_20211001_models.DescribeWafSourceIpSegmentRequest,
    ) -> waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_source_ip_segment_with_options(request, runtime)

    async def describe_waf_source_ip_segment_async(
        self,
        request: waf_openapi_20211001_models.DescribeWafSourceIpSegmentRequest,
    ) -> waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_waf_source_ip_segment_with_options_async(request, runtime)

    def modify_defense_resource_group_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_list):
            query['AddList'] = request.add_list
        if not UtilClient.is_unset(request.delete_list):
            query['DeleteList'] = request.delete_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_resource_group_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_list):
            query['AddList'] = request.add_list
        if not UtilClient.is_unset(request.delete_list):
            query['DeleteList'] = request.delete_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_resource_group(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_resource_group_with_options(request, runtime)

    async def modify_defense_resource_group_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceGroupRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_resource_group_with_options_async(request, runtime)

    def modify_defense_resource_xff_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceXffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceXffResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acw_cookie_status):
            query['AcwCookieStatus'] = request.acw_cookie_status
        if not UtilClient.is_unset(request.acw_secure_status):
            query['AcwSecureStatus'] = request.acw_secure_status
        if not UtilClient.is_unset(request.acw_v3secure_status):
            query['AcwV3SecureStatus'] = request.acw_v3secure_status
        if not UtilClient.is_unset(request.custom_headers):
            query['CustomHeaders'] = request.custom_headers
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.xff_status):
            query['XffStatus'] = request.xff_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseResourceXff',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseResourceXffResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_resource_xff_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceXffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceXffResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acw_cookie_status):
            query['AcwCookieStatus'] = request.acw_cookie_status
        if not UtilClient.is_unset(request.acw_secure_status):
            query['AcwSecureStatus'] = request.acw_secure_status
        if not UtilClient.is_unset(request.acw_v3secure_status):
            query['AcwV3SecureStatus'] = request.acw_v3secure_status
        if not UtilClient.is_unset(request.custom_headers):
            query['CustomHeaders'] = request.custom_headers
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.xff_status):
            query['XffStatus'] = request.xff_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseResourceXff',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseResourceXffResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_resource_xff(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceXffRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceXffResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_resource_xff_with_options(request, runtime)

    async def modify_defense_resource_xff_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseResourceXffRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseResourceXffResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_resource_xff_with_options_async(request, runtime)

    def modify_defense_rule_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_rule_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_rule(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_rule_with_options(request, runtime)

    async def modify_defense_rule_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_rule_with_options_async(request, runtime)

    def modify_defense_rule_cache_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRuleCache',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_rule_cache_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRuleCache',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_rule_cache(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleCacheRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_rule_cache_with_options(request, runtime)

    async def modify_defense_rule_cache_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleCacheRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_rule_cache_with_options_async(request, runtime)

    def modify_defense_rule_status_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRuleStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_rule_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRuleStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_rule_status(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_rule_status_with_options(request, runtime)

    async def modify_defense_rule_status_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseRuleStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_rule_status_with_options_async(request, runtime)

    def modify_defense_template_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_template_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_template(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_template_with_options(request, runtime)

    async def modify_defense_template_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_template_with_options_async(request, runtime)

    def modify_defense_template_status_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_status):
            query['TemplateStatus'] = request.template_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseTemplateStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_template_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_status):
            query['TemplateStatus'] = request.template_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseTemplateStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_template_status(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_template_status_with_options(request, runtime)

    async def modify_defense_template_status_async(
        self,
        request: waf_openapi_20211001_models.ModifyDefenseTemplateStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_template_status_with_options_async(request, runtime)

    def modify_domain_with_options(
        self,
        tmp_req: waf_openapi_20211001_models.ModifyDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDomainResponse:
        UtilClient.validate_model(tmp_req)
        request = waf_openapi_20211001_models.ModifyDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.listen):
            request.listen_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not UtilClient.is_unset(tmp_req.redirect):
            request.redirect_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not UtilClient.is_unset(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_with_options_async(
        self,
        tmp_req: waf_openapi_20211001_models.ModifyDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyDomainResponse:
        UtilClient.validate_model(tmp_req)
        request = waf_openapi_20211001_models.ModifyDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.listen):
            request.listen_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not UtilClient.is_unset(tmp_req.redirect):
            request.redirect_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not UtilClient.is_unset(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain(
        self,
        request: waf_openapi_20211001_models.ModifyDomainRequest,
    ) -> waf_openapi_20211001_models.ModifyDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_with_options(request, runtime)

    async def modify_domain_async(
        self,
        request: waf_openapi_20211001_models.ModifyDomainRequest,
    ) -> waf_openapi_20211001_models.ModifyDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_with_options_async(request, runtime)

    def modify_hybrid_cloud_cluster_bypass_status_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_resource_id):
            query['ClusterResourceId'] = request.cluster_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_status):
            query['RuleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridCloudClusterBypassStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_cloud_cluster_bypass_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_resource_id):
            query['ClusterResourceId'] = request.cluster_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_status):
            query['RuleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridCloudClusterBypassStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_cloud_cluster_bypass_status(
        self,
        request: waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_hybrid_cloud_cluster_bypass_status_with_options(request, runtime)

    async def modify_hybrid_cloud_cluster_bypass_status_async(
        self,
        request: waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyHybridCloudClusterBypassStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_hybrid_cloud_cluster_bypass_status_with_options_async(request, runtime)

    def modify_major_protection_black_ip_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_major_protection_black_ip_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_major_protection_black_ip(
        self,
        request: waf_openapi_20211001_models.ModifyMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_major_protection_black_ip_with_options(request, runtime)

    async def modify_major_protection_black_ip_async(
        self,
        request: waf_openapi_20211001_models.ModifyMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_major_protection_black_ip_with_options_async(request, runtime)

    def modify_member_account_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyMemberAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyMemberAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMemberAccount',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyMemberAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_member_account_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyMemberAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyMemberAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMemberAccount',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyMemberAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_member_account(
        self,
        request: waf_openapi_20211001_models.ModifyMemberAccountRequest,
    ) -> waf_openapi_20211001_models.ModifyMemberAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_member_account_with_options(request, runtime)

    async def modify_member_account_async(
        self,
        request: waf_openapi_20211001_models.ModifyMemberAccountRequest,
    ) -> waf_openapi_20211001_models.ModifyMemberAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_member_account_with_options_async(request, runtime)

    def modify_resource_log_status_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyResourceLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyResourceLogStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyResourceLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_log_status_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyResourceLogStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyResourceLogStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyResourceLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_log_status(
        self,
        request: waf_openapi_20211001_models.ModifyResourceLogStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyResourceLogStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_log_status_with_options(request, runtime)

    async def modify_resource_log_status_async(
        self,
        request: waf_openapi_20211001_models.ModifyResourceLogStatusRequest,
    ) -> waf_openapi_20211001_models.ModifyResourceLogStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_log_status_with_options_async(request, runtime)

    def modify_template_resources_with_options(
        self,
        request: waf_openapi_20211001_models.ModifyTemplateResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyTemplateResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_resource_groups):
            query['BindResourceGroups'] = request.bind_resource_groups
        if not UtilClient.is_unset(request.bind_resources):
            query['BindResources'] = request.bind_resources
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.unbind_resource_groups):
            query['UnbindResourceGroups'] = request.unbind_resource_groups
        if not UtilClient.is_unset(request.unbind_resources):
            query['UnbindResources'] = request.unbind_resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTemplateResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyTemplateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_template_resources_with_options_async(
        self,
        request: waf_openapi_20211001_models.ModifyTemplateResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.ModifyTemplateResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_resource_groups):
            query['BindResourceGroups'] = request.bind_resource_groups
        if not UtilClient.is_unset(request.bind_resources):
            query['BindResources'] = request.bind_resources
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.unbind_resource_groups):
            query['UnbindResourceGroups'] = request.unbind_resource_groups
        if not UtilClient.is_unset(request.unbind_resources):
            query['UnbindResources'] = request.unbind_resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTemplateResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyTemplateResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_template_resources(
        self,
        request: waf_openapi_20211001_models.ModifyTemplateResourcesRequest,
    ) -> waf_openapi_20211001_models.ModifyTemplateResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_template_resources_with_options(request, runtime)

    async def modify_template_resources_async(
        self,
        request: waf_openapi_20211001_models.ModifyTemplateResourcesRequest,
    ) -> waf_openapi_20211001_models.ModifyTemplateResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_template_resources_with_options_async(request, runtime)
