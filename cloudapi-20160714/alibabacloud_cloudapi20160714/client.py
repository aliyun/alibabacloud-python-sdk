# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudapi20160714 import models as cloud_api20160714_models
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
        request: cloud_api20160714_models.AbolishApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.AbolishApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AbolishApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AbolishApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def abolish_api_with_options_async(
        self,
        request: cloud_api20160714_models.AbolishApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.AbolishApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AbolishApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AbolishApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abolish_api(
        self,
        request: cloud_api20160714_models.AbolishApiRequest,
    ) -> cloud_api20160714_models.AbolishApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.abolish_api_with_options(request, runtime)

    async def abolish_api_async(
        self,
        request: cloud_api20160714_models.AbolishApiRequest,
    ) -> cloud_api20160714_models.AbolishApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abolish_api_with_options_async(request, runtime)

    def add_ip_control_policy_item_with_options(
        self,
        request: cloud_api20160714_models.AddIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.AddIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CidrIp'] = request.cidr_ip
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AddIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ip_control_policy_item_with_options_async(
        self,
        request: cloud_api20160714_models.AddIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.AddIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CidrIp'] = request.cidr_ip
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AddIpControlPolicyItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ip_control_policy_item(
        self,
        request: cloud_api20160714_models.AddIpControlPolicyItemRequest,
    ) -> cloud_api20160714_models.AddIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ip_control_policy_item_with_options(request, runtime)

    async def add_ip_control_policy_item_async(
        self,
        request: cloud_api20160714_models.AddIpControlPolicyItemRequest,
    ) -> cloud_api20160714_models.AddIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ip_control_policy_item_with_options_async(request, runtime)

    def add_traffic_special_control_with_options(
        self,
        request: cloud_api20160714_models.AddTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.AddTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SpecialKey'] = request.special_key
        query['SpecialType'] = request.special_type
        query['TrafficControlId'] = request.traffic_control_id
        query['TrafficValue'] = request.traffic_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AddTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_traffic_special_control_with_options_async(
        self,
        request: cloud_api20160714_models.AddTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.AddTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SpecialKey'] = request.special_key
        query['SpecialType'] = request.special_type
        query['TrafficControlId'] = request.traffic_control_id
        query['TrafficValue'] = request.traffic_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AddTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_traffic_special_control(
        self,
        request: cloud_api20160714_models.AddTrafficSpecialControlRequest,
    ) -> cloud_api20160714_models.AddTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_traffic_special_control_with_options(request, runtime)

    async def add_traffic_special_control_async(
        self,
        request: cloud_api20160714_models.AddTrafficSpecialControlRequest,
    ) -> cloud_api20160714_models.AddTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_traffic_special_control_with_options_async(request, runtime)

    def attach_plugin_with_options(
        self,
        request: cloud_api20160714_models.AttachPluginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.AttachPluginResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PluginId'] = request.plugin_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachPlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AttachPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_plugin_with_options_async(
        self,
        request: cloud_api20160714_models.AttachPluginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.AttachPluginResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PluginId'] = request.plugin_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachPlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AttachPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_plugin(
        self,
        request: cloud_api20160714_models.AttachPluginRequest,
    ) -> cloud_api20160714_models.AttachPluginResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_plugin_with_options(request, runtime)

    async def attach_plugin_async(
        self,
        request: cloud_api20160714_models.AttachPluginRequest,
    ) -> cloud_api20160714_models.AttachPluginResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_plugin_with_options_async(request, runtime)

    def batch_abolish_apis_with_options(
        self,
        request: cloud_api20160714_models.BatchAbolishApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.BatchAbolishApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Api'] = request.api
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchAbolishApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.BatchAbolishApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_abolish_apis_with_options_async(
        self,
        request: cloud_api20160714_models.BatchAbolishApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.BatchAbolishApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Api'] = request.api
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchAbolishApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.BatchAbolishApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_abolish_apis(
        self,
        request: cloud_api20160714_models.BatchAbolishApisRequest,
    ) -> cloud_api20160714_models.BatchAbolishApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_abolish_apis_with_options(request, runtime)

    async def batch_abolish_apis_async(
        self,
        request: cloud_api20160714_models.BatchAbolishApisRequest,
    ) -> cloud_api20160714_models.BatchAbolishApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_abolish_apis_with_options_async(request, runtime)

    def batch_deploy_apis_with_options(
        self,
        request: cloud_api20160714_models.BatchDeployApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.BatchDeployApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Api'] = request.api
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchDeployApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.BatchDeployApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_deploy_apis_with_options_async(
        self,
        request: cloud_api20160714_models.BatchDeployApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.BatchDeployApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Api'] = request.api
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchDeployApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.BatchDeployApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_deploy_apis(
        self,
        request: cloud_api20160714_models.BatchDeployApisRequest,
    ) -> cloud_api20160714_models.BatchDeployApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_deploy_apis_with_options(request, runtime)

    async def batch_deploy_apis_async(
        self,
        request: cloud_api20160714_models.BatchDeployApisRequest,
    ) -> cloud_api20160714_models.BatchDeployApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_deploy_apis_with_options_async(request, runtime)

    def create_api_with_options(
        self,
        request: cloud_api20160714_models.CreateApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AllowSignatureMethod'] = request.allow_signature_method
        query['ApiName'] = request.api_name
        query['AppCodeAuthType'] = request.app_code_auth_type
        query['AuthType'] = request.auth_type
        query['ConstantParameters'] = request.constant_parameters
        query['Description'] = request.description
        query['DisableInternet'] = request.disable_internet
        query['ErrorCodeSamples'] = request.error_code_samples
        query['FailResultSample'] = request.fail_result_sample
        query['ForceNonceCheck'] = request.force_nonce_check
        query['GroupId'] = request.group_id
        query['OpenIdConnectConfig'] = request.open_id_connect_config
        query['RequestConfig'] = request.request_config
        query['RequestParameters'] = request.request_parameters
        query['ResultBodyModel'] = request.result_body_model
        query['ResultDescriptions'] = request.result_descriptions
        query['ResultSample'] = request.result_sample
        query['ResultType'] = request.result_type
        query['SecurityToken'] = request.security_token
        query['ServiceConfig'] = request.service_config
        query['ServiceParameters'] = request.service_parameters
        query['ServiceParametersMap'] = request.service_parameters_map
        query['SystemParameters'] = request.system_parameters
        query['Visibility'] = request.visibility
        query['WebSocketApiType'] = request.web_socket_api_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_with_options_async(
        self,
        request: cloud_api20160714_models.CreateApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AllowSignatureMethod'] = request.allow_signature_method
        query['ApiName'] = request.api_name
        query['AppCodeAuthType'] = request.app_code_auth_type
        query['AuthType'] = request.auth_type
        query['ConstantParameters'] = request.constant_parameters
        query['Description'] = request.description
        query['DisableInternet'] = request.disable_internet
        query['ErrorCodeSamples'] = request.error_code_samples
        query['FailResultSample'] = request.fail_result_sample
        query['ForceNonceCheck'] = request.force_nonce_check
        query['GroupId'] = request.group_id
        query['OpenIdConnectConfig'] = request.open_id_connect_config
        query['RequestConfig'] = request.request_config
        query['RequestParameters'] = request.request_parameters
        query['ResultBodyModel'] = request.result_body_model
        query['ResultDescriptions'] = request.result_descriptions
        query['ResultSample'] = request.result_sample
        query['ResultType'] = request.result_type
        query['SecurityToken'] = request.security_token
        query['ServiceConfig'] = request.service_config
        query['ServiceParameters'] = request.service_parameters
        query['ServiceParametersMap'] = request.service_parameters_map
        query['SystemParameters'] = request.system_parameters
        query['Visibility'] = request.visibility
        query['WebSocketApiType'] = request.web_socket_api_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api(
        self,
        request: cloud_api20160714_models.CreateApiRequest,
    ) -> cloud_api20160714_models.CreateApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_api_with_options(request, runtime)

    async def create_api_async(
        self,
        request: cloud_api20160714_models.CreateApiRequest,
    ) -> cloud_api20160714_models.CreateApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_api_with_options_async(request, runtime)

    def create_api_group_with_options(
        self,
        request: cloud_api20160714_models.CreateApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BasePath'] = request.base_path
        query['Description'] = request.description
        query['GroupName'] = request.group_name
        query['InstanceId'] = request.instance_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_group_with_options_async(
        self,
        request: cloud_api20160714_models.CreateApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BasePath'] = request.base_path
        query['Description'] = request.description
        query['GroupName'] = request.group_name
        query['InstanceId'] = request.instance_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_group(
        self,
        request: cloud_api20160714_models.CreateApiGroupRequest,
    ) -> cloud_api20160714_models.CreateApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_api_group_with_options(request, runtime)

    async def create_api_group_async(
        self,
        request: cloud_api20160714_models.CreateApiGroupRequest,
    ) -> cloud_api20160714_models.CreateApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_api_group_with_options_async(request, runtime)

    def create_api_stage_variable_with_options(
        self,
        request: cloud_api20160714_models.CreateApiStageVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateApiStageVariableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageId'] = request.stage_id
        query['StageRouteModel'] = request.stage_route_model
        query['SupportRoute'] = request.support_route
        query['VariableName'] = request.variable_name
        query['VariableValue'] = request.variable_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApiStageVariable',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiStageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_stage_variable_with_options_async(
        self,
        request: cloud_api20160714_models.CreateApiStageVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateApiStageVariableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageId'] = request.stage_id
        query['StageRouteModel'] = request.stage_route_model
        query['SupportRoute'] = request.support_route
        query['VariableName'] = request.variable_name
        query['VariableValue'] = request.variable_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApiStageVariable',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiStageVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_stage_variable(
        self,
        request: cloud_api20160714_models.CreateApiStageVariableRequest,
    ) -> cloud_api20160714_models.CreateApiStageVariableResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_api_stage_variable_with_options(request, runtime)

    async def create_api_stage_variable_async(
        self,
        request: cloud_api20160714_models.CreateApiStageVariableRequest,
    ) -> cloud_api20160714_models.CreateApiStageVariableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_api_stage_variable_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: cloud_api20160714_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['Source'] = request.source
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: cloud_api20160714_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['Source'] = request.source
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: cloud_api20160714_models.CreateAppRequest,
    ) -> cloud_api20160714_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: cloud_api20160714_models.CreateAppRequest,
    ) -> cloud_api20160714_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: cloud_api20160714_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutoPay'] = request.auto_pay
        query['ChargeType'] = request.charge_type
        query['Duration'] = request.duration
        query['HttpsPolicy'] = request.https_policy
        query['InstanceName'] = request.instance_name
        query['InstanceSpec'] = request.instance_spec
        query['PricingCycle'] = request.pricing_cycle
        query['Token'] = request.token
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: cloud_api20160714_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutoPay'] = request.auto_pay
        query['ChargeType'] = request.charge_type
        query['Duration'] = request.duration
        query['HttpsPolicy'] = request.https_policy
        query['InstanceName'] = request.instance_name
        query['InstanceSpec'] = request.instance_spec
        query['PricingCycle'] = request.pricing_cycle
        query['Token'] = request.token
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: cloud_api20160714_models.CreateInstanceRequest,
    ) -> cloud_api20160714_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: cloud_api20160714_models.CreateInstanceRequest,
    ) -> cloud_api20160714_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_intranet_domain_with_options(
        self,
        request: cloud_api20160714_models.CreateIntranetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateIntranetDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateIntranetDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateIntranetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_intranet_domain_with_options_async(
        self,
        request: cloud_api20160714_models.CreateIntranetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateIntranetDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateIntranetDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateIntranetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_intranet_domain(
        self,
        request: cloud_api20160714_models.CreateIntranetDomainRequest,
    ) -> cloud_api20160714_models.CreateIntranetDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_intranet_domain_with_options(request, runtime)

    async def create_intranet_domain_async(
        self,
        request: cloud_api20160714_models.CreateIntranetDomainRequest,
    ) -> cloud_api20160714_models.CreateIntranetDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_intranet_domain_with_options_async(request, runtime)

    def create_ip_control_with_options(
        self,
        request: cloud_api20160714_models.CreateIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['IpControlName'] = request.ip_control_name
        query['IpControlPolicys'] = request.ip_control_policys
        query['IpControlType'] = request.ip_control_type
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ip_control_with_options_async(
        self,
        request: cloud_api20160714_models.CreateIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['IpControlName'] = request.ip_control_name
        query['IpControlPolicys'] = request.ip_control_policys
        query['IpControlType'] = request.ip_control_type
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ip_control(
        self,
        request: cloud_api20160714_models.CreateIpControlRequest,
    ) -> cloud_api20160714_models.CreateIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ip_control_with_options(request, runtime)

    async def create_ip_control_async(
        self,
        request: cloud_api20160714_models.CreateIpControlRequest,
    ) -> cloud_api20160714_models.CreateIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ip_control_with_options_async(request, runtime)

    def create_log_config_with_options(
        self,
        request: cloud_api20160714_models.CreateLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        query['SlsLogStore'] = request.sls_log_store
        query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_log_config_with_options_async(
        self,
        request: cloud_api20160714_models.CreateLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        query['SlsLogStore'] = request.sls_log_store
        query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_log_config(
        self,
        request: cloud_api20160714_models.CreateLogConfigRequest,
    ) -> cloud_api20160714_models.CreateLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_log_config_with_options(request, runtime)

    async def create_log_config_async(
        self,
        request: cloud_api20160714_models.CreateLogConfigRequest,
    ) -> cloud_api20160714_models.CreateLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_log_config_with_options_async(request, runtime)

    def create_model_with_options(
        self,
        request: cloud_api20160714_models.CreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['ModelName'] = request.model_name
        query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_with_options_async(
        self,
        request: cloud_api20160714_models.CreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['ModelName'] = request.model_name
        query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model(
        self,
        request: cloud_api20160714_models.CreateModelRequest,
    ) -> cloud_api20160714_models.CreateModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_model_with_options(request, runtime)

    async def create_model_async(
        self,
        request: cloud_api20160714_models.CreateModelRequest,
    ) -> cloud_api20160714_models.CreateModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_model_with_options_async(request, runtime)

    def create_monitor_group_with_options(
        self,
        request: cloud_api20160714_models.CreateMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateMonitorGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Auth'] = request.auth
        query['GroupId'] = request.group_id
        query['RawMonitorGroupId'] = request.raw_monitor_group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_group_with_options_async(
        self,
        request: cloud_api20160714_models.CreateMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateMonitorGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Auth'] = request.auth
        query['GroupId'] = request.group_id
        query['RawMonitorGroupId'] = request.raw_monitor_group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateMonitorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_group(
        self,
        request: cloud_api20160714_models.CreateMonitorGroupRequest,
    ) -> cloud_api20160714_models.CreateMonitorGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_with_options(request, runtime)

    async def create_monitor_group_async(
        self,
        request: cloud_api20160714_models.CreateMonitorGroupRequest,
    ) -> cloud_api20160714_models.CreateMonitorGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_group_with_options_async(request, runtime)

    def create_plugin_with_options(
        self,
        request: cloud_api20160714_models.CreatePluginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreatePluginResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['PluginData'] = request.plugin_data
        query['PluginName'] = request.plugin_name
        query['PluginType'] = request.plugin_type
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreatePluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_plugin_with_options_async(
        self,
        request: cloud_api20160714_models.CreatePluginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreatePluginResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['PluginData'] = request.plugin_data
        query['PluginName'] = request.plugin_name
        query['PluginType'] = request.plugin_type
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreatePluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_plugin(
        self,
        request: cloud_api20160714_models.CreatePluginRequest,
    ) -> cloud_api20160714_models.CreatePluginResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_plugin_with_options(request, runtime)

    async def create_plugin_async(
        self,
        request: cloud_api20160714_models.CreatePluginRequest,
    ) -> cloud_api20160714_models.CreatePluginResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_plugin_with_options_async(request, runtime)

    def create_signature_with_options(
        self,
        request: cloud_api20160714_models.CreateSignatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateSignatureResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SignatureKey'] = request.signature_key
        query['SignatureName'] = request.signature_name
        query['SignatureSecret'] = request.signature_secret
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_signature_with_options_async(
        self,
        request: cloud_api20160714_models.CreateSignatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateSignatureResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SignatureKey'] = request.signature_key
        query['SignatureName'] = request.signature_name
        query['SignatureSecret'] = request.signature_secret
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_signature(
        self,
        request: cloud_api20160714_models.CreateSignatureRequest,
    ) -> cloud_api20160714_models.CreateSignatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_signature_with_options(request, runtime)

    async def create_signature_async(
        self,
        request: cloud_api20160714_models.CreateSignatureRequest,
    ) -> cloud_api20160714_models.CreateSignatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_signature_with_options_async(request, runtime)

    def create_traffic_control_with_options(
        self,
        request: cloud_api20160714_models.CreateTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiDefault'] = request.api_default
        query['AppDefault'] = request.app_default
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['TrafficControlName'] = request.traffic_control_name
        query['TrafficControlUnit'] = request.traffic_control_unit
        query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_traffic_control_with_options_async(
        self,
        request: cloud_api20160714_models.CreateTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.CreateTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiDefault'] = request.api_default
        query['AppDefault'] = request.app_default
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['TrafficControlName'] = request.traffic_control_name
        query['TrafficControlUnit'] = request.traffic_control_unit
        query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_traffic_control(
        self,
        request: cloud_api20160714_models.CreateTrafficControlRequest,
    ) -> cloud_api20160714_models.CreateTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_control_with_options(request, runtime)

    async def create_traffic_control_async(
        self,
        request: cloud_api20160714_models.CreateTrafficControlRequest,
    ) -> cloud_api20160714_models.CreateTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_traffic_control_with_options_async(request, runtime)

    def delete_all_traffic_special_control_with_options(
        self,
        request: cloud_api20160714_models.DeleteAllTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteAllTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAllTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteAllTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_all_traffic_special_control_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteAllTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteAllTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAllTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteAllTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_all_traffic_special_control(
        self,
        request: cloud_api20160714_models.DeleteAllTrafficSpecialControlRequest,
    ) -> cloud_api20160714_models.DeleteAllTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_all_traffic_special_control_with_options(request, runtime)

    async def delete_all_traffic_special_control_async(
        self,
        request: cloud_api20160714_models.DeleteAllTrafficSpecialControlRequest,
    ) -> cloud_api20160714_models.DeleteAllTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_all_traffic_special_control_with_options_async(request, runtime)

    def delete_api_with_options(
        self,
        request: cloud_api20160714_models.DeleteApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api(
        self,
        request: cloud_api20160714_models.DeleteApiRequest,
    ) -> cloud_api20160714_models.DeleteApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_api_with_options(request, runtime)

    async def delete_api_async(
        self,
        request: cloud_api20160714_models.DeleteApiRequest,
    ) -> cloud_api20160714_models.DeleteApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_with_options_async(request, runtime)

    def delete_api_group_with_options(
        self,
        request: cloud_api20160714_models.DeleteApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_group_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_group(
        self,
        request: cloud_api20160714_models.DeleteApiGroupRequest,
    ) -> cloud_api20160714_models.DeleteApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_api_group_with_options(request, runtime)

    async def delete_api_group_async(
        self,
        request: cloud_api20160714_models.DeleteApiGroupRequest,
    ) -> cloud_api20160714_models.DeleteApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_group_with_options_async(request, runtime)

    def delete_api_stage_variable_with_options(
        self,
        request: cloud_api20160714_models.DeleteApiStageVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteApiStageVariableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageId'] = request.stage_id
        query['VariableName'] = request.variable_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApiStageVariable',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiStageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_stage_variable_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteApiStageVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteApiStageVariableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageId'] = request.stage_id
        query['VariableName'] = request.variable_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApiStageVariable',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiStageVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_stage_variable(
        self,
        request: cloud_api20160714_models.DeleteApiStageVariableRequest,
    ) -> cloud_api20160714_models.DeleteApiStageVariableResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_api_stage_variable_with_options(request, runtime)

    async def delete_api_stage_variable_async(
        self,
        request: cloud_api20160714_models.DeleteApiStageVariableRequest,
    ) -> cloud_api20160714_models.DeleteApiStageVariableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_stage_variable_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: cloud_api20160714_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: cloud_api20160714_models.DeleteAppRequest,
    ) -> cloud_api20160714_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: cloud_api20160714_models.DeleteAppRequest,
    ) -> cloud_api20160714_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: cloud_api20160714_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: cloud_api20160714_models.DeleteDomainRequest,
    ) -> cloud_api20160714_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: cloud_api20160714_models.DeleteDomainRequest,
    ) -> cloud_api20160714_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_domain_certificate_with_options(
        self,
        request: cloud_api20160714_models.DeleteDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CertificateId'] = request.certificate_id
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomainCertificate',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_certificate_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CertificateId'] = request.certificate_id
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomainCertificate',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_certificate(
        self,
        request: cloud_api20160714_models.DeleteDomainCertificateRequest,
    ) -> cloud_api20160714_models.DeleteDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_certificate_with_options(request, runtime)

    async def delete_domain_certificate_async(
        self,
        request: cloud_api20160714_models.DeleteDomainCertificateRequest,
    ) -> cloud_api20160714_models.DeleteDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_certificate_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: cloud_api20160714_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: cloud_api20160714_models.DeleteInstanceRequest,
    ) -> cloud_api20160714_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: cloud_api20160714_models.DeleteInstanceRequest,
    ) -> cloud_api20160714_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_ip_control_with_options(
        self,
        request: cloud_api20160714_models.DeleteIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ip_control_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ip_control(
        self,
        request: cloud_api20160714_models.DeleteIpControlRequest,
    ) -> cloud_api20160714_models.DeleteIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_control_with_options(request, runtime)

    async def delete_ip_control_async(
        self,
        request: cloud_api20160714_models.DeleteIpControlRequest,
    ) -> cloud_api20160714_models.DeleteIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ip_control_with_options_async(request, runtime)

    def delete_log_config_with_options(
        self,
        request: cloud_api20160714_models.DeleteLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_config_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_config(
        self,
        request: cloud_api20160714_models.DeleteLogConfigRequest,
    ) -> cloud_api20160714_models.DeleteLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_log_config_with_options(request, runtime)

    async def delete_log_config_async(
        self,
        request: cloud_api20160714_models.DeleteLogConfigRequest,
    ) -> cloud_api20160714_models.DeleteLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_log_config_with_options_async(request, runtime)

    def delete_model_with_options(
        self,
        request: cloud_api20160714_models.DeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['ModelName'] = request.model_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['ModelName'] = request.model_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model(
        self,
        request: cloud_api20160714_models.DeleteModelRequest,
    ) -> cloud_api20160714_models.DeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_model_with_options(request, runtime)

    async def delete_model_async(
        self,
        request: cloud_api20160714_models.DeleteModelRequest,
    ) -> cloud_api20160714_models.DeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_model_with_options_async(request, runtime)

    def delete_plugin_with_options(
        self,
        request: cloud_api20160714_models.DeletePluginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeletePluginResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PluginId'] = request.plugin_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeletePluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_plugin_with_options_async(
        self,
        request: cloud_api20160714_models.DeletePluginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeletePluginResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PluginId'] = request.plugin_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeletePluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_plugin(
        self,
        request: cloud_api20160714_models.DeletePluginRequest,
    ) -> cloud_api20160714_models.DeletePluginResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_plugin_with_options(request, runtime)

    async def delete_plugin_async(
        self,
        request: cloud_api20160714_models.DeletePluginRequest,
    ) -> cloud_api20160714_models.DeletePluginResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_plugin_with_options_async(request, runtime)

    def delete_signature_with_options(
        self,
        request: cloud_api20160714_models.DeleteSignatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteSignatureResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_signature_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteSignatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteSignatureResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_signature(
        self,
        request: cloud_api20160714_models.DeleteSignatureRequest,
    ) -> cloud_api20160714_models.DeleteSignatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_signature_with_options(request, runtime)

    async def delete_signature_async(
        self,
        request: cloud_api20160714_models.DeleteSignatureRequest,
    ) -> cloud_api20160714_models.DeleteSignatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_signature_with_options_async(request, runtime)

    def delete_traffic_control_with_options(
        self,
        request: cloud_api20160714_models.DeleteTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_control_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_control(
        self,
        request: cloud_api20160714_models.DeleteTrafficControlRequest,
    ) -> cloud_api20160714_models.DeleteTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_control_with_options(request, runtime)

    async def delete_traffic_control_async(
        self,
        request: cloud_api20160714_models.DeleteTrafficControlRequest,
    ) -> cloud_api20160714_models.DeleteTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_traffic_control_with_options_async(request, runtime)

    def delete_traffic_special_control_with_options(
        self,
        request: cloud_api20160714_models.DeleteTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SpecialKey'] = request.special_key
        query['SpecialType'] = request.special_type
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_special_control_with_options_async(
        self,
        request: cloud_api20160714_models.DeleteTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeleteTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SpecialKey'] = request.special_key
        query['SpecialType'] = request.special_type
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_special_control(
        self,
        request: cloud_api20160714_models.DeleteTrafficSpecialControlRequest,
    ) -> cloud_api20160714_models.DeleteTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_special_control_with_options(request, runtime)

    async def delete_traffic_special_control_async(
        self,
        request: cloud_api20160714_models.DeleteTrafficSpecialControlRequest,
    ) -> cloud_api20160714_models.DeleteTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_traffic_special_control_with_options_async(request, runtime)

    def deploy_api_with_options(
        self,
        request: cloud_api20160714_models.DeployApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeployApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeployApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeployApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_api_with_options_async(
        self,
        request: cloud_api20160714_models.DeployApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DeployApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeployApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeployApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_api(
        self,
        request: cloud_api20160714_models.DeployApiRequest,
    ) -> cloud_api20160714_models.DeployApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_api_with_options(request, runtime)

    async def deploy_api_async(
        self,
        request: cloud_api20160714_models.DeployApiRequest,
    ) -> cloud_api20160714_models.DeployApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_api_with_options_async(request, runtime)

    def describe_abolish_api_task_with_options(
        self,
        request: cloud_api20160714_models.DescribeAbolishApiTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAbolishApiTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OperationUid'] = request.operation_uid
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAbolishApiTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAbolishApiTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_abolish_api_task_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeAbolishApiTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAbolishApiTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OperationUid'] = request.operation_uid
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAbolishApiTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAbolishApiTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_abolish_api_task(
        self,
        request: cloud_api20160714_models.DescribeAbolishApiTaskRequest,
    ) -> cloud_api20160714_models.DescribeAbolishApiTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_abolish_api_task_with_options(request, runtime)

    async def describe_abolish_api_task_async(
        self,
        request: cloud_api20160714_models.DescribeAbolishApiTaskRequest,
    ) -> cloud_api20160714_models.DescribeAbolishApiTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_abolish_api_task_with_options_async(request, runtime)

    def describe_api_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api(
        self,
        request: cloud_api20160714_models.DescribeApiRequest,
    ) -> cloud_api20160714_models.DescribeApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_with_options(request, runtime)

    async def describe_api_async(
        self,
        request: cloud_api20160714_models.DescribeApiRequest,
    ) -> cloud_api20160714_models.DescribeApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_with_options_async(request, runtime)

    def describe_api_doc_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiDocResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiDoc',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_doc_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiDocResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiDoc',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_doc(
        self,
        request: cloud_api20160714_models.DescribeApiDocRequest,
    ) -> cloud_api20160714_models.DescribeApiDocResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_doc_with_options(request, runtime)

    async def describe_api_doc_async(
        self,
        request: cloud_api20160714_models.DescribeApiDocRequest,
    ) -> cloud_api20160714_models.DescribeApiDocResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_doc_with_options_async(request, runtime)

    def describe_api_group_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_group_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_group(
        self,
        request: cloud_api20160714_models.DescribeApiGroupRequest,
    ) -> cloud_api20160714_models.DescribeApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_group_with_options(request, runtime)

    async def describe_api_group_async(
        self,
        request: cloud_api20160714_models.DescribeApiGroupRequest,
    ) -> cloud_api20160714_models.DescribeApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_group_with_options_async(request, runtime)

    def describe_api_group_vpc_whitelist_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiGroupVpcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiGroupVpcWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiGroupVpcWhitelist',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupVpcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_group_vpc_whitelist_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiGroupVpcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiGroupVpcWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiGroupVpcWhitelist',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupVpcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_group_vpc_whitelist(
        self,
        request: cloud_api20160714_models.DescribeApiGroupVpcWhitelistRequest,
    ) -> cloud_api20160714_models.DescribeApiGroupVpcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_group_vpc_whitelist_with_options(request, runtime)

    async def describe_api_group_vpc_whitelist_async(
        self,
        request: cloud_api20160714_models.DescribeApiGroupVpcWhitelistRequest,
    ) -> cloud_api20160714_models.DescribeApiGroupVpcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_group_vpc_whitelist_with_options_async(request, runtime)

    def describe_api_groups_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EnableTagAuth'] = request.enable_tag_auth
        query['GroupId'] = request.group_id
        query['GroupName'] = request.group_name
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['Sort'] = request.sort
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiGroups',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_groups_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EnableTagAuth'] = request.enable_tag_auth
        query['GroupId'] = request.group_id
        query['GroupName'] = request.group_name
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['Sort'] = request.sort
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiGroups',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_groups(
        self,
        request: cloud_api20160714_models.DescribeApiGroupsRequest,
    ) -> cloud_api20160714_models.DescribeApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_groups_with_options(request, runtime)

    async def describe_api_groups_async(
        self,
        request: cloud_api20160714_models.DescribeApiGroupsRequest,
    ) -> cloud_api20160714_models.DescribeApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_groups_with_options_async(request, runtime)

    def describe_api_histories_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiHistoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiHistories',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_histories_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiHistoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiHistories',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_histories(
        self,
        request: cloud_api20160714_models.DescribeApiHistoriesRequest,
    ) -> cloud_api20160714_models.DescribeApiHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_histories_with_options(request, runtime)

    async def describe_api_histories_async(
        self,
        request: cloud_api20160714_models.DescribeApiHistoriesRequest,
    ) -> cloud_api20160714_models.DescribeApiHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_histories_with_options_async(request, runtime)

    def describe_api_history_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['HistoryVersion'] = request.history_version
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiHistory',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_history_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['HistoryVersion'] = request.history_version
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiHistory',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_history(
        self,
        request: cloud_api20160714_models.DescribeApiHistoryRequest,
    ) -> cloud_api20160714_models.DescribeApiHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_history_with_options(request, runtime)

    async def describe_api_history_async(
        self,
        request: cloud_api20160714_models.DescribeApiHistoryRequest,
    ) -> cloud_api20160714_models.DescribeApiHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_history_with_options_async(request, runtime)

    def describe_api_ip_controls_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiIpControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiIpControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiIpControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiIpControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_ip_controls_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiIpControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiIpControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiIpControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiIpControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_ip_controls(
        self,
        request: cloud_api20160714_models.DescribeApiIpControlsRequest,
    ) -> cloud_api20160714_models.DescribeApiIpControlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_ip_controls_with_options(request, runtime)

    async def describe_api_ip_controls_async(
        self,
        request: cloud_api20160714_models.DescribeApiIpControlsRequest,
    ) -> cloud_api20160714_models.DescribeApiIpControlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_ip_controls_with_options_async(request, runtime)

    def describe_api_latency_data_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiLatencyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiLatencyDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['EndTime'] = request.end_time
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiLatencyData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiLatencyDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_latency_data_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiLatencyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiLatencyDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['EndTime'] = request.end_time
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiLatencyData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiLatencyDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_latency_data(
        self,
        request: cloud_api20160714_models.DescribeApiLatencyDataRequest,
    ) -> cloud_api20160714_models.DescribeApiLatencyDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_latency_data_with_options(request, runtime)

    async def describe_api_latency_data_async(
        self,
        request: cloud_api20160714_models.DescribeApiLatencyDataRequest,
    ) -> cloud_api20160714_models.DescribeApiLatencyDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_latency_data_with_options_async(request, runtime)

    def describe_api_market_attributes_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiMarketAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiMarketAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiMarketAttributes',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiMarketAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_market_attributes_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiMarketAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiMarketAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiMarketAttributes',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiMarketAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_market_attributes(
        self,
        request: cloud_api20160714_models.DescribeApiMarketAttributesRequest,
    ) -> cloud_api20160714_models.DescribeApiMarketAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_market_attributes_with_options(request, runtime)

    async def describe_api_market_attributes_async(
        self,
        request: cloud_api20160714_models.DescribeApiMarketAttributesRequest,
    ) -> cloud_api20160714_models.DescribeApiMarketAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_market_attributes_with_options_async(request, runtime)

    def describe_api_qps_data_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiQpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['EndTime'] = request.end_time
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiQpsData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_qps_data_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiQpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['EndTime'] = request.end_time
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiQpsData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_qps_data(
        self,
        request: cloud_api20160714_models.DescribeApiQpsDataRequest,
    ) -> cloud_api20160714_models.DescribeApiQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_qps_data_with_options(request, runtime)

    async def describe_api_qps_data_async(
        self,
        request: cloud_api20160714_models.DescribeApiQpsDataRequest,
    ) -> cloud_api20160714_models.DescribeApiQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_qps_data_with_options_async(request, runtime)

    def describe_api_signatures_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiSignaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiSignaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiSignatures',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_signatures_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiSignaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiSignaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiSignatures',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiSignaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_signatures(
        self,
        request: cloud_api20160714_models.DescribeApiSignaturesRequest,
    ) -> cloud_api20160714_models.DescribeApiSignaturesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_signatures_with_options(request, runtime)

    async def describe_api_signatures_async(
        self,
        request: cloud_api20160714_models.DescribeApiSignaturesRequest,
    ) -> cloud_api20160714_models.DescribeApiSignaturesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_signatures_with_options_async(request, runtime)

    def describe_api_traffic_controls_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiTrafficControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiTrafficControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiTrafficControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiTrafficControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_traffic_controls_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiTrafficControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiTrafficControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiTrafficControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiTrafficControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_traffic_controls(
        self,
        request: cloud_api20160714_models.DescribeApiTrafficControlsRequest,
    ) -> cloud_api20160714_models.DescribeApiTrafficControlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_traffic_controls_with_options(request, runtime)

    async def describe_api_traffic_controls_async(
        self,
        request: cloud_api20160714_models.DescribeApiTrafficControlsRequest,
    ) -> cloud_api20160714_models.DescribeApiTrafficControlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_traffic_controls_with_options_async(request, runtime)

    def describe_api_traffic_data_with_options(
        self,
        request: cloud_api20160714_models.DescribeApiTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['EndTime'] = request.end_time
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiTrafficData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_traffic_data_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApiTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApiTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['EndTime'] = request.end_time
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiTrafficData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_traffic_data(
        self,
        request: cloud_api20160714_models.DescribeApiTrafficDataRequest,
    ) -> cloud_api20160714_models.DescribeApiTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_traffic_data_with_options(request, runtime)

    async def describe_api_traffic_data_async(
        self,
        request: cloud_api20160714_models.DescribeApiTrafficDataRequest,
    ) -> cloud_api20160714_models.DescribeApiTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_traffic_data_with_options_async(request, runtime)

    def describe_apis_with_options(
        self,
        request: cloud_api20160714_models.DescribeApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['CatalogId'] = request.catalog_id
        query['EnableTagAuth'] = request.enable_tag_auth
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['CatalogId'] = request.catalog_id
        query['EnableTagAuth'] = request.enable_tag_auth
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis(
        self,
        request: cloud_api20160714_models.DescribeApisRequest,
    ) -> cloud_api20160714_models.DescribeApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_with_options(request, runtime)

    async def describe_apis_async(
        self,
        request: cloud_api20160714_models.DescribeApisRequest,
    ) -> cloud_api20160714_models.DescribeApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_with_options_async(request, runtime)

    def describe_apis_by_app_with_options(
        self,
        request: cloud_api20160714_models.DescribeApisByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApisByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiName'] = request.api_name
        query['ApiUid'] = request.api_uid
        query['AppId'] = request.app_id
        query['Method'] = request.method
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Path'] = request.path
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisByApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_app_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApisByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApisByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiName'] = request.api_name
        query['ApiUid'] = request.api_uid
        query['AppId'] = request.app_id
        query['Method'] = request.method
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Path'] = request.path
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisByApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_app(
        self,
        request: cloud_api20160714_models.DescribeApisByAppRequest,
    ) -> cloud_api20160714_models.DescribeApisByAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_app_with_options(request, runtime)

    async def describe_apis_by_app_async(
        self,
        request: cloud_api20160714_models.DescribeApisByAppRequest,
    ) -> cloud_api20160714_models.DescribeApisByAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_by_app_with_options_async(request, runtime)

    def describe_apis_by_ip_control_with_options(
        self,
        request: cloud_api20160714_models.DescribeApisByIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApisByIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisByIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_ip_control_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApisByIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApisByIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisByIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_ip_control(
        self,
        request: cloud_api20160714_models.DescribeApisByIpControlRequest,
    ) -> cloud_api20160714_models.DescribeApisByIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_ip_control_with_options(request, runtime)

    async def describe_apis_by_ip_control_async(
        self,
        request: cloud_api20160714_models.DescribeApisByIpControlRequest,
    ) -> cloud_api20160714_models.DescribeApisByIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_by_ip_control_with_options_async(request, runtime)

    def describe_apis_by_signature_with_options(
        self,
        request: cloud_api20160714_models.DescribeApisBySignatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApisBySignatureResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisBySignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisBySignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_signature_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApisBySignatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApisBySignatureResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisBySignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisBySignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_signature(
        self,
        request: cloud_api20160714_models.DescribeApisBySignatureRequest,
    ) -> cloud_api20160714_models.DescribeApisBySignatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_signature_with_options(request, runtime)

    async def describe_apis_by_signature_async(
        self,
        request: cloud_api20160714_models.DescribeApisBySignatureRequest,
    ) -> cloud_api20160714_models.DescribeApisBySignatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_by_signature_with_options_async(request, runtime)

    def describe_apis_by_traffic_control_with_options(
        self,
        request: cloud_api20160714_models.DescribeApisByTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApisByTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisByTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_traffic_control_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeApisByTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeApisByTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisByTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_traffic_control(
        self,
        request: cloud_api20160714_models.DescribeApisByTrafficControlRequest,
    ) -> cloud_api20160714_models.DescribeApisByTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_traffic_control_with_options(request, runtime)

    async def describe_apis_by_traffic_control_async(
        self,
        request: cloud_api20160714_models.DescribeApisByTrafficControlRequest,
    ) -> cloud_api20160714_models.DescribeApisByTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_by_traffic_control_with_options_async(request, runtime)

    def describe_app_with_options(
        self,
        request: cloud_api20160714_models.DescribeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app(
        self,
        request: cloud_api20160714_models.DescribeAppRequest,
    ) -> cloud_api20160714_models.DescribeAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_with_options(request, runtime)

    async def describe_app_async(
        self,
        request: cloud_api20160714_models.DescribeAppRequest,
    ) -> cloud_api20160714_models.DescribeAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_with_options_async(request, runtime)

    def describe_app_attributes_with_options(
        self,
        request: cloud_api20160714_models.DescribeAppAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAppAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppCode'] = request.app_code
        query['AppId'] = request.app_id
        query['AppKey'] = request.app_key
        query['AppName'] = request.app_name
        query['EnableTagAuth'] = request.enable_tag_auth
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['Sort'] = request.sort
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppAttributes',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_attributes_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeAppAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAppAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppCode'] = request.app_code
        query['AppId'] = request.app_id
        query['AppKey'] = request.app_key
        query['AppName'] = request.app_name
        query['EnableTagAuth'] = request.enable_tag_auth
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['Sort'] = request.sort
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppAttributes',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_attributes(
        self,
        request: cloud_api20160714_models.DescribeAppAttributesRequest,
    ) -> cloud_api20160714_models.DescribeAppAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_attributes_with_options(request, runtime)

    async def describe_app_attributes_async(
        self,
        request: cloud_api20160714_models.DescribeAppAttributesRequest,
    ) -> cloud_api20160714_models.DescribeAppAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_attributes_with_options_async(request, runtime)

    def describe_app_security_with_options(
        self,
        request: cloud_api20160714_models.DescribeAppSecurityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAppSecurityResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurity',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppSecurityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_security_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeAppSecurityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAppSecurityResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurity',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppSecurityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_security(
        self,
        request: cloud_api20160714_models.DescribeAppSecurityRequest,
    ) -> cloud_api20160714_models.DescribeAppSecurityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_security_with_options(request, runtime)

    async def describe_app_security_async(
        self,
        request: cloud_api20160714_models.DescribeAppSecurityRequest,
    ) -> cloud_api20160714_models.DescribeAppSecurityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_security_with_options_async(request, runtime)

    def describe_apps_with_options(
        self,
        request: cloud_api20160714_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AppOwner'] = request.app_owner
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AppOwner'] = request.app_owner
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps(
        self,
        request: cloud_api20160714_models.DescribeAppsRequest,
    ) -> cloud_api20160714_models.DescribeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    async def describe_apps_async(
        self,
        request: cloud_api20160714_models.DescribeAppsRequest,
    ) -> cloud_api20160714_models.DescribeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apps_with_options_async(request, runtime)

    def describe_authorized_apis_with_options(
        self,
        request: cloud_api20160714_models.DescribeAuthorizedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAuthorizedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAuthorizedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAuthorizedApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_authorized_apis_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeAuthorizedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAuthorizedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAuthorizedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAuthorizedApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_authorized_apis(
        self,
        request: cloud_api20160714_models.DescribeAuthorizedApisRequest,
    ) -> cloud_api20160714_models.DescribeAuthorizedApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_authorized_apis_with_options(request, runtime)

    async def describe_authorized_apis_async(
        self,
        request: cloud_api20160714_models.DescribeAuthorizedApisRequest,
    ) -> cloud_api20160714_models.DescribeAuthorizedApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_authorized_apis_with_options_async(request, runtime)

    def describe_authorized_apps_with_options(
        self,
        request: cloud_api20160714_models.DescribeAuthorizedAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAuthorizedAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['AppId'] = request.app_id
        query['AppName'] = request.app_name
        query['AppOwnerId'] = request.app_owner_id
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAuthorizedApps',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAuthorizedAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_authorized_apps_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeAuthorizedAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeAuthorizedAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['AppId'] = request.app_id
        query['AppName'] = request.app_name
        query['AppOwnerId'] = request.app_owner_id
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAuthorizedApps',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAuthorizedAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_authorized_apps(
        self,
        request: cloud_api20160714_models.DescribeAuthorizedAppsRequest,
    ) -> cloud_api20160714_models.DescribeAuthorizedAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_authorized_apps_with_options(request, runtime)

    async def describe_authorized_apps_async(
        self,
        request: cloud_api20160714_models.DescribeAuthorizedAppsRequest,
    ) -> cloud_api20160714_models.DescribeAuthorizedAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_authorized_apps_with_options_async(request, runtime)

    def describe_deploy_api_task_with_options(
        self,
        request: cloud_api20160714_models.DescribeDeployApiTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeDeployApiTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OperationUid'] = request.operation_uid
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeployApiTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployApiTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deploy_api_task_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeDeployApiTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeDeployApiTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OperationUid'] = request.operation_uid
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeployApiTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployApiTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deploy_api_task(
        self,
        request: cloud_api20160714_models.DescribeDeployApiTaskRequest,
    ) -> cloud_api20160714_models.DescribeDeployApiTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deploy_api_task_with_options(request, runtime)

    async def describe_deploy_api_task_async(
        self,
        request: cloud_api20160714_models.DescribeDeployApiTaskRequest,
    ) -> cloud_api20160714_models.DescribeDeployApiTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deploy_api_task_with_options_async(request, runtime)

    def describe_deployed_api_with_options(
        self,
        request: cloud_api20160714_models.DescribeDeployedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeDeployedApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployedApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployed_api_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeDeployedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeDeployedApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployedApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployed_api(
        self,
        request: cloud_api20160714_models.DescribeDeployedApiRequest,
    ) -> cloud_api20160714_models.DescribeDeployedApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deployed_api_with_options(request, runtime)

    async def describe_deployed_api_async(
        self,
        request: cloud_api20160714_models.DescribeDeployedApiRequest,
    ) -> cloud_api20160714_models.DescribeDeployedApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deployed_api_with_options_async(request, runtime)

    def describe_deployed_apis_with_options(
        self,
        request: cloud_api20160714_models.DescribeDeployedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeDeployedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['EnableTagAuth'] = request.enable_tag_auth
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployedApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployed_apis_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeDeployedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeDeployedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['EnableTagAuth'] = request.enable_tag_auth
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployedApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployed_apis(
        self,
        request: cloud_api20160714_models.DescribeDeployedApisRequest,
    ) -> cloud_api20160714_models.DescribeDeployedApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deployed_apis_with_options(request, runtime)

    async def describe_deployed_apis_async(
        self,
        request: cloud_api20160714_models.DescribeDeployedApisRequest,
    ) -> cloud_api20160714_models.DescribeDeployedApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deployed_apis_with_options_async(request, runtime)

    def describe_domain_with_options(
        self,
        request: cloud_api20160714_models.DescribeDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain(
        self,
        request: cloud_api20160714_models.DescribeDomainRequest,
    ) -> cloud_api20160714_models.DescribeDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_options(request, runtime)

    async def describe_domain_async(
        self,
        request: cloud_api20160714_models.DescribeDomainRequest,
    ) -> cloud_api20160714_models.DescribeDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_with_options_async(request, runtime)

    def describe_history_apis_with_options(
        self,
        request: cloud_api20160714_models.DescribeHistoryApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeHistoryApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeHistoryApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_apis_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeHistoryApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeHistoryApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeHistoryApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_apis(
        self,
        request: cloud_api20160714_models.DescribeHistoryApisRequest,
    ) -> cloud_api20160714_models.DescribeHistoryApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_history_apis_with_options(request, runtime)

    async def describe_history_apis_async(
        self,
        request: cloud_api20160714_models.DescribeHistoryApisRequest,
    ) -> cloud_api20160714_models.DescribeHistoryApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_apis_with_options_async(request, runtime)

    def describe_ip_control_policy_items_with_options(
        self,
        request: cloud_api20160714_models.DescribeIpControlPolicyItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeIpControlPolicyItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PolicyItemId'] = request.policy_item_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeIpControlPolicyItems',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeIpControlPolicyItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_control_policy_items_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeIpControlPolicyItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeIpControlPolicyItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PolicyItemId'] = request.policy_item_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeIpControlPolicyItems',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeIpControlPolicyItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_control_policy_items(
        self,
        request: cloud_api20160714_models.DescribeIpControlPolicyItemsRequest,
    ) -> cloud_api20160714_models.DescribeIpControlPolicyItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_control_policy_items_with_options(request, runtime)

    async def describe_ip_control_policy_items_async(
        self,
        request: cloud_api20160714_models.DescribeIpControlPolicyItemsRequest,
    ) -> cloud_api20160714_models.DescribeIpControlPolicyItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_control_policy_items_with_options_async(request, runtime)

    def describe_ip_controls_with_options(
        self,
        request: cloud_api20160714_models.DescribeIpControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeIpControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['IpControlName'] = request.ip_control_name
        query['IpControlType'] = request.ip_control_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeIpControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeIpControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_controls_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeIpControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeIpControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['IpControlName'] = request.ip_control_name
        query['IpControlType'] = request.ip_control_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeIpControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeIpControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_controls(
        self,
        request: cloud_api20160714_models.DescribeIpControlsRequest,
    ) -> cloud_api20160714_models.DescribeIpControlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_controls_with_options(request, runtime)

    async def describe_ip_controls_async(
        self,
        request: cloud_api20160714_models.DescribeIpControlsRequest,
    ) -> cloud_api20160714_models.DescribeIpControlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_controls_with_options_async(request, runtime)

    def describe_log_config_with_options(
        self,
        request: cloud_api20160714_models.DescribeLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_config_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_config(
        self,
        request: cloud_api20160714_models.DescribeLogConfigRequest,
    ) -> cloud_api20160714_models.DescribeLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_config_with_options(request, runtime)

    async def describe_log_config_async(
        self,
        request: cloud_api20160714_models.DescribeLogConfigRequest,
    ) -> cloud_api20160714_models.DescribeLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_config_with_options_async(request, runtime)

    def describe_market_remains_quota_with_options(
        self,
        request: cloud_api20160714_models.DescribeMarketRemainsQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeMarketRemainsQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMarketRemainsQuota',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeMarketRemainsQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_market_remains_quota_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeMarketRemainsQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeMarketRemainsQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMarketRemainsQuota',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeMarketRemainsQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_market_remains_quota(
        self,
        request: cloud_api20160714_models.DescribeMarketRemainsQuotaRequest,
    ) -> cloud_api20160714_models.DescribeMarketRemainsQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_market_remains_quota_with_options(request, runtime)

    async def describe_market_remains_quota_async(
        self,
        request: cloud_api20160714_models.DescribeMarketRemainsQuotaRequest,
    ) -> cloud_api20160714_models.DescribeMarketRemainsQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_market_remains_quota_with_options_async(request, runtime)

    def describe_models_with_options(
        self,
        request: cloud_api20160714_models.DescribeModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['ModelId'] = request.model_id
        query['ModelName'] = request.model_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeModels',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_models_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['ModelId'] = request.model_id
        query['ModelName'] = request.model_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeModels',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_models(
        self,
        request: cloud_api20160714_models.DescribeModelsRequest,
    ) -> cloud_api20160714_models.DescribeModelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_models_with_options(request, runtime)

    async def describe_models_async(
        self,
        request: cloud_api20160714_models.DescribeModelsRequest,
    ) -> cloud_api20160714_models.DescribeModelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_models_with_options_async(request, runtime)

    def describe_plugin_schemas_with_options(
        self,
        request: cloud_api20160714_models.DescribePluginSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePluginSchemasResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePluginSchemas',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_plugin_schemas_with_options_async(
        self,
        request: cloud_api20160714_models.DescribePluginSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePluginSchemasResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePluginSchemas',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_plugin_schemas(
        self,
        request: cloud_api20160714_models.DescribePluginSchemasRequest,
    ) -> cloud_api20160714_models.DescribePluginSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_plugin_schemas_with_options(request, runtime)

    async def describe_plugin_schemas_async(
        self,
        request: cloud_api20160714_models.DescribePluginSchemasRequest,
    ) -> cloud_api20160714_models.DescribePluginSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_plugin_schemas_with_options_async(request, runtime)

    def describe_plugin_templates_with_options(
        self,
        request: cloud_api20160714_models.DescribePluginTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePluginTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Language'] = request.language
        query['PluginName'] = request.plugin_name
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePluginTemplates',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_plugin_templates_with_options_async(
        self,
        request: cloud_api20160714_models.DescribePluginTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePluginTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Language'] = request.language
        query['PluginName'] = request.plugin_name
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePluginTemplates',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_plugin_templates(
        self,
        request: cloud_api20160714_models.DescribePluginTemplatesRequest,
    ) -> cloud_api20160714_models.DescribePluginTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_plugin_templates_with_options(request, runtime)

    async def describe_plugin_templates_async(
        self,
        request: cloud_api20160714_models.DescribePluginTemplatesRequest,
    ) -> cloud_api20160714_models.DescribePluginTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_plugin_templates_with_options_async(request, runtime)

    def describe_plugins_with_options(
        self,
        request: cloud_api20160714_models.DescribePluginsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePluginsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PluginId'] = request.plugin_id
        query['PluginName'] = request.plugin_name
        query['PluginType'] = request.plugin_type
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePlugins',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_plugins_with_options_async(
        self,
        request: cloud_api20160714_models.DescribePluginsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePluginsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PluginId'] = request.plugin_id
        query['PluginName'] = request.plugin_name
        query['PluginType'] = request.plugin_type
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePlugins',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_plugins(
        self,
        request: cloud_api20160714_models.DescribePluginsRequest,
    ) -> cloud_api20160714_models.DescribePluginsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_plugins_with_options(request, runtime)

    async def describe_plugins_async(
        self,
        request: cloud_api20160714_models.DescribePluginsRequest,
    ) -> cloud_api20160714_models.DescribePluginsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_plugins_with_options_async(request, runtime)

    def describe_plugins_by_api_with_options(
        self,
        request: cloud_api20160714_models.DescribePluginsByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePluginsByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePluginsByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginsByApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_plugins_by_api_with_options_async(
        self,
        request: cloud_api20160714_models.DescribePluginsByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePluginsByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePluginsByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginsByApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_plugins_by_api(
        self,
        request: cloud_api20160714_models.DescribePluginsByApiRequest,
    ) -> cloud_api20160714_models.DescribePluginsByApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_plugins_by_api_with_options(request, runtime)

    async def describe_plugins_by_api_async(
        self,
        request: cloud_api20160714_models.DescribePluginsByApiRequest,
    ) -> cloud_api20160714_models.DescribePluginsByApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_plugins_by_api_with_options_async(request, runtime)

    def describe_purchased_api_group_with_options(
        self,
        request: cloud_api20160714_models.DescribePurchasedApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePurchasedApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_api_group_with_options_async(
        self,
        request: cloud_api20160714_models.DescribePurchasedApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePurchasedApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_api_group(
        self,
        request: cloud_api20160714_models.DescribePurchasedApiGroupRequest,
    ) -> cloud_api20160714_models.DescribePurchasedApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_group_with_options(request, runtime)

    async def describe_purchased_api_group_async(
        self,
        request: cloud_api20160714_models.DescribePurchasedApiGroupRequest,
    ) -> cloud_api20160714_models.DescribePurchasedApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_api_group_with_options_async(request, runtime)

    def describe_purchased_api_groups_with_options(
        self,
        request: cloud_api20160714_models.DescribePurchasedApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePurchasedApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroups',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_api_groups_with_options_async(
        self,
        request: cloud_api20160714_models.DescribePurchasedApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePurchasedApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroups',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_api_groups(
        self,
        request: cloud_api20160714_models.DescribePurchasedApiGroupsRequest,
    ) -> cloud_api20160714_models.DescribePurchasedApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_groups_with_options(request, runtime)

    async def describe_purchased_api_groups_async(
        self,
        request: cloud_api20160714_models.DescribePurchasedApiGroupsRequest,
    ) -> cloud_api20160714_models.DescribePurchasedApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_api_groups_with_options_async(request, runtime)

    def describe_purchased_apis_with_options(
        self,
        request: cloud_api20160714_models.DescribePurchasedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePurchasedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_apis_with_options_async(
        self,
        request: cloud_api20160714_models.DescribePurchasedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribePurchasedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_apis(
        self,
        request: cloud_api20160714_models.DescribePurchasedApisRequest,
    ) -> cloud_api20160714_models.DescribePurchasedApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_apis_with_options(request, runtime)

    async def describe_purchased_apis_async(
        self,
        request: cloud_api20160714_models.DescribePurchasedApisRequest,
    ) -> cloud_api20160714_models.DescribePurchasedApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_apis_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: cloud_api20160714_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: cloud_api20160714_models.DescribeRegionsRequest,
    ) -> cloud_api20160714_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: cloud_api20160714_models.DescribeRegionsRequest,
    ) -> cloud_api20160714_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_signatures_with_options(
        self,
        request: cloud_api20160714_models.DescribeSignaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeSignaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['SignatureName'] = request.signature_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSignatures',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_signatures_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeSignaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeSignaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['SignatureName'] = request.signature_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSignatures',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSignaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_signatures(
        self,
        request: cloud_api20160714_models.DescribeSignaturesRequest,
    ) -> cloud_api20160714_models.DescribeSignaturesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_signatures_with_options(request, runtime)

    async def describe_signatures_async(
        self,
        request: cloud_api20160714_models.DescribeSignaturesRequest,
    ) -> cloud_api20160714_models.DescribeSignaturesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_signatures_with_options_async(request, runtime)

    def describe_signatures_by_api_with_options(
        self,
        request: cloud_api20160714_models.DescribeSignaturesByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeSignaturesByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSignaturesByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSignaturesByApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_signatures_by_api_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeSignaturesByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeSignaturesByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSignaturesByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSignaturesByApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_signatures_by_api(
        self,
        request: cloud_api20160714_models.DescribeSignaturesByApiRequest,
    ) -> cloud_api20160714_models.DescribeSignaturesByApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_signatures_by_api_with_options(request, runtime)

    async def describe_signatures_by_api_async(
        self,
        request: cloud_api20160714_models.DescribeSignaturesByApiRequest,
    ) -> cloud_api20160714_models.DescribeSignaturesByApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_signatures_by_api_with_options_async(request, runtime)

    def describe_system_parameters_with_options(
        self,
        request: cloud_api20160714_models.DescribeSystemParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeSystemParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSystemParameters',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSystemParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_parameters_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeSystemParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeSystemParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSystemParameters',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSystemParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_parameters(
        self,
        request: cloud_api20160714_models.DescribeSystemParametersRequest,
    ) -> cloud_api20160714_models.DescribeSystemParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_system_parameters_with_options(request, runtime)

    async def describe_system_parameters_async(
        self,
        request: cloud_api20160714_models.DescribeSystemParametersRequest,
    ) -> cloud_api20160714_models.DescribeSystemParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_parameters_with_options_async(request, runtime)

    def describe_traffic_controls_with_options(
        self,
        request: cloud_api20160714_models.DescribeTrafficControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeTrafficControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['TrafficControlId'] = request.traffic_control_id
        query['TrafficControlName'] = request.traffic_control_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeTrafficControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_traffic_controls_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeTrafficControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeTrafficControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['TrafficControlId'] = request.traffic_control_id
        query['TrafficControlName'] = request.traffic_control_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeTrafficControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_traffic_controls(
        self,
        request: cloud_api20160714_models.DescribeTrafficControlsRequest,
    ) -> cloud_api20160714_models.DescribeTrafficControlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_controls_with_options(request, runtime)

    async def describe_traffic_controls_async(
        self,
        request: cloud_api20160714_models.DescribeTrafficControlsRequest,
    ) -> cloud_api20160714_models.DescribeTrafficControlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_traffic_controls_with_options_async(request, runtime)

    def describe_traffic_controls_by_api_with_options(
        self,
        request: cloud_api20160714_models.DescribeTrafficControlsByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeTrafficControlsByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControlsByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeTrafficControlsByApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_traffic_controls_by_api_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeTrafficControlsByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeTrafficControlsByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControlsByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeTrafficControlsByApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_traffic_controls_by_api(
        self,
        request: cloud_api20160714_models.DescribeTrafficControlsByApiRequest,
    ) -> cloud_api20160714_models.DescribeTrafficControlsByApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_controls_by_api_with_options(request, runtime)

    async def describe_traffic_controls_by_api_async(
        self,
        request: cloud_api20160714_models.DescribeTrafficControlsByApiRequest,
    ) -> cloud_api20160714_models.DescribeTrafficControlsByApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_traffic_controls_by_api_with_options_async(request, runtime)

    def describe_update_vpc_info_task_with_options(
        self,
        request: cloud_api20160714_models.DescribeUpdateVpcInfoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeUpdateVpcInfoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OperationUid'] = request.operation_uid
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUpdateVpcInfoTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeUpdateVpcInfoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_update_vpc_info_task_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeUpdateVpcInfoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeUpdateVpcInfoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OperationUid'] = request.operation_uid
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUpdateVpcInfoTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeUpdateVpcInfoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_update_vpc_info_task(
        self,
        request: cloud_api20160714_models.DescribeUpdateVpcInfoTaskRequest,
    ) -> cloud_api20160714_models.DescribeUpdateVpcInfoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_update_vpc_info_task_with_options(request, runtime)

    async def describe_update_vpc_info_task_async(
        self,
        request: cloud_api20160714_models.DescribeUpdateVpcInfoTaskRequest,
    ) -> cloud_api20160714_models.DescribeUpdateVpcInfoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_update_vpc_info_task_with_options_async(request, runtime)

    def describe_vpc_accesses_with_options(
        self,
        request: cloud_api20160714_models.DescribeVpcAccessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeVpcAccessesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['VpcAccessId'] = request.vpc_access_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVpcAccesses',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeVpcAccessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_accesses_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeVpcAccessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeVpcAccessesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['VpcAccessId'] = request.vpc_access_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVpcAccesses',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeVpcAccessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_accesses(
        self,
        request: cloud_api20160714_models.DescribeVpcAccessesRequest,
    ) -> cloud_api20160714_models.DescribeVpcAccessesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_accesses_with_options(request, runtime)

    async def describe_vpc_accesses_async(
        self,
        request: cloud_api20160714_models.DescribeVpcAccessesRequest,
    ) -> cloud_api20160714_models.DescribeVpcAccessesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_accesses_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: cloud_api20160714_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: cloud_api20160714_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: cloud_api20160714_models.DescribeZonesRequest,
    ) -> cloud_api20160714_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: cloud_api20160714_models.DescribeZonesRequest,
    ) -> cloud_api20160714_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def dry_run_swagger_with_options(
        self,
        tmp_req: cloud_api20160714_models.DryRunSwaggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DryRunSwaggerResponse:
        UtilClient.validate_model(tmp_req)
        request = cloud_api20160714_models.DryRunSwaggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_condition):
            request.global_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        query['DataFormat'] = request.data_format
        query['GlobalCondition'] = request.global_condition_shrink
        query['GroupId'] = request.group_id
        query['Overwrite'] = request.overwrite
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DryRunSwagger',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DryRunSwaggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def dry_run_swagger_with_options_async(
        self,
        tmp_req: cloud_api20160714_models.DryRunSwaggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.DryRunSwaggerResponse:
        UtilClient.validate_model(tmp_req)
        request = cloud_api20160714_models.DryRunSwaggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_condition):
            request.global_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        query['DataFormat'] = request.data_format
        query['GlobalCondition'] = request.global_condition_shrink
        query['GroupId'] = request.group_id
        query['Overwrite'] = request.overwrite
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DryRunSwagger',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DryRunSwaggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dry_run_swagger(
        self,
        request: cloud_api20160714_models.DryRunSwaggerRequest,
    ) -> cloud_api20160714_models.DryRunSwaggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.dry_run_swagger_with_options(request, runtime)

    async def dry_run_swagger_async(
        self,
        request: cloud_api20160714_models.DryRunSwaggerRequest,
    ) -> cloud_api20160714_models.DryRunSwaggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dry_run_swagger_with_options_async(request, runtime)

    def import_swagger_with_options(
        self,
        tmp_req: cloud_api20160714_models.ImportSwaggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ImportSwaggerResponse:
        UtilClient.validate_model(tmp_req)
        request = cloud_api20160714_models.ImportSwaggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_condition):
            request.global_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        query['DataFormat'] = request.data_format
        query['DryRun'] = request.dry_run
        query['GlobalCondition'] = request.global_condition_shrink
        query['GroupId'] = request.group_id
        query['Overwrite'] = request.overwrite
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportSwagger',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ImportSwaggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_swagger_with_options_async(
        self,
        tmp_req: cloud_api20160714_models.ImportSwaggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ImportSwaggerResponse:
        UtilClient.validate_model(tmp_req)
        request = cloud_api20160714_models.ImportSwaggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_condition):
            request.global_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        query['DataFormat'] = request.data_format
        query['DryRun'] = request.dry_run
        query['GlobalCondition'] = request.global_condition_shrink
        query['GroupId'] = request.group_id
        query['Overwrite'] = request.overwrite
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportSwagger',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ImportSwaggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_swagger(
        self,
        request: cloud_api20160714_models.ImportSwaggerRequest,
    ) -> cloud_api20160714_models.ImportSwaggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_swagger_with_options(request, runtime)

    async def import_swagger_async(
        self,
        request: cloud_api20160714_models.ImportSwaggerRequest,
    ) -> cloud_api20160714_models.ImportSwaggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_swagger_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: cloud_api20160714_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: cloud_api20160714_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: cloud_api20160714_models.ListTagResourcesRequest,
    ) -> cloud_api20160714_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: cloud_api20160714_models.ListTagResourcesRequest,
    ) -> cloud_api20160714_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_api_with_options(
        self,
        request: cloud_api20160714_models.ModifyApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AllowSignatureMethod'] = request.allow_signature_method
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['AppCodeAuthType'] = request.app_code_auth_type
        query['AuthType'] = request.auth_type
        query['ConstantParameters'] = request.constant_parameters
        query['Description'] = request.description
        query['DisableInternet'] = request.disable_internet
        query['ErrorCodeSamples'] = request.error_code_samples
        query['FailResultSample'] = request.fail_result_sample
        query['ForceNonceCheck'] = request.force_nonce_check
        query['GroupId'] = request.group_id
        query['OpenIdConnectConfig'] = request.open_id_connect_config
        query['RequestConfig'] = request.request_config
        query['RequestParameters'] = request.request_parameters
        query['ResultBodyModel'] = request.result_body_model
        query['ResultDescriptions'] = request.result_descriptions
        query['ResultSample'] = request.result_sample
        query['ResultType'] = request.result_type
        query['SecurityToken'] = request.security_token
        query['ServiceConfig'] = request.service_config
        query['ServiceParameters'] = request.service_parameters
        query['ServiceParametersMap'] = request.service_parameters_map
        query['SystemParameters'] = request.system_parameters
        query['Visibility'] = request.visibility
        query['WebSocketApiType'] = request.web_socket_api_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_with_options_async(
        self,
        request: cloud_api20160714_models.ModifyApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AllowSignatureMethod'] = request.allow_signature_method
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['AppCodeAuthType'] = request.app_code_auth_type
        query['AuthType'] = request.auth_type
        query['ConstantParameters'] = request.constant_parameters
        query['Description'] = request.description
        query['DisableInternet'] = request.disable_internet
        query['ErrorCodeSamples'] = request.error_code_samples
        query['FailResultSample'] = request.fail_result_sample
        query['ForceNonceCheck'] = request.force_nonce_check
        query['GroupId'] = request.group_id
        query['OpenIdConnectConfig'] = request.open_id_connect_config
        query['RequestConfig'] = request.request_config
        query['RequestParameters'] = request.request_parameters
        query['ResultBodyModel'] = request.result_body_model
        query['ResultDescriptions'] = request.result_descriptions
        query['ResultSample'] = request.result_sample
        query['ResultType'] = request.result_type
        query['SecurityToken'] = request.security_token
        query['ServiceConfig'] = request.service_config
        query['ServiceParameters'] = request.service_parameters
        query['ServiceParametersMap'] = request.service_parameters_map
        query['SystemParameters'] = request.system_parameters
        query['Visibility'] = request.visibility
        query['WebSocketApiType'] = request.web_socket_api_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api(
        self,
        request: cloud_api20160714_models.ModifyApiRequest,
    ) -> cloud_api20160714_models.ModifyApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_api_with_options(request, runtime)

    async def modify_api_async(
        self,
        request: cloud_api20160714_models.ModifyApiRequest,
    ) -> cloud_api20160714_models.ModifyApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_with_options_async(request, runtime)

    def modify_api_group_with_options(
        self,
        request: cloud_api20160714_models.ModifyApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BasePath'] = request.base_path
        query['CompatibleFlags'] = request.compatible_flags
        query['CustomTraceConfig'] = request.custom_trace_config
        query['CustomerConfigs'] = request.customer_configs
        query['DefaultDomain'] = request.default_domain
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['GroupName'] = request.group_name
        query['PassthroughHeaders'] = request.passthrough_headers
        query['RpcPattern'] = request.rpc_pattern
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        query['UserLogConfig'] = request.user_log_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_group_with_options_async(
        self,
        request: cloud_api20160714_models.ModifyApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BasePath'] = request.base_path
        query['CompatibleFlags'] = request.compatible_flags
        query['CustomTraceConfig'] = request.custom_trace_config
        query['CustomerConfigs'] = request.customer_configs
        query['DefaultDomain'] = request.default_domain
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['GroupName'] = request.group_name
        query['PassthroughHeaders'] = request.passthrough_headers
        query['RpcPattern'] = request.rpc_pattern
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        query['UserLogConfig'] = request.user_log_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_group(
        self,
        request: cloud_api20160714_models.ModifyApiGroupRequest,
    ) -> cloud_api20160714_models.ModifyApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_api_group_with_options(request, runtime)

    async def modify_api_group_async(
        self,
        request: cloud_api20160714_models.ModifyApiGroupRequest,
    ) -> cloud_api20160714_models.ModifyApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_group_with_options_async(request, runtime)

    def modify_api_group_vpc_whitelist_with_options(
        self,
        request: cloud_api20160714_models.ModifyApiGroupVpcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyApiGroupVpcWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['VpcIds'] = request.vpc_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApiGroupVpcWhitelist',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiGroupVpcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_group_vpc_whitelist_with_options_async(
        self,
        request: cloud_api20160714_models.ModifyApiGroupVpcWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyApiGroupVpcWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['VpcIds'] = request.vpc_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApiGroupVpcWhitelist',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiGroupVpcWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_group_vpc_whitelist(
        self,
        request: cloud_api20160714_models.ModifyApiGroupVpcWhitelistRequest,
    ) -> cloud_api20160714_models.ModifyApiGroupVpcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_api_group_vpc_whitelist_with_options(request, runtime)

    async def modify_api_group_vpc_whitelist_async(
        self,
        request: cloud_api20160714_models.ModifyApiGroupVpcWhitelistRequest,
    ) -> cloud_api20160714_models.ModifyApiGroupVpcWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_group_vpc_whitelist_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: cloud_api20160714_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AppName'] = request.app_name
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: cloud_api20160714_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AppName'] = request.app_name
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        request: cloud_api20160714_models.ModifyAppRequest,
    ) -> cloud_api20160714_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: cloud_api20160714_models.ModifyAppRequest,
    ) -> cloud_api20160714_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_instance_spec_with_options(
        self,
        request: cloud_api20160714_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutoPay'] = request.auto_pay
        query['InstanceId'] = request.instance_id
        query['InstanceSpec'] = request.instance_spec
        query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_spec_with_options_async(
        self,
        request: cloud_api20160714_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutoPay'] = request.auto_pay
        query['InstanceId'] = request.instance_id
        query['InstanceSpec'] = request.instance_spec
        query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_spec(
        self,
        request: cloud_api20160714_models.ModifyInstanceSpecRequest,
    ) -> cloud_api20160714_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    async def modify_instance_spec_async(
        self,
        request: cloud_api20160714_models.ModifyInstanceSpecRequest,
    ) -> cloud_api20160714_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_spec_with_options_async(request, runtime)

    def modify_ip_control_with_options(
        self,
        request: cloud_api20160714_models.ModifyIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['IpControlId'] = request.ip_control_id
        query['IpControlName'] = request.ip_control_name
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ip_control_with_options_async(
        self,
        request: cloud_api20160714_models.ModifyIpControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyIpControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['IpControlId'] = request.ip_control_id
        query['IpControlName'] = request.ip_control_name
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyIpControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ip_control(
        self,
        request: cloud_api20160714_models.ModifyIpControlRequest,
    ) -> cloud_api20160714_models.ModifyIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_control_with_options(request, runtime)

    async def modify_ip_control_async(
        self,
        request: cloud_api20160714_models.ModifyIpControlRequest,
    ) -> cloud_api20160714_models.ModifyIpControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ip_control_with_options_async(request, runtime)

    def modify_ip_control_policy_item_with_options(
        self,
        request: cloud_api20160714_models.ModifyIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CidrIp'] = request.cidr_ip
        query['IpControlId'] = request.ip_control_id
        query['PolicyItemId'] = request.policy_item_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ip_control_policy_item_with_options_async(
        self,
        request: cloud_api20160714_models.ModifyIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CidrIp'] = request.cidr_ip
        query['IpControlId'] = request.ip_control_id
        query['PolicyItemId'] = request.policy_item_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyIpControlPolicyItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ip_control_policy_item(
        self,
        request: cloud_api20160714_models.ModifyIpControlPolicyItemRequest,
    ) -> cloud_api20160714_models.ModifyIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_control_policy_item_with_options(request, runtime)

    async def modify_ip_control_policy_item_async(
        self,
        request: cloud_api20160714_models.ModifyIpControlPolicyItemRequest,
    ) -> cloud_api20160714_models.ModifyIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ip_control_policy_item_with_options_async(request, runtime)

    def modify_log_config_with_options(
        self,
        request: cloud_api20160714_models.ModifyLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        query['SlsLogStore'] = request.sls_log_store
        query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_log_config_with_options_async(
        self,
        request: cloud_api20160714_models.ModifyLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        query['SlsLogStore'] = request.sls_log_store
        query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_log_config(
        self,
        request: cloud_api20160714_models.ModifyLogConfigRequest,
    ) -> cloud_api20160714_models.ModifyLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_log_config_with_options(request, runtime)

    async def modify_log_config_async(
        self,
        request: cloud_api20160714_models.ModifyLogConfigRequest,
    ) -> cloud_api20160714_models.ModifyLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_log_config_with_options_async(request, runtime)

    def modify_model_with_options(
        self,
        request: cloud_api20160714_models.ModifyModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['ModelName'] = request.model_name
        query['NewModelName'] = request.new_model_name
        query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_model_with_options_async(
        self,
        request: cloud_api20160714_models.ModifyModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['ModelName'] = request.model_name
        query['NewModelName'] = request.new_model_name
        query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_model(
        self,
        request: cloud_api20160714_models.ModifyModelRequest,
    ) -> cloud_api20160714_models.ModifyModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_model_with_options(request, runtime)

    async def modify_model_async(
        self,
        request: cloud_api20160714_models.ModifyModelRequest,
    ) -> cloud_api20160714_models.ModifyModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_model_with_options_async(request, runtime)

    def modify_plugin_with_options(
        self,
        request: cloud_api20160714_models.ModifyPluginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyPluginResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['PluginData'] = request.plugin_data
        query['PluginId'] = request.plugin_id
        query['PluginName'] = request.plugin_name
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyPlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_plugin_with_options_async(
        self,
        request: cloud_api20160714_models.ModifyPluginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyPluginResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['PluginData'] = request.plugin_data
        query['PluginId'] = request.plugin_id
        query['PluginName'] = request.plugin_name
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyPlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_plugin(
        self,
        request: cloud_api20160714_models.ModifyPluginRequest,
    ) -> cloud_api20160714_models.ModifyPluginResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_plugin_with_options(request, runtime)

    async def modify_plugin_async(
        self,
        request: cloud_api20160714_models.ModifyPluginRequest,
    ) -> cloud_api20160714_models.ModifyPluginResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_plugin_with_options_async(request, runtime)

    def modify_signature_with_options(
        self,
        request: cloud_api20160714_models.ModifySignatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifySignatureResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['SignatureKey'] = request.signature_key
        query['SignatureName'] = request.signature_name
        query['SignatureSecret'] = request.signature_secret
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifySignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_signature_with_options_async(
        self,
        request: cloud_api20160714_models.ModifySignatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifySignatureResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['SignatureKey'] = request.signature_key
        query['SignatureName'] = request.signature_name
        query['SignatureSecret'] = request.signature_secret
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifySignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_signature(
        self,
        request: cloud_api20160714_models.ModifySignatureRequest,
    ) -> cloud_api20160714_models.ModifySignatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_signature_with_options(request, runtime)

    async def modify_signature_async(
        self,
        request: cloud_api20160714_models.ModifySignatureRequest,
    ) -> cloud_api20160714_models.ModifySignatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_signature_with_options_async(request, runtime)

    def modify_traffic_control_with_options(
        self,
        request: cloud_api20160714_models.ModifyTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiDefault'] = request.api_default
        query['AppDefault'] = request.app_default
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        query['TrafficControlName'] = request.traffic_control_name
        query['TrafficControlUnit'] = request.traffic_control_unit
        query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_traffic_control_with_options_async(
        self,
        request: cloud_api20160714_models.ModifyTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ModifyTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiDefault'] = request.api_default
        query['AppDefault'] = request.app_default
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        query['TrafficControlName'] = request.traffic_control_name
        query['TrafficControlUnit'] = request.traffic_control_unit
        query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_traffic_control(
        self,
        request: cloud_api20160714_models.ModifyTrafficControlRequest,
    ) -> cloud_api20160714_models.ModifyTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_traffic_control_with_options(request, runtime)

    async def modify_traffic_control_async(
        self,
        request: cloud_api20160714_models.ModifyTrafficControlRequest,
    ) -> cloud_api20160714_models.ModifyTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_traffic_control_with_options_async(request, runtime)

    def open_api_gateway_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.OpenApiGatewayServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenApiGatewayService',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.OpenApiGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_api_gateway_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.OpenApiGatewayServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenApiGatewayService',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.OpenApiGatewayServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_api_gateway_service(self) -> cloud_api20160714_models.OpenApiGatewayServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_api_gateway_service_with_options(runtime)

    async def open_api_gateway_service_async(self) -> cloud_api20160714_models.OpenApiGatewayServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_api_gateway_service_with_options_async(runtime)

    def reactivate_domain_with_options(
        self,
        request: cloud_api20160714_models.ReactivateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ReactivateDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReactivateDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ReactivateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def reactivate_domain_with_options_async(
        self,
        request: cloud_api20160714_models.ReactivateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ReactivateDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReactivateDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ReactivateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reactivate_domain(
        self,
        request: cloud_api20160714_models.ReactivateDomainRequest,
    ) -> cloud_api20160714_models.ReactivateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.reactivate_domain_with_options(request, runtime)

    async def reactivate_domain_async(
        self,
        request: cloud_api20160714_models.ReactivateDomainRequest,
    ) -> cloud_api20160714_models.ReactivateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reactivate_domain_with_options_async(request, runtime)

    def remove_apis_authorities_with_options(
        self,
        request: cloud_api20160714_models.RemoveApisAuthoritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveApisAuthoritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['AppId'] = request.app_id
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveApisAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveApisAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_apis_authorities_with_options_async(
        self,
        request: cloud_api20160714_models.RemoveApisAuthoritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveApisAuthoritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['AppId'] = request.app_id
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveApisAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveApisAuthoritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_apis_authorities(
        self,
        request: cloud_api20160714_models.RemoveApisAuthoritiesRequest,
    ) -> cloud_api20160714_models.RemoveApisAuthoritiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_apis_authorities_with_options(request, runtime)

    async def remove_apis_authorities_async(
        self,
        request: cloud_api20160714_models.RemoveApisAuthoritiesRequest,
    ) -> cloud_api20160714_models.RemoveApisAuthoritiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_apis_authorities_with_options_async(request, runtime)

    def remove_apps_authorities_with_options(
        self,
        request: cloud_api20160714_models.RemoveAppsAuthoritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveAppsAuthoritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['AppIds'] = request.app_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveAppsAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveAppsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_apps_authorities_with_options_async(
        self,
        request: cloud_api20160714_models.RemoveAppsAuthoritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveAppsAuthoritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['AppIds'] = request.app_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveAppsAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveAppsAuthoritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_apps_authorities(
        self,
        request: cloud_api20160714_models.RemoveAppsAuthoritiesRequest,
    ) -> cloud_api20160714_models.RemoveAppsAuthoritiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_apps_authorities_with_options(request, runtime)

    async def remove_apps_authorities_async(
        self,
        request: cloud_api20160714_models.RemoveAppsAuthoritiesRequest,
    ) -> cloud_api20160714_models.RemoveAppsAuthoritiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_apps_authorities_with_options_async(request, runtime)

    def remove_ip_control_apis_with_options(
        self,
        request: cloud_api20160714_models.RemoveIpControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveIpControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveIpControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveIpControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_ip_control_apis_with_options_async(
        self,
        request: cloud_api20160714_models.RemoveIpControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveIpControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveIpControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveIpControlApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_ip_control_apis(
        self,
        request: cloud_api20160714_models.RemoveIpControlApisRequest,
    ) -> cloud_api20160714_models.RemoveIpControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_ip_control_apis_with_options(request, runtime)

    async def remove_ip_control_apis_async(
        self,
        request: cloud_api20160714_models.RemoveIpControlApisRequest,
    ) -> cloud_api20160714_models.RemoveIpControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_ip_control_apis_with_options_async(request, runtime)

    def remove_ip_control_policy_item_with_options(
        self,
        request: cloud_api20160714_models.RemoveIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['PolicyItemIds'] = request.policy_item_ids
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_ip_control_policy_item_with_options_async(
        self,
        request: cloud_api20160714_models.RemoveIpControlPolicyItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveIpControlPolicyItemResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['PolicyItemIds'] = request.policy_item_ids
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveIpControlPolicyItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_ip_control_policy_item(
        self,
        request: cloud_api20160714_models.RemoveIpControlPolicyItemRequest,
    ) -> cloud_api20160714_models.RemoveIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_ip_control_policy_item_with_options(request, runtime)

    async def remove_ip_control_policy_item_async(
        self,
        request: cloud_api20160714_models.RemoveIpControlPolicyItemRequest,
    ) -> cloud_api20160714_models.RemoveIpControlPolicyItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_ip_control_policy_item_with_options_async(request, runtime)

    def remove_signature_apis_with_options(
        self,
        request: cloud_api20160714_models.RemoveSignatureApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveSignatureApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveSignatureApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveSignatureApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_signature_apis_with_options_async(
        self,
        request: cloud_api20160714_models.RemoveSignatureApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveSignatureApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveSignatureApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveSignatureApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_signature_apis(
        self,
        request: cloud_api20160714_models.RemoveSignatureApisRequest,
    ) -> cloud_api20160714_models.RemoveSignatureApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_signature_apis_with_options(request, runtime)

    async def remove_signature_apis_async(
        self,
        request: cloud_api20160714_models.RemoveSignatureApisRequest,
    ) -> cloud_api20160714_models.RemoveSignatureApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_signature_apis_with_options_async(request, runtime)

    def remove_traffic_control_apis_with_options(
        self,
        request: cloud_api20160714_models.RemoveTrafficControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveTrafficControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveTrafficControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveTrafficControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_traffic_control_apis_with_options_async(
        self,
        request: cloud_api20160714_models.RemoveTrafficControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveTrafficControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveTrafficControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveTrafficControlApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_traffic_control_apis(
        self,
        request: cloud_api20160714_models.RemoveTrafficControlApisRequest,
    ) -> cloud_api20160714_models.RemoveTrafficControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_traffic_control_apis_with_options(request, runtime)

    async def remove_traffic_control_apis_async(
        self,
        request: cloud_api20160714_models.RemoveTrafficControlApisRequest,
    ) -> cloud_api20160714_models.RemoveTrafficControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_traffic_control_apis_with_options_async(request, runtime)

    def remove_vpc_access_with_options(
        self,
        request: cloud_api20160714_models.RemoveVpcAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveVpcAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NeedBatchWork'] = request.need_batch_work
        query['Port'] = request.port
        query['SecurityToken'] = request.security_token
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveVpcAccess',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveVpcAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_vpc_access_with_options_async(
        self,
        request: cloud_api20160714_models.RemoveVpcAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveVpcAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NeedBatchWork'] = request.need_batch_work
        query['Port'] = request.port
        query['SecurityToken'] = request.security_token
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveVpcAccess',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveVpcAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_vpc_access(
        self,
        request: cloud_api20160714_models.RemoveVpcAccessRequest,
    ) -> cloud_api20160714_models.RemoveVpcAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_vpc_access_with_options(request, runtime)

    async def remove_vpc_access_async(
        self,
        request: cloud_api20160714_models.RemoveVpcAccessRequest,
    ) -> cloud_api20160714_models.RemoveVpcAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_vpc_access_with_options_async(request, runtime)

    def remove_vpc_access_and_abolish_apis_with_options(
        self,
        request: cloud_api20160714_models.RemoveVpcAccessAndAbolishApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveVpcAccessAndAbolishApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NeedBatchWork'] = request.need_batch_work
        query['Port'] = request.port
        query['SecurityToken'] = request.security_token
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveVpcAccessAndAbolishApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveVpcAccessAndAbolishApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_vpc_access_and_abolish_apis_with_options_async(
        self,
        request: cloud_api20160714_models.RemoveVpcAccessAndAbolishApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.RemoveVpcAccessAndAbolishApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NeedBatchWork'] = request.need_batch_work
        query['Port'] = request.port
        query['SecurityToken'] = request.security_token
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveVpcAccessAndAbolishApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveVpcAccessAndAbolishApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_vpc_access_and_abolish_apis(
        self,
        request: cloud_api20160714_models.RemoveVpcAccessAndAbolishApisRequest,
    ) -> cloud_api20160714_models.RemoveVpcAccessAndAbolishApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_vpc_access_and_abolish_apis_with_options(request, runtime)

    async def remove_vpc_access_and_abolish_apis_async(
        self,
        request: cloud_api20160714_models.RemoveVpcAccessAndAbolishApisRequest,
    ) -> cloud_api20160714_models.RemoveVpcAccessAndAbolishApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_vpc_access_and_abolish_apis_with_options_async(request, runtime)

    def reset_app_code_with_options(
        self,
        request: cloud_api20160714_models.ResetAppCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ResetAppCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppCode'] = request.app_code
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAppCode',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ResetAppCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_app_code_with_options_async(
        self,
        request: cloud_api20160714_models.ResetAppCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ResetAppCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppCode'] = request.app_code
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAppCode',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ResetAppCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_app_code(
        self,
        request: cloud_api20160714_models.ResetAppCodeRequest,
    ) -> cloud_api20160714_models.ResetAppCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_app_code_with_options(request, runtime)

    async def reset_app_code_async(
        self,
        request: cloud_api20160714_models.ResetAppCodeRequest,
    ) -> cloud_api20160714_models.ResetAppCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_app_code_with_options_async(request, runtime)

    def reset_app_secret_with_options(
        self,
        request: cloud_api20160714_models.ResetAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ResetAppSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppKey'] = request.app_key
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAppSecret',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ResetAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_app_secret_with_options_async(
        self,
        request: cloud_api20160714_models.ResetAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.ResetAppSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppKey'] = request.app_key
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAppSecret',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ResetAppSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_app_secret(
        self,
        request: cloud_api20160714_models.ResetAppSecretRequest,
    ) -> cloud_api20160714_models.ResetAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_app_secret_with_options(request, runtime)

    async def reset_app_secret_async(
        self,
        request: cloud_api20160714_models.ResetAppSecretRequest,
    ) -> cloud_api20160714_models.ResetAppSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_app_secret_with_options_async(request, runtime)

    def sdk_generate_by_app_with_options(
        self,
        request: cloud_api20160714_models.SdkGenerateByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SdkGenerateByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SdkGenerateByApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SdkGenerateByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdk_generate_by_app_with_options_async(
        self,
        request: cloud_api20160714_models.SdkGenerateByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SdkGenerateByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SdkGenerateByApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SdkGenerateByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdk_generate_by_app(
        self,
        request: cloud_api20160714_models.SdkGenerateByAppRequest,
    ) -> cloud_api20160714_models.SdkGenerateByAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_by_app_with_options(request, runtime)

    async def sdk_generate_by_app_async(
        self,
        request: cloud_api20160714_models.SdkGenerateByAppRequest,
    ) -> cloud_api20160714_models.SdkGenerateByAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sdk_generate_by_app_with_options_async(request, runtime)

    def sdk_generate_by_group_with_options(
        self,
        request: cloud_api20160714_models.SdkGenerateByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SdkGenerateByGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SdkGenerateByGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SdkGenerateByGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdk_generate_by_group_with_options_async(
        self,
        request: cloud_api20160714_models.SdkGenerateByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SdkGenerateByGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SdkGenerateByGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SdkGenerateByGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdk_generate_by_group(
        self,
        request: cloud_api20160714_models.SdkGenerateByGroupRequest,
    ) -> cloud_api20160714_models.SdkGenerateByGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_by_group_with_options(request, runtime)

    async def sdk_generate_by_group_async(
        self,
        request: cloud_api20160714_models.SdkGenerateByGroupRequest,
    ) -> cloud_api20160714_models.SdkGenerateByGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sdk_generate_by_group_with_options_async(request, runtime)

    def set_apis_authorities_with_options(
        self,
        request: cloud_api20160714_models.SetApisAuthoritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetApisAuthoritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['AppId'] = request.app_id
        query['AuthValidTime'] = request.auth_valid_time
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetApisAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetApisAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_apis_authorities_with_options_async(
        self,
        request: cloud_api20160714_models.SetApisAuthoritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetApisAuthoritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['AppId'] = request.app_id
        query['AuthValidTime'] = request.auth_valid_time
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetApisAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetApisAuthoritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_apis_authorities(
        self,
        request: cloud_api20160714_models.SetApisAuthoritiesRequest,
    ) -> cloud_api20160714_models.SetApisAuthoritiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_apis_authorities_with_options(request, runtime)

    async def set_apis_authorities_async(
        self,
        request: cloud_api20160714_models.SetApisAuthoritiesRequest,
    ) -> cloud_api20160714_models.SetApisAuthoritiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_apis_authorities_with_options_async(request, runtime)

    def set_apps_authorities_with_options(
        self,
        request: cloud_api20160714_models.SetAppsAuthoritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetAppsAuthoritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['AppIds'] = request.app_ids
        query['AuthValidTime'] = request.auth_valid_time
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetAppsAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetAppsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_apps_authorities_with_options_async(
        self,
        request: cloud_api20160714_models.SetAppsAuthoritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetAppsAuthoritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['AppIds'] = request.app_ids
        query['AuthValidTime'] = request.auth_valid_time
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetAppsAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetAppsAuthoritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_apps_authorities(
        self,
        request: cloud_api20160714_models.SetAppsAuthoritiesRequest,
    ) -> cloud_api20160714_models.SetAppsAuthoritiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_apps_authorities_with_options(request, runtime)

    async def set_apps_authorities_async(
        self,
        request: cloud_api20160714_models.SetAppsAuthoritiesRequest,
    ) -> cloud_api20160714_models.SetAppsAuthoritiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_apps_authorities_with_options_async(request, runtime)

    def set_domain_with_options(
        self,
        request: cloud_api20160714_models.SetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BindStageName'] = request.bind_stage_name
        query['CustomDomainType'] = request.custom_domain_type
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['IsForce'] = request.is_force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_with_options_async(
        self,
        request: cloud_api20160714_models.SetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BindStageName'] = request.bind_stage_name
        query['CustomDomainType'] = request.custom_domain_type
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['IsForce'] = request.is_force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain(
        self,
        request: cloud_api20160714_models.SetDomainRequest,
    ) -> cloud_api20160714_models.SetDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_with_options(request, runtime)

    async def set_domain_async(
        self,
        request: cloud_api20160714_models.SetDomainRequest,
    ) -> cloud_api20160714_models.SetDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_with_options_async(request, runtime)

    def set_domain_certificate_with_options(
        self,
        request: cloud_api20160714_models.SetDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CaCertificateBody'] = request.ca_certificate_body
        query['CertificateBody'] = request.certificate_body
        query['CertificateName'] = request.certificate_name
        query['CertificatePrivateKey'] = request.certificate_private_key
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomainCertificate',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_certificate_with_options_async(
        self,
        request: cloud_api20160714_models.SetDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CaCertificateBody'] = request.ca_certificate_body
        query['CertificateBody'] = request.certificate_body
        query['CertificateName'] = request.certificate_name
        query['CertificatePrivateKey'] = request.certificate_private_key
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomainCertificate',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_certificate(
        self,
        request: cloud_api20160714_models.SetDomainCertificateRequest,
    ) -> cloud_api20160714_models.SetDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_certificate_with_options(request, runtime)

    async def set_domain_certificate_async(
        self,
        request: cloud_api20160714_models.SetDomainCertificateRequest,
    ) -> cloud_api20160714_models.SetDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_certificate_with_options_async(request, runtime)

    def set_domain_web_socket_status_with_options(
        self,
        request: cloud_api20160714_models.SetDomainWebSocketStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetDomainWebSocketStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActionValue'] = request.action_value
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomainWebSocketStatus',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainWebSocketStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_web_socket_status_with_options_async(
        self,
        request: cloud_api20160714_models.SetDomainWebSocketStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetDomainWebSocketStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActionValue'] = request.action_value
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomainWebSocketStatus',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainWebSocketStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_web_socket_status(
        self,
        request: cloud_api20160714_models.SetDomainWebSocketStatusRequest,
    ) -> cloud_api20160714_models.SetDomainWebSocketStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_web_socket_status_with_options(request, runtime)

    async def set_domain_web_socket_status_async(
        self,
        request: cloud_api20160714_models.SetDomainWebSocketStatusRequest,
    ) -> cloud_api20160714_models.SetDomainWebSocketStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_web_socket_status_with_options_async(request, runtime)

    def set_ip_control_apis_with_options(
        self,
        request: cloud_api20160714_models.SetIpControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetIpControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetIpControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetIpControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_ip_control_apis_with_options_async(
        self,
        request: cloud_api20160714_models.SetIpControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetIpControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetIpControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetIpControlApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_ip_control_apis(
        self,
        request: cloud_api20160714_models.SetIpControlApisRequest,
    ) -> cloud_api20160714_models.SetIpControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_ip_control_apis_with_options(request, runtime)

    async def set_ip_control_apis_async(
        self,
        request: cloud_api20160714_models.SetIpControlApisRequest,
    ) -> cloud_api20160714_models.SetIpControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_ip_control_apis_with_options_async(request, runtime)

    def set_signature_apis_with_options(
        self,
        request: cloud_api20160714_models.SetSignatureApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetSignatureApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetSignatureApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetSignatureApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_signature_apis_with_options_async(
        self,
        request: cloud_api20160714_models.SetSignatureApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetSignatureApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetSignatureApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetSignatureApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_signature_apis(
        self,
        request: cloud_api20160714_models.SetSignatureApisRequest,
    ) -> cloud_api20160714_models.SetSignatureApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_signature_apis_with_options(request, runtime)

    async def set_signature_apis_async(
        self,
        request: cloud_api20160714_models.SetSignatureApisRequest,
    ) -> cloud_api20160714_models.SetSignatureApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_signature_apis_with_options_async(request, runtime)

    def set_traffic_control_apis_with_options(
        self,
        request: cloud_api20160714_models.SetTrafficControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetTrafficControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetTrafficControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetTrafficControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_traffic_control_apis_with_options_async(
        self,
        request: cloud_api20160714_models.SetTrafficControlApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetTrafficControlApisResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetTrafficControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetTrafficControlApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_traffic_control_apis(
        self,
        request: cloud_api20160714_models.SetTrafficControlApisRequest,
    ) -> cloud_api20160714_models.SetTrafficControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_traffic_control_apis_with_options(request, runtime)

    async def set_traffic_control_apis_async(
        self,
        request: cloud_api20160714_models.SetTrafficControlApisRequest,
    ) -> cloud_api20160714_models.SetTrafficControlApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_traffic_control_apis_with_options_async(request, runtime)

    def set_vpc_access_with_options(
        self,
        request: cloud_api20160714_models.SetVpcAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetVpcAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['Port'] = request.port
        query['SecurityToken'] = request.security_token
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetVpcAccess',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetVpcAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_vpc_access_with_options_async(
        self,
        request: cloud_api20160714_models.SetVpcAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetVpcAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['Port'] = request.port
        query['SecurityToken'] = request.security_token
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetVpcAccess',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetVpcAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_vpc_access(
        self,
        request: cloud_api20160714_models.SetVpcAccessRequest,
    ) -> cloud_api20160714_models.SetVpcAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_vpc_access_with_options(request, runtime)

    async def set_vpc_access_async(
        self,
        request: cloud_api20160714_models.SetVpcAccessRequest,
    ) -> cloud_api20160714_models.SetVpcAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_vpc_access_with_options_async(request, runtime)

    def set_wildcard_domain_patterns_with_options(
        self,
        request: cloud_api20160714_models.SetWildcardDomainPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetWildcardDomainPatternsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['WildcardDomainPatterns'] = request.wildcard_domain_patterns
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetWildcardDomainPatterns',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetWildcardDomainPatternsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_wildcard_domain_patterns_with_options_async(
        self,
        request: cloud_api20160714_models.SetWildcardDomainPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SetWildcardDomainPatternsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['WildcardDomainPatterns'] = request.wildcard_domain_patterns
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetWildcardDomainPatterns',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetWildcardDomainPatternsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_wildcard_domain_patterns(
        self,
        request: cloud_api20160714_models.SetWildcardDomainPatternsRequest,
    ) -> cloud_api20160714_models.SetWildcardDomainPatternsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_wildcard_domain_patterns_with_options(request, runtime)

    async def set_wildcard_domain_patterns_async(
        self,
        request: cloud_api20160714_models.SetWildcardDomainPatternsRequest,
    ) -> cloud_api20160714_models.SetWildcardDomainPatternsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_wildcard_domain_patterns_with_options_async(request, runtime)

    def switch_api_with_options(
        self,
        request: cloud_api20160714_models.SwitchApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SwitchApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['HistoryVersion'] = request.history_version
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SwitchApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_api_with_options_async(
        self,
        request: cloud_api20160714_models.SwitchApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.SwitchApiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['HistoryVersion'] = request.history_version
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SwitchApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_api(
        self,
        request: cloud_api20160714_models.SwitchApiRequest,
    ) -> cloud_api20160714_models.SwitchApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_api_with_options(request, runtime)

    async def switch_api_async(
        self,
        request: cloud_api20160714_models.SwitchApiRequest,
    ) -> cloud_api20160714_models.SwitchApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_api_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: cloud_api20160714_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: cloud_api20160714_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: cloud_api20160714_models.TagResourcesRequest,
    ) -> cloud_api20160714_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: cloud_api20160714_models.TagResourcesRequest,
    ) -> cloud_api20160714_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: cloud_api20160714_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['SecurityToken'] = request.security_token
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: cloud_api20160714_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160714_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['SecurityToken'] = request.security_token
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: cloud_api20160714_models.UntagResourcesRequest,
    ) -> cloud_api20160714_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: cloud_api20160714_models.UntagResourcesRequest,
    ) -> cloud_api20160714_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
