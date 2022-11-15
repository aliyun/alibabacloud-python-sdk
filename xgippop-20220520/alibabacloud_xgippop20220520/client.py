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
        self._signature_algorithm = 'v2'
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

    def charge_flow_with_options(
        self,
        request: xgip_pop_20220520_models.ChargeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ChargeFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_code):
            query['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_code):
            query['ItemCode'] = request.item_code
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.order_time):
            query['OrderTime'] = request.order_time
        if not UtilClient.is_unset(request.out_biz_no):
            query['OutBizNo'] = request.out_biz_no
        if not UtilClient.is_unset(request.uid):
            query['UId'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChargeFlow',
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
            xgip_pop_20220520_models.ChargeFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def charge_flow_with_options_async(
        self,
        request: xgip_pop_20220520_models.ChargeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ChargeFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_code):
            query['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_code):
            query['ItemCode'] = request.item_code
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.order_time):
            query['OrderTime'] = request.order_time
        if not UtilClient.is_unset(request.out_biz_no):
            query['OutBizNo'] = request.out_biz_no
        if not UtilClient.is_unset(request.uid):
            query['UId'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChargeFlow',
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
            xgip_pop_20220520_models.ChargeFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def charge_flow(
        self,
        request: xgip_pop_20220520_models.ChargeFlowRequest,
    ) -> xgip_pop_20220520_models.ChargeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.charge_flow_with_options(request, runtime)

    async def charge_flow_async(
        self,
        request: xgip_pop_20220520_models.ChargeFlowRequest,
    ) -> xgip_pop_20220520_models.ChargeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.charge_flow_with_options_async(request, runtime)

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

    def get_aliyun_xgip_token_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetAliyunXgipTokenResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAliyunXgipToken',
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
            xgip_pop_20220520_models.GetAliyunXgipTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aliyun_xgip_token_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetAliyunXgipTokenResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAliyunXgipToken',
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
            xgip_pop_20220520_models.GetAliyunXgipTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aliyun_xgip_token(self) -> xgip_pop_20220520_models.GetAliyunXgipTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aliyun_xgip_token_with_options(runtime)

    async def get_aliyun_xgip_token_async(self) -> xgip_pop_20220520_models.GetAliyunXgipTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aliyun_xgip_token_with_options_async(runtime)

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

    def get_inventory_info_with_options(
        self,
        request: xgip_pop_20220520_models.GetInventoryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetInventoryInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInventoryInfo',
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
            xgip_pop_20220520_models.GetInventoryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inventory_info_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetInventoryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetInventoryInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInventoryInfo',
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
            xgip_pop_20220520_models.GetInventoryInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inventory_info(
        self,
        request: xgip_pop_20220520_models.GetInventoryInfoRequest,
    ) -> xgip_pop_20220520_models.GetInventoryInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_inventory_info_with_options(request, runtime)

    async def get_inventory_info_async(
        self,
        request: xgip_pop_20220520_models.GetInventoryInfoRequest,
    ) -> xgip_pop_20220520_models.GetInventoryInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_inventory_info_with_options_async(request, runtime)

    def get_item_inst_list_with_options(
        self,
        request: xgip_pop_20220520_models.GetItemInstListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetItemInstListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetItemInstList',
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
            xgip_pop_20220520_models.GetItemInstListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_item_inst_list_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetItemInstListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetItemInstListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetItemInstList',
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
            xgip_pop_20220520_models.GetItemInstListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_item_inst_list(
        self,
        request: xgip_pop_20220520_models.GetItemInstListRequest,
    ) -> xgip_pop_20220520_models.GetItemInstListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_item_inst_list_with_options(request, runtime)

    async def get_item_inst_list_async(
        self,
        request: xgip_pop_20220520_models.GetItemInstListRequest,
    ) -> xgip_pop_20220520_models.GetItemInstListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_item_inst_list_with_options_async(request, runtime)

    def get_item_list_with_options(
        self,
        request: xgip_pop_20220520_models.GetItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetItemListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetItemList',
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
            xgip_pop_20220520_models.GetItemListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_item_list_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetItemListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetItemList',
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
            xgip_pop_20220520_models.GetItemListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_item_list(
        self,
        request: xgip_pop_20220520_models.GetItemListRequest,
    ) -> xgip_pop_20220520_models.GetItemListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_item_list_with_options(request, runtime)

    async def get_item_list_async(
        self,
        request: xgip_pop_20220520_models.GetItemListRequest,
    ) -> xgip_pop_20220520_models.GetItemListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_item_list_with_options_async(request, runtime)

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

    def get_order_item_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetOrderItemListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetOrderItemList',
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
            xgip_pop_20220520_models.GetOrderItemListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_order_item_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetOrderItemListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetOrderItemList',
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
            xgip_pop_20220520_models.GetOrderItemListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_order_item_list(self) -> xgip_pop_20220520_models.GetOrderItemListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_order_item_list_with_options(runtime)

    async def get_order_item_list_async(self) -> xgip_pop_20220520_models.GetOrderItemListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_order_item_list_with_options_async(runtime)

    def get_qos_flow_usage_with_options(
        self,
        request: xgip_pop_20220520_models.GetQosFlowUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetQosFlowUsageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQosFlowUsage',
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
            xgip_pop_20220520_models.GetQosFlowUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qos_flow_usage_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetQosFlowUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetQosFlowUsageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQosFlowUsage',
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
            xgip_pop_20220520_models.GetQosFlowUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qos_flow_usage(
        self,
        request: xgip_pop_20220520_models.GetQosFlowUsageRequest,
    ) -> xgip_pop_20220520_models.GetQosFlowUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_qos_flow_usage_with_options(request, runtime)

    async def get_qos_flow_usage_async(
        self,
        request: xgip_pop_20220520_models.GetQosFlowUsageRequest,
    ) -> xgip_pop_20220520_models.GetQosFlowUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_qos_flow_usage_with_options_async(request, runtime)

    def get_qos_usage_statistic_with_options(
        self,
        request: xgip_pop_20220520_models.GetQosUsageStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetQosUsageStatisticResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQosUsageStatistic',
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
            xgip_pop_20220520_models.GetQosUsageStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qos_usage_statistic_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetQosUsageStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetQosUsageStatisticResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQosUsageStatistic',
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
            xgip_pop_20220520_models.GetQosUsageStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qos_usage_statistic(
        self,
        request: xgip_pop_20220520_models.GetQosUsageStatisticRequest,
    ) -> xgip_pop_20220520_models.GetQosUsageStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_qos_usage_statistic_with_options(request, runtime)

    async def get_qos_usage_statistic_async(
        self,
        request: xgip_pop_20220520_models.GetQosUsageStatisticRequest,
    ) -> xgip_pop_20220520_models.GetQosUsageStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_qos_usage_statistic_with_options_async(request, runtime)

    def get_uat_data_list_with_options(
        self,
        request: xgip_pop_20220520_models.GetUatDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetUatDataListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUatDataList',
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
            xgip_pop_20220520_models.GetUatDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_uat_data_list_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetUatDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetUatDataListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUatDataList',
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
            xgip_pop_20220520_models.GetUatDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_uat_data_list(
        self,
        request: xgip_pop_20220520_models.GetUatDataListRequest,
    ) -> xgip_pop_20220520_models.GetUatDataListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_uat_data_list_with_options(request, runtime)

    async def get_uat_data_list_async(
        self,
        request: xgip_pop_20220520_models.GetUatDataListRequest,
    ) -> xgip_pop_20220520_models.GetUatDataListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_uat_data_list_with_options_async(request, runtime)

    def get_uat_spec_ct_data_with_options(
        self,
        request: xgip_pop_20220520_models.GetUatSpecCtDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetUatSpecCtDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUatSpecCtData',
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
            xgip_pop_20220520_models.GetUatSpecCtDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_uat_spec_ct_data_with_options_async(
        self,
        request: xgip_pop_20220520_models.GetUatSpecCtDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.GetUatSpecCtDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUatSpecCtData',
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
            xgip_pop_20220520_models.GetUatSpecCtDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_uat_spec_ct_data(
        self,
        request: xgip_pop_20220520_models.GetUatSpecCtDataRequest,
    ) -> xgip_pop_20220520_models.GetUatSpecCtDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_uat_spec_ct_data_with_options(request, runtime)

    async def get_uat_spec_ct_data_async(
        self,
        request: xgip_pop_20220520_models.GetUatSpecCtDataRequest,
    ) -> xgip_pop_20220520_models.GetUatSpecCtDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_uat_spec_ct_data_with_options_async(request, runtime)

    def mock_get_order_free_flow_product_status_with_options(
        self,
        request: xgip_pop_20220520_models.MockGetOrderFreeFlowProductStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.MockGetOrderFreeFlowProductStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MockGetOrderFreeFlowProductStatus',
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
            xgip_pop_20220520_models.MockGetOrderFreeFlowProductStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def mock_get_order_free_flow_product_status_with_options_async(
        self,
        request: xgip_pop_20220520_models.MockGetOrderFreeFlowProductStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.MockGetOrderFreeFlowProductStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MockGetOrderFreeFlowProductStatus',
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
            xgip_pop_20220520_models.MockGetOrderFreeFlowProductStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mock_get_order_free_flow_product_status(
        self,
        request: xgip_pop_20220520_models.MockGetOrderFreeFlowProductStatusRequest,
    ) -> xgip_pop_20220520_models.MockGetOrderFreeFlowProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.mock_get_order_free_flow_product_status_with_options(request, runtime)

    async def mock_get_order_free_flow_product_status_async(
        self,
        request: xgip_pop_20220520_models.MockGetOrderFreeFlowProductStatusRequest,
    ) -> xgip_pop_20220520_models.MockGetOrderFreeFlowProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mock_get_order_free_flow_product_status_with_options_async(request, runtime)

    def mock_order_free_flow_product_with_options(
        self,
        request: xgip_pop_20220520_models.MockOrderFreeFlowProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.MockOrderFreeFlowProductResponse:
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
            action='MockOrderFreeFlowProduct',
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
            xgip_pop_20220520_models.MockOrderFreeFlowProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def mock_order_free_flow_product_with_options_async(
        self,
        request: xgip_pop_20220520_models.MockOrderFreeFlowProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.MockOrderFreeFlowProductResponse:
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
            action='MockOrderFreeFlowProduct',
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
            xgip_pop_20220520_models.MockOrderFreeFlowProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mock_order_free_flow_product(
        self,
        request: xgip_pop_20220520_models.MockOrderFreeFlowProductRequest,
    ) -> xgip_pop_20220520_models.MockOrderFreeFlowProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.mock_order_free_flow_product_with_options(request, runtime)

    async def mock_order_free_flow_product_async(
        self,
        request: xgip_pop_20220520_models.MockOrderFreeFlowProductRequest,
    ) -> xgip_pop_20220520_models.MockOrderFreeFlowProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mock_order_free_flow_product_with_options_async(request, runtime)

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

    def order_qos_product_with_options(
        self,
        request: xgip_pop_20220520_models.OrderQosProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.OrderQosProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provice):
            query['Provice'] = request.provice
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.ipv_6):
            body['IPv6'] = request.ipv_6
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_type):
            body['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.mobile_number):
            body['MobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.private_ipv_4):
            body['PrivateIpv4'] = request.private_ipv_4
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.public_ipv_4):
            body['PublicIpv4'] = request.public_ipv_4
        if not UtilClient.is_unset(request.qos_request_id):
            body['QosRequestId'] = request.qos_request_id
        if not UtilClient.is_unset(request.target_ip_list):
            body['TargetIpList'] = request.target_ip_list
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.unit_num):
            body['UnitNum'] = request.unit_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OrderQosProduct',
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
            xgip_pop_20220520_models.OrderQosProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_qos_product_with_options_async(
        self,
        request: xgip_pop_20220520_models.OrderQosProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.OrderQosProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provice):
            query['Provice'] = request.provice
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.ipv_6):
            body['IPv6'] = request.ipv_6
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_type):
            body['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.mobile_number):
            body['MobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.private_ipv_4):
            body['PrivateIpv4'] = request.private_ipv_4
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.public_ipv_4):
            body['PublicIpv4'] = request.public_ipv_4
        if not UtilClient.is_unset(request.qos_request_id):
            body['QosRequestId'] = request.qos_request_id
        if not UtilClient.is_unset(request.target_ip_list):
            body['TargetIpList'] = request.target_ip_list
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.unit_num):
            body['UnitNum'] = request.unit_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OrderQosProduct',
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
            xgip_pop_20220520_models.OrderQosProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_qos_product(
        self,
        request: xgip_pop_20220520_models.OrderQosProductRequest,
    ) -> xgip_pop_20220520_models.OrderQosProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.order_qos_product_with_options(request, runtime)

    async def order_qos_product_async(
        self,
        request: xgip_pop_20220520_models.OrderQosProductRequest,
    ) -> xgip_pop_20220520_models.OrderQosProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.order_qos_product_with_options_async(request, runtime)

    def query_order_list_with_options(
        self,
        request: xgip_pop_20220520_models.QueryOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.QueryOrderListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderList',
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
            xgip_pop_20220520_models.QueryOrderListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_list_with_options_async(
        self,
        request: xgip_pop_20220520_models.QueryOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.QueryOrderListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderList',
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
            xgip_pop_20220520_models.QueryOrderListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_list(
        self,
        request: xgip_pop_20220520_models.QueryOrderListRequest,
    ) -> xgip_pop_20220520_models.QueryOrderListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_list_with_options(request, runtime)

    async def query_order_list_async(
        self,
        request: xgip_pop_20220520_models.QueryOrderListRequest,
    ) -> xgip_pop_20220520_models.QueryOrderListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_list_with_options_async(request, runtime)

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

    def sdk_get_inventory_info_with_options(
        self,
        request: xgip_pop_20220520_models.SdkGetInventoryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.SdkGetInventoryInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkGetInventoryInfo',
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
            xgip_pop_20220520_models.SdkGetInventoryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdk_get_inventory_info_with_options_async(
        self,
        request: xgip_pop_20220520_models.SdkGetInventoryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.SdkGetInventoryInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkGetInventoryInfo',
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
            xgip_pop_20220520_models.SdkGetInventoryInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdk_get_inventory_info(
        self,
        request: xgip_pop_20220520_models.SdkGetInventoryInfoRequest,
    ) -> xgip_pop_20220520_models.SdkGetInventoryInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.sdk_get_inventory_info_with_options(request, runtime)

    async def sdk_get_inventory_info_async(
        self,
        request: xgip_pop_20220520_models.SdkGetInventoryInfoRequest,
    ) -> xgip_pop_20220520_models.SdkGetInventoryInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sdk_get_inventory_info_with_options_async(request, runtime)

    def sdk_order_qos_product_with_options(
        self,
        request: xgip_pop_20220520_models.SdkOrderQosProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.SdkOrderQosProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.ct_token):
            query['CtToken'] = request.ct_token
        if not UtilClient.is_unset(request.ipv_6):
            query['IPv6'] = request.ipv_6
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        if not UtilClient.is_unset(request.private_ipv_4):
            query['PrivateIpv4'] = request.private_ipv_4
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.provice):
            query['Provice'] = request.provice
        if not UtilClient.is_unset(request.public_ipv_4):
            query['PublicIpv4'] = request.public_ipv_4
        if not UtilClient.is_unset(request.qos_request_id):
            query['QosRequestId'] = request.qos_request_id
        if not UtilClient.is_unset(request.target_ip_list):
            query['TargetIpList'] = request.target_ip_list
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.unit_num):
            query['UnitNum'] = request.unit_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkOrderQosProduct',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.SdkOrderQosProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdk_order_qos_product_with_options_async(
        self,
        request: xgip_pop_20220520_models.SdkOrderQosProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.SdkOrderQosProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.ct_token):
            query['CtToken'] = request.ct_token
        if not UtilClient.is_unset(request.ipv_6):
            query['IPv6'] = request.ipv_6
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        if not UtilClient.is_unset(request.private_ipv_4):
            query['PrivateIpv4'] = request.private_ipv_4
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.provice):
            query['Provice'] = request.provice
        if not UtilClient.is_unset(request.public_ipv_4):
            query['PublicIpv4'] = request.public_ipv_4
        if not UtilClient.is_unset(request.qos_request_id):
            query['QosRequestId'] = request.qos_request_id
        if not UtilClient.is_unset(request.target_ip_list):
            query['TargetIpList'] = request.target_ip_list
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.unit_num):
            query['UnitNum'] = request.unit_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkOrderQosProduct',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.SdkOrderQosProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdk_order_qos_product(
        self,
        request: xgip_pop_20220520_models.SdkOrderQosProductRequest,
    ) -> xgip_pop_20220520_models.SdkOrderQosProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.sdk_order_qos_product_with_options(request, runtime)

    async def sdk_order_qos_product_async(
        self,
        request: xgip_pop_20220520_models.SdkOrderQosProductRequest,
    ) -> xgip_pop_20220520_models.SdkOrderQosProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sdk_order_qos_product_with_options_async(request, runtime)

    def sdk_validate_status_with_options(
        self,
        request: xgip_pop_20220520_models.SdkValidateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.SdkValidateStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkValidateStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.SdkValidateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def sdk_validate_status_with_options_async(
        self,
        request: xgip_pop_20220520_models.SdkValidateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.SdkValidateStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkValidateStatus',
            version='2022-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xgip_pop_20220520_models.SdkValidateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sdk_validate_status(
        self,
        request: xgip_pop_20220520_models.SdkValidateStatusRequest,
    ) -> xgip_pop_20220520_models.SdkValidateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.sdk_validate_status_with_options(request, runtime)

    async def sdk_validate_status_async(
        self,
        request: xgip_pop_20220520_models.SdkValidateStatusRequest,
    ) -> xgip_pop_20220520_models.SdkValidateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sdk_validate_status_with_options_async(request, runtime)

    def valid_controller_author_with_options(
        self,
        request: xgip_pop_20220520_models.ValidControllerAuthorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ValidControllerAuthorResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidControllerAuthor',
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
            xgip_pop_20220520_models.ValidControllerAuthorResponse(),
            self.call_api(params, req, runtime)
        )

    async def valid_controller_author_with_options_async(
        self,
        request: xgip_pop_20220520_models.ValidControllerAuthorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ValidControllerAuthorResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidControllerAuthor',
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
            xgip_pop_20220520_models.ValidControllerAuthorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def valid_controller_author(
        self,
        request: xgip_pop_20220520_models.ValidControllerAuthorRequest,
    ) -> xgip_pop_20220520_models.ValidControllerAuthorResponse:
        runtime = util_models.RuntimeOptions()
        return self.valid_controller_author_with_options(request, runtime)

    async def valid_controller_author_async(
        self,
        request: xgip_pop_20220520_models.ValidControllerAuthorRequest,
    ) -> xgip_pop_20220520_models.ValidControllerAuthorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.valid_controller_author_with_options_async(request, runtime)

    def valid_flow_with_options(
        self,
        request: xgip_pop_20220520_models.ValidFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ValidFlowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidFlow',
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
            xgip_pop_20220520_models.ValidFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def valid_flow_with_options_async(
        self,
        request: xgip_pop_20220520_models.ValidFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> xgip_pop_20220520_models.ValidFlowResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidFlow',
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
            xgip_pop_20220520_models.ValidFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def valid_flow(
        self,
        request: xgip_pop_20220520_models.ValidFlowRequest,
    ) -> xgip_pop_20220520_models.ValidFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.valid_flow_with_options(request, runtime)

    async def valid_flow_async(
        self,
        request: xgip_pop_20220520_models.ValidFlowRequest,
    ) -> xgip_pop_20220520_models.ValidFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.valid_flow_with_options_async(request, runtime)

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
