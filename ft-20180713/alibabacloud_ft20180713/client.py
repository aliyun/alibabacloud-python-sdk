# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ft20180713 import models as ft_20180713_models
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
            'ap-northeast-2-pop': 'ft.aliyuncs.com',
            'ap-south-1': 'ft.aliyuncs.com',
            'ap-southeast-1': 'ft.aliyuncs.com',
            'ap-southeast-2': 'ft.aliyuncs.com',
            'ap-southeast-3': 'ft.aliyuncs.com',
            'ap-southeast-5': 'ft.aliyuncs.com',
            'cn-beijing': 'ft.aliyuncs.com',
            'cn-beijing-finance-1': 'ft.aliyuncs.com',
            'cn-beijing-finance-pop': 'ft.aliyuncs.com',
            'cn-beijing-gov-1': 'ft.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ft.aliyuncs.com',
            'cn-chengdu': 'ft.aliyuncs.com',
            'cn-edge-1': 'ft.aliyuncs.com',
            'cn-fujian': 'ft.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ft.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ft.aliyuncs.com',
            'cn-hangzhou-finance': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ft.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ft.aliyuncs.com',
            'cn-hangzhou-test-306': 'ft.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ft.aliyuncs.com',
            'cn-huhehaote': 'ft.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ft.aliyuncs.com',
            'cn-qingdao': 'ft.aliyuncs.com',
            'cn-qingdao-nebula': 'ft.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ft.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ft.aliyuncs.com',
            'cn-shanghai-finance-1': 'ft.aliyuncs.com',
            'cn-shanghai-inner': 'ft.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ft.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ft.aliyuncs.com',
            'cn-shenzhen-inner': 'ft.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ft.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ft.aliyuncs.com',
            'cn-wuhan': 'ft.aliyuncs.com',
            'cn-wulanchabu': 'ft.aliyuncs.com',
            'cn-yushanfang': 'ft.aliyuncs.com',
            'cn-zhangbei': 'ft.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ft.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ft.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ft.aliyuncs.com',
            'eu-central-1': 'ft.aliyuncs.com',
            'eu-west-1': 'ft.aliyuncs.com',
            'eu-west-1-oxs': 'ft.aliyuncs.com',
            'me-east-1': 'ft.aliyuncs.com',
            'rus-west-1-pop': 'ft.aliyuncs.com',
            'us-west-1': 'ft.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ft', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_audit_test_01with_options(
        self,
        request: ft_20180713_models.BatchAuditTest01Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.BatchAuditTest01Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.BatchAuditTest01Response().from_map(
            self.do_rpcrequest('BatchAuditTest01', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_audit_test_01with_options_async(
        self,
        request: ft_20180713_models.BatchAuditTest01Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.BatchAuditTest01Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.BatchAuditTest01Response().from_map(
            await self.do_rpcrequest_async('BatchAuditTest01', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_audit_test_01(
        self,
        request: ft_20180713_models.BatchAuditTest01Request,
    ) -> ft_20180713_models.BatchAuditTest01Response:
        runtime = util_models.RuntimeOptions()
        return self.batch_audit_test_01with_options(request, runtime)

    async def batch_audit_test_01_async(
        self,
        request: ft_20180713_models.BatchAuditTest01Request,
    ) -> ft_20180713_models.BatchAuditTest01Response:
        runtime = util_models.RuntimeOptions()
        return await self.batch_audit_test_01with_options_async(request, runtime)

    def f_tapi_alias_api_with_options(
        self,
        request: ft_20180713_models.FTApiAliasApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FTApiAliasApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FTApiAliasApiResponse().from_map(
            self.do_rpcrequest('FTApiAliasApi', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def f_tapi_alias_api_with_options_async(
        self,
        request: ft_20180713_models.FTApiAliasApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FTApiAliasApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FTApiAliasApiResponse().from_map(
            await self.do_rpcrequest_async('FTApiAliasApi', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def f_tapi_alias_api(
        self,
        request: ft_20180713_models.FTApiAliasApiRequest,
    ) -> ft_20180713_models.FTApiAliasApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.f_tapi_alias_api_with_options(request, runtime)

    async def f_tapi_alias_api_async(
        self,
        request: ft_20180713_models.FTApiAliasApiRequest,
    ) -> ft_20180713_models.FTApiAliasApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.f_tapi_alias_api_with_options_async(request, runtime)

    def ft_dynamic_address_dubbo_with_options(
        self,
        request: ft_20180713_models.FtDynamicAddressDubboRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtDynamicAddressDubboResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtDynamicAddressDubboResponse().from_map(
            self.do_rpcrequest('FtDynamicAddressDubbo', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ft_dynamic_address_dubbo_with_options_async(
        self,
        request: ft_20180713_models.FtDynamicAddressDubboRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtDynamicAddressDubboResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtDynamicAddressDubboResponse().from_map(
            await self.do_rpcrequest_async('FtDynamicAddressDubbo', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ft_dynamic_address_dubbo(
        self,
        request: ft_20180713_models.FtDynamicAddressDubboRequest,
    ) -> ft_20180713_models.FtDynamicAddressDubboResponse:
        runtime = util_models.RuntimeOptions()
        return self.ft_dynamic_address_dubbo_with_options(request, runtime)

    async def ft_dynamic_address_dubbo_async(
        self,
        request: ft_20180713_models.FtDynamicAddressDubboRequest,
    ) -> ft_20180713_models.FtDynamicAddressDubboResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ft_dynamic_address_dubbo_with_options_async(request, runtime)

    def ft_dynamic_address_hsf_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtDynamicAddressHsfResponse:
        req = open_api_models.OpenApiRequest()
        return ft_20180713_models.FtDynamicAddressHsfResponse().from_map(
            self.do_rpcrequest('FtDynamicAddressHsf', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ft_dynamic_address_hsf_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtDynamicAddressHsfResponse:
        req = open_api_models.OpenApiRequest()
        return ft_20180713_models.FtDynamicAddressHsfResponse().from_map(
            await self.do_rpcrequest_async('FtDynamicAddressHsf', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ft_dynamic_address_hsf(self) -> ft_20180713_models.FtDynamicAddressHsfResponse:
        runtime = util_models.RuntimeOptions()
        return self.ft_dynamic_address_hsf_with_options(runtime)

    async def ft_dynamic_address_hsf_async(self) -> ft_20180713_models.FtDynamicAddressHsfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ft_dynamic_address_hsf_with_options_async(runtime)

    def ft_eagle_eye_with_options(
        self,
        request: ft_20180713_models.FtEagleEyeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtEagleEyeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtEagleEyeResponse().from_map(
            self.do_rpcrequest('FtEagleEye', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ft_eagle_eye_with_options_async(
        self,
        request: ft_20180713_models.FtEagleEyeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtEagleEyeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtEagleEyeResponse().from_map(
            await self.do_rpcrequest_async('FtEagleEye', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ft_eagle_eye(
        self,
        request: ft_20180713_models.FtEagleEyeRequest,
    ) -> ft_20180713_models.FtEagleEyeResponse:
        runtime = util_models.RuntimeOptions()
        return self.ft_eagle_eye_with_options(request, runtime)

    async def ft_eagle_eye_async(
        self,
        request: ft_20180713_models.FtEagleEyeRequest,
    ) -> ft_20180713_models.FtEagleEyeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ft_eagle_eye_with_options_async(request, runtime)

    def ft_flow_special_with_options(
        self,
        request: ft_20180713_models.FtFlowSpecialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtFlowSpecialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtFlowSpecialResponse().from_map(
            self.do_rpcrequest('FtFlowSpecial', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ft_flow_special_with_options_async(
        self,
        request: ft_20180713_models.FtFlowSpecialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtFlowSpecialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtFlowSpecialResponse().from_map(
            await self.do_rpcrequest_async('FtFlowSpecial', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ft_flow_special(
        self,
        request: ft_20180713_models.FtFlowSpecialRequest,
    ) -> ft_20180713_models.FtFlowSpecialResponse:
        runtime = util_models.RuntimeOptions()
        return self.ft_flow_special_with_options(request, runtime)

    async def ft_flow_special_async(
        self,
        request: ft_20180713_models.FtFlowSpecialRequest,
    ) -> ft_20180713_models.FtFlowSpecialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ft_flow_special_with_options_async(request, runtime)

    def ft_gated_launch_policy_4with_options(
        self,
        request: ft_20180713_models.FtGatedLaunchPolicy4Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtGatedLaunchPolicy4Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtGatedLaunchPolicy4Response().from_map(
            self.do_rpcrequest('FtGatedLaunchPolicy4', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ft_gated_launch_policy_4with_options_async(
        self,
        request: ft_20180713_models.FtGatedLaunchPolicy4Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtGatedLaunchPolicy4Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtGatedLaunchPolicy4Response().from_map(
            await self.do_rpcrequest_async('FtGatedLaunchPolicy4', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ft_gated_launch_policy_4(
        self,
        request: ft_20180713_models.FtGatedLaunchPolicy4Request,
    ) -> ft_20180713_models.FtGatedLaunchPolicy4Response:
        runtime = util_models.RuntimeOptions()
        return self.ft_gated_launch_policy_4with_options(request, runtime)

    async def ft_gated_launch_policy_4_async(
        self,
        request: ft_20180713_models.FtGatedLaunchPolicy4Request,
    ) -> ft_20180713_models.FtGatedLaunchPolicy4Response:
        runtime = util_models.RuntimeOptions()
        return await self.ft_gated_launch_policy_4with_options_async(request, runtime)

    def ft_ip_flow_control_with_options(
        self,
        request: ft_20180713_models.FtIpFlowControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtIpFlowControlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtIpFlowControlResponse().from_map(
            self.do_rpcrequest('FtIpFlowControl', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ft_ip_flow_control_with_options_async(
        self,
        request: ft_20180713_models.FtIpFlowControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtIpFlowControlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtIpFlowControlResponse().from_map(
            await self.do_rpcrequest_async('FtIpFlowControl', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ft_ip_flow_control(
        self,
        request: ft_20180713_models.FtIpFlowControlRequest,
    ) -> ft_20180713_models.FtIpFlowControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.ft_ip_flow_control_with_options(request, runtime)

    async def ft_ip_flow_control_async(
        self,
        request: ft_20180713_models.FtIpFlowControlRequest,
    ) -> ft_20180713_models.FtIpFlowControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ft_ip_flow_control_with_options_async(request, runtime)

    def ft_param_list_with_options(
        self,
        request: ft_20180713_models.FtParamListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtParamListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtParamListResponse().from_map(
            self.do_rpcrequest('FtParamList', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ft_param_list_with_options_async(
        self,
        request: ft_20180713_models.FtParamListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtParamListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.FtParamListResponse().from_map(
            await self.do_rpcrequest_async('FtParamList', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ft_param_list(
        self,
        request: ft_20180713_models.FtParamListRequest,
    ) -> ft_20180713_models.FtParamListResponse:
        runtime = util_models.RuntimeOptions()
        return self.ft_param_list_with_options(request, runtime)

    async def ft_param_list_async(
        self,
        request: ft_20180713_models.FtParamListRequest,
    ) -> ft_20180713_models.FtParamListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ft_param_list_with_options_async(request, runtime)

    def test_flow_strategy_01with_options(
        self,
        tmp_req: ft_20180713_models.TestFlowStrategy01Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.TestFlowStrategy01Response:
        UtilClient.validate_model(tmp_req)
        request = ft_20180713_models.TestFlowStrategy01ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.names):
            request.names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.names, 'Names', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.TestFlowStrategy01Response().from_map(
            self.do_rpcrequest('TestFlowStrategy01', '2018-07-13', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    async def test_flow_strategy_01with_options_async(
        self,
        tmp_req: ft_20180713_models.TestFlowStrategy01Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.TestFlowStrategy01Response:
        UtilClient.validate_model(tmp_req)
        request = ft_20180713_models.TestFlowStrategy01ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.names):
            request.names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.names, 'Names', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.TestFlowStrategy01Response().from_map(
            await self.do_rpcrequest_async('TestFlowStrategy01', '2018-07-13', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    def test_flow_strategy_01(
        self,
        request: ft_20180713_models.TestFlowStrategy01Request,
    ) -> ft_20180713_models.TestFlowStrategy01Response:
        runtime = util_models.RuntimeOptions()
        return self.test_flow_strategy_01with_options(request, runtime)

    async def test_flow_strategy_01_async(
        self,
        request: ft_20180713_models.TestFlowStrategy01Request,
    ) -> ft_20180713_models.TestFlowStrategy01Response:
        runtime = util_models.RuntimeOptions()
        return await self.test_flow_strategy_01with_options_async(request, runtime)

    def test_http_api_with_options(
        self,
        tmp_req: ft_20180713_models.TestHttpApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.TestHttpApiResponse:
        UtilClient.validate_model(tmp_req)
        request = ft_20180713_models.TestHttpApiShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.string_value):
            request.string_value_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.string_value, 'StringValue', 'json')
        if not UtilClient.is_unset(tmp_req.default_value):
            request.default_value_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.default_value, 'DefaultValue', 'json')
        if not UtilClient.is_unset(tmp_req.other_param):
            request.other_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.other_param, 'OtherParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.TestHttpApiResponse().from_map(
            self.do_rpcrequest('TestHttpApi', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def test_http_api_with_options_async(
        self,
        tmp_req: ft_20180713_models.TestHttpApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.TestHttpApiResponse:
        UtilClient.validate_model(tmp_req)
        request = ft_20180713_models.TestHttpApiShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.string_value):
            request.string_value_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.string_value, 'StringValue', 'json')
        if not UtilClient.is_unset(tmp_req.default_value):
            request.default_value_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.default_value, 'DefaultValue', 'json')
        if not UtilClient.is_unset(tmp_req.other_param):
            request.other_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.other_param, 'OtherParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ft_20180713_models.TestHttpApiResponse().from_map(
            await self.do_rpcrequest_async('TestHttpApi', '2018-07-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def test_http_api(
        self,
        request: ft_20180713_models.TestHttpApiRequest,
    ) -> ft_20180713_models.TestHttpApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.test_http_api_with_options(request, runtime)

    async def test_http_api_async(
        self,
        request: ft_20180713_models.TestHttpApiRequest,
    ) -> ft_20180713_models.TestHttpApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.test_http_api_with_options_async(request, runtime)
