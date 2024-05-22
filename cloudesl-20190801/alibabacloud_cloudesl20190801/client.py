# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudesl20190801 import models as cloudesl_20190801_models
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
            'ap-northeast-1': 'cloudesl.aliyuncs.com',
            'ap-northeast-2-pop': 'cloudesl.aliyuncs.com',
            'ap-south-1': 'cloudesl.aliyuncs.com',
            'ap-southeast-1': 'cloudesl.aliyuncs.com',
            'ap-southeast-2': 'cloudesl.aliyuncs.com',
            'ap-southeast-3': 'cloudesl.aliyuncs.com',
            'ap-southeast-5': 'cloudesl.aliyuncs.com',
            'cn-beijing': 'cloudesl.aliyuncs.com',
            'cn-beijing-finance-1': 'cloudesl.aliyuncs.com',
            'cn-beijing-finance-pop': 'cloudesl.aliyuncs.com',
            'cn-beijing-gov-1': 'cloudesl.aliyuncs.com',
            'cn-beijing-nu16-b01': 'cloudesl.aliyuncs.com',
            'cn-chengdu': 'cloudesl.aliyuncs.com',
            'cn-edge-1': 'cloudesl.aliyuncs.com',
            'cn-fujian': 'cloudesl.aliyuncs.com',
            'cn-haidian-cm12-c01': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-finance': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-test-306': 'cloudesl.aliyuncs.com',
            'cn-hongkong': 'cloudesl.aliyuncs.com',
            'cn-hongkong-finance-pop': 'cloudesl.aliyuncs.com',
            'cn-huhehaote': 'cloudesl.aliyuncs.com',
            'cn-north-2-gov-1': 'cloudesl.aliyuncs.com',
            'cn-qingdao': 'cloudesl.aliyuncs.com',
            'cn-qingdao-nebula': 'cloudesl.aliyuncs.com',
            'cn-shanghai': 'cloudesl.aliyuncs.com',
            'cn-shanghai-et15-b01': 'cloudesl.aliyuncs.com',
            'cn-shanghai-et2-b01': 'cloudesl.aliyuncs.com',
            'cn-shanghai-finance-1': 'cloudesl.aliyuncs.com',
            'cn-shanghai-inner': 'cloudesl.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'cloudesl.aliyuncs.com',
            'cn-shenzhen': 'cloudesl.aliyuncs.com',
            'cn-shenzhen-finance-1': 'cloudesl.aliyuncs.com',
            'cn-shenzhen-inner': 'cloudesl.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'cloudesl.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'cloudesl.aliyuncs.com',
            'cn-wuhan': 'cloudesl.aliyuncs.com',
            'cn-yushanfang': 'cloudesl.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'cloudesl.aliyuncs.com',
            'cn-zhangjiakou': 'cloudesl.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'cloudesl.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'cloudesl.aliyuncs.com',
            'eu-central-1': 'cloudesl.aliyuncs.com',
            'eu-west-1': 'cloudesl.aliyuncs.com',
            'eu-west-1-oxs': 'cloudesl.aliyuncs.com',
            'me-east-1': 'cloudesl.aliyuncs.com',
            'rus-west-1-pop': 'cloudesl.aliyuncs.com',
            'us-east-1': 'cloudesl.aliyuncs.com',
            'us-west-1': 'cloudesl.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudesl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_ap_device_with_options(
        self,
        request: cloudesl_20190801_models.ActivateApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.ActivateApDeviceResponse:
        """
        @param request: ActivateApDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateApDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateApDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.ActivateApDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_ap_device_with_options_async(
        self,
        request: cloudesl_20190801_models.ActivateApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.ActivateApDeviceResponse:
        """
        @param request: ActivateApDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateApDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateApDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.ActivateApDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_ap_device(
        self,
        request: cloudesl_20190801_models.ActivateApDeviceRequest,
    ) -> cloudesl_20190801_models.ActivateApDeviceResponse:
        """
        @param request: ActivateApDeviceRequest
        @return: ActivateApDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.activate_ap_device_with_options(request, runtime)

    async def activate_ap_device_async(
        self,
        request: cloudesl_20190801_models.ActivateApDeviceRequest,
    ) -> cloudesl_20190801_models.ActivateApDeviceResponse:
        """
        @param request: ActivateApDeviceRequest
        @return: ActivateApDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.activate_ap_device_with_options_async(request, runtime)

    def add_ap_device_with_options(
        self,
        request: cloudesl_20190801_models.AddApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.AddApDeviceResponse:
        """
        @param request: AddApDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddApDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddApDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.AddApDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ap_device_with_options_async(
        self,
        request: cloudesl_20190801_models.AddApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.AddApDeviceResponse:
        """
        @param request: AddApDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddApDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddApDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.AddApDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ap_device(
        self,
        request: cloudesl_20190801_models.AddApDeviceRequest,
    ) -> cloudesl_20190801_models.AddApDeviceResponse:
        """
        @param request: AddApDeviceRequest
        @return: AddApDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_ap_device_with_options(request, runtime)

    async def add_ap_device_async(
        self,
        request: cloudesl_20190801_models.AddApDeviceRequest,
    ) -> cloudesl_20190801_models.AddApDeviceResponse:
        """
        @param request: AddApDeviceRequest
        @return: AddApDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_ap_device_with_options_async(request, runtime)

    def add_esl_device_with_options(
        self,
        request: cloudesl_20190801_models.AddEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.AddEslDeviceResponse:
        """
        @param request: AddEslDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddEslDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEslDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.AddEslDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_esl_device_with_options_async(
        self,
        request: cloudesl_20190801_models.AddEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.AddEslDeviceResponse:
        """
        @param request: AddEslDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddEslDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEslDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.AddEslDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_esl_device(
        self,
        request: cloudesl_20190801_models.AddEslDeviceRequest,
    ) -> cloudesl_20190801_models.AddEslDeviceResponse:
        """
        @param request: AddEslDeviceRequest
        @return: AddEslDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_esl_device_with_options(request, runtime)

    async def add_esl_device_async(
        self,
        request: cloudesl_20190801_models.AddEslDeviceRequest,
    ) -> cloudesl_20190801_models.AddEslDeviceResponse:
        """
        @param request: AddEslDeviceRequest
        @return: AddEslDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_esl_device_with_options_async(request, runtime)

    def add_user_with_options(
        self,
        request: cloudesl_20190801_models.AddUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.AddUserResponse:
        """
        @param request: AddUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUser',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.AddUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_with_options_async(
        self,
        request: cloudesl_20190801_models.AddUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.AddUserResponse:
        """
        @param request: AddUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUser',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.AddUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user(
        self,
        request: cloudesl_20190801_models.AddUserRequest,
    ) -> cloudesl_20190801_models.AddUserResponse:
        """
        @param request: AddUserRequest
        @return: AddUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_with_options(request, runtime)

    async def add_user_async(
        self,
        request: cloudesl_20190801_models.AddUserRequest,
    ) -> cloudesl_20190801_models.AddUserResponse:
        """
        @param request: AddUserRequest
        @return: AddUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_with_options_async(request, runtime)

    def assign_user_with_options(
        self,
        request: cloudesl_20190801_models.AssignUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.AssignUserResponse:
        """
        @param request: AssignUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.stores):
            body['Stores'] = request.stores
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignUser',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.AssignUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_user_with_options_async(
        self,
        request: cloudesl_20190801_models.AssignUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.AssignUserResponse:
        """
        @param request: AssignUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.stores):
            body['Stores'] = request.stores
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignUser',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.AssignUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_user(
        self,
        request: cloudesl_20190801_models.AssignUserRequest,
    ) -> cloudesl_20190801_models.AssignUserResponse:
        """
        @param request: AssignUserRequest
        @return: AssignUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assign_user_with_options(request, runtime)

    async def assign_user_async(
        self,
        request: cloudesl_20190801_models.AssignUserRequest,
    ) -> cloudesl_20190801_models.AssignUserResponse:
        """
        @param request: AssignUserRequest
        @return: AssignUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assign_user_with_options_async(request, runtime)

    def batch_insert_items_with_options(
        self,
        request: cloudesl_20190801_models.BatchInsertItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.BatchInsertItemsResponse:
        """
        @param request: BatchInsertItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchInsertItemsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.item_info):
            body['ItemInfo'] = request.item_info
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchInsertItems',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.BatchInsertItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_insert_items_with_options_async(
        self,
        request: cloudesl_20190801_models.BatchInsertItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.BatchInsertItemsResponse:
        """
        @param request: BatchInsertItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchInsertItemsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.item_info):
            body['ItemInfo'] = request.item_info
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchInsertItems',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.BatchInsertItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_insert_items(
        self,
        request: cloudesl_20190801_models.BatchInsertItemsRequest,
    ) -> cloudesl_20190801_models.BatchInsertItemsResponse:
        """
        @param request: BatchInsertItemsRequest
        @return: BatchInsertItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_insert_items_with_options(request, runtime)

    async def batch_insert_items_async(
        self,
        request: cloudesl_20190801_models.BatchInsertItemsRequest,
    ) -> cloudesl_20190801_models.BatchInsertItemsResponse:
        """
        @param request: BatchInsertItemsRequest
        @return: BatchInsertItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_insert_items_with_options_async(request, runtime)

    def bind_esl_device_with_options(
        self,
        request: cloudesl_20190801_models.BindEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.BindEslDeviceResponse:
        """
        @param request: BindEslDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindEslDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindEslDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.BindEslDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_esl_device_with_options_async(
        self,
        request: cloudesl_20190801_models.BindEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.BindEslDeviceResponse:
        """
        @param request: BindEslDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindEslDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindEslDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.BindEslDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_esl_device(
        self,
        request: cloudesl_20190801_models.BindEslDeviceRequest,
    ) -> cloudesl_20190801_models.BindEslDeviceResponse:
        """
        @param request: BindEslDeviceRequest
        @return: BindEslDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_esl_device_with_options(request, runtime)

    async def bind_esl_device_async(
        self,
        request: cloudesl_20190801_models.BindEslDeviceRequest,
    ) -> cloudesl_20190801_models.BindEslDeviceResponse:
        """
        @param request: BindEslDeviceRequest
        @return: BindEslDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_esl_device_with_options_async(request, runtime)

    def bind_esl_device_shelf_with_options(
        self,
        request: cloudesl_20190801_models.BindEslDeviceShelfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.BindEslDeviceShelfResponse:
        """
        @param request: BindEslDeviceShelfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindEslDeviceShelfResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.shelf_code):
            body['ShelfCode'] = request.shelf_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindEslDeviceShelf',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.BindEslDeviceShelfResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_esl_device_shelf_with_options_async(
        self,
        request: cloudesl_20190801_models.BindEslDeviceShelfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.BindEslDeviceShelfResponse:
        """
        @param request: BindEslDeviceShelfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindEslDeviceShelfResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.shelf_code):
            body['ShelfCode'] = request.shelf_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindEslDeviceShelf',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.BindEslDeviceShelfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_esl_device_shelf(
        self,
        request: cloudesl_20190801_models.BindEslDeviceShelfRequest,
    ) -> cloudesl_20190801_models.BindEslDeviceShelfResponse:
        """
        @param request: BindEslDeviceShelfRequest
        @return: BindEslDeviceShelfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_esl_device_shelf_with_options(request, runtime)

    async def bind_esl_device_shelf_async(
        self,
        request: cloudesl_20190801_models.BindEslDeviceShelfRequest,
    ) -> cloudesl_20190801_models.BindEslDeviceShelfResponse:
        """
        @param request: BindEslDeviceShelfRequest
        @return: BindEslDeviceShelfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_esl_device_shelf_with_options_async(request, runtime)

    def confirm_logistics_with_options(
        self,
        request: cloudesl_20190801_models.ConfirmLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.ConfirmLogisticsResponse:
        """
        @param request: ConfirmLogisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmLogisticsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.logistics_documents):
            body['LogisticsDocuments'] = request.logistics_documents
        if not UtilClient.is_unset(request.po_number):
            body['PoNumber'] = request.po_number
        if not UtilClient.is_unset(request.pr_number):
            body['PrNumber'] = request.pr_number
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfirmLogistics',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.ConfirmLogisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_logistics_with_options_async(
        self,
        request: cloudesl_20190801_models.ConfirmLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.ConfirmLogisticsResponse:
        """
        @param request: ConfirmLogisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmLogisticsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.logistics_documents):
            body['LogisticsDocuments'] = request.logistics_documents
        if not UtilClient.is_unset(request.po_number):
            body['PoNumber'] = request.po_number
        if not UtilClient.is_unset(request.pr_number):
            body['PrNumber'] = request.pr_number
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfirmLogistics',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.ConfirmLogisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_logistics(
        self,
        request: cloudesl_20190801_models.ConfirmLogisticsRequest,
    ) -> cloudesl_20190801_models.ConfirmLogisticsResponse:
        """
        @param request: ConfirmLogisticsRequest
        @return: ConfirmLogisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.confirm_logistics_with_options(request, runtime)

    async def confirm_logistics_async(
        self,
        request: cloudesl_20190801_models.ConfirmLogisticsRequest,
    ) -> cloudesl_20190801_models.ConfirmLogisticsResponse:
        """
        @param request: ConfirmLogisticsRequest
        @return: ConfirmLogisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.confirm_logistics_with_options_async(request, runtime)

    def create_store_with_options(
        self,
        request: cloudesl_20190801_models.CreateStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.CreateStoreResponse:
        """
        @param request: CreateStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.brand):
            body['Brand'] = request.brand
        if not UtilClient.is_unset(request.comments):
            body['Comments'] = request.comments
        if not UtilClient.is_unset(request.company_id):
            body['CompanyId'] = request.company_id
        if not UtilClient.is_unset(request.groups):
            body['Groups'] = request.groups
        if not UtilClient.is_unset(request.out_id):
            body['OutId'] = request.out_id
        if not UtilClient.is_unset(request.parent_id):
            body['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.store_name):
            body['StoreName'] = request.store_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStore',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.CreateStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_store_with_options_async(
        self,
        request: cloudesl_20190801_models.CreateStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.CreateStoreResponse:
        """
        @param request: CreateStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.brand):
            body['Brand'] = request.brand
        if not UtilClient.is_unset(request.comments):
            body['Comments'] = request.comments
        if not UtilClient.is_unset(request.company_id):
            body['CompanyId'] = request.company_id
        if not UtilClient.is_unset(request.groups):
            body['Groups'] = request.groups
        if not UtilClient.is_unset(request.out_id):
            body['OutId'] = request.out_id
        if not UtilClient.is_unset(request.parent_id):
            body['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.store_name):
            body['StoreName'] = request.store_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStore',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.CreateStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_store(
        self,
        request: cloudesl_20190801_models.CreateStoreRequest,
    ) -> cloudesl_20190801_models.CreateStoreResponse:
        """
        @param request: CreateStoreRequest
        @return: CreateStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_store_with_options(request, runtime)

    async def create_store_async(
        self,
        request: cloudesl_20190801_models.CreateStoreRequest,
    ) -> cloudesl_20190801_models.CreateStoreResponse:
        """
        @param request: CreateStoreRequest
        @return: CreateStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_store_with_options_async(request, runtime)

    def delete_ap_device_with_options(
        self,
        request: cloudesl_20190801_models.DeleteApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteApDeviceResponse:
        """
        @param request: DeleteApDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteApDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ap_device_with_options_async(
        self,
        request: cloudesl_20190801_models.DeleteApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteApDeviceResponse:
        """
        @param request: DeleteApDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteApDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ap_device(
        self,
        request: cloudesl_20190801_models.DeleteApDeviceRequest,
    ) -> cloudesl_20190801_models.DeleteApDeviceResponse:
        """
        @param request: DeleteApDeviceRequest
        @return: DeleteApDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ap_device_with_options(request, runtime)

    async def delete_ap_device_async(
        self,
        request: cloudesl_20190801_models.DeleteApDeviceRequest,
    ) -> cloudesl_20190801_models.DeleteApDeviceResponse:
        """
        @param request: DeleteApDeviceRequest
        @return: DeleteApDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ap_device_with_options_async(request, runtime)

    def delete_esl_device_with_options(
        self,
        request: cloudesl_20190801_models.DeleteEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteEslDeviceResponse:
        """
        @param request: DeleteEslDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEslDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEslDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteEslDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_esl_device_with_options_async(
        self,
        request: cloudesl_20190801_models.DeleteEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteEslDeviceResponse:
        """
        @param request: DeleteEslDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEslDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEslDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteEslDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_esl_device(
        self,
        request: cloudesl_20190801_models.DeleteEslDeviceRequest,
    ) -> cloudesl_20190801_models.DeleteEslDeviceResponse:
        """
        @param request: DeleteEslDeviceRequest
        @return: DeleteEslDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_esl_device_with_options(request, runtime)

    async def delete_esl_device_async(
        self,
        request: cloudesl_20190801_models.DeleteEslDeviceRequest,
    ) -> cloudesl_20190801_models.DeleteEslDeviceResponse:
        """
        @param request: DeleteEslDeviceRequest
        @return: DeleteEslDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_esl_device_with_options_async(request, runtime)

    def delete_item_with_options(
        self,
        request: cloudesl_20190801_models.DeleteItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteItemResponse:
        """
        @param request: DeleteItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteItem',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_item_with_options_async(
        self,
        request: cloudesl_20190801_models.DeleteItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteItemResponse:
        """
        @param request: DeleteItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteItem',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_item(
        self,
        request: cloudesl_20190801_models.DeleteItemRequest,
    ) -> cloudesl_20190801_models.DeleteItemResponse:
        """
        @param request: DeleteItemRequest
        @return: DeleteItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_item_with_options(request, runtime)

    async def delete_item_async(
        self,
        request: cloudesl_20190801_models.DeleteItemRequest,
    ) -> cloudesl_20190801_models.DeleteItemResponse:
        """
        @param request: DeleteItemRequest
        @return: DeleteItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_item_with_options_async(request, runtime)

    def delete_item_by_sku_id_with_options(
        self,
        request: cloudesl_20190801_models.DeleteItemBySkuIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteItemBySkuIdResponse:
        """
        @param request: DeleteItemBySkuIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteItemBySkuIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sku_id):
            body['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteItemBySkuId',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteItemBySkuIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_item_by_sku_id_with_options_async(
        self,
        request: cloudesl_20190801_models.DeleteItemBySkuIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteItemBySkuIdResponse:
        """
        @param request: DeleteItemBySkuIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteItemBySkuIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sku_id):
            body['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteItemBySkuId',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteItemBySkuIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_item_by_sku_id(
        self,
        request: cloudesl_20190801_models.DeleteItemBySkuIdRequest,
    ) -> cloudesl_20190801_models.DeleteItemBySkuIdResponse:
        """
        @param request: DeleteItemBySkuIdRequest
        @return: DeleteItemBySkuIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_item_by_sku_id_with_options(request, runtime)

    async def delete_item_by_sku_id_async(
        self,
        request: cloudesl_20190801_models.DeleteItemBySkuIdRequest,
    ) -> cloudesl_20190801_models.DeleteItemBySkuIdResponse:
        """
        @param request: DeleteItemBySkuIdRequest
        @return: DeleteItemBySkuIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_item_by_sku_id_with_options_async(request, runtime)

    def delete_store_with_options(
        self,
        request: cloudesl_20190801_models.DeleteStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteStoreResponse:
        """
        @param request: DeleteStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteStore',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_store_with_options_async(
        self,
        request: cloudesl_20190801_models.DeleteStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteStoreResponse:
        """
        @param request: DeleteStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteStore',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_store(
        self,
        request: cloudesl_20190801_models.DeleteStoreRequest,
    ) -> cloudesl_20190801_models.DeleteStoreResponse:
        """
        @param request: DeleteStoreRequest
        @return: DeleteStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_store_with_options(request, runtime)

    async def delete_store_async(
        self,
        request: cloudesl_20190801_models.DeleteStoreRequest,
    ) -> cloudesl_20190801_models.DeleteStoreResponse:
        """
        @param request: DeleteStoreRequest
        @return: DeleteStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_store_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: cloudesl_20190801_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteUserResponse:
        """
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: cloudesl_20190801_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DeleteUserResponse:
        """
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: cloudesl_20190801_models.DeleteUserRequest,
    ) -> cloudesl_20190801_models.DeleteUserResponse:
        """
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: cloudesl_20190801_models.DeleteUserRequest,
    ) -> cloudesl_20190801_models.DeleteUserResponse:
        """
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def describe_alarms_with_options(
        self,
        request: cloudesl_20190801_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeAlarmsResponse:
        """
        @param request: DescribeAlarmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlarmsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.alarm_status):
            body['AlarmStatus'] = request.alarm_status
        if not UtilClient.is_unset(request.alarm_type):
            body['AlarmType'] = request.alarm_type
        if not UtilClient.is_unset(request.error_type):
            body['ErrorType'] = request.error_type
        if not UtilClient.is_unset(request.from_alarm_time):
            body['FromAlarmTime'] = request.from_alarm_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.to_alarm_time):
            body['ToAlarmTime'] = request.to_alarm_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlarms',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarms_with_options_async(
        self,
        request: cloudesl_20190801_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeAlarmsResponse:
        """
        @param request: DescribeAlarmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlarmsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.alarm_status):
            body['AlarmStatus'] = request.alarm_status
        if not UtilClient.is_unset(request.alarm_type):
            body['AlarmType'] = request.alarm_type
        if not UtilClient.is_unset(request.error_type):
            body['ErrorType'] = request.error_type
        if not UtilClient.is_unset(request.from_alarm_time):
            body['FromAlarmTime'] = request.from_alarm_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.to_alarm_time):
            body['ToAlarmTime'] = request.to_alarm_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlarms',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarms(
        self,
        request: cloudesl_20190801_models.DescribeAlarmsRequest,
    ) -> cloudesl_20190801_models.DescribeAlarmsResponse:
        """
        @param request: DescribeAlarmsRequest
        @return: DescribeAlarmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alarms_with_options(request, runtime)

    async def describe_alarms_async(
        self,
        request: cloudesl_20190801_models.DescribeAlarmsRequest,
    ) -> cloudesl_20190801_models.DescribeAlarmsResponse:
        """
        @param request: DescribeAlarmsRequest
        @return: DescribeAlarmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarms_with_options_async(request, runtime)

    def describe_ap_devices_with_options(
        self,
        request: cloudesl_20190801_models.DescribeApDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeApDevicesResponse:
        """
        @param request: DescribeApDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.activated):
            body['Activated'] = request.activated
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeApDevices',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeApDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ap_devices_with_options_async(
        self,
        request: cloudesl_20190801_models.DescribeApDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeApDevicesResponse:
        """
        @param request: DescribeApDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.activated):
            body['Activated'] = request.activated
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeApDevices',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeApDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ap_devices(
        self,
        request: cloudesl_20190801_models.DescribeApDevicesRequest,
    ) -> cloudesl_20190801_models.DescribeApDevicesResponse:
        """
        @param request: DescribeApDevicesRequest
        @return: DescribeApDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ap_devices_with_options(request, runtime)

    async def describe_ap_devices_async(
        self,
        request: cloudesl_20190801_models.DescribeApDevicesRequest,
    ) -> cloudesl_20190801_models.DescribeApDevicesResponse:
        """
        @param request: DescribeApDevicesRequest
        @return: DescribeApDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ap_devices_with_options_async(request, runtime)

    def describe_esl_devices_with_options(
        self,
        request: cloudesl_20190801_models.DescribeEslDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeEslDevicesResponse:
        """
        @param request: DescribeEslDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEslDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.be_bind):
            body['BeBind'] = request.be_bind
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.esl_status):
            body['EslStatus'] = request.esl_status
        if not UtilClient.is_unset(request.from_battery_level):
            body['FromBatteryLevel'] = request.from_battery_level
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.shelf_code):
            body['ShelfCode'] = request.shelf_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.to_battery_level):
            body['ToBatteryLevel'] = request.to_battery_level
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEslDevices',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeEslDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_esl_devices_with_options_async(
        self,
        request: cloudesl_20190801_models.DescribeEslDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeEslDevicesResponse:
        """
        @param request: DescribeEslDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEslDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.be_bind):
            body['BeBind'] = request.be_bind
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.esl_status):
            body['EslStatus'] = request.esl_status
        if not UtilClient.is_unset(request.from_battery_level):
            body['FromBatteryLevel'] = request.from_battery_level
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.shelf_code):
            body['ShelfCode'] = request.shelf_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.to_battery_level):
            body['ToBatteryLevel'] = request.to_battery_level
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEslDevices',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeEslDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_esl_devices(
        self,
        request: cloudesl_20190801_models.DescribeEslDevicesRequest,
    ) -> cloudesl_20190801_models.DescribeEslDevicesResponse:
        """
        @param request: DescribeEslDevicesRequest
        @return: DescribeEslDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_esl_devices_with_options(request, runtime)

    async def describe_esl_devices_async(
        self,
        request: cloudesl_20190801_models.DescribeEslDevicesRequest,
    ) -> cloudesl_20190801_models.DescribeEslDevicesResponse:
        """
        @param request: DescribeEslDevicesRequest
        @return: DescribeEslDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_esl_devices_with_options_async(request, runtime)

    def describe_items_with_options(
        self,
        request: cloudesl_20190801_models.DescribeItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeItemsResponse:
        """
        @param request: DescribeItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeItemsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.be_promotion):
            body['BePromotion'] = request.be_promotion
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_title):
            body['ItemTitle'] = request.item_title
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sku_id):
            body['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeItems',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_items_with_options_async(
        self,
        request: cloudesl_20190801_models.DescribeItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeItemsResponse:
        """
        @param request: DescribeItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeItemsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.be_promotion):
            body['BePromotion'] = request.be_promotion
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_title):
            body['ItemTitle'] = request.item_title
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sku_id):
            body['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeItems',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_items(
        self,
        request: cloudesl_20190801_models.DescribeItemsRequest,
    ) -> cloudesl_20190801_models.DescribeItemsResponse:
        """
        @param request: DescribeItemsRequest
        @return: DescribeItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_items_with_options(request, runtime)

    async def describe_items_async(
        self,
        request: cloudesl_20190801_models.DescribeItemsRequest,
    ) -> cloudesl_20190801_models.DescribeItemsResponse:
        """
        @param request: DescribeItemsRequest
        @return: DescribeItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_items_with_options_async(request, runtime)

    def describe_logistics_with_options(
        self,
        request: cloudesl_20190801_models.DescribeLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeLogisticsResponse:
        """
        @param request: DescribeLogisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogisticsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogistics',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeLogisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_logistics_with_options_async(
        self,
        request: cloudesl_20190801_models.DescribeLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeLogisticsResponse:
        """
        @param request: DescribeLogisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogisticsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogistics',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeLogisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_logistics(
        self,
        request: cloudesl_20190801_models.DescribeLogisticsRequest,
    ) -> cloudesl_20190801_models.DescribeLogisticsResponse:
        """
        @param request: DescribeLogisticsRequest
        @return: DescribeLogisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_logistics_with_options(request, runtime)

    async def describe_logistics_async(
        self,
        request: cloudesl_20190801_models.DescribeLogisticsRequest,
    ) -> cloudesl_20190801_models.DescribeLogisticsResponse:
        """
        @param request: DescribeLogisticsRequest
        @return: DescribeLogisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_logistics_with_options_async(request, runtime)

    def describe_pay_orders_with_options(
        self,
        request: cloudesl_20190801_models.DescribePayOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribePayOrdersResponse:
        """
        @param request: DescribePayOrdersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePayOrdersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_date):
            body['FromDate'] = request.from_date
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.to_date):
            body['ToDate'] = request.to_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePayOrders',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribePayOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pay_orders_with_options_async(
        self,
        request: cloudesl_20190801_models.DescribePayOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribePayOrdersResponse:
        """
        @param request: DescribePayOrdersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePayOrdersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_date):
            body['FromDate'] = request.from_date
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.to_date):
            body['ToDate'] = request.to_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePayOrders',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribePayOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pay_orders(
        self,
        request: cloudesl_20190801_models.DescribePayOrdersRequest,
    ) -> cloudesl_20190801_models.DescribePayOrdersResponse:
        """
        @param request: DescribePayOrdersRequest
        @return: DescribePayOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pay_orders_with_options(request, runtime)

    async def describe_pay_orders_async(
        self,
        request: cloudesl_20190801_models.DescribePayOrdersRequest,
    ) -> cloudesl_20190801_models.DescribePayOrdersResponse:
        """
        @param request: DescribePayOrdersRequest
        @return: DescribePayOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pay_orders_with_options_async(request, runtime)

    def describe_planogram_rails_with_options(
        self,
        request: cloudesl_20190801_models.DescribePlanogramRailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribePlanogramRailsResponse:
        """
        @param request: DescribePlanogramRailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlanogramRailsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.layer):
            body['Layer'] = request.layer
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rail_code):
            body['RailCode'] = request.rail_code
        if not UtilClient.is_unset(request.shelf):
            body['Shelf'] = request.shelf
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePlanogramRails',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribePlanogramRailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_planogram_rails_with_options_async(
        self,
        request: cloudesl_20190801_models.DescribePlanogramRailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribePlanogramRailsResponse:
        """
        @param request: DescribePlanogramRailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlanogramRailsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.layer):
            body['Layer'] = request.layer
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rail_code):
            body['RailCode'] = request.rail_code
        if not UtilClient.is_unset(request.shelf):
            body['Shelf'] = request.shelf
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePlanogramRails',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribePlanogramRailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_planogram_rails(
        self,
        request: cloudesl_20190801_models.DescribePlanogramRailsRequest,
    ) -> cloudesl_20190801_models.DescribePlanogramRailsResponse:
        """
        @param request: DescribePlanogramRailsRequest
        @return: DescribePlanogramRailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_planogram_rails_with_options(request, runtime)

    async def describe_planogram_rails_async(
        self,
        request: cloudesl_20190801_models.DescribePlanogramRailsRequest,
    ) -> cloudesl_20190801_models.DescribePlanogramRailsResponse:
        """
        @param request: DescribePlanogramRailsRequest
        @return: DescribePlanogramRailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_planogram_rails_with_options_async(request, runtime)

    def describe_stores_with_options(
        self,
        request: cloudesl_20190801_models.DescribeStoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeStoresResponse:
        """
        @param request: DescribeStoresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStoresResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.brand):
            body['Brand'] = request.brand
        if not UtilClient.is_unset(request.company_id):
            body['CompanyId'] = request.company_id
        if not UtilClient.is_unset(request.from_date):
            body['FromDate'] = request.from_date
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.store_name):
            body['StoreName'] = request.store_name
        if not UtilClient.is_unset(request.to_date):
            body['ToDate'] = request.to_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStores',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeStoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_stores_with_options_async(
        self,
        request: cloudesl_20190801_models.DescribeStoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeStoresResponse:
        """
        @param request: DescribeStoresRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStoresResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.brand):
            body['Brand'] = request.brand
        if not UtilClient.is_unset(request.company_id):
            body['CompanyId'] = request.company_id
        if not UtilClient.is_unset(request.from_date):
            body['FromDate'] = request.from_date
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.store_name):
            body['StoreName'] = request.store_name
        if not UtilClient.is_unset(request.to_date):
            body['ToDate'] = request.to_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStores',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeStoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_stores(
        self,
        request: cloudesl_20190801_models.DescribeStoresRequest,
    ) -> cloudesl_20190801_models.DescribeStoresResponse:
        """
        @param request: DescribeStoresRequest
        @return: DescribeStoresResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_stores_with_options(request, runtime)

    async def describe_stores_async(
        self,
        request: cloudesl_20190801_models.DescribeStoresRequest,
    ) -> cloudesl_20190801_models.DescribeStoresResponse:
        """
        @param request: DescribeStoresRequest
        @return: DescribeStoresResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_stores_with_options_async(request, runtime)

    def describe_user_log_with_options(
        self,
        request: cloudesl_20190801_models.DescribeUserLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeUserLogResponse:
        """
        @param request: DescribeUserLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.from_date):
            body['FromDate'] = request.from_date
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_title):
            body['ItemTitle'] = request.item_title
        if not UtilClient.is_unset(request.operate_status):
            body['OperateStatus'] = request.operate_status
        if not UtilClient.is_unset(request.operate_type):
            body['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.operate_user_id):
            body['OperateUserId'] = request.operate_user_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            body['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.to_date):
            body['ToDate'] = request.to_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUserLog',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeUserLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_log_with_options_async(
        self,
        request: cloudesl_20190801_models.DescribeUserLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeUserLogResponse:
        """
        @param request: DescribeUserLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.from_date):
            body['FromDate'] = request.from_date
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_title):
            body['ItemTitle'] = request.item_title
        if not UtilClient.is_unset(request.operate_status):
            body['OperateStatus'] = request.operate_status
        if not UtilClient.is_unset(request.operate_type):
            body['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.operate_user_id):
            body['OperateUserId'] = request.operate_user_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            body['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.to_date):
            body['ToDate'] = request.to_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUserLog',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeUserLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_log(
        self,
        request: cloudesl_20190801_models.DescribeUserLogRequest,
    ) -> cloudesl_20190801_models.DescribeUserLogResponse:
        """
        @param request: DescribeUserLogRequest
        @return: DescribeUserLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_log_with_options(request, runtime)

    async def describe_user_log_async(
        self,
        request: cloudesl_20190801_models.DescribeUserLogRequest,
    ) -> cloudesl_20190801_models.DescribeUserLogResponse:
        """
        @param request: DescribeUserLogRequest
        @return: DescribeUserLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_log_with_options_async(request, runtime)

    def describe_users_with_options(
        self,
        request: cloudesl_20190801_models.DescribeUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeUsersResponse:
        """
        @param request: DescribeUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUsers',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_users_with_options_async(
        self,
        request: cloudesl_20190801_models.DescribeUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.DescribeUsersResponse:
        """
        @param request: DescribeUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUsers',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.DescribeUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_users(
        self,
        request: cloudesl_20190801_models.DescribeUsersRequest,
    ) -> cloudesl_20190801_models.DescribeUsersResponse:
        """
        @param request: DescribeUsersRequest
        @return: DescribeUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_users_with_options(request, runtime)

    async def describe_users_async(
        self,
        request: cloudesl_20190801_models.DescribeUsersRequest,
    ) -> cloudesl_20190801_models.DescribeUsersResponse:
        """
        @param request: DescribeUsersRequest
        @return: DescribeUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_users_with_options_async(request, runtime)

    def get_company_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.GetCompanyResponse:
        """
        @param request: GetCompanyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCompanyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCompany',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.GetCompanyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_company_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.GetCompanyResponse:
        """
        @param request: GetCompanyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCompanyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCompany',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.GetCompanyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_company(self) -> cloudesl_20190801_models.GetCompanyResponse:
        """
        @return: GetCompanyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_company_with_options(runtime)

    async def get_company_async(self) -> cloudesl_20190801_models.GetCompanyResponse:
        """
        @return: GetCompanyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_company_with_options_async(runtime)

    def get_user_with_options(
        self,
        request: cloudesl_20190801_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.GetUserResponse:
        """
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: cloudesl_20190801_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.GetUserResponse:
        """
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: cloudesl_20190801_models.GetUserRequest,
    ) -> cloudesl_20190801_models.GetUserResponse:
        """
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: cloudesl_20190801_models.GetUserRequest,
    ) -> cloudesl_20190801_models.GetUserResponse:
        """
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def map_planogram_rail_with_options(
        self,
        request: cloudesl_20190801_models.MapPlanogramRailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.MapPlanogramRailResponse:
        """
        @param request: MapPlanogramRailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MapPlanogramRailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.layer):
            body['Layer'] = request.layer
        if not UtilClient.is_unset(request.rail_code):
            body['RailCode'] = request.rail_code
        if not UtilClient.is_unset(request.shelf):
            body['Shelf'] = request.shelf
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MapPlanogramRail',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.MapPlanogramRailResponse(),
            self.call_api(params, req, runtime)
        )

    async def map_planogram_rail_with_options_async(
        self,
        request: cloudesl_20190801_models.MapPlanogramRailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.MapPlanogramRailResponse:
        """
        @param request: MapPlanogramRailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MapPlanogramRailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.layer):
            body['Layer'] = request.layer
        if not UtilClient.is_unset(request.rail_code):
            body['RailCode'] = request.rail_code
        if not UtilClient.is_unset(request.shelf):
            body['Shelf'] = request.shelf
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MapPlanogramRail',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.MapPlanogramRailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def map_planogram_rail(
        self,
        request: cloudesl_20190801_models.MapPlanogramRailRequest,
    ) -> cloudesl_20190801_models.MapPlanogramRailResponse:
        """
        @param request: MapPlanogramRailRequest
        @return: MapPlanogramRailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.map_planogram_rail_with_options(request, runtime)

    async def map_planogram_rail_async(
        self,
        request: cloudesl_20190801_models.MapPlanogramRailRequest,
    ) -> cloudesl_20190801_models.MapPlanogramRailResponse:
        """
        @param request: MapPlanogramRailRequest
        @return: MapPlanogramRailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.map_planogram_rail_with_options_async(request, runtime)

    def refresh_taobao_item_with_options(
        self,
        request: cloudesl_20190801_models.RefreshTaobaoItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.RefreshTaobaoItemResponse:
        """
        @param request: RefreshTaobaoItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshTaobaoItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.outer_id):
            body['OuterId'] = request.outer_id
        if not UtilClient.is_unset(request.sku_id):
            body['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.taobao_item_id):
            body['TaobaoItemId'] = request.taobao_item_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshTaobaoItem',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.RefreshTaobaoItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_taobao_item_with_options_async(
        self,
        request: cloudesl_20190801_models.RefreshTaobaoItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.RefreshTaobaoItemResponse:
        """
        @param request: RefreshTaobaoItemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshTaobaoItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.outer_id):
            body['OuterId'] = request.outer_id
        if not UtilClient.is_unset(request.sku_id):
            body['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.taobao_item_id):
            body['TaobaoItemId'] = request.taobao_item_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshTaobaoItem',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.RefreshTaobaoItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_taobao_item(
        self,
        request: cloudesl_20190801_models.RefreshTaobaoItemRequest,
    ) -> cloudesl_20190801_models.RefreshTaobaoItemResponse:
        """
        @param request: RefreshTaobaoItemRequest
        @return: RefreshTaobaoItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_taobao_item_with_options(request, runtime)

    async def refresh_taobao_item_async(
        self,
        request: cloudesl_20190801_models.RefreshTaobaoItemRequest,
    ) -> cloudesl_20190801_models.RefreshTaobaoItemResponse:
        """
        @param request: RefreshTaobaoItemRequest
        @return: RefreshTaobaoItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_taobao_item_with_options_async(request, runtime)

    def unassign_user_with_options(
        self,
        request: cloudesl_20190801_models.UnassignUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UnassignUserResponse:
        """
        @param request: UnassignUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnassignUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnassignUser',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UnassignUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unassign_user_with_options_async(
        self,
        request: cloudesl_20190801_models.UnassignUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UnassignUserResponse:
        """
        @param request: UnassignUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnassignUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnassignUser',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UnassignUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unassign_user(
        self,
        request: cloudesl_20190801_models.UnassignUserRequest,
    ) -> cloudesl_20190801_models.UnassignUserResponse:
        """
        @param request: UnassignUserRequest
        @return: UnassignUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unassign_user_with_options(request, runtime)

    async def unassign_user_async(
        self,
        request: cloudesl_20190801_models.UnassignUserRequest,
    ) -> cloudesl_20190801_models.UnassignUserResponse:
        """
        @param request: UnassignUserRequest
        @return: UnassignUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unassign_user_with_options_async(request, runtime)

    def unbind_esl_device_with_options(
        self,
        request: cloudesl_20190801_models.UnbindEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UnbindEslDeviceResponse:
        """
        @param request: UnbindEslDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindEslDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindEslDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UnbindEslDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_esl_device_with_options_async(
        self,
        request: cloudesl_20190801_models.UnbindEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UnbindEslDeviceResponse:
        """
        @param request: UnbindEslDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindEslDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindEslDevice',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UnbindEslDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_esl_device(
        self,
        request: cloudesl_20190801_models.UnbindEslDeviceRequest,
    ) -> cloudesl_20190801_models.UnbindEslDeviceResponse:
        """
        @param request: UnbindEslDeviceRequest
        @return: UnbindEslDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_esl_device_with_options(request, runtime)

    async def unbind_esl_device_async(
        self,
        request: cloudesl_20190801_models.UnbindEslDeviceRequest,
    ) -> cloudesl_20190801_models.UnbindEslDeviceResponse:
        """
        @param request: UnbindEslDeviceRequest
        @return: UnbindEslDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_esl_device_with_options_async(request, runtime)

    def unbind_esl_device_shelf_with_options(
        self,
        request: cloudesl_20190801_models.UnbindEslDeviceShelfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UnbindEslDeviceShelfResponse:
        """
        @param request: UnbindEslDeviceShelfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindEslDeviceShelfResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindEslDeviceShelf',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UnbindEslDeviceShelfResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_esl_device_shelf_with_options_async(
        self,
        request: cloudesl_20190801_models.UnbindEslDeviceShelfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UnbindEslDeviceShelfResponse:
        """
        @param request: UnbindEslDeviceShelfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindEslDeviceShelfResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindEslDeviceShelf',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UnbindEslDeviceShelfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_esl_device_shelf(
        self,
        request: cloudesl_20190801_models.UnbindEslDeviceShelfRequest,
    ) -> cloudesl_20190801_models.UnbindEslDeviceShelfResponse:
        """
        @param request: UnbindEslDeviceShelfRequest
        @return: UnbindEslDeviceShelfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_esl_device_shelf_with_options(request, runtime)

    async def unbind_esl_device_shelf_async(
        self,
        request: cloudesl_20190801_models.UnbindEslDeviceShelfRequest,
    ) -> cloudesl_20190801_models.UnbindEslDeviceShelfResponse:
        """
        @param request: UnbindEslDeviceShelfRequest
        @return: UnbindEslDeviceShelfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_esl_device_shelf_with_options_async(request, runtime)

    def unmap_planogram_rail_with_options(
        self,
        request: cloudesl_20190801_models.UnmapPlanogramRailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UnmapPlanogramRailResponse:
        """
        @param request: UnmapPlanogramRailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnmapPlanogramRailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rail_code):
            body['RailCode'] = request.rail_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnmapPlanogramRail',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UnmapPlanogramRailResponse(),
            self.call_api(params, req, runtime)
        )

    async def unmap_planogram_rail_with_options_async(
        self,
        request: cloudesl_20190801_models.UnmapPlanogramRailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UnmapPlanogramRailResponse:
        """
        @param request: UnmapPlanogramRailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnmapPlanogramRailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rail_code):
            body['RailCode'] = request.rail_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnmapPlanogramRail',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UnmapPlanogramRailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unmap_planogram_rail(
        self,
        request: cloudesl_20190801_models.UnmapPlanogramRailRequest,
    ) -> cloudesl_20190801_models.UnmapPlanogramRailResponse:
        """
        @param request: UnmapPlanogramRailRequest
        @return: UnmapPlanogramRailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unmap_planogram_rail_with_options(request, runtime)

    async def unmap_planogram_rail_async(
        self,
        request: cloudesl_20190801_models.UnmapPlanogramRailRequest,
    ) -> cloudesl_20190801_models.UnmapPlanogramRailResponse:
        """
        @param request: UnmapPlanogramRailRequest
        @return: UnmapPlanogramRailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unmap_planogram_rail_with_options_async(request, runtime)

    def update_esl_device_light_with_options(
        self,
        request: cloudesl_20190801_models.UpdateEslDeviceLightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UpdateEslDeviceLightResponse:
        """
        @param request: UpdateEslDeviceLightRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEslDeviceLightResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.frequency):
            body['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.led_color):
            body['LedColor'] = request.led_color
        if not UtilClient.is_unset(request.light_up_time):
            body['LightUpTime'] = request.light_up_time
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEslDeviceLight',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UpdateEslDeviceLightResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_esl_device_light_with_options_async(
        self,
        request: cloudesl_20190801_models.UpdateEslDeviceLightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UpdateEslDeviceLightResponse:
        """
        @param request: UpdateEslDeviceLightRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEslDeviceLightResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.frequency):
            body['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.led_color):
            body['LedColor'] = request.led_color
        if not UtilClient.is_unset(request.light_up_time):
            body['LightUpTime'] = request.light_up_time
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEslDeviceLight',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UpdateEslDeviceLightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_esl_device_light(
        self,
        request: cloudesl_20190801_models.UpdateEslDeviceLightRequest,
    ) -> cloudesl_20190801_models.UpdateEslDeviceLightResponse:
        """
        @param request: UpdateEslDeviceLightRequest
        @return: UpdateEslDeviceLightResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_esl_device_light_with_options(request, runtime)

    async def update_esl_device_light_async(
        self,
        request: cloudesl_20190801_models.UpdateEslDeviceLightRequest,
    ) -> cloudesl_20190801_models.UpdateEslDeviceLightResponse:
        """
        @param request: UpdateEslDeviceLightRequest
        @return: UpdateEslDeviceLightResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_esl_device_light_with_options_async(request, runtime)

    def update_store_with_options(
        self,
        request: cloudesl_20190801_models.UpdateStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UpdateStoreResponse:
        """
        @param request: UpdateStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.brand):
            body['Brand'] = request.brand
        if not UtilClient.is_unset(request.comments):
            body['Comments'] = request.comments
        if not UtilClient.is_unset(request.groups):
            body['Groups'] = request.groups
        if not UtilClient.is_unset(request.out_id):
            body['OutId'] = request.out_id
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.store_name):
            body['StoreName'] = request.store_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStore',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UpdateStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_store_with_options_async(
        self,
        request: cloudesl_20190801_models.UpdateStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20190801_models.UpdateStoreResponse:
        """
        @param request: UpdateStoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.brand):
            body['Brand'] = request.brand
        if not UtilClient.is_unset(request.comments):
            body['Comments'] = request.comments
        if not UtilClient.is_unset(request.groups):
            body['Groups'] = request.groups
        if not UtilClient.is_unset(request.out_id):
            body['OutId'] = request.out_id
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.store_name):
            body['StoreName'] = request.store_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStore',
            version='2019-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20190801_models.UpdateStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_store(
        self,
        request: cloudesl_20190801_models.UpdateStoreRequest,
    ) -> cloudesl_20190801_models.UpdateStoreResponse:
        """
        @param request: UpdateStoreRequest
        @return: UpdateStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_store_with_options(request, runtime)

    async def update_store_async(
        self,
        request: cloudesl_20190801_models.UpdateStoreRequest,
    ) -> cloudesl_20190801_models.UpdateStoreResponse:
        """
        @param request: UpdateStoreRequest
        @return: UpdateStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_store_with_options_async(request, runtime)
