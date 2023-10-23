# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkvisual20230630 import models as linkvisual_20230630_models
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
            'ap-northeast-1': 'linkvisual.aliyuncs.com',
            'ap-northeast-2-pop': 'linkvisual.aliyuncs.com',
            'ap-south-1': 'linkvisual.aliyuncs.com',
            'ap-southeast-1': 'linkvisual.aliyuncs.com',
            'ap-southeast-2': 'linkvisual.aliyuncs.com',
            'ap-southeast-3': 'linkvisual.aliyuncs.com',
            'ap-southeast-5': 'linkvisual.aliyuncs.com',
            'cn-beijing': 'linkvisual.aliyuncs.com',
            'cn-beijing-finance-1': 'linkvisual.aliyuncs.com',
            'cn-beijing-finance-pop': 'linkvisual.aliyuncs.com',
            'cn-beijing-gov-1': 'linkvisual.aliyuncs.com',
            'cn-beijing-nu16-b01': 'linkvisual.aliyuncs.com',
            'cn-chengdu': 'linkvisual.aliyuncs.com',
            'cn-edge-1': 'linkvisual.aliyuncs.com',
            'cn-fujian': 'linkvisual.aliyuncs.com',
            'cn-haidian-cm12-c01': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-finance': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-test-306': 'linkvisual.aliyuncs.com',
            'cn-hongkong': 'linkvisual.aliyuncs.com',
            'cn-hongkong-finance-pop': 'linkvisual.aliyuncs.com',
            'cn-huhehaote': 'linkvisual.aliyuncs.com',
            'cn-north-2-gov-1': 'linkvisual.aliyuncs.com',
            'cn-qingdao': 'linkvisual.aliyuncs.com',
            'cn-qingdao-nebula': 'linkvisual.aliyuncs.com',
            'cn-shanghai-et15-b01': 'linkvisual.aliyuncs.com',
            'cn-shanghai-et2-b01': 'linkvisual.aliyuncs.com',
            'cn-shanghai-finance-1': 'linkvisual.aliyuncs.com',
            'cn-shanghai-inner': 'linkvisual.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'linkvisual.aliyuncs.com',
            'cn-shenzhen': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-finance-1': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-inner': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'linkvisual.aliyuncs.com',
            'cn-wuhan': 'linkvisual.aliyuncs.com',
            'cn-yushanfang': 'linkvisual.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'linkvisual.aliyuncs.com',
            'cn-zhangjiakou': 'linkvisual.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'linkvisual.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'linkvisual.aliyuncs.com',
            'eu-central-1': 'linkvisual.aliyuncs.com',
            'eu-west-1': 'linkvisual.aliyuncs.com',
            'eu-west-1-oxs': 'linkvisual.aliyuncs.com',
            'me-east-1': 'linkvisual.aliyuncs.com',
            'rus-west-1-pop': 'linkvisual.aliyuncs.com',
            'us-east-1': 'linkvisual.aliyuncs.com',
            'us-west-1': 'linkvisual.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('linkvisual', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bind_storage_order_with_options(
        self,
        request: linkvisual_20230630_models.BindStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.BindStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.max_record_file_duration):
            query['MaxRecordFileDuration'] = request.max_record_file_duration
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.BindStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_storage_order_with_options_async(
        self,
        request: linkvisual_20230630_models.BindStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.BindStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.max_record_file_duration):
            query['MaxRecordFileDuration'] = request.max_record_file_duration
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.BindStorageOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_storage_order(
        self,
        request: linkvisual_20230630_models.BindStorageOrderRequest,
    ) -> linkvisual_20230630_models.BindStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_storage_order_with_options(request, runtime)

    async def bind_storage_order_async(
        self,
        request: linkvisual_20230630_models.BindStorageOrderRequest,
    ) -> linkvisual_20230630_models.BindStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_storage_order_with_options_async(request, runtime)

    def check_free_storage_valid_with_options(
        self,
        request: linkvisual_20230630_models.CheckFreeStorageValidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.CheckFreeStorageValidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckFreeStorageValid',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.CheckFreeStorageValidResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_free_storage_valid_with_options_async(
        self,
        request: linkvisual_20230630_models.CheckFreeStorageValidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.CheckFreeStorageValidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckFreeStorageValid',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.CheckFreeStorageValidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_free_storage_valid(
        self,
        request: linkvisual_20230630_models.CheckFreeStorageValidRequest,
    ) -> linkvisual_20230630_models.CheckFreeStorageValidResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_free_storage_valid_with_options(request, runtime)

    async def check_free_storage_valid_async(
        self,
        request: linkvisual_20230630_models.CheckFreeStorageValidRequest,
    ) -> linkvisual_20230630_models.CheckFreeStorageValidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_free_storage_valid_with_options_async(request, runtime)

    def consume_free_storage_with_options(
        self,
        request: linkvisual_20230630_models.ConsumeFreeStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.ConsumeFreeStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.immediate_use):
            query['ImmediateUse'] = request.immediate_use
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.quota):
            query['Quota'] = request.quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConsumeFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.ConsumeFreeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def consume_free_storage_with_options_async(
        self,
        request: linkvisual_20230630_models.ConsumeFreeStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.ConsumeFreeStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.immediate_use):
            query['ImmediateUse'] = request.immediate_use
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.quota):
            query['Quota'] = request.quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConsumeFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.ConsumeFreeStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def consume_free_storage(
        self,
        request: linkvisual_20230630_models.ConsumeFreeStorageRequest,
    ) -> linkvisual_20230630_models.ConsumeFreeStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.consume_free_storage_with_options(request, runtime)

    async def consume_free_storage_async(
        self,
        request: linkvisual_20230630_models.ConsumeFreeStorageRequest,
    ) -> linkvisual_20230630_models.ConsumeFreeStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.consume_free_storage_with_options_async(request, runtime)

    def create_and_pay_storage_order_with_options(
        self,
        request: linkvisual_20230630_models.CreateAndPayStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.CreateAndPayStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.copies):
            query['Copies'] = request.copies
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.immediate_use):
            query['ImmediateUse'] = request.immediate_use
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.max_record_file_duration):
            query['MaxRecordFileDuration'] = request.max_record_file_duration
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndPayStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.CreateAndPayStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_and_pay_storage_order_with_options_async(
        self,
        request: linkvisual_20230630_models.CreateAndPayStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.CreateAndPayStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.copies):
            query['Copies'] = request.copies
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.immediate_use):
            query['ImmediateUse'] = request.immediate_use
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.max_record_file_duration):
            query['MaxRecordFileDuration'] = request.max_record_file_duration
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndPayStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.CreateAndPayStorageOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_and_pay_storage_order(
        self,
        request: linkvisual_20230630_models.CreateAndPayStorageOrderRequest,
    ) -> linkvisual_20230630_models.CreateAndPayStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_and_pay_storage_order_with_options(request, runtime)

    async def create_and_pay_storage_order_async(
        self,
        request: linkvisual_20230630_models.CreateAndPayStorageOrderRequest,
    ) -> linkvisual_20230630_models.CreateAndPayStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_and_pay_storage_order_with_options_async(request, runtime)

    def enable_free_storage_with_options(
        self,
        request: linkvisual_20230630_models.EnableFreeStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.EnableFreeStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.EnableFreeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_free_storage_with_options_async(
        self,
        request: linkvisual_20230630_models.EnableFreeStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.EnableFreeStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.EnableFreeStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_free_storage(
        self,
        request: linkvisual_20230630_models.EnableFreeStorageRequest,
    ) -> linkvisual_20230630_models.EnableFreeStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_free_storage_with_options(request, runtime)

    async def enable_free_storage_async(
        self,
        request: linkvisual_20230630_models.EnableFreeStorageRequest,
    ) -> linkvisual_20230630_models.EnableFreeStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_free_storage_with_options_async(request, runtime)

    def enable_storage_order_with_options(
        self,
        request: linkvisual_20230630_models.EnableStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.EnableStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.EnableStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_storage_order_with_options_async(
        self,
        request: linkvisual_20230630_models.EnableStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.EnableStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.EnableStorageOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_storage_order(
        self,
        request: linkvisual_20230630_models.EnableStorageOrderRequest,
    ) -> linkvisual_20230630_models.EnableStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_storage_order_with_options(request, runtime)

    async def enable_storage_order_async(
        self,
        request: linkvisual_20230630_models.EnableStorageOrderRequest,
    ) -> linkvisual_20230630_models.EnableStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_storage_order_with_options_async(request, runtime)

    def freeze_free_storage_with_options(
        self,
        request: linkvisual_20230630_models.FreezeFreeStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.FreezeFreeStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FreezeFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.FreezeFreeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def freeze_free_storage_with_options_async(
        self,
        request: linkvisual_20230630_models.FreezeFreeStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.FreezeFreeStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FreezeFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.FreezeFreeStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def freeze_free_storage(
        self,
        request: linkvisual_20230630_models.FreezeFreeStorageRequest,
    ) -> linkvisual_20230630_models.FreezeFreeStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.freeze_free_storage_with_options(request, runtime)

    async def freeze_free_storage_async(
        self,
        request: linkvisual_20230630_models.FreezeFreeStorageRequest,
    ) -> linkvisual_20230630_models.FreezeFreeStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.freeze_free_storage_with_options_async(request, runtime)

    def freeze_storage_order_with_options(
        self,
        request: linkvisual_20230630_models.FreezeStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.FreezeStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FreezeStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.FreezeStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def freeze_storage_order_with_options_async(
        self,
        request: linkvisual_20230630_models.FreezeStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.FreezeStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FreezeStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.FreezeStorageOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def freeze_storage_order(
        self,
        request: linkvisual_20230630_models.FreezeStorageOrderRequest,
    ) -> linkvisual_20230630_models.FreezeStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.freeze_storage_order_with_options(request, runtime)

    async def freeze_storage_order_async(
        self,
        request: linkvisual_20230630_models.FreezeStorageOrderRequest,
    ) -> linkvisual_20230630_models.FreezeStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.freeze_storage_order_with_options_async(request, runtime)

    def generate_device_with_options(
        self,
        request: linkvisual_20230630_models.GenerateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.GenerateDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDevice',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.GenerateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_device_with_options_async(
        self,
        request: linkvisual_20230630_models.GenerateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.GenerateDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDevice',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.GenerateDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_device(
        self,
        request: linkvisual_20230630_models.GenerateDeviceRequest,
    ) -> linkvisual_20230630_models.GenerateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_device_with_options(request, runtime)

    async def generate_device_async(
        self,
        request: linkvisual_20230630_models.GenerateDeviceRequest,
    ) -> linkvisual_20230630_models.GenerateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_device_with_options_async(request, runtime)

    def generate_device_by_batch_id_with_options(
        self,
        request: linkvisual_20230630_models.GenerateDeviceByBatchIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.GenerateDeviceByBatchIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDeviceByBatchId',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.GenerateDeviceByBatchIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_device_by_batch_id_with_options_async(
        self,
        request: linkvisual_20230630_models.GenerateDeviceByBatchIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.GenerateDeviceByBatchIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDeviceByBatchId',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.GenerateDeviceByBatchIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_device_by_batch_id(
        self,
        request: linkvisual_20230630_models.GenerateDeviceByBatchIdRequest,
    ) -> linkvisual_20230630_models.GenerateDeviceByBatchIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_device_by_batch_id_with_options(request, runtime)

    async def generate_device_by_batch_id_async(
        self,
        request: linkvisual_20230630_models.GenerateDeviceByBatchIdRequest,
    ) -> linkvisual_20230630_models.GenerateDeviceByBatchIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_device_by_batch_id_with_options_async(request, runtime)

    def query_batch_status_with_options(
        self,
        request: linkvisual_20230630_models.QueryBatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryBatchStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBatchStatus',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryBatchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_batch_status_with_options_async(
        self,
        request: linkvisual_20230630_models.QueryBatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryBatchStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBatchStatus',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryBatchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_batch_status(
        self,
        request: linkvisual_20230630_models.QueryBatchStatusRequest,
    ) -> linkvisual_20230630_models.QueryBatchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_batch_status_with_options(request, runtime)

    async def query_batch_status_async(
        self,
        request: linkvisual_20230630_models.QueryBatchStatusRequest,
    ) -> linkvisual_20230630_models.QueryBatchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_batch_status_with_options_async(request, runtime)

    def query_devices_download_url_with_options(
        self,
        request: linkvisual_20230630_models.QueryDevicesDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryDevicesDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicesDownloadUrl',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryDevicesDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_devices_download_url_with_options_async(
        self,
        request: linkvisual_20230630_models.QueryDevicesDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryDevicesDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicesDownloadUrl',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryDevicesDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_devices_download_url(
        self,
        request: linkvisual_20230630_models.QueryDevicesDownloadUrlRequest,
    ) -> linkvisual_20230630_models.QueryDevicesDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_devices_download_url_with_options(request, runtime)

    async def query_devices_download_url_async(
        self,
        request: linkvisual_20230630_models.QueryDevicesDownloadUrlRequest,
    ) -> linkvisual_20230630_models.QueryDevicesDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_devices_download_url_with_options_async(request, runtime)

    def query_free_storage_with_options(
        self,
        request: linkvisual_20230630_models.QueryFreeStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryFreeStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryFreeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_free_storage_with_options_async(
        self,
        request: linkvisual_20230630_models.QueryFreeStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryFreeStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryFreeStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_free_storage(
        self,
        request: linkvisual_20230630_models.QueryFreeStorageRequest,
    ) -> linkvisual_20230630_models.QueryFreeStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_free_storage_with_options(request, runtime)

    async def query_free_storage_async(
        self,
        request: linkvisual_20230630_models.QueryFreeStorageRequest,
    ) -> linkvisual_20230630_models.QueryFreeStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_free_storage_with_options_async(request, runtime)

    def query_generate_devices_info_list_with_options(
        self,
        request: linkvisual_20230630_models.QueryGenerateDevicesInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryGenerateDevicesInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGenerateDevicesInfoList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryGenerateDevicesInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_generate_devices_info_list_with_options_async(
        self,
        request: linkvisual_20230630_models.QueryGenerateDevicesInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryGenerateDevicesInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGenerateDevicesInfoList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryGenerateDevicesInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_generate_devices_info_list(
        self,
        request: linkvisual_20230630_models.QueryGenerateDevicesInfoListRequest,
    ) -> linkvisual_20230630_models.QueryGenerateDevicesInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_generate_devices_info_list_with_options(request, runtime)

    async def query_generate_devices_info_list_async(
        self,
        request: linkvisual_20230630_models.QueryGenerateDevicesInfoListRequest,
    ) -> linkvisual_20230630_models.QueryGenerateDevicesInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_generate_devices_info_list_with_options_async(request, runtime)

    def query_generate_devices_record_with_options(
        self,
        request: linkvisual_20230630_models.QueryGenerateDevicesRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryGenerateDevicesRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryGenerateDevicesRecord',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryGenerateDevicesRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_generate_devices_record_with_options_async(
        self,
        request: linkvisual_20230630_models.QueryGenerateDevicesRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryGenerateDevicesRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryGenerateDevicesRecord',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryGenerateDevicesRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_generate_devices_record(
        self,
        request: linkvisual_20230630_models.QueryGenerateDevicesRecordRequest,
    ) -> linkvisual_20230630_models.QueryGenerateDevicesRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_generate_devices_record_with_options(request, runtime)

    async def query_generate_devices_record_async(
        self,
        request: linkvisual_20230630_models.QueryGenerateDevicesRecordRequest,
    ) -> linkvisual_20230630_models.QueryGenerateDevicesRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_generate_devices_record_with_options_async(request, runtime)

    def query_storage_commodity_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryStorageCommodityListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryStorageCommodityList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryStorageCommodityListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_storage_commodity_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryStorageCommodityListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryStorageCommodityList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryStorageCommodityListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_storage_commodity_list(self) -> linkvisual_20230630_models.QueryStorageCommodityListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_storage_commodity_list_with_options(runtime)

    async def query_storage_commodity_list_async(self) -> linkvisual_20230630_models.QueryStorageCommodityListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_storage_commodity_list_with_options_async(runtime)

    def query_storage_order_with_options(
        self,
        request: linkvisual_20230630_models.QueryStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_storage_order_with_options_async(
        self,
        request: linkvisual_20230630_models.QueryStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryStorageOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_storage_order(
        self,
        request: linkvisual_20230630_models.QueryStorageOrderRequest,
    ) -> linkvisual_20230630_models.QueryStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_storage_order_with_options(request, runtime)

    async def query_storage_order_async(
        self,
        request: linkvisual_20230630_models.QueryStorageOrderRequest,
    ) -> linkvisual_20230630_models.QueryStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_storage_order_with_options_async(request, runtime)

    def query_storage_order_list_with_options(
        self,
        request: linkvisual_20230630_models.QueryStorageOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryStorageOrderListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStorageOrderList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryStorageOrderListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_storage_order_list_with_options_async(
        self,
        request: linkvisual_20230630_models.QueryStorageOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.QueryStorageOrderListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStorageOrderList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryStorageOrderListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_storage_order_list(
        self,
        request: linkvisual_20230630_models.QueryStorageOrderListRequest,
    ) -> linkvisual_20230630_models.QueryStorageOrderListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_storage_order_list_with_options(request, runtime)

    async def query_storage_order_list_async(
        self,
        request: linkvisual_20230630_models.QueryStorageOrderListRequest,
    ) -> linkvisual_20230630_models.QueryStorageOrderListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_storage_order_list_with_options_async(request, runtime)

    def transfer_storage_order_with_options(
        self,
        request: linkvisual_20230630_models.TransferStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.TransferStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_iot_id):
            query['DstIotId'] = request.dst_iot_id
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.immediate_use):
            query['ImmediateUse'] = request.immediate_use
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.src_iot_id):
            query['SrcIotId'] = request.src_iot_id
        if not UtilClient.is_unset(request.src_order_id):
            query['SrcOrderId'] = request.src_order_id
        if not UtilClient.is_unset(request.support_cross_identity_transfer):
            query['SupportCrossIdentityTransfer'] = request.support_cross_identity_transfer
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.TransferStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_storage_order_with_options_async(
        self,
        request: linkvisual_20230630_models.TransferStorageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.TransferStorageOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_iot_id):
            query['DstIotId'] = request.dst_iot_id
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.immediate_use):
            query['ImmediateUse'] = request.immediate_use
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.src_iot_id):
            query['SrcIotId'] = request.src_iot_id
        if not UtilClient.is_unset(request.src_order_id):
            query['SrcOrderId'] = request.src_order_id
        if not UtilClient.is_unset(request.support_cross_identity_transfer):
            query['SupportCrossIdentityTransfer'] = request.support_cross_identity_transfer
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.TransferStorageOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_storage_order(
        self,
        request: linkvisual_20230630_models.TransferStorageOrderRequest,
    ) -> linkvisual_20230630_models.TransferStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_storage_order_with_options(request, runtime)

    async def transfer_storage_order_async(
        self,
        request: linkvisual_20230630_models.TransferStorageOrderRequest,
    ) -> linkvisual_20230630_models.TransferStorageOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_storage_order_with_options_async(request, runtime)

    def upload_device_name_list_with_options(
        self,
        request: linkvisual_20230630_models.UploadDeviceNameListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.UploadDeviceNameListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not UtilClient.is_unset(request.device_names):
            body['DeviceNames'] = request.device_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDeviceNameList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.UploadDeviceNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_device_name_list_with_options_async(
        self,
        request: linkvisual_20230630_models.UploadDeviceNameListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20230630_models.UploadDeviceNameListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not UtilClient.is_unset(request.device_names):
            body['DeviceNames'] = request.device_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDeviceNameList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.UploadDeviceNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_device_name_list(
        self,
        request: linkvisual_20230630_models.UploadDeviceNameListRequest,
    ) -> linkvisual_20230630_models.UploadDeviceNameListResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_device_name_list_with_options(request, runtime)

    async def upload_device_name_list_async(
        self,
        request: linkvisual_20230630_models.UploadDeviceNameListRequest,
    ) -> linkvisual_20230630_models.UploadDeviceNameListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_device_name_list_with_options_async(request, runtime)
