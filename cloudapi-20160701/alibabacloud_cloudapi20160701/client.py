# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudapi20160701 import models as cloud_api20160701_models
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
            'cn-qingdao': 'apigateway.cn-qingdao.aliyuncs.com',
            'cn-beijing': 'apigateway.cn-beijing.aliyuncs.com',
            'cn-chengdu': 'apigateway.cn-chengdu.aliyuncs.com',
            'cn-zhangjiakou': 'apigateway.cn-zhangjiakou.aliyuncs.com',
            'cn-huhehaote': 'apigateway.cn-huhehaote.aliyuncs.com',
            'cn-hangzhou': 'apigateway.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'apigateway.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'apigateway.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'apigateway.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'apigateway.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'apigateway.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'apigateway.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'apigateway.ap-southeast-5.aliyuncs.com',
            'ap-northeast-1': 'apigateway.ap-northeast-1.aliyuncs.com',
            'eu-west-1': 'apigateway.eu-west-1.aliyuncs.com',
            'us-west-1': 'apigateway.us-west-1.aliyuncs.com',
            'us-east-1': 'apigateway.us-east-1.aliyuncs.com',
            'eu-central-1': 'apigateway.eu-central-1.aliyuncs.com',
            'me-east-1': 'apigateway.me-east-1.aliyuncs.com',
            'ap-south-1': 'apigateway.ap-south-1.aliyuncs.com',
            'cn-north-2-gov-1': 'apigateway.cn-north-2-gov-1.aliyuncs.com',
            'cn-hangzhou-finance': 'apigateway.aliyuncs.com',
            'cn-shenzhen-finance-1': 'apigateway.aliyuncs.com',
            'cn-shanghai-finance-1': 'apigateway.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abolish_api_with_options(
        self,
        request: cloud_api20160701_models.AbolishApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.AbolishApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbolishApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.AbolishApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def abolish_api_with_options_async(
        self,
        request: cloud_api20160701_models.AbolishApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.AbolishApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbolishApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.AbolishApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abolish_api(
        self,
        request: cloud_api20160701_models.AbolishApiRequest,
    ) -> cloud_api20160701_models.AbolishApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.abolish_api_with_options(request, runtime)

    async def abolish_api_async(
        self,
        request: cloud_api20160701_models.AbolishApiRequest,
    ) -> cloud_api20160701_models.AbolishApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abolish_api_with_options_async(request, runtime)

    def add_black_list_with_options(
        self,
        request: cloud_api20160701_models.AddBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.AddBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_content):
            query['BlackContent'] = request.black_content
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBlackList',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.AddBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_black_list_with_options_async(
        self,
        request: cloud_api20160701_models.AddBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.AddBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_content):
            query['BlackContent'] = request.black_content
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBlackList',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.AddBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_black_list(
        self,
        request: cloud_api20160701_models.AddBlackListRequest,
    ) -> cloud_api20160701_models.AddBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_black_list_with_options(request, runtime)

    async def add_black_list_async(
        self,
        request: cloud_api20160701_models.AddBlackListRequest,
    ) -> cloud_api20160701_models.AddBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_black_list_with_options_async(request, runtime)

    def add_ip_control_policy_item_with_options(
        self,
        request: cloud_api20160701_models.AddIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.AddIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cidr_ip):
            query['CidrIp'] = request.cidr_ip
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIpControlPolicyItem',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.AddIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ip_control_policy_item_with_options_async(
        self,
        request: cloud_api20160701_models.AddIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.AddIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cidr_ip):
            query['CidrIp'] = request.cidr_ip
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIpControlPolicyItem',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.AddIpControlPolicyItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ip_control_policy_item(
        self,
        request: cloud_api20160701_models.AddIpControlPolicyItemRequest,
    ) -> cloud_api20160701_models.AddIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ip_control_policy_item_with_options(request, runtime)

    async def add_ip_control_policy_item_async(
        self,
        request: cloud_api20160701_models.AddIpControlPolicyItemRequest,
    ) -> cloud_api20160701_models.AddIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ip_control_policy_item_with_options_async(request, runtime)

    def add_traffic_special_control_with_options(
        self,
        request: cloud_api20160701_models.AddTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.AddTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.special_key):
            query['SpecialKey'] = request.special_key
        if not UtilClient.is_unset(request.special_type):
            query['SpecialType'] = request.special_type
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_value):
            query['TrafficValue'] = request.traffic_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTrafficSpecialControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.AddTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_traffic_special_control_with_options_async(
        self,
        request: cloud_api20160701_models.AddTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.AddTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.special_key):
            query['SpecialKey'] = request.special_key
        if not UtilClient.is_unset(request.special_type):
            query['SpecialType'] = request.special_type
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_value):
            query['TrafficValue'] = request.traffic_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTrafficSpecialControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.AddTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_traffic_special_control(
        self,
        request: cloud_api20160701_models.AddTrafficSpecialControlRequest,
    ) -> cloud_api20160701_models.AddTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_traffic_special_control_with_options(request, runtime)

    async def add_traffic_special_control_async(
        self,
        request: cloud_api20160701_models.AddTrafficSpecialControlRequest,
    ) -> cloud_api20160701_models.AddTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_traffic_special_control_with_options_async(request, runtime)

    def create_api_with_options(
        self,
        request: cloud_api20160701_models.CreateApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not UtilClient.is_unset(request.error_code_samples):
            query['ErrorCodeSamples'] = request.error_code_samples
        if not UtilClient.is_unset(request.fail_result_sample):
            query['FailResultSample'] = request.fail_result_sample
        if not UtilClient.is_unset(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.open_id_connect_config):
            query['OpenIdConnectConfig'] = request.open_id_connect_config
        if not UtilClient.is_unset(request.request_config):
            query['RequestConfig'] = request.request_config
        if not UtilClient.is_unset(request.request_paramters):
            query['RequestParamters'] = request.request_paramters
        if not UtilClient.is_unset(request.result_body_model):
            query['ResultBodyModel'] = request.result_body_model
        if not UtilClient.is_unset(request.result_descriptions):
            query['ResultDescriptions'] = request.result_descriptions
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not UtilClient.is_unset(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        if not UtilClient.is_unset(request.web_socket_api_type):
            query['WebSocketApiType'] = request.web_socket_api_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_with_options_async(
        self,
        request: cloud_api20160701_models.CreateApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not UtilClient.is_unset(request.error_code_samples):
            query['ErrorCodeSamples'] = request.error_code_samples
        if not UtilClient.is_unset(request.fail_result_sample):
            query['FailResultSample'] = request.fail_result_sample
        if not UtilClient.is_unset(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.open_id_connect_config):
            query['OpenIdConnectConfig'] = request.open_id_connect_config
        if not UtilClient.is_unset(request.request_config):
            query['RequestConfig'] = request.request_config
        if not UtilClient.is_unset(request.request_paramters):
            query['RequestParamters'] = request.request_paramters
        if not UtilClient.is_unset(request.result_body_model):
            query['ResultBodyModel'] = request.result_body_model
        if not UtilClient.is_unset(request.result_descriptions):
            query['ResultDescriptions'] = request.result_descriptions
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not UtilClient.is_unset(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        if not UtilClient.is_unset(request.web_socket_api_type):
            query['WebSocketApiType'] = request.web_socket_api_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api(
        self,
        request: cloud_api20160701_models.CreateApiRequest,
    ) -> cloud_api20160701_models.CreateApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_api_with_options(request, runtime)

    async def create_api_async(
        self,
        request: cloud_api20160701_models.CreateApiRequest,
    ) -> cloud_api20160701_models.CreateApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_api_with_options_async(request, runtime)

    def create_api_group_with_options(
        self,
        request: cloud_api20160701_models.CreateApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiGroup',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_group_with_options_async(
        self,
        request: cloud_api20160701_models.CreateApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiGroup',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_group(
        self,
        request: cloud_api20160701_models.CreateApiGroupRequest,
    ) -> cloud_api20160701_models.CreateApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_api_group_with_options(request, runtime)

    async def create_api_group_async(
        self,
        request: cloud_api20160701_models.CreateApiGroupRequest,
    ) -> cloud_api20160701_models.CreateApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_api_group_with_options_async(request, runtime)

    def create_api_stage_variable_with_options(
        self,
        request: cloud_api20160701_models.CreateApiStageVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateApiStageVariableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.stage_route_model):
            query['StageRouteModel'] = request.stage_route_model
        if not UtilClient.is_unset(request.support_route):
            query['SupportRoute'] = request.support_route
        if not UtilClient.is_unset(request.variable_name):
            query['VariableName'] = request.variable_name
        if not UtilClient.is_unset(request.variable_value):
            query['VariableValue'] = request.variable_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiStageVariable',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateApiStageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_stage_variable_with_options_async(
        self,
        request: cloud_api20160701_models.CreateApiStageVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateApiStageVariableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.stage_route_model):
            query['StageRouteModel'] = request.stage_route_model
        if not UtilClient.is_unset(request.support_route):
            query['SupportRoute'] = request.support_route
        if not UtilClient.is_unset(request.variable_name):
            query['VariableName'] = request.variable_name
        if not UtilClient.is_unset(request.variable_value):
            query['VariableValue'] = request.variable_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiStageVariable',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateApiStageVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_stage_variable(
        self,
        request: cloud_api20160701_models.CreateApiStageVariableRequest,
    ) -> cloud_api20160701_models.CreateApiStageVariableResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_api_stage_variable_with_options(request, runtime)

    async def create_api_stage_variable_async(
        self,
        request: cloud_api20160701_models.CreateApiStageVariableRequest,
    ) -> cloud_api20160701_models.CreateApiStageVariableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_api_stage_variable_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: cloud_api20160701_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: cloud_api20160701_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: cloud_api20160701_models.CreateAppRequest,
    ) -> cloud_api20160701_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: cloud_api20160701_models.CreateAppRequest,
    ) -> cloud_api20160701_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_customized_info_with_options(
        self,
        request: cloud_api20160701_models.CreateCustomizedInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateCustomizedInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.csharp_demo):
            query['CsharpDemo'] = request.csharp_demo
        if not UtilClient.is_unset(request.curl_demo):
            query['CurlDemo'] = request.curl_demo
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.java_demo):
            query['JavaDemo'] = request.java_demo
        if not UtilClient.is_unset(request.objectc_demo):
            query['ObjectcDemo'] = request.objectc_demo
        if not UtilClient.is_unset(request.php_demo):
            query['PhpDemo'] = request.php_demo
        if not UtilClient.is_unset(request.python_demo):
            query['PythonDemo'] = request.python_demo
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomizedInfo',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateCustomizedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_customized_info_with_options_async(
        self,
        request: cloud_api20160701_models.CreateCustomizedInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateCustomizedInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.csharp_demo):
            query['CsharpDemo'] = request.csharp_demo
        if not UtilClient.is_unset(request.curl_demo):
            query['CurlDemo'] = request.curl_demo
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.java_demo):
            query['JavaDemo'] = request.java_demo
        if not UtilClient.is_unset(request.objectc_demo):
            query['ObjectcDemo'] = request.objectc_demo
        if not UtilClient.is_unset(request.php_demo):
            query['PhpDemo'] = request.php_demo
        if not UtilClient.is_unset(request.python_demo):
            query['PythonDemo'] = request.python_demo
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomizedInfo',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateCustomizedInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_customized_info(
        self,
        request: cloud_api20160701_models.CreateCustomizedInfoRequest,
    ) -> cloud_api20160701_models.CreateCustomizedInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_customized_info_with_options(request, runtime)

    async def create_customized_info_async(
        self,
        request: cloud_api20160701_models.CreateCustomizedInfoRequest,
    ) -> cloud_api20160701_models.CreateCustomizedInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_customized_info_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: cloud_api20160701_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_quantity):
            query['AccountQuantity'] = request.account_quantity
        if not UtilClient.is_unset(request.expired_on):
            query['ExpiredOn'] = request.expired_on
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sku_id):
            query['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: cloud_api20160701_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_quantity):
            query['AccountQuantity'] = request.account_quantity
        if not UtilClient.is_unset(request.expired_on):
            query['ExpiredOn'] = request.expired_on
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sku_id):
            query['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: cloud_api20160701_models.CreateInstanceRequest,
    ) -> cloud_api20160701_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: cloud_api20160701_models.CreateInstanceRequest,
    ) -> cloud_api20160701_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_intranet_domain_with_options(
        self,
        request: cloud_api20160701_models.CreateIntranetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateIntranetDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntranetDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateIntranetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_intranet_domain_with_options_async(
        self,
        request: cloud_api20160701_models.CreateIntranetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateIntranetDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntranetDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateIntranetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_intranet_domain(
        self,
        request: cloud_api20160701_models.CreateIntranetDomainRequest,
    ) -> cloud_api20160701_models.CreateIntranetDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_intranet_domain_with_options(request, runtime)

    async def create_intranet_domain_async(
        self,
        request: cloud_api20160701_models.CreateIntranetDomainRequest,
    ) -> cloud_api20160701_models.CreateIntranetDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_intranet_domain_with_options_async(request, runtime)

    def create_ip_control_with_options(
        self,
        request: cloud_api20160701_models.CreateIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not UtilClient.is_unset(request.ip_control_policys):
            query['IpControlPolicys'] = request.ip_control_policys
        if not UtilClient.is_unset(request.ip_control_type):
            query['IpControlType'] = request.ip_control_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ip_control_with_options_async(
        self,
        request: cloud_api20160701_models.CreateIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not UtilClient.is_unset(request.ip_control_policys):
            query['IpControlPolicys'] = request.ip_control_policys
        if not UtilClient.is_unset(request.ip_control_type):
            query['IpControlType'] = request.ip_control_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ip_control(
        self,
        request: cloud_api20160701_models.CreateIpControlRequest,
    ) -> cloud_api20160701_models.CreateIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ip_control_with_options(request, runtime)

    async def create_ip_control_async(
        self,
        request: cloud_api20160701_models.CreateIpControlRequest,
    ) -> cloud_api20160701_models.CreateIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ip_control_with_options_async(request, runtime)

    def create_log_config_with_options(
        self,
        request: cloud_api20160701_models.CreateLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogConfig',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_log_config_with_options_async(
        self,
        request: cloud_api20160701_models.CreateLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogConfig',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_log_config(
        self,
        request: cloud_api20160701_models.CreateLogConfigRequest,
    ) -> cloud_api20160701_models.CreateLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_log_config_with_options(request, runtime)

    async def create_log_config_async(
        self,
        request: cloud_api20160701_models.CreateLogConfigRequest,
    ) -> cloud_api20160701_models.CreateLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_log_config_with_options_async(request, runtime)

    def create_race_work_for_inner_with_options(
        self,
        request: cloud_api20160701_models.CreateRaceWorkForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateRaceWorkForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.short_description):
            query['ShortDescription'] = request.short_description
        if not UtilClient.is_unset(request.work_name):
            query['WorkName'] = request.work_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRaceWorkForInner',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateRaceWorkForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_race_work_for_inner_with_options_async(
        self,
        request: cloud_api20160701_models.CreateRaceWorkForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateRaceWorkForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.short_description):
            query['ShortDescription'] = request.short_description
        if not UtilClient.is_unset(request.work_name):
            query['WorkName'] = request.work_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRaceWorkForInner',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateRaceWorkForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_race_work_for_inner(
        self,
        request: cloud_api20160701_models.CreateRaceWorkForInnerRequest,
    ) -> cloud_api20160701_models.CreateRaceWorkForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_race_work_for_inner_with_options(request, runtime)

    async def create_race_work_for_inner_async(
        self,
        request: cloud_api20160701_models.CreateRaceWorkForInnerRequest,
    ) -> cloud_api20160701_models.CreateRaceWorkForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_race_work_for_inner_with_options_async(request, runtime)

    def create_secret_key_with_options(
        self,
        request: cloud_api20160701_models.CreateSecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateSecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        if not UtilClient.is_unset(request.secret_value):
            query['SecretValue'] = request.secret_value
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecretKey',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateSecretKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_key_with_options_async(
        self,
        request: cloud_api20160701_models.CreateSecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateSecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        if not UtilClient.is_unset(request.secret_value):
            query['SecretValue'] = request.secret_value
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecretKey',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateSecretKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret_key(
        self,
        request: cloud_api20160701_models.CreateSecretKeyRequest,
    ) -> cloud_api20160701_models.CreateSecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_secret_key_with_options(request, runtime)

    async def create_secret_key_async(
        self,
        request: cloud_api20160701_models.CreateSecretKeyRequest,
    ) -> cloud_api20160701_models.CreateSecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_secret_key_with_options_async(request, runtime)

    def create_traffic_control_with_options(
        self,
        request: cloud_api20160701_models.CreateTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_default):
            query['ApiDefault'] = request.api_default
        if not UtilClient.is_unset(request.app_default):
            query['AppDefault'] = request.app_default
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not UtilClient.is_unset(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not UtilClient.is_unset(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrafficControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_traffic_control_with_options_async(
        self,
        request: cloud_api20160701_models.CreateTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.CreateTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_default):
            query['ApiDefault'] = request.api_default
        if not UtilClient.is_unset(request.app_default):
            query['AppDefault'] = request.app_default
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not UtilClient.is_unset(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not UtilClient.is_unset(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrafficControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.CreateTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_traffic_control(
        self,
        request: cloud_api20160701_models.CreateTrafficControlRequest,
    ) -> cloud_api20160701_models.CreateTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_control_with_options(request, runtime)

    async def create_traffic_control_async(
        self,
        request: cloud_api20160701_models.CreateTrafficControlRequest,
    ) -> cloud_api20160701_models.CreateTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_traffic_control_with_options_async(request, runtime)

    def delete_all_traffic_special_control_with_options(
        self,
        request: cloud_api20160701_models.DeleteAllTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteAllTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAllTrafficSpecialControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteAllTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_all_traffic_special_control_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteAllTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteAllTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAllTrafficSpecialControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteAllTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_all_traffic_special_control(
        self,
        request: cloud_api20160701_models.DeleteAllTrafficSpecialControlRequest,
    ) -> cloud_api20160701_models.DeleteAllTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_all_traffic_special_control_with_options(request, runtime)

    async def delete_all_traffic_special_control_async(
        self,
        request: cloud_api20160701_models.DeleteAllTrafficSpecialControlRequest,
    ) -> cloud_api20160701_models.DeleteAllTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_all_traffic_special_control_with_options_async(request, runtime)

    def delete_api_with_options(
        self,
        request: cloud_api20160701_models.DeleteApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api(
        self,
        request: cloud_api20160701_models.DeleteApiRequest,
    ) -> cloud_api20160701_models.DeleteApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_api_with_options(request, runtime)

    async def delete_api_async(
        self,
        request: cloud_api20160701_models.DeleteApiRequest,
    ) -> cloud_api20160701_models.DeleteApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_with_options_async(request, runtime)

    def delete_api_group_with_options(
        self,
        request: cloud_api20160701_models.DeleteApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiGroup',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_group_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiGroup',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_group(
        self,
        request: cloud_api20160701_models.DeleteApiGroupRequest,
    ) -> cloud_api20160701_models.DeleteApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_api_group_with_options(request, runtime)

    async def delete_api_group_async(
        self,
        request: cloud_api20160701_models.DeleteApiGroupRequest,
    ) -> cloud_api20160701_models.DeleteApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_group_with_options_async(request, runtime)

    def delete_api_stage_variable_with_options(
        self,
        request: cloud_api20160701_models.DeleteApiStageVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteApiStageVariableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.variable_name):
            query['VariableName'] = request.variable_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiStageVariable',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteApiStageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_stage_variable_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteApiStageVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteApiStageVariableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.variable_name):
            query['VariableName'] = request.variable_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiStageVariable',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteApiStageVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_stage_variable(
        self,
        request: cloud_api20160701_models.DeleteApiStageVariableRequest,
    ) -> cloud_api20160701_models.DeleteApiStageVariableResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_api_stage_variable_with_options(request, runtime)

    async def delete_api_stage_variable_async(
        self,
        request: cloud_api20160701_models.DeleteApiStageVariableRequest,
    ) -> cloud_api20160701_models.DeleteApiStageVariableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_stage_variable_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: cloud_api20160701_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: cloud_api20160701_models.DeleteAppRequest,
    ) -> cloud_api20160701_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: cloud_api20160701_models.DeleteAppRequest,
    ) -> cloud_api20160701_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: cloud_api20160701_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: cloud_api20160701_models.DeleteDomainRequest,
    ) -> cloud_api20160701_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: cloud_api20160701_models.DeleteDomainRequest,
    ) -> cloud_api20160701_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_domain_certificate_with_options(
        self,
        request: cloud_api20160701_models.DeleteDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainCertificate',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_certificate_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainCertificate',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_certificate(
        self,
        request: cloud_api20160701_models.DeleteDomainCertificateRequest,
    ) -> cloud_api20160701_models.DeleteDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_certificate_with_options(request, runtime)

    async def delete_domain_certificate_async(
        self,
        request: cloud_api20160701_models.DeleteDomainCertificateRequest,
    ) -> cloud_api20160701_models.DeleteDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_certificate_with_options_async(request, runtime)

    def delete_ip_control_with_options(
        self,
        request: cloud_api20160701_models.DeleteIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIpControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ip_control_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIpControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ip_control(
        self,
        request: cloud_api20160701_models.DeleteIpControlRequest,
    ) -> cloud_api20160701_models.DeleteIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_control_with_options(request, runtime)

    async def delete_ip_control_async(
        self,
        request: cloud_api20160701_models.DeleteIpControlRequest,
    ) -> cloud_api20160701_models.DeleteIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ip_control_with_options_async(request, runtime)

    def delete_log_config_with_options(
        self,
        request: cloud_api20160701_models.DeleteLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogConfig',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_config_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogConfig',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_config(
        self,
        request: cloud_api20160701_models.DeleteLogConfigRequest,
    ) -> cloud_api20160701_models.DeleteLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_log_config_with_options(request, runtime)

    async def delete_log_config_async(
        self,
        request: cloud_api20160701_models.DeleteLogConfigRequest,
    ) -> cloud_api20160701_models.DeleteLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_log_config_with_options_async(request, runtime)

    def delete_secret_key_with_options(
        self,
        request: cloud_api20160701_models.DeleteSecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteSecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecretKey',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteSecretKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_key_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteSecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteSecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecretKey',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteSecretKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret_key(
        self,
        request: cloud_api20160701_models.DeleteSecretKeyRequest,
    ) -> cloud_api20160701_models.DeleteSecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_key_with_options(request, runtime)

    async def delete_secret_key_async(
        self,
        request: cloud_api20160701_models.DeleteSecretKeyRequest,
    ) -> cloud_api20160701_models.DeleteSecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_secret_key_with_options_async(request, runtime)

    def delete_traffic_control_with_options(
        self,
        request: cloud_api20160701_models.DeleteTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_control_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_control(
        self,
        request: cloud_api20160701_models.DeleteTrafficControlRequest,
    ) -> cloud_api20160701_models.DeleteTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_control_with_options(request, runtime)

    async def delete_traffic_control_async(
        self,
        request: cloud_api20160701_models.DeleteTrafficControlRequest,
    ) -> cloud_api20160701_models.DeleteTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_traffic_control_with_options_async(request, runtime)

    def delete_traffic_special_control_with_options(
        self,
        request: cloud_api20160701_models.DeleteTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.special_key):
            query['SpecialKey'] = request.special_key
        if not UtilClient.is_unset(request.special_type):
            query['SpecialType'] = request.special_type
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficSpecialControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_special_control_with_options_async(
        self,
        request: cloud_api20160701_models.DeleteTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeleteTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.special_key):
            query['SpecialKey'] = request.special_key
        if not UtilClient.is_unset(request.special_type):
            query['SpecialType'] = request.special_type
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficSpecialControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeleteTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_special_control(
        self,
        request: cloud_api20160701_models.DeleteTrafficSpecialControlRequest,
    ) -> cloud_api20160701_models.DeleteTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_special_control_with_options(request, runtime)

    async def delete_traffic_special_control_async(
        self,
        request: cloud_api20160701_models.DeleteTrafficSpecialControlRequest,
    ) -> cloud_api20160701_models.DeleteTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_traffic_special_control_with_options_async(request, runtime)

    def deploy_api_with_options(
        self,
        request: cloud_api20160701_models.DeployApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeployApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.support_mock):
            query['SupportMock'] = request.support_mock
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeployApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_api_with_options_async(
        self,
        request: cloud_api20160701_models.DeployApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DeployApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.support_mock):
            query['SupportMock'] = request.support_mock
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DeployApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_api(
        self,
        request: cloud_api20160701_models.DeployApiRequest,
    ) -> cloud_api20160701_models.DeployApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_api_with_options(request, runtime)

    async def deploy_api_async(
        self,
        request: cloud_api20160701_models.DeployApiRequest,
    ) -> cloud_api20160701_models.DeployApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_api_with_options_async(request, runtime)

    def describe_api_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api(
        self,
        request: cloud_api20160701_models.DescribeApiRequest,
    ) -> cloud_api20160701_models.DescribeApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_with_options(request, runtime)

    async def describe_api_async(
        self,
        request: cloud_api20160701_models.DescribeApiRequest,
    ) -> cloud_api20160701_models.DescribeApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_with_options_async(request, runtime)

    def describe_api_doc_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiDocResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiDoc',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_doc_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiDocResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiDoc',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_doc(
        self,
        request: cloud_api20160701_models.DescribeApiDocRequest,
    ) -> cloud_api20160701_models.DescribeApiDocResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_doc_with_options(request, runtime)

    async def describe_api_doc_async(
        self,
        request: cloud_api20160701_models.DescribeApiDocRequest,
    ) -> cloud_api20160701_models.DescribeApiDocResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_doc_with_options_async(request, runtime)

    def describe_api_docs_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiDocsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiDocsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiDocs',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiDocsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_docs_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiDocsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiDocsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiDocs',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiDocsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_docs(
        self,
        request: cloud_api20160701_models.DescribeApiDocsRequest,
    ) -> cloud_api20160701_models.DescribeApiDocsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_docs_with_options(request, runtime)

    async def describe_api_docs_async(
        self,
        request: cloud_api20160701_models.DescribeApiDocsRequest,
    ) -> cloud_api20160701_models.DescribeApiDocsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_docs_with_options_async(request, runtime)

    def describe_api_error_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiErrorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiErrorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiError',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiErrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_error_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiErrorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiErrorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiError',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiErrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_error(
        self,
        request: cloud_api20160701_models.DescribeApiErrorRequest,
    ) -> cloud_api20160701_models.DescribeApiErrorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_error_with_options(request, runtime)

    async def describe_api_error_async(
        self,
        request: cloud_api20160701_models.DescribeApiErrorRequest,
    ) -> cloud_api20160701_models.DescribeApiErrorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_error_with_options_async(request, runtime)

    def describe_api_group_detail_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroupDetail',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_group_detail_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroupDetail',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_group_detail(
        self,
        request: cloud_api20160701_models.DescribeApiGroupDetailRequest,
    ) -> cloud_api20160701_models.DescribeApiGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_group_detail_with_options(request, runtime)

    async def describe_api_group_detail_async(
        self,
        request: cloud_api20160701_models.DescribeApiGroupDetailRequest,
    ) -> cloud_api20160701_models.DescribeApiGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_group_detail_with_options_async(request, runtime)

    def describe_api_group_detail_for_consumer_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiGroupDetailForConsumerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiGroupDetailForConsumerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroupDetailForConsumer',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiGroupDetailForConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_group_detail_for_consumer_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiGroupDetailForConsumerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiGroupDetailForConsumerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroupDetailForConsumer',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiGroupDetailForConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_group_detail_for_consumer(
        self,
        request: cloud_api20160701_models.DescribeApiGroupDetailForConsumerRequest,
    ) -> cloud_api20160701_models.DescribeApiGroupDetailForConsumerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_group_detail_for_consumer_with_options(request, runtime)

    async def describe_api_group_detail_for_consumer_async(
        self,
        request: cloud_api20160701_models.DescribeApiGroupDetailForConsumerRequest,
    ) -> cloud_api20160701_models.DescribeApiGroupDetailForConsumerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_group_detail_for_consumer_with_options_async(request, runtime)

    def describe_api_groups_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.not_classic):
            query['NotClassic'] = request.not_classic
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroups',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_groups_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.not_classic):
            query['NotClassic'] = request.not_classic
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroups',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_groups(
        self,
        request: cloud_api20160701_models.DescribeApiGroupsRequest,
    ) -> cloud_api20160701_models.DescribeApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_groups_with_options(request, runtime)

    async def describe_api_groups_async(
        self,
        request: cloud_api20160701_models.DescribeApiGroupsRequest,
    ) -> cloud_api20160701_models.DescribeApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_groups_with_options_async(request, runtime)

    def describe_api_ip_controls_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiIpControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiIpControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiIpControls',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiIpControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_ip_controls_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiIpControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiIpControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiIpControls',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiIpControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_ip_controls(
        self,
        request: cloud_api20160701_models.DescribeApiIpControlsRequest,
    ) -> cloud_api20160701_models.DescribeApiIpControlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_ip_controls_with_options(request, runtime)

    async def describe_api_ip_controls_async(
        self,
        request: cloud_api20160701_models.DescribeApiIpControlsRequest,
    ) -> cloud_api20160701_models.DescribeApiIpControlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_ip_controls_with_options_async(request, runtime)

    def describe_api_latency_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiLatencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiLatencyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiLatency',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiLatencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_latency_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiLatencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiLatencyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiLatency',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiLatencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_latency(
        self,
        request: cloud_api20160701_models.DescribeApiLatencyRequest,
    ) -> cloud_api20160701_models.DescribeApiLatencyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_latency_with_options(request, runtime)

    async def describe_api_latency_async(
        self,
        request: cloud_api20160701_models.DescribeApiLatencyRequest,
    ) -> cloud_api20160701_models.DescribeApiLatencyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_latency_with_options_async(request, runtime)

    def describe_api_qps_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiQpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiQps',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_qps_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiQpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiQps',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_qps(
        self,
        request: cloud_api20160701_models.DescribeApiQpsRequest,
    ) -> cloud_api20160701_models.DescribeApiQpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_qps_with_options(request, runtime)

    async def describe_api_qps_async(
        self,
        request: cloud_api20160701_models.DescribeApiQpsRequest,
    ) -> cloud_api20160701_models.DescribeApiQpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_qps_with_options_async(request, runtime)

    def describe_api_rules_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiRules',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_rules_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiRules',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_rules(
        self,
        request: cloud_api20160701_models.DescribeApiRulesRequest,
    ) -> cloud_api20160701_models.DescribeApiRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_rules_with_options(request, runtime)

    async def describe_api_rules_async(
        self,
        request: cloud_api20160701_models.DescribeApiRulesRequest,
    ) -> cloud_api20160701_models.DescribeApiRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_rules_with_options_async(request, runtime)

    def describe_api_stage_detail_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiStageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiStageDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiStageDetail',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiStageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_stage_detail_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiStageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiStageDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiStageDetail',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiStageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_stage_detail(
        self,
        request: cloud_api20160701_models.DescribeApiStageDetailRequest,
    ) -> cloud_api20160701_models.DescribeApiStageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_stage_detail_with_options(request, runtime)

    async def describe_api_stage_detail_async(
        self,
        request: cloud_api20160701_models.DescribeApiStageDetailRequest,
    ) -> cloud_api20160701_models.DescribeApiStageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_stage_detail_with_options_async(request, runtime)

    def describe_api_traffic_with_options(
        self,
        request: cloud_api20160701_models.DescribeApiTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiTrafficResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiTraffic',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_traffic_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApiTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApiTrafficResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiTraffic',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApiTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_traffic(
        self,
        request: cloud_api20160701_models.DescribeApiTrafficRequest,
    ) -> cloud_api20160701_models.DescribeApiTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_traffic_with_options(request, runtime)

    async def describe_api_traffic_async(
        self,
        request: cloud_api20160701_models.DescribeApiTrafficRequest,
    ) -> cloud_api20160701_models.DescribeApiTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_traffic_with_options_async(request, runtime)

    def describe_apis_with_options(
        self,
        request: cloud_api20160701_models.DescribeApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis(
        self,
        request: cloud_api20160701_models.DescribeApisRequest,
    ) -> cloud_api20160701_models.DescribeApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_with_options(request, runtime)

    async def describe_apis_async(
        self,
        request: cloud_api20160701_models.DescribeApisRequest,
    ) -> cloud_api20160701_models.DescribeApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_with_options_async(request, runtime)

    def describe_apis_by_app_with_options(
        self,
        request: cloud_api20160701_models.DescribeApisByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApisByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApisByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_app_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApisByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApisByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApisByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_app(
        self,
        request: cloud_api20160701_models.DescribeApisByAppRequest,
    ) -> cloud_api20160701_models.DescribeApisByAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_app_with_options(request, runtime)

    async def describe_apis_by_app_async(
        self,
        request: cloud_api20160701_models.DescribeApisByAppRequest,
    ) -> cloud_api20160701_models.DescribeApisByAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_by_app_with_options_async(request, runtime)

    def describe_apis_by_ip_control_with_options(
        self,
        request: cloud_api20160701_models.DescribeApisByIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApisByIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByIpControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApisByIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_ip_control_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApisByIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApisByIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByIpControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApisByIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_ip_control(
        self,
        request: cloud_api20160701_models.DescribeApisByIpControlRequest,
    ) -> cloud_api20160701_models.DescribeApisByIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_ip_control_with_options(request, runtime)

    async def describe_apis_by_ip_control_async(
        self,
        request: cloud_api20160701_models.DescribeApisByIpControlRequest,
    ) -> cloud_api20160701_models.DescribeApisByIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_by_ip_control_with_options_async(request, runtime)

    def describe_apis_by_rule_with_options(
        self,
        request: cloud_api20160701_models.DescribeApisByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApisByRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByRule',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApisByRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_rule_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApisByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApisByRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByRule',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApisByRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_rule(
        self,
        request: cloud_api20160701_models.DescribeApisByRuleRequest,
    ) -> cloud_api20160701_models.DescribeApisByRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_rule_with_options(request, runtime)

    async def describe_apis_by_rule_async(
        self,
        request: cloud_api20160701_models.DescribeApisByRuleRequest,
    ) -> cloud_api20160701_models.DescribeApisByRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_by_rule_with_options_async(request, runtime)

    def describe_apis_for_console_with_options(
        self,
        request: cloud_api20160701_models.DescribeApisForConsoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApisForConsoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisForConsole',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApisForConsoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_for_console_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeApisForConsoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeApisForConsoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisForConsole',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeApisForConsoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_for_console(
        self,
        request: cloud_api20160701_models.DescribeApisForConsoleRequest,
    ) -> cloud_api20160701_models.DescribeApisForConsoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_for_console_with_options(request, runtime)

    async def describe_apis_for_console_async(
        self,
        request: cloud_api20160701_models.DescribeApisForConsoleRequest,
    ) -> cloud_api20160701_models.DescribeApisForConsoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_for_console_with_options_async(request, runtime)

    def describe_app_with_options(
        self,
        request: cloud_api20160701_models.DescribeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app(
        self,
        request: cloud_api20160701_models.DescribeAppRequest,
    ) -> cloud_api20160701_models.DescribeAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_with_options(request, runtime)

    async def describe_app_async(
        self,
        request: cloud_api20160701_models.DescribeAppRequest,
    ) -> cloud_api20160701_models.DescribeAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_with_options_async(request, runtime)

    def describe_app_securities_with_options(
        self,
        request: cloud_api20160701_models.DescribeAppSecuritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppSecuritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurities',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppSecuritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_securities_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeAppSecuritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppSecuritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurities',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppSecuritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_securities(
        self,
        request: cloud_api20160701_models.DescribeAppSecuritiesRequest,
    ) -> cloud_api20160701_models.DescribeAppSecuritiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_securities_with_options(request, runtime)

    async def describe_app_securities_async(
        self,
        request: cloud_api20160701_models.DescribeAppSecuritiesRequest,
    ) -> cloud_api20160701_models.DescribeAppSecuritiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_securities_with_options_async(request, runtime)

    def describe_app_security_with_options(
        self,
        request: cloud_api20160701_models.DescribeAppSecurityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppSecurityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurity',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppSecurityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_security_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeAppSecurityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppSecurityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurity',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppSecurityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_security(
        self,
        request: cloud_api20160701_models.DescribeAppSecurityRequest,
    ) -> cloud_api20160701_models.DescribeAppSecurityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_security_with_options(request, runtime)

    async def describe_app_security_async(
        self,
        request: cloud_api20160701_models.DescribeAppSecurityRequest,
    ) -> cloud_api20160701_models.DescribeAppSecurityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_security_with_options_async(request, runtime)

    def describe_apps_with_options(
        self,
        request: cloud_api20160701_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps(
        self,
        request: cloud_api20160701_models.DescribeAppsRequest,
    ) -> cloud_api20160701_models.DescribeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    async def describe_apps_async(
        self,
        request: cloud_api20160701_models.DescribeAppsRequest,
    ) -> cloud_api20160701_models.DescribeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apps_with_options_async(request, runtime)

    def describe_apps_by_api_with_options(
        self,
        request: cloud_api20160701_models.DescribeAppsByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppsByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_owner_id):
            query['AppOwnerId'] = request.app_owner_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppsByApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppsByApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_by_api_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeAppsByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppsByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_owner_id):
            query['AppOwnerId'] = request.app_owner_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppsByApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppsByApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps_by_api(
        self,
        request: cloud_api20160701_models.DescribeAppsByApiRequest,
    ) -> cloud_api20160701_models.DescribeAppsByApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_by_api_with_options(request, runtime)

    async def describe_apps_by_api_async(
        self,
        request: cloud_api20160701_models.DescribeAppsByApiRequest,
    ) -> cloud_api20160701_models.DescribeAppsByApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apps_by_api_with_options_async(request, runtime)

    def describe_apps_for_provider_with_options(
        self,
        request: cloud_api20160701_models.DescribeAppsForProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppsForProviderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_owner_id):
            query['AppOwnerId'] = request.app_owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppsForProvider',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppsForProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_for_provider_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeAppsForProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeAppsForProviderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_owner_id):
            query['AppOwnerId'] = request.app_owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppsForProvider',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeAppsForProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps_for_provider(
        self,
        request: cloud_api20160701_models.DescribeAppsForProviderRequest,
    ) -> cloud_api20160701_models.DescribeAppsForProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_for_provider_with_options(request, runtime)

    async def describe_apps_for_provider_async(
        self,
        request: cloud_api20160701_models.DescribeAppsForProviderRequest,
    ) -> cloud_api20160701_models.DescribeAppsForProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apps_for_provider_with_options_async(request, runtime)

    def describe_black_lists_with_options(
        self,
        request: cloud_api20160701_models.DescribeBlackListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeBlackListsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlackLists',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeBlackListsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_black_lists_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeBlackListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeBlackListsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlackLists',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeBlackListsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_black_lists(
        self,
        request: cloud_api20160701_models.DescribeBlackListsRequest,
    ) -> cloud_api20160701_models.DescribeBlackListsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_black_lists_with_options(request, runtime)

    async def describe_black_lists_async(
        self,
        request: cloud_api20160701_models.DescribeBlackListsRequest,
    ) -> cloud_api20160701_models.DescribeBlackListsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_black_lists_with_options_async(request, runtime)

    def describe_deployed_api_with_options(
        self,
        request: cloud_api20160701_models.DescribeDeployedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeDeployedApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeDeployedApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployed_api_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeDeployedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeDeployedApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeDeployedApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployed_api(
        self,
        request: cloud_api20160701_models.DescribeDeployedApiRequest,
    ) -> cloud_api20160701_models.DescribeDeployedApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deployed_api_with_options(request, runtime)

    async def describe_deployed_api_async(
        self,
        request: cloud_api20160701_models.DescribeDeployedApiRequest,
    ) -> cloud_api20160701_models.DescribeDeployedApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deployed_api_with_options_async(request, runtime)

    def describe_deployed_apis_with_options(
        self,
        request: cloud_api20160701_models.DescribeDeployedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeDeployedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeDeployedApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployed_apis_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeDeployedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeDeployedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeDeployedApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployed_apis(
        self,
        request: cloud_api20160701_models.DescribeDeployedApisRequest,
    ) -> cloud_api20160701_models.DescribeDeployedApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deployed_apis_with_options(request, runtime)

    async def describe_deployed_apis_async(
        self,
        request: cloud_api20160701_models.DescribeDeployedApisRequest,
    ) -> cloud_api20160701_models.DescribeDeployedApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deployed_apis_with_options_async(request, runtime)

    def describe_domain_with_options(
        self,
        request: cloud_api20160701_models.DescribeDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain(
        self,
        request: cloud_api20160701_models.DescribeDomainRequest,
    ) -> cloud_api20160701_models.DescribeDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_options(request, runtime)

    async def describe_domain_async(
        self,
        request: cloud_api20160701_models.DescribeDomainRequest,
    ) -> cloud_api20160701_models.DescribeDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_with_options_async(request, runtime)

    def describe_domain_resolution_with_options(
        self,
        request: cloud_api20160701_models.DescribeDomainResolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeDomainResolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResolution',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeDomainResolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_resolution_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeDomainResolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeDomainResolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResolution',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeDomainResolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_resolution(
        self,
        request: cloud_api20160701_models.DescribeDomainResolutionRequest,
    ) -> cloud_api20160701_models.DescribeDomainResolutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_resolution_with_options(request, runtime)

    async def describe_domain_resolution_async(
        self,
        request: cloud_api20160701_models.DescribeDomainResolutionRequest,
    ) -> cloud_api20160701_models.DescribeDomainResolutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_resolution_with_options_async(request, runtime)

    def describe_history_api_with_options(
        self,
        request: cloud_api20160701_models.DescribeHistoryApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeHistoryApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeHistoryApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_api_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeHistoryApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeHistoryApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeHistoryApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_api(
        self,
        request: cloud_api20160701_models.DescribeHistoryApiRequest,
    ) -> cloud_api20160701_models.DescribeHistoryApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_history_api_with_options(request, runtime)

    async def describe_history_api_async(
        self,
        request: cloud_api20160701_models.DescribeHistoryApiRequest,
    ) -> cloud_api20160701_models.DescribeHistoryApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_api_with_options_async(request, runtime)

    def describe_history_apis_with_options(
        self,
        request: cloud_api20160701_models.DescribeHistoryApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeHistoryApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeHistoryApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_apis_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeHistoryApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeHistoryApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeHistoryApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_apis(
        self,
        request: cloud_api20160701_models.DescribeHistoryApisRequest,
    ) -> cloud_api20160701_models.DescribeHistoryApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_history_apis_with_options(request, runtime)

    async def describe_history_apis_async(
        self,
        request: cloud_api20160701_models.DescribeHistoryApisRequest,
    ) -> cloud_api20160701_models.DescribeHistoryApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_apis_with_options_async(request, runtime)

    def describe_ip_control_policy_items_with_options(
        self,
        request: cloud_api20160701_models.DescribeIpControlPolicyItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeIpControlPolicyItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_item_id):
            query['PolicyItemId'] = request.policy_item_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpControlPolicyItems',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeIpControlPolicyItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_control_policy_items_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeIpControlPolicyItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeIpControlPolicyItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_item_id):
            query['PolicyItemId'] = request.policy_item_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpControlPolicyItems',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeIpControlPolicyItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_control_policy_items(
        self,
        request: cloud_api20160701_models.DescribeIpControlPolicyItemsRequest,
    ) -> cloud_api20160701_models.DescribeIpControlPolicyItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_control_policy_items_with_options(request, runtime)

    async def describe_ip_control_policy_items_async(
        self,
        request: cloud_api20160701_models.DescribeIpControlPolicyItemsRequest,
    ) -> cloud_api20160701_models.DescribeIpControlPolicyItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_control_policy_items_with_options_async(request, runtime)

    def describe_ip_controls_with_options(
        self,
        request: cloud_api20160701_models.DescribeIpControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeIpControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not UtilClient.is_unset(request.ip_control_type):
            query['IpControlType'] = request.ip_control_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpControls',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeIpControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_controls_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeIpControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeIpControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not UtilClient.is_unset(request.ip_control_type):
            query['IpControlType'] = request.ip_control_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpControls',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeIpControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_controls(
        self,
        request: cloud_api20160701_models.DescribeIpControlsRequest,
    ) -> cloud_api20160701_models.DescribeIpControlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_controls_with_options(request, runtime)

    async def describe_ip_controls_async(
        self,
        request: cloud_api20160701_models.DescribeIpControlsRequest,
    ) -> cloud_api20160701_models.DescribeIpControlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_controls_with_options_async(request, runtime)

    def describe_log_config_with_options(
        self,
        request: cloud_api20160701_models.DescribeLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogConfig',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_config_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogConfig',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_config(
        self,
        request: cloud_api20160701_models.DescribeLogConfigRequest,
    ) -> cloud_api20160701_models.DescribeLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_config_with_options(request, runtime)

    async def describe_log_config_async(
        self,
        request: cloud_api20160701_models.DescribeLogConfigRequest,
    ) -> cloud_api20160701_models.DescribeLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_config_with_options_async(request, runtime)

    def describe_purchased_api_with_options(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribePurchasedApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribePurchasedApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_api_with_options_async(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribePurchasedApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribePurchasedApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_api(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiRequest,
    ) -> cloud_api20160701_models.DescribePurchasedApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_with_options(request, runtime)

    async def describe_purchased_api_async(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiRequest,
    ) -> cloud_api20160701_models.DescribePurchasedApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_api_with_options_async(request, runtime)

    def describe_purchased_api_group_detail_with_options(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribePurchasedApiGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroupDetail',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribePurchasedApiGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_api_group_detail_with_options_async(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribePurchasedApiGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroupDetail',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribePurchasedApiGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_api_group_detail(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiGroupDetailRequest,
    ) -> cloud_api20160701_models.DescribePurchasedApiGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_group_detail_with_options(request, runtime)

    async def describe_purchased_api_group_detail_async(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiGroupDetailRequest,
    ) -> cloud_api20160701_models.DescribePurchasedApiGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_api_group_detail_with_options_async(request, runtime)

    def describe_purchased_api_groups_with_options(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribePurchasedApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroups',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribePurchasedApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_api_groups_with_options_async(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribePurchasedApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroups',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribePurchasedApiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_api_groups(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiGroupsRequest,
    ) -> cloud_api20160701_models.DescribePurchasedApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_groups_with_options(request, runtime)

    async def describe_purchased_api_groups_async(
        self,
        request: cloud_api20160701_models.DescribePurchasedApiGroupsRequest,
    ) -> cloud_api20160701_models.DescribePurchasedApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_api_groups_with_options_async(request, runtime)

    def describe_purchased_apis_with_options(
        self,
        request: cloud_api20160701_models.DescribePurchasedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribePurchasedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribePurchasedApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_apis_with_options_async(
        self,
        request: cloud_api20160701_models.DescribePurchasedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribePurchasedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribePurchasedApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_apis(
        self,
        request: cloud_api20160701_models.DescribePurchasedApisRequest,
    ) -> cloud_api20160701_models.DescribePurchasedApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_apis_with_options(request, runtime)

    async def describe_purchased_apis_async(
        self,
        request: cloud_api20160701_models.DescribePurchasedApisRequest,
    ) -> cloud_api20160701_models.DescribePurchasedApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_apis_with_options_async(request, runtime)

    def describe_race_work_for_inner_with_options(
        self,
        request: cloud_api20160701_models.DescribeRaceWorkForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeRaceWorkForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRaceWorkForInner',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeRaceWorkForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_race_work_for_inner_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeRaceWorkForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeRaceWorkForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRaceWorkForInner',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeRaceWorkForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_race_work_for_inner(
        self,
        request: cloud_api20160701_models.DescribeRaceWorkForInnerRequest,
    ) -> cloud_api20160701_models.DescribeRaceWorkForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_race_work_for_inner_with_options(request, runtime)

    async def describe_race_work_for_inner_async(
        self,
        request: cloud_api20160701_models.DescribeRaceWorkForInnerRequest,
    ) -> cloud_api20160701_models.DescribeRaceWorkForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_race_work_for_inner_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: cloud_api20160701_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: cloud_api20160701_models.DescribeRegionsRequest,
    ) -> cloud_api20160701_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: cloud_api20160701_models.DescribeRegionsRequest,
    ) -> cloud_api20160701_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_rules_by_api_with_options(
        self,
        request: cloud_api20160701_models.DescribeRulesByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeRulesByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRulesByApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeRulesByApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rules_by_api_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeRulesByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeRulesByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRulesByApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeRulesByApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rules_by_api(
        self,
        request: cloud_api20160701_models.DescribeRulesByApiRequest,
    ) -> cloud_api20160701_models.DescribeRulesByApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rules_by_api_with_options(request, runtime)

    async def describe_rules_by_api_async(
        self,
        request: cloud_api20160701_models.DescribeRulesByApiRequest,
    ) -> cloud_api20160701_models.DescribeRulesByApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rules_by_api_with_options_async(request, runtime)

    def describe_secret_keys_with_options(
        self,
        request: cloud_api20160701_models.DescribeSecretKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeSecretKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecretKeys',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeSecretKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_secret_keys_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeSecretKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeSecretKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecretKeys',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeSecretKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_secret_keys(
        self,
        request: cloud_api20160701_models.DescribeSecretKeysRequest,
    ) -> cloud_api20160701_models.DescribeSecretKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_secret_keys_with_options(request, runtime)

    async def describe_secret_keys_async(
        self,
        request: cloud_api20160701_models.DescribeSecretKeysRequest,
    ) -> cloud_api20160701_models.DescribeSecretKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_secret_keys_with_options_async(request, runtime)

    def describe_system_parameters_with_options(
        self,
        request: cloud_api20160701_models.DescribeSystemParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeSystemParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemParameters',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeSystemParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_parameters_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeSystemParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeSystemParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemParameters',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeSystemParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_parameters(
        self,
        request: cloud_api20160701_models.DescribeSystemParametersRequest,
    ) -> cloud_api20160701_models.DescribeSystemParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_system_parameters_with_options(request, runtime)

    async def describe_system_parameters_async(
        self,
        request: cloud_api20160701_models.DescribeSystemParametersRequest,
    ) -> cloud_api20160701_models.DescribeSystemParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_parameters_with_options_async(request, runtime)

    def describe_system_params_with_options(
        self,
        request: cloud_api20160701_models.DescribeSystemParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeSystemParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemParams',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeSystemParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_params_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeSystemParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeSystemParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemParams',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeSystemParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_params(
        self,
        request: cloud_api20160701_models.DescribeSystemParamsRequest,
    ) -> cloud_api20160701_models.DescribeSystemParamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_system_params_with_options(request, runtime)

    async def describe_system_params_async(
        self,
        request: cloud_api20160701_models.DescribeSystemParamsRequest,
    ) -> cloud_api20160701_models.DescribeSystemParamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_params_with_options_async(request, runtime)

    def describe_traffic_controls_with_options(
        self,
        request: cloud_api20160701_models.DescribeTrafficControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeTrafficControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControls',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeTrafficControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_traffic_controls_with_options_async(
        self,
        request: cloud_api20160701_models.DescribeTrafficControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.DescribeTrafficControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControls',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.DescribeTrafficControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_traffic_controls(
        self,
        request: cloud_api20160701_models.DescribeTrafficControlsRequest,
    ) -> cloud_api20160701_models.DescribeTrafficControlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_controls_with_options(request, runtime)

    async def describe_traffic_controls_async(
        self,
        request: cloud_api20160701_models.DescribeTrafficControlsRequest,
    ) -> cloud_api20160701_models.DescribeTrafficControlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_traffic_controls_with_options_async(request, runtime)

    def export_swagger_with_options(
        self,
        request: cloud_api20160701_models.ExportSwaggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ExportSwaggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not UtilClient.is_unset(request.data_format):
            query['DataFormat'] = request.data_format
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportSwagger',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ExportSwaggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_swagger_with_options_async(
        self,
        request: cloud_api20160701_models.ExportSwaggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ExportSwaggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not UtilClient.is_unset(request.data_format):
            query['DataFormat'] = request.data_format
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportSwagger',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ExportSwaggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_swagger(
        self,
        request: cloud_api20160701_models.ExportSwaggerRequest,
    ) -> cloud_api20160701_models.ExportSwaggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_swagger_with_options(request, runtime)

    async def export_swagger_async(
        self,
        request: cloud_api20160701_models.ExportSwaggerRequest,
    ) -> cloud_api20160701_models.ExportSwaggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_swagger_with_options_async(request, runtime)

    def get_api_methods_with_options(
        self,
        request: cloud_api20160701_models.GetApiMethodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.GetApiMethodsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_path):
            query['ApiPath'] = request.api_path
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiMethods',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.GetApiMethodsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_methods_with_options_async(
        self,
        request: cloud_api20160701_models.GetApiMethodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.GetApiMethodsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_path):
            query['ApiPath'] = request.api_path
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiMethods',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.GetApiMethodsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_methods(
        self,
        request: cloud_api20160701_models.GetApiMethodsRequest,
    ) -> cloud_api20160701_models.GetApiMethodsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_api_methods_with_options(request, runtime)

    async def get_api_methods_async(
        self,
        request: cloud_api20160701_models.GetApiMethodsRequest,
    ) -> cloud_api20160701_models.GetApiMethodsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_api_methods_with_options_async(request, runtime)

    def get_customized_info_with_options(
        self,
        request: cloud_api20160701_models.GetCustomizedInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.GetCustomizedInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomizedInfo',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.GetCustomizedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customized_info_with_options_async(
        self,
        request: cloud_api20160701_models.GetCustomizedInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.GetCustomizedInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomizedInfo',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.GetCustomizedInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customized_info(
        self,
        request: cloud_api20160701_models.GetCustomizedInfoRequest,
    ) -> cloud_api20160701_models.GetCustomizedInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_customized_info_with_options(request, runtime)

    async def get_customized_info_async(
        self,
        request: cloud_api20160701_models.GetCustomizedInfoRequest,
    ) -> cloud_api20160701_models.GetCustomizedInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_customized_info_with_options_async(request, runtime)

    def import_swagger_with_options(
        self,
        request: cloud_api20160701_models.ImportSwaggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ImportSwaggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_format):
            query['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportSwagger',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ImportSwaggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_swagger_with_options_async(
        self,
        request: cloud_api20160701_models.ImportSwaggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ImportSwaggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_format):
            query['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportSwagger',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ImportSwaggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_swagger(
        self,
        request: cloud_api20160701_models.ImportSwaggerRequest,
    ) -> cloud_api20160701_models.ImportSwaggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_swagger_with_options(request, runtime)

    async def import_swagger_async(
        self,
        request: cloud_api20160701_models.ImportSwaggerRequest,
    ) -> cloud_api20160701_models.ImportSwaggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_swagger_with_options_async(request, runtime)

    def modify_api_with_options(
        self,
        request: cloud_api20160701_models.ModifyApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not UtilClient.is_unset(request.error_code_samples):
            query['ErrorCodeSamples'] = request.error_code_samples
        if not UtilClient.is_unset(request.fail_result_sample):
            query['FailResultSample'] = request.fail_result_sample
        if not UtilClient.is_unset(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.open_id_connect_config):
            query['OpenIdConnectConfig'] = request.open_id_connect_config
        if not UtilClient.is_unset(request.request_config):
            query['RequestConfig'] = request.request_config
        if not UtilClient.is_unset(request.request_paramters):
            query['RequestParamters'] = request.request_paramters
        if not UtilClient.is_unset(request.result_body_model):
            query['ResultBodyModel'] = request.result_body_model
        if not UtilClient.is_unset(request.result_descriptions):
            query['ResultDescriptions'] = request.result_descriptions
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not UtilClient.is_unset(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        if not UtilClient.is_unset(request.web_socket_api_type):
            query['WebSocketApiType'] = request.web_socket_api_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_with_options_async(
        self,
        request: cloud_api20160701_models.ModifyApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not UtilClient.is_unset(request.error_code_samples):
            query['ErrorCodeSamples'] = request.error_code_samples
        if not UtilClient.is_unset(request.fail_result_sample):
            query['FailResultSample'] = request.fail_result_sample
        if not UtilClient.is_unset(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.open_id_connect_config):
            query['OpenIdConnectConfig'] = request.open_id_connect_config
        if not UtilClient.is_unset(request.request_config):
            query['RequestConfig'] = request.request_config
        if not UtilClient.is_unset(request.request_paramters):
            query['RequestParamters'] = request.request_paramters
        if not UtilClient.is_unset(request.result_body_model):
            query['ResultBodyModel'] = request.result_body_model
        if not UtilClient.is_unset(request.result_descriptions):
            query['ResultDescriptions'] = request.result_descriptions
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not UtilClient.is_unset(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        if not UtilClient.is_unset(request.web_socket_api_type):
            query['WebSocketApiType'] = request.web_socket_api_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api(
        self,
        request: cloud_api20160701_models.ModifyApiRequest,
    ) -> cloud_api20160701_models.ModifyApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_api_with_options(request, runtime)

    async def modify_api_async(
        self,
        request: cloud_api20160701_models.ModifyApiRequest,
    ) -> cloud_api20160701_models.ModifyApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_with_options_async(request, runtime)

    def modify_api_group_with_options(
        self,
        request: cloud_api20160701_models.ModifyApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compatible_flags):
            query['CompatibleFlags'] = request.compatible_flags
        if not UtilClient.is_unset(request.custom_trace_config):
            query['CustomTraceConfig'] = request.custom_trace_config
        if not UtilClient.is_unset(request.default_domain):
            query['DefaultDomain'] = request.default_domain
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.passthrough_headers):
            query['PassthroughHeaders'] = request.passthrough_headers
        if not UtilClient.is_unset(request.rpc_pattern):
            query['RpcPattern'] = request.rpc_pattern
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.user_log_config):
            query['UserLogConfig'] = request.user_log_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiGroup',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_group_with_options_async(
        self,
        request: cloud_api20160701_models.ModifyApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compatible_flags):
            query['CompatibleFlags'] = request.compatible_flags
        if not UtilClient.is_unset(request.custom_trace_config):
            query['CustomTraceConfig'] = request.custom_trace_config
        if not UtilClient.is_unset(request.default_domain):
            query['DefaultDomain'] = request.default_domain
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.passthrough_headers):
            query['PassthroughHeaders'] = request.passthrough_headers
        if not UtilClient.is_unset(request.rpc_pattern):
            query['RpcPattern'] = request.rpc_pattern
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.user_log_config):
            query['UserLogConfig'] = request.user_log_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiGroup',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_group(
        self,
        request: cloud_api20160701_models.ModifyApiGroupRequest,
    ) -> cloud_api20160701_models.ModifyApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_api_group_with_options(request, runtime)

    async def modify_api_group_async(
        self,
        request: cloud_api20160701_models.ModifyApiGroupRequest,
    ) -> cloud_api20160701_models.ModifyApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_group_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: cloud_api20160701_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: cloud_api20160701_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        request: cloud_api20160701_models.ModifyAppRequest,
    ) -> cloud_api20160701_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: cloud_api20160701_models.ModifyAppRequest,
    ) -> cloud_api20160701_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: cloud_api20160701_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.https_policy):
            query['HttpsPolicy'] = request.https_policy
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: cloud_api20160701_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.https_policy):
            query['HttpsPolicy'] = request.https_policy
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: cloud_api20160701_models.ModifyInstanceAttributeRequest,
    ) -> cloud_api20160701_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: cloud_api20160701_models.ModifyInstanceAttributeRequest,
    ) -> cloud_api20160701_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_instance_vpc_attribute_with_options(
        self,
        request: cloud_api20160701_models.ModifyInstanceVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyInstanceVpcAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVpcAttribute',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyInstanceVpcAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_vpc_attribute_with_options_async(
        self,
        request: cloud_api20160701_models.ModifyInstanceVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyInstanceVpcAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVpcAttribute',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyInstanceVpcAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_vpc_attribute(
        self,
        request: cloud_api20160701_models.ModifyInstanceVpcAttributeRequest,
    ) -> cloud_api20160701_models.ModifyInstanceVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_attribute_with_options(request, runtime)

    async def modify_instance_vpc_attribute_async(
        self,
        request: cloud_api20160701_models.ModifyInstanceVpcAttributeRequest,
    ) -> cloud_api20160701_models.ModifyInstanceVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vpc_attribute_with_options_async(request, runtime)

    def modify_ip_control_with_options(
        self,
        request: cloud_api20160701_models.ModifyIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ip_control_with_options_async(
        self,
        request: cloud_api20160701_models.ModifyIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ip_control(
        self,
        request: cloud_api20160701_models.ModifyIpControlRequest,
    ) -> cloud_api20160701_models.ModifyIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_control_with_options(request, runtime)

    async def modify_ip_control_async(
        self,
        request: cloud_api20160701_models.ModifyIpControlRequest,
    ) -> cloud_api20160701_models.ModifyIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ip_control_with_options_async(request, runtime)

    def modify_ip_control_policy_item_with_options(
        self,
        request: cloud_api20160701_models.ModifyIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cidr_ip):
            query['CidrIp'] = request.cidr_ip
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.policy_item_id):
            query['PolicyItemId'] = request.policy_item_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpControlPolicyItem',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ip_control_policy_item_with_options_async(
        self,
        request: cloud_api20160701_models.ModifyIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cidr_ip):
            query['CidrIp'] = request.cidr_ip
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.policy_item_id):
            query['PolicyItemId'] = request.policy_item_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpControlPolicyItem',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyIpControlPolicyItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ip_control_policy_item(
        self,
        request: cloud_api20160701_models.ModifyIpControlPolicyItemRequest,
    ) -> cloud_api20160701_models.ModifyIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_control_policy_item_with_options(request, runtime)

    async def modify_ip_control_policy_item_async(
        self,
        request: cloud_api20160701_models.ModifyIpControlPolicyItemRequest,
    ) -> cloud_api20160701_models.ModifyIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ip_control_policy_item_with_options_async(request, runtime)

    def modify_log_config_with_options(
        self,
        request: cloud_api20160701_models.ModifyLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogConfig',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_log_config_with_options_async(
        self,
        request: cloud_api20160701_models.ModifyLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogConfig',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_log_config(
        self,
        request: cloud_api20160701_models.ModifyLogConfigRequest,
    ) -> cloud_api20160701_models.ModifyLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_log_config_with_options(request, runtime)

    async def modify_log_config_async(
        self,
        request: cloud_api20160701_models.ModifyLogConfigRequest,
    ) -> cloud_api20160701_models.ModifyLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_log_config_with_options_async(request, runtime)

    def modify_secret_key_with_options(
        self,
        request: cloud_api20160701_models.ModifySecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifySecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        if not UtilClient.is_unset(request.secret_value):
            query['SecretValue'] = request.secret_value
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecretKey',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifySecretKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_secret_key_with_options_async(
        self,
        request: cloud_api20160701_models.ModifySecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifySecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        if not UtilClient.is_unset(request.secret_value):
            query['SecretValue'] = request.secret_value
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecretKey',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifySecretKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_secret_key(
        self,
        request: cloud_api20160701_models.ModifySecretKeyRequest,
    ) -> cloud_api20160701_models.ModifySecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_secret_key_with_options(request, runtime)

    async def modify_secret_key_async(
        self,
        request: cloud_api20160701_models.ModifySecretKeyRequest,
    ) -> cloud_api20160701_models.ModifySecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_secret_key_with_options_async(request, runtime)

    def modify_traffic_control_with_options(
        self,
        request: cloud_api20160701_models.ModifyTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_default):
            query['ApiDefault'] = request.api_default
        if not UtilClient.is_unset(request.app_default):
            query['AppDefault'] = request.app_default
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not UtilClient.is_unset(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not UtilClient.is_unset(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTrafficControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_traffic_control_with_options_async(
        self,
        request: cloud_api20160701_models.ModifyTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ModifyTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_default):
            query['ApiDefault'] = request.api_default
        if not UtilClient.is_unset(request.app_default):
            query['AppDefault'] = request.app_default
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not UtilClient.is_unset(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not UtilClient.is_unset(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTrafficControl',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ModifyTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_traffic_control(
        self,
        request: cloud_api20160701_models.ModifyTrafficControlRequest,
    ) -> cloud_api20160701_models.ModifyTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_traffic_control_with_options(request, runtime)

    async def modify_traffic_control_async(
        self,
        request: cloud_api20160701_models.ModifyTrafficControlRequest,
    ) -> cloud_api20160701_models.ModifyTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_traffic_control_with_options_async(request, runtime)

    def reactivate_domain_with_options(
        self,
        request: cloud_api20160701_models.ReactivateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ReactivateDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReactivateDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ReactivateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def reactivate_domain_with_options_async(
        self,
        request: cloud_api20160701_models.ReactivateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ReactivateDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReactivateDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ReactivateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reactivate_domain(
        self,
        request: cloud_api20160701_models.ReactivateDomainRequest,
    ) -> cloud_api20160701_models.ReactivateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.reactivate_domain_with_options(request, runtime)

    async def reactivate_domain_async(
        self,
        request: cloud_api20160701_models.ReactivateDomainRequest,
    ) -> cloud_api20160701_models.ReactivateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reactivate_domain_with_options_async(request, runtime)

    def recover_api_from_historical_with_options(
        self,
        request: cloud_api20160701_models.RecoverApiFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RecoverApiFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverApiFromHistorical',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RecoverApiFromHistoricalResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_api_from_historical_with_options_async(
        self,
        request: cloud_api20160701_models.RecoverApiFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RecoverApiFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverApiFromHistorical',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RecoverApiFromHistoricalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_api_from_historical(
        self,
        request: cloud_api20160701_models.RecoverApiFromHistoricalRequest,
    ) -> cloud_api20160701_models.RecoverApiFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return self.recover_api_from_historical_with_options(request, runtime)

    async def recover_api_from_historical_async(
        self,
        request: cloud_api20160701_models.RecoverApiFromHistoricalRequest,
    ) -> cloud_api20160701_models.RecoverApiFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recover_api_from_historical_with_options_async(request, runtime)

    def recovery_api_define_from_historical_with_options(
        self,
        request: cloud_api20160701_models.RecoveryApiDefineFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RecoveryApiDefineFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryApiDefineFromHistorical',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RecoveryApiDefineFromHistoricalResponse(),
            self.call_api(params, req, runtime)
        )

    async def recovery_api_define_from_historical_with_options_async(
        self,
        request: cloud_api20160701_models.RecoveryApiDefineFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RecoveryApiDefineFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryApiDefineFromHistorical',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RecoveryApiDefineFromHistoricalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recovery_api_define_from_historical(
        self,
        request: cloud_api20160701_models.RecoveryApiDefineFromHistoricalRequest,
    ) -> cloud_api20160701_models.RecoveryApiDefineFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return self.recovery_api_define_from_historical_with_options(request, runtime)

    async def recovery_api_define_from_historical_async(
        self,
        request: cloud_api20160701_models.RecoveryApiDefineFromHistoricalRequest,
    ) -> cloud_api20160701_models.RecoveryApiDefineFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recovery_api_define_from_historical_with_options_async(request, runtime)

    def recovery_api_from_historical_with_options(
        self,
        request: cloud_api20160701_models.RecoveryApiFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RecoveryApiFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryApiFromHistorical',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RecoveryApiFromHistoricalResponse(),
            self.call_api(params, req, runtime)
        )

    async def recovery_api_from_historical_with_options_async(
        self,
        request: cloud_api20160701_models.RecoveryApiFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RecoveryApiFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryApiFromHistorical',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RecoveryApiFromHistoricalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recovery_api_from_historical(
        self,
        request: cloud_api20160701_models.RecoveryApiFromHistoricalRequest,
    ) -> cloud_api20160701_models.RecoveryApiFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return self.recovery_api_from_historical_with_options(request, runtime)

    async def recovery_api_from_historical_async(
        self,
        request: cloud_api20160701_models.RecoveryApiFromHistoricalRequest,
    ) -> cloud_api20160701_models.RecoveryApiFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recovery_api_from_historical_with_options_async(request, runtime)

    def refresh_domain_with_options(
        self,
        request: cloud_api20160701_models.RefreshDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RefreshDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RefreshDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_domain_with_options_async(
        self,
        request: cloud_api20160701_models.RefreshDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RefreshDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RefreshDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_domain(
        self,
        request: cloud_api20160701_models.RefreshDomainRequest,
    ) -> cloud_api20160701_models.RefreshDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_domain_with_options(request, runtime)

    async def refresh_domain_async(
        self,
        request: cloud_api20160701_models.RefreshDomainRequest,
    ) -> cloud_api20160701_models.RefreshDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_domain_with_options_async(request, runtime)

    def remove_access_permission_by_apis_with_options(
        self,
        request: cloud_api20160701_models.RemoveAccessPermissionByApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveAccessPermissionByApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessPermissionByApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveAccessPermissionByApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_access_permission_by_apis_with_options_async(
        self,
        request: cloud_api20160701_models.RemoveAccessPermissionByApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveAccessPermissionByApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessPermissionByApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveAccessPermissionByApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_access_permission_by_apis(
        self,
        request: cloud_api20160701_models.RemoveAccessPermissionByApisRequest,
    ) -> cloud_api20160701_models.RemoveAccessPermissionByApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_access_permission_by_apis_with_options(request, runtime)

    async def remove_access_permission_by_apis_async(
        self,
        request: cloud_api20160701_models.RemoveAccessPermissionByApisRequest,
    ) -> cloud_api20160701_models.RemoveAccessPermissionByApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_access_permission_by_apis_with_options_async(request, runtime)

    def remove_access_permission_by_apps_with_options(
        self,
        request: cloud_api20160701_models.RemoveAccessPermissionByAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveAccessPermissionByAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessPermissionByApps',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveAccessPermissionByAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_access_permission_by_apps_with_options_async(
        self,
        request: cloud_api20160701_models.RemoveAccessPermissionByAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveAccessPermissionByAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessPermissionByApps',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveAccessPermissionByAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_access_permission_by_apps(
        self,
        request: cloud_api20160701_models.RemoveAccessPermissionByAppsRequest,
    ) -> cloud_api20160701_models.RemoveAccessPermissionByAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_access_permission_by_apps_with_options(request, runtime)

    async def remove_access_permission_by_apps_async(
        self,
        request: cloud_api20160701_models.RemoveAccessPermissionByAppsRequest,
    ) -> cloud_api20160701_models.RemoveAccessPermissionByAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_access_permission_by_apps_with_options_async(request, runtime)

    def remove_all_black_list_with_options(
        self,
        request: cloud_api20160701_models.RemoveAllBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveAllBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAllBlackList',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveAllBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_all_black_list_with_options_async(
        self,
        request: cloud_api20160701_models.RemoveAllBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveAllBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAllBlackList',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveAllBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_all_black_list(
        self,
        request: cloud_api20160701_models.RemoveAllBlackListRequest,
    ) -> cloud_api20160701_models.RemoveAllBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_all_black_list_with_options(request, runtime)

    async def remove_all_black_list_async(
        self,
        request: cloud_api20160701_models.RemoveAllBlackListRequest,
    ) -> cloud_api20160701_models.RemoveAllBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_all_black_list_with_options_async(request, runtime)

    def remove_api_rule_with_options(
        self,
        request: cloud_api20160701_models.RemoveApiRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveApiRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveApiRule',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveApiRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_api_rule_with_options_async(
        self,
        request: cloud_api20160701_models.RemoveApiRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveApiRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveApiRule',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveApiRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_api_rule(
        self,
        request: cloud_api20160701_models.RemoveApiRuleRequest,
    ) -> cloud_api20160701_models.RemoveApiRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_api_rule_with_options(request, runtime)

    async def remove_api_rule_async(
        self,
        request: cloud_api20160701_models.RemoveApiRuleRequest,
    ) -> cloud_api20160701_models.RemoveApiRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_api_rule_with_options_async(request, runtime)

    def remove_black_list_with_options(
        self,
        request: cloud_api20160701_models.RemoveBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_content):
            query['BlackContent'] = request.black_content
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBlackList',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_black_list_with_options_async(
        self,
        request: cloud_api20160701_models.RemoveBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_content):
            query['BlackContent'] = request.black_content
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBlackList',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_black_list(
        self,
        request: cloud_api20160701_models.RemoveBlackListRequest,
    ) -> cloud_api20160701_models.RemoveBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_black_list_with_options(request, runtime)

    async def remove_black_list_async(
        self,
        request: cloud_api20160701_models.RemoveBlackListRequest,
    ) -> cloud_api20160701_models.RemoveBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_black_list_with_options_async(request, runtime)

    def remove_ip_control_apis_with_options(
        self,
        request: cloud_api20160701_models.RemoveIpControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveIpControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveIpControlApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveIpControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_ip_control_apis_with_options_async(
        self,
        request: cloud_api20160701_models.RemoveIpControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveIpControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveIpControlApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveIpControlApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_ip_control_apis(
        self,
        request: cloud_api20160701_models.RemoveIpControlApisRequest,
    ) -> cloud_api20160701_models.RemoveIpControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_ip_control_apis_with_options(request, runtime)

    async def remove_ip_control_apis_async(
        self,
        request: cloud_api20160701_models.RemoveIpControlApisRequest,
    ) -> cloud_api20160701_models.RemoveIpControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_ip_control_apis_with_options_async(request, runtime)

    def remove_ip_control_policy_item_with_options(
        self,
        request: cloud_api20160701_models.RemoveIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.policy_item_ids):
            query['PolicyItemIds'] = request.policy_item_ids
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveIpControlPolicyItem',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_ip_control_policy_item_with_options_async(
        self,
        request: cloud_api20160701_models.RemoveIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.RemoveIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.policy_item_ids):
            query['PolicyItemIds'] = request.policy_item_ids
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveIpControlPolicyItem',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.RemoveIpControlPolicyItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_ip_control_policy_item(
        self,
        request: cloud_api20160701_models.RemoveIpControlPolicyItemRequest,
    ) -> cloud_api20160701_models.RemoveIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_ip_control_policy_item_with_options(request, runtime)

    async def remove_ip_control_policy_item_async(
        self,
        request: cloud_api20160701_models.RemoveIpControlPolicyItemRequest,
    ) -> cloud_api20160701_models.RemoveIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_ip_control_policy_item_with_options_async(request, runtime)

    def reset_app_key_secret_with_options(
        self,
        request: cloud_api20160701_models.ResetAppKeySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ResetAppKeySecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppKeySecret',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ResetAppKeySecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_app_key_secret_with_options_async(
        self,
        request: cloud_api20160701_models.ResetAppKeySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ResetAppKeySecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppKeySecret',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ResetAppKeySecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_app_key_secret(
        self,
        request: cloud_api20160701_models.ResetAppKeySecretRequest,
    ) -> cloud_api20160701_models.ResetAppKeySecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_app_key_secret_with_options(request, runtime)

    async def reset_app_key_secret_async(
        self,
        request: cloud_api20160701_models.ResetAppKeySecretRequest,
    ) -> cloud_api20160701_models.ResetAppKeySecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_app_key_secret_with_options_async(request, runtime)

    def reset_customized_with_options(
        self,
        request: cloud_api20160701_models.ResetCustomizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ResetCustomizedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetCustomized',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ResetCustomizedResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_customized_with_options_async(
        self,
        request: cloud_api20160701_models.ResetCustomizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.ResetCustomizedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetCustomized',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.ResetCustomizedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_customized(
        self,
        request: cloud_api20160701_models.ResetCustomizedRequest,
    ) -> cloud_api20160701_models.ResetCustomizedResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_customized_with_options(request, runtime)

    async def reset_customized_async(
        self,
        request: cloud_api20160701_models.ResetCustomizedRequest,
    ) -> cloud_api20160701_models.ResetCustomizedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_customized_with_options_async(request, runtime)

    def sdk_generate_with_options(
        self,
        request: cloud_api20160701_models.SdkGenerateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SdkGenerateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkGenerate',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SdkGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdk_generate_with_options_async(
        self,
        request: cloud_api20160701_models.SdkGenerateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SdkGenerateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkGenerate',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SdkGenerateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdk_generate(
        self,
        request: cloud_api20160701_models.SdkGenerateRequest,
    ) -> cloud_api20160701_models.SdkGenerateResponse:
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_with_options(request, runtime)

    async def sdk_generate_async(
        self,
        request: cloud_api20160701_models.SdkGenerateRequest,
    ) -> cloud_api20160701_models.SdkGenerateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sdk_generate_with_options_async(request, runtime)

    def sdk_generate_by_app_with_options(
        self,
        request: cloud_api20160701_models.SdkGenerateByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SdkGenerateByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkGenerateByApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SdkGenerateByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdk_generate_by_app_with_options_async(
        self,
        request: cloud_api20160701_models.SdkGenerateByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SdkGenerateByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkGenerateByApp',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SdkGenerateByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdk_generate_by_app(
        self,
        request: cloud_api20160701_models.SdkGenerateByAppRequest,
    ) -> cloud_api20160701_models.SdkGenerateByAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_by_app_with_options(request, runtime)

    async def sdk_generate_by_app_async(
        self,
        request: cloud_api20160701_models.SdkGenerateByAppRequest,
    ) -> cloud_api20160701_models.SdkGenerateByAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sdk_generate_by_app_with_options_async(request, runtime)

    def sdk_generate_by_group_with_options(
        self,
        request: cloud_api20160701_models.SdkGenerateByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SdkGenerateByGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkGenerateByGroup',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SdkGenerateByGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdk_generate_by_group_with_options_async(
        self,
        request: cloud_api20160701_models.SdkGenerateByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SdkGenerateByGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkGenerateByGroup',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SdkGenerateByGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdk_generate_by_group(
        self,
        request: cloud_api20160701_models.SdkGenerateByGroupRequest,
    ) -> cloud_api20160701_models.SdkGenerateByGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_by_group_with_options(request, runtime)

    async def sdk_generate_by_group_async(
        self,
        request: cloud_api20160701_models.SdkGenerateByGroupRequest,
    ) -> cloud_api20160701_models.SdkGenerateByGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sdk_generate_by_group_with_options_async(request, runtime)

    def set_access_permission_by_apis_with_options(
        self,
        request: cloud_api20160701_models.SetAccessPermissionByApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetAccessPermissionByApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissionByApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetAccessPermissionByApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_access_permission_by_apis_with_options_async(
        self,
        request: cloud_api20160701_models.SetAccessPermissionByApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetAccessPermissionByApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissionByApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetAccessPermissionByApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_access_permission_by_apis(
        self,
        request: cloud_api20160701_models.SetAccessPermissionByApisRequest,
    ) -> cloud_api20160701_models.SetAccessPermissionByApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_access_permission_by_apis_with_options(request, runtime)

    async def set_access_permission_by_apis_async(
        self,
        request: cloud_api20160701_models.SetAccessPermissionByApisRequest,
    ) -> cloud_api20160701_models.SetAccessPermissionByApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_access_permission_by_apis_with_options_async(request, runtime)

    def set_access_permissions_with_options(
        self,
        request: cloud_api20160701_models.SetAccessPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetAccessPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissions',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetAccessPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_access_permissions_with_options_async(
        self,
        request: cloud_api20160701_models.SetAccessPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetAccessPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissions',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetAccessPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_access_permissions(
        self,
        request: cloud_api20160701_models.SetAccessPermissionsRequest,
    ) -> cloud_api20160701_models.SetAccessPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_access_permissions_with_options(request, runtime)

    async def set_access_permissions_async(
        self,
        request: cloud_api20160701_models.SetAccessPermissionsRequest,
    ) -> cloud_api20160701_models.SetAccessPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_access_permissions_with_options_async(request, runtime)

    def set_api_rule_with_options(
        self,
        request: cloud_api20160701_models.SetApiRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetApiRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApiRule',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetApiRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_api_rule_with_options_async(
        self,
        request: cloud_api20160701_models.SetApiRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetApiRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApiRule',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetApiRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_api_rule(
        self,
        request: cloud_api20160701_models.SetApiRuleRequest,
    ) -> cloud_api20160701_models.SetApiRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_api_rule_with_options(request, runtime)

    async def set_api_rule_async(
        self,
        request: cloud_api20160701_models.SetApiRuleRequest,
    ) -> cloud_api20160701_models.SetApiRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_api_rule_with_options_async(request, runtime)

    def set_domain_with_options(
        self,
        request: cloud_api20160701_models.SetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_stage_name):
            query['BindStageName'] = request.bind_stage_name
        if not UtilClient.is_unset(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.is_force):
            query['IsForce'] = request.is_force
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_with_options_async(
        self,
        request: cloud_api20160701_models.SetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_stage_name):
            query['BindStageName'] = request.bind_stage_name
        if not UtilClient.is_unset(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.is_force):
            query['IsForce'] = request.is_force
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomain',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain(
        self,
        request: cloud_api20160701_models.SetDomainRequest,
    ) -> cloud_api20160701_models.SetDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_with_options(request, runtime)

    async def set_domain_async(
        self,
        request: cloud_api20160701_models.SetDomainRequest,
    ) -> cloud_api20160701_models.SetDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_with_options_async(request, runtime)

    def set_domain_certificate_with_options(
        self,
        request: cloud_api20160701_models.SetDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_certificate_body):
            query['CaCertificateBody'] = request.ca_certificate_body
        if not UtilClient.is_unset(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainCertificate',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_certificate_with_options_async(
        self,
        request: cloud_api20160701_models.SetDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_certificate_body):
            query['CaCertificateBody'] = request.ca_certificate_body
        if not UtilClient.is_unset(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainCertificate',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_certificate(
        self,
        request: cloud_api20160701_models.SetDomainCertificateRequest,
    ) -> cloud_api20160701_models.SetDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_certificate_with_options(request, runtime)

    async def set_domain_certificate_async(
        self,
        request: cloud_api20160701_models.SetDomainCertificateRequest,
    ) -> cloud_api20160701_models.SetDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_certificate_with_options_async(request, runtime)

    def set_domain_web_socket_status_with_options(
        self,
        request: cloud_api20160701_models.SetDomainWebSocketStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetDomainWebSocketStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_value):
            query['ActionValue'] = request.action_value
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainWebSocketStatus',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetDomainWebSocketStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_web_socket_status_with_options_async(
        self,
        request: cloud_api20160701_models.SetDomainWebSocketStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetDomainWebSocketStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_value):
            query['ActionValue'] = request.action_value
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainWebSocketStatus',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetDomainWebSocketStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_web_socket_status(
        self,
        request: cloud_api20160701_models.SetDomainWebSocketStatusRequest,
    ) -> cloud_api20160701_models.SetDomainWebSocketStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_web_socket_status_with_options(request, runtime)

    async def set_domain_web_socket_status_async(
        self,
        request: cloud_api20160701_models.SetDomainWebSocketStatusRequest,
    ) -> cloud_api20160701_models.SetDomainWebSocketStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_web_socket_status_with_options_async(request, runtime)

    def set_ip_control_apis_with_options(
        self,
        request: cloud_api20160701_models.SetIpControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetIpControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIpControlApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetIpControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_ip_control_apis_with_options_async(
        self,
        request: cloud_api20160701_models.SetIpControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetIpControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIpControlApis',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetIpControlApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_ip_control_apis(
        self,
        request: cloud_api20160701_models.SetIpControlApisRequest,
    ) -> cloud_api20160701_models.SetIpControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_ip_control_apis_with_options(request, runtime)

    async def set_ip_control_apis_async(
        self,
        request: cloud_api20160701_models.SetIpControlApisRequest,
    ) -> cloud_api20160701_models.SetIpControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_ip_control_apis_with_options_async(request, runtime)

    def set_mock_integration_with_options(
        self,
        request: cloud_api20160701_models.SetMockIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetMockIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.mock):
            query['Mock'] = request.mock
        if not UtilClient.is_unset(request.mock_result):
            query['MockResult'] = request.mock_result
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMockIntegration',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetMockIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_mock_integration_with_options_async(
        self,
        request: cloud_api20160701_models.SetMockIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetMockIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.mock):
            query['Mock'] = request.mock
        if not UtilClient.is_unset(request.mock_result):
            query['MockResult'] = request.mock_result
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMockIntegration',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetMockIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_mock_integration(
        self,
        request: cloud_api20160701_models.SetMockIntegrationRequest,
    ) -> cloud_api20160701_models.SetMockIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_mock_integration_with_options(request, runtime)

    async def set_mock_integration_async(
        self,
        request: cloud_api20160701_models.SetMockIntegrationRequest,
    ) -> cloud_api20160701_models.SetMockIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_mock_integration_with_options_async(request, runtime)

    def set_wildcard_domain_patterns_with_options(
        self,
        request: cloud_api20160701_models.SetWildcardDomainPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetWildcardDomainPatternsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.wildcard_domain_patterns):
            query['WildcardDomainPatterns'] = request.wildcard_domain_patterns
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWildcardDomainPatterns',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetWildcardDomainPatternsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_wildcard_domain_patterns_with_options_async(
        self,
        request: cloud_api20160701_models.SetWildcardDomainPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SetWildcardDomainPatternsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.wildcard_domain_patterns):
            query['WildcardDomainPatterns'] = request.wildcard_domain_patterns
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWildcardDomainPatterns',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SetWildcardDomainPatternsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_wildcard_domain_patterns(
        self,
        request: cloud_api20160701_models.SetWildcardDomainPatternsRequest,
    ) -> cloud_api20160701_models.SetWildcardDomainPatternsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_wildcard_domain_patterns_with_options(request, runtime)

    async def set_wildcard_domain_patterns_async(
        self,
        request: cloud_api20160701_models.SetWildcardDomainPatternsRequest,
    ) -> cloud_api20160701_models.SetWildcardDomainPatternsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_wildcard_domain_patterns_with_options_async(request, runtime)

    def switch_api_with_options(
        self,
        request: cloud_api20160701_models.SwitchApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SwitchApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SwitchApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_api_with_options_async(
        self,
        request: cloud_api20160701_models.SwitchApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.SwitchApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchApi',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.SwitchApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_api(
        self,
        request: cloud_api20160701_models.SwitchApiRequest,
    ) -> cloud_api20160701_models.SwitchApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_api_with_options(request, runtime)

    async def switch_api_async(
        self,
        request: cloud_api20160701_models.SwitchApiRequest,
    ) -> cloud_api20160701_models.SwitchApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_api_with_options_async(request, runtime)

    def vpc_describe_accesses_with_options(
        self,
        request: cloud_api20160701_models.VpcDescribeAccessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.VpcDescribeAccessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_port):
            query['InstancePort'] = request.instance_port
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcDescribeAccesses',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.VpcDescribeAccessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def vpc_describe_accesses_with_options_async(
        self,
        request: cloud_api20160701_models.VpcDescribeAccessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.VpcDescribeAccessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_port):
            query['InstancePort'] = request.instance_port
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcDescribeAccesses',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.VpcDescribeAccessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vpc_describe_accesses(
        self,
        request: cloud_api20160701_models.VpcDescribeAccessesRequest,
    ) -> cloud_api20160701_models.VpcDescribeAccessesResponse:
        runtime = util_models.RuntimeOptions()
        return self.vpc_describe_accesses_with_options(request, runtime)

    async def vpc_describe_accesses_async(
        self,
        request: cloud_api20160701_models.VpcDescribeAccessesRequest,
    ) -> cloud_api20160701_models.VpcDescribeAccessesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vpc_describe_accesses_with_options_async(request, runtime)

    def vpc_grant_access_with_options(
        self,
        request: cloud_api20160701_models.VpcGrantAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.VpcGrantAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_port):
            query['InstancePort'] = request.instance_port
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcGrantAccess',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.VpcGrantAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def vpc_grant_access_with_options_async(
        self,
        request: cloud_api20160701_models.VpcGrantAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.VpcGrantAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_port):
            query['InstancePort'] = request.instance_port
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcGrantAccess',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.VpcGrantAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vpc_grant_access(
        self,
        request: cloud_api20160701_models.VpcGrantAccessRequest,
    ) -> cloud_api20160701_models.VpcGrantAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.vpc_grant_access_with_options(request, runtime)

    async def vpc_grant_access_async(
        self,
        request: cloud_api20160701_models.VpcGrantAccessRequest,
    ) -> cloud_api20160701_models.VpcGrantAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vpc_grant_access_with_options_async(request, runtime)

    def vpc_modify_access_with_options(
        self,
        request: cloud_api20160701_models.VpcModifyAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.VpcModifyAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_port):
            query['InstancePort'] = request.instance_port
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcModifyAccess',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.VpcModifyAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def vpc_modify_access_with_options_async(
        self,
        request: cloud_api20160701_models.VpcModifyAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.VpcModifyAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_port):
            query['InstancePort'] = request.instance_port
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcModifyAccess',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.VpcModifyAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vpc_modify_access(
        self,
        request: cloud_api20160701_models.VpcModifyAccessRequest,
    ) -> cloud_api20160701_models.VpcModifyAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.vpc_modify_access_with_options(request, runtime)

    async def vpc_modify_access_async(
        self,
        request: cloud_api20160701_models.VpcModifyAccessRequest,
    ) -> cloud_api20160701_models.VpcModifyAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vpc_modify_access_with_options_async(request, runtime)

    def vpc_revoke_access_with_options(
        self,
        request: cloud_api20160701_models.VpcRevokeAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.VpcRevokeAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_port):
            query['InstancePort'] = request.instance_port
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcRevokeAccess',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.VpcRevokeAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def vpc_revoke_access_with_options_async(
        self,
        request: cloud_api20160701_models.VpcRevokeAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160701_models.VpcRevokeAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_port):
            query['InstancePort'] = request.instance_port
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcRevokeAccess',
            version='2016-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160701_models.VpcRevokeAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vpc_revoke_access(
        self,
        request: cloud_api20160701_models.VpcRevokeAccessRequest,
    ) -> cloud_api20160701_models.VpcRevokeAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.vpc_revoke_access_with_options(request, runtime)

    async def vpc_revoke_access_async(
        self,
        request: cloud_api20160701_models.VpcRevokeAccessRequest,
    ) -> cloud_api20160701_models.VpcRevokeAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vpc_revoke_access_with_options_async(request, runtime)
