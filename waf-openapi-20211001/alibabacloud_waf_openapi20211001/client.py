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

    def create_major_protection_black_ip_with_options(
        self,
        request: waf_openapi_20211001_models.CreateMajorProtectionBlackIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_major_protection_black_ip_with_options(request, runtime)

    async def create_major_protection_black_ip_async(
        self,
        request: waf_openapi_20211001_models.CreateMajorProtectionBlackIpRequest,
    ) -> waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_major_protection_black_ip_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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

    def describe_instance_compatible_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceCompatibleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeInstanceCompatibleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceCompatible',
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
            waf_openapi_20211001_models.DescribeInstanceCompatibleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_compatible_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceCompatibleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeInstanceCompatibleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceCompatible',
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
            waf_openapi_20211001_models.DescribeInstanceCompatibleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_compatible(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceCompatibleRequest,
    ) -> waf_openapi_20211001_models.DescribeInstanceCompatibleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_compatible_with_options(request, runtime)

    async def describe_instance_compatible_async(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceCompatibleRequest,
    ) -> waf_openapi_20211001_models.DescribeInstanceCompatibleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_compatible_with_options_async(request, runtime)

    def describe_instance_extend_with_options(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceExtendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeInstanceExtendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceExtend',
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
            waf_openapi_20211001_models.DescribeInstanceExtendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_extend_with_options_async(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceExtendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20211001_models.DescribeInstanceExtendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceExtend',
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
            waf_openapi_20211001_models.DescribeInstanceExtendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_extend(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceExtendRequest,
    ) -> waf_openapi_20211001_models.DescribeInstanceExtendResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_extend_with_options(request, runtime)

    async def describe_instance_extend_async(
        self,
        request: waf_openapi_20211001_models.DescribeInstanceExtendRequest,
    ) -> waf_openapi_20211001_models.DescribeInstanceExtendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_extend_with_options_async(request, runtime)
