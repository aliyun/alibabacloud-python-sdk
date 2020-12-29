# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_ft20180713 import models as ft_20180713_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
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

    def test_flow_strategy_01with_options(
        self,
        tmp: ft_20180713_models.TestFlowStrategy01Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.TestFlowStrategy01Response:
        UtilClient.validate_model(tmp)
        request = ft_20180713_models.TestFlowStrategy01ShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.names):
            request.names_shrink = UtilClient.to_jsonstring(tmp.names)
        return ft_20180713_models.TestFlowStrategy01Response().from_map(
            self.do_request('TestFlowStrategy01', 'HTTPS', 'PUT', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def test_flow_strategy_01with_options_async(
        self,
        tmp: ft_20180713_models.TestFlowStrategy01Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.TestFlowStrategy01Response:
        UtilClient.validate_model(tmp)
        request = ft_20180713_models.TestFlowStrategy01ShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.names):
            request.names_shrink = UtilClient.to_jsonstring(tmp.names)
        return ft_20180713_models.TestFlowStrategy01Response().from_map(
            await self.do_request_async('TestFlowStrategy01', 'HTTPS', 'PUT', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
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
        tmp: ft_20180713_models.TestHttpApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.TestHttpApiResponse:
        UtilClient.validate_model(tmp)
        request = ft_20180713_models.TestHttpApiShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.string_value):
            request.string_value_shrink = UtilClient.to_jsonstring(tmp.string_value)
        if not UtilClient.is_unset(tmp.default_value):
            request.default_value_shrink = UtilClient.to_jsonstring(tmp.default_value)
        if not UtilClient.is_unset(tmp.other_param):
            request.other_param_shrink = UtilClient.to_jsonstring(tmp.other_param)
        return ft_20180713_models.TestHttpApiResponse().from_map(
            self.do_request('TestHttpApi', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def test_http_api_with_options_async(
        self,
        tmp: ft_20180713_models.TestHttpApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.TestHttpApiResponse:
        UtilClient.validate_model(tmp)
        request = ft_20180713_models.TestHttpApiShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.string_value):
            request.string_value_shrink = UtilClient.to_jsonstring(tmp.string_value)
        if not UtilClient.is_unset(tmp.default_value):
            request.default_value_shrink = UtilClient.to_jsonstring(tmp.default_value)
        if not UtilClient.is_unset(tmp.other_param):
            request.other_param_shrink = UtilClient.to_jsonstring(tmp.other_param)
        return ft_20180713_models.TestHttpApiResponse().from_map(
            await self.do_request_async('TestHttpApi', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
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

    def batch_audit_test_01with_options(
        self,
        request: ft_20180713_models.BatchAuditTest01Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.BatchAuditTest01Response:
        UtilClient.validate_model(request)
        return ft_20180713_models.BatchAuditTest01Response().from_map(
            self.do_request('BatchAuditTest01', 'HTTPS', 'POST', '2018-07-13', 'Anonymous', None, TeaCore.to_map(request), runtime)
        )

    async def batch_audit_test_01with_options_async(
        self,
        request: ft_20180713_models.BatchAuditTest01Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.BatchAuditTest01Response:
        UtilClient.validate_model(request)
        return ft_20180713_models.BatchAuditTest01Response().from_map(
            await self.do_request_async('BatchAuditTest01', 'HTTPS', 'POST', '2018-07-13', 'Anonymous', None, TeaCore.to_map(request), runtime)
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

    def ft_ip_flow_control_with_options(
        self,
        request: ft_20180713_models.FtIpFlowControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtIpFlowControlResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtIpFlowControlResponse().from_map(
            self.do_request('FtIpFlowControl', 'HTTPS', 'POST', '2018-07-13', 'Anonymous', None, TeaCore.to_map(request), runtime)
        )

    async def ft_ip_flow_control_with_options_async(
        self,
        request: ft_20180713_models.FtIpFlowControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtIpFlowControlResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtIpFlowControlResponse().from_map(
            await self.do_request_async('FtIpFlowControl', 'HTTPS', 'POST', '2018-07-13', 'Anonymous', None, TeaCore.to_map(request), runtime)
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

    def ft_dynamic_address_dubbo_with_options(
        self,
        request: ft_20180713_models.FtDynamicAddressDubboRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtDynamicAddressDubboResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtDynamicAddressDubboResponse().from_map(
            self.do_request('FtDynamicAddressDubbo', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def ft_dynamic_address_dubbo_with_options_async(
        self,
        request: ft_20180713_models.FtDynamicAddressDubboRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtDynamicAddressDubboResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtDynamicAddressDubboResponse().from_map(
            await self.do_request_async('FtDynamicAddressDubbo', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
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
        request: ft_20180713_models.FtDynamicAddressHsfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtDynamicAddressHsfResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtDynamicAddressHsfResponse().from_map(
            self.do_request('FtDynamicAddressHsf', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def ft_dynamic_address_hsf_with_options_async(
        self,
        request: ft_20180713_models.FtDynamicAddressHsfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtDynamicAddressHsfResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtDynamicAddressHsfResponse().from_map(
            await self.do_request_async('FtDynamicAddressHsf', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def ft_dynamic_address_hsf(
        self,
        request: ft_20180713_models.FtDynamicAddressHsfRequest,
    ) -> ft_20180713_models.FtDynamicAddressHsfResponse:
        runtime = util_models.RuntimeOptions()
        return self.ft_dynamic_address_hsf_with_options(request, runtime)

    async def ft_dynamic_address_hsf_async(
        self,
        request: ft_20180713_models.FtDynamicAddressHsfRequest,
    ) -> ft_20180713_models.FtDynamicAddressHsfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ft_dynamic_address_hsf_with_options_async(request, runtime)

    def ft_flow_special_with_options(
        self,
        request: ft_20180713_models.FtFlowSpecialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtFlowSpecialResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtFlowSpecialResponse().from_map(
            self.do_request('FtFlowSpecial', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def ft_flow_special_with_options_async(
        self,
        request: ft_20180713_models.FtFlowSpecialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtFlowSpecialResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtFlowSpecialResponse().from_map(
            await self.do_request_async('FtFlowSpecial', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
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

    def ftapi_alias_api_with_options(
        self,
        request: ft_20180713_models.FTApiAliasApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FTApiAliasApiResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FTApiAliasApiResponse().from_map(
            self.do_request('FTApiAliasApi', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def ftapi_alias_api_with_options_async(
        self,
        request: ft_20180713_models.FTApiAliasApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FTApiAliasApiResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FTApiAliasApiResponse().from_map(
            await self.do_request_async('FTApiAliasApi', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def ftapi_alias_api(
        self,
        request: ft_20180713_models.FTApiAliasApiRequest,
    ) -> ft_20180713_models.FTApiAliasApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.ftapi_alias_api_with_options(request, runtime)

    async def ftapi_alias_api_async(
        self,
        request: ft_20180713_models.FTApiAliasApiRequest,
    ) -> ft_20180713_models.FTApiAliasApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ftapi_alias_api_with_options_async(request, runtime)

    def ft_eagle_eye_with_options(
        self,
        request: ft_20180713_models.FtEagleEyeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtEagleEyeResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtEagleEyeResponse().from_map(
            self.do_request('FtEagleEye', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def ft_eagle_eye_with_options_async(
        self,
        request: ft_20180713_models.FtEagleEyeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtEagleEyeResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtEagleEyeResponse().from_map(
            await self.do_request_async('FtEagleEye', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
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

    def ft_param_list_with_options(
        self,
        request: ft_20180713_models.FtParamListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtParamListResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtParamListResponse().from_map(
            self.do_request('FtParamList', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def ft_param_list_with_options_async(
        self,
        request: ft_20180713_models.FtParamListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtParamListResponse:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtParamListResponse().from_map(
            await self.do_request_async('FtParamList', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
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

    def ft_gated_launch_policy_4with_options(
        self,
        request: ft_20180713_models.FtGatedLaunchPolicy4Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtGatedLaunchPolicy4Response:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtGatedLaunchPolicy4Response().from_map(
            self.do_request('FtGatedLaunchPolicy4', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def ft_gated_launch_policy_4with_options_async(
        self,
        request: ft_20180713_models.FtGatedLaunchPolicy4Request,
        runtime: util_models.RuntimeOptions,
    ) -> ft_20180713_models.FtGatedLaunchPolicy4Response:
        UtilClient.validate_model(request)
        return ft_20180713_models.FtGatedLaunchPolicy4Response().from_map(
            await self.do_request_async('FtGatedLaunchPolicy4', 'HTTPS', 'POST', '2018-07-13', 'AK', None, TeaCore.to_map(request), runtime)
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
