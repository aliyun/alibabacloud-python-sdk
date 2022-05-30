# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_xgippop20220520 import models as xgip_pop_20220520_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('xgippop', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def change_application_info_with_options(
        self,
        request: xgip_pop_20220520_models.ChangeApplicationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ChangeApplicationInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        if not UtilClient.is_unset(request.item_code):
            body['ItemCode'] = request.item_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeApplicationInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.ChangeApplicationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_application_info_with_options_async(
        self,
        request: xgip_pop_20220520_models.ChangeApplicationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ChangeApplicationInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        if not UtilClient.is_unset(request.item_code):
            body['ItemCode'] = request.item_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeApplicationInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.ChangeApplicationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_application_info(
        self,
        request: xgip_pop_20220520_models.ChangeApplicationInfoRequest,
    ) -> xgip_pop_20220520_models.ChangeApplicationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_application_info_with_options(request, runtime)

    async def change_application_info_async(
        self,
        request: xgip_pop_20220520_models.ChangeApplicationInfoRequest,
    ) -> xgip_pop_20220520_models.ChangeApplicationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_application_info_with_options_async(request, runtime)

    def create_application_info_with_options(
        self,
        request: xgip_pop_20220520_models.CreateApplicationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.CreateApplicationInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        if not UtilClient.is_unset(request.item_code):
            body['ItemCode'] = request.item_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplicationInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.CreateApplicationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_info_with_options_async(
        self,
        request: xgip_pop_20220520_models.CreateApplicationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.CreateApplicationInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        if not UtilClient.is_unset(request.item_code):
            body['ItemCode'] = request.item_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplicationInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.CreateApplicationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_info(
        self,
        request: xgip_pop_20220520_models.CreateApplicationInfoRequest,
    ) -> xgip_pop_20220520_models.CreateApplicationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_application_info_with_options(request, runtime)

    async def create_application_info_async(
        self,
        request: xgip_pop_20220520_models.CreateApplicationInfoRequest,
    ) -> xgip_pop_20220520_models.CreateApplicationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_application_info_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: xgip_pop_20220520_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetApplicationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: xgip_pop_20220520_models.GetApplicationRequest,
    ) -> xgip_pop_20220520_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: xgip_pop_20220520_models.GetApplicationRequest,
    ) -> xgip_pop_20220520_models.GetApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def get_free_flow_instance_with_options(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetFreeFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowInstance',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_free_flow_instance_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetFreeFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowInstance',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_free_flow_instance(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowInstanceRequest,
    ) -> xgip_pop_20220520_models.GetFreeFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_free_flow_instance_with_options(request, runtime)

    async def get_free_flow_instance_async(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowInstanceRequest,
    ) -> xgip_pop_20220520_models.GetFreeFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_free_flow_instance_with_options_async(request, runtime)

    def get_free_flow_product_list_with_options(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetFreeFlowProductListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowProductList',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowProductListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_free_flow_product_list_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetFreeFlowProductListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowProductList',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowProductListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_free_flow_product_list(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowProductListRequest,
    ) -> xgip_pop_20220520_models.GetFreeFlowProductListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_free_flow_product_list_with_options(request, runtime)

    async def get_free_flow_product_list_async(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowProductListRequest,
    ) -> xgip_pop_20220520_models.GetFreeFlowProductListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_free_flow_product_list_with_options_async(request, runtime)

    def get_free_flow_status_with_options(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetFreeFlowStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_free_flow_status_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetFreeFlowStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_free_flow_status(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowStatusRequest,
    ) -> xgip_pop_20220520_models.GetFreeFlowStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_free_flow_status_with_options(request, runtime)

    async def get_free_flow_status_async(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowStatusRequest,
    ) -> xgip_pop_20220520_models.GetFreeFlowStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_free_flow_status_with_options_async(request, runtime)

    def get_free_flow_usage_with_options(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetFreeFlowUsageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowUsage',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_free_flow_usage_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetFreeFlowUsageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowUsage',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_free_flow_usage(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowUsageRequest,
    ) -> xgip_pop_20220520_models.GetFreeFlowUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_free_flow_usage_with_options(request, runtime)

    async def get_free_flow_usage_async(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowUsageRequest,
    ) -> xgip_pop_20220520_models.GetFreeFlowUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_free_flow_usage_with_options_async(request, runtime)

    def get_free_flow_usage_statistic_with_options(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowUsageStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetFreeFlowUsageStatisticResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowUsageStatistic',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowUsageStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_free_flow_usage_statistic_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowUsageStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetFreeFlowUsageStatisticResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeFlowUsageStatistic',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetFreeFlowUsageStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_free_flow_usage_statistic(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowUsageStatisticRequest,
    ) -> xgip_pop_20220520_models.GetFreeFlowUsageStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_free_flow_usage_statistic_with_options(request, runtime)

    async def get_free_flow_usage_statistic_async(
        self,
        request: xgip_pop_20220520_models.GetFreeFlowUsageStatisticRequest,
    ) -> xgip_pop_20220520_models.GetFreeFlowUsageStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_free_flow_usage_statistic_with_options_async(request, runtime)

    def get_order_free_flow_product_status_with_options(
        self,
        request: xgip_pop_20220520_models.GetOrderFreeFlowProductStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetOrderFreeFlowProductStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderFreeFlowProductStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetOrderFreeFlowProductStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_order_free_flow_product_status_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetOrderFreeFlowProductStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetOrderFreeFlowProductStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderFreeFlowProductStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.GetOrderFreeFlowProductStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_order_free_flow_product_status(
        self,
        request: xgip_pop_20220520_models.GetOrderFreeFlowProductStatusRequest,
    ) -> xgip_pop_20220520_models.GetOrderFreeFlowProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_order_free_flow_product_status_with_options(request, runtime)

    async def get_order_free_flow_product_status_async(
        self,
        request: xgip_pop_20220520_models.GetOrderFreeFlowProductStatusRequest,
    ) -> xgip_pop_20220520_models.GetOrderFreeFlowProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_order_free_flow_product_status_with_options_async(request, runtime)

    def modify_application_with_options(
        self,
        request: xgip_pop_20220520_models.ModifyApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ModifyApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApplication',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.ModifyApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_application_with_options_async(
        self,
        request: xgip_pop_20220520_models.ModifyApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ModifyApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApplication',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.ModifyApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_application(
        self,
        request: xgip_pop_20220520_models.ModifyApplicationRequest,
    ) -> xgip_pop_20220520_models.ModifyApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_application_with_options(request, runtime)

    async def modify_application_async(
        self,
        request: xgip_pop_20220520_models.ModifyApplicationRequest,
    ) -> xgip_pop_20220520_models.ModifyApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_application_with_options_async(request, runtime)

    def order_free_flow_product_with_options(
        self,
        request: xgip_pop_20220520_models.OrderFreeFlowProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.OrderFreeFlowProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.customer_flow_request_id):
            query['CustomerFlowRequestId'] = request.customer_flow_request_id
        if not UtilClient.is_unset(request.flow_product_id):
            query['FlowProductId'] = request.flow_product_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lasting):
            query['Lasting'] = request.lasting
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        if not UtilClient.is_unset(request.purchase_order_id):
            query['PurchaseOrderId'] = request.purchase_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderFreeFlowProduct',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.OrderFreeFlowProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_free_flow_product_with_options_async(
        self,
        request: xgip_pop_20220520_models.OrderFreeFlowProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.OrderFreeFlowProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.customer_flow_request_id):
            query['CustomerFlowRequestId'] = request.customer_flow_request_id
        if not UtilClient.is_unset(request.flow_product_id):
            query['FlowProductId'] = request.flow_product_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lasting):
            query['Lasting'] = request.lasting
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        if not UtilClient.is_unset(request.purchase_order_id):
            query['PurchaseOrderId'] = request.purchase_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderFreeFlowProduct',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.OrderFreeFlowProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_free_flow_product(
        self,
        request: xgip_pop_20220520_models.OrderFreeFlowProductRequest,
    ) -> xgip_pop_20220520_models.OrderFreeFlowProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.order_free_flow_product_with_options(request, runtime)

    async def order_free_flow_product_async(
        self,
        request: xgip_pop_20220520_models.OrderFreeFlowProductRequest,
    ) -> xgip_pop_20220520_models.OrderFreeFlowProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.order_free_flow_product_with_options_async(request, runtime)

    def save_application_info_with_options(
        self,
        request: xgip_pop_20220520_models.SaveApplicationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.SaveApplicationInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        if not UtilClient.is_unset(request.item_code):
            body['ItemCode'] = request.item_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveApplicationInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.SaveApplicationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_application_info_with_options_async(
        self,
        request: xgip_pop_20220520_models.SaveApplicationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.SaveApplicationInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type_list):
            body['AppTypeList'] = request.app_type_list
        if not UtilClient.is_unset(request.apping_list):
            body['AppingList'] = request.apping_list
        if not UtilClient.is_unset(request.item_code):
            body['ItemCode'] = request.item_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveApplicationInfo',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.SaveApplicationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_application_info(
        self,
        request: xgip_pop_20220520_models.SaveApplicationInfoRequest,
    ) -> xgip_pop_20220520_models.SaveApplicationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_application_info_with_options(request, runtime)

    async def save_application_info_async(
        self,
        request: xgip_pop_20220520_models.SaveApplicationInfoRequest,
    ) -> xgip_pop_20220520_models.SaveApplicationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_application_info_with_options_async(request, runtime)

    def validate_status_with_options(
        self,
        request: xgip_pop_20220520_models.ValidateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ValidateStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.ValidateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_status_with_options_async(
        self,
        request: xgip_pop_20220520_models.ValidateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ValidateStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.ValidateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_status(
        self,
        request: xgip_pop_20220520_models.ValidateStatusRequest,
    ) -> xgip_pop_20220520_models.ValidateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_status_with_options(request, runtime)

    async def validate_status_async(
        self,
        request: xgip_pop_20220520_models.ValidateStatusRequest,
    ) -> xgip_pop_20220520_models.ValidateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_status_with_options_async(request, runtime)
