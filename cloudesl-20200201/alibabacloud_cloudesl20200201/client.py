# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudesl20200201 import models as cloudesl_20200201_models
from alibabacloud_tea_util import models as util_models


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
        request: cloudesl_20200201_models.ActivateApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.ActivateApDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ActivateApDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.ActivateApDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_ap_device_with_options_async(
        self,
        request: cloudesl_20200201_models.ActivateApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.ActivateApDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ActivateApDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.ActivateApDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_ap_device(
        self,
        request: cloudesl_20200201_models.ActivateApDeviceRequest,
    ) -> cloudesl_20200201_models.ActivateApDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_ap_device_with_options(request, runtime)

    async def activate_ap_device_async(
        self,
        request: cloudesl_20200201_models.ActivateApDeviceRequest,
    ) -> cloudesl_20200201_models.ActivateApDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_ap_device_with_options_async(request, runtime)

    def add_ap_device_with_options(
        self,
        request: cloudesl_20200201_models.AddApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AddApDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddApDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AddApDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ap_device_with_options_async(
        self,
        request: cloudesl_20200201_models.AddApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AddApDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddApDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AddApDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ap_device(
        self,
        request: cloudesl_20200201_models.AddApDeviceRequest,
    ) -> cloudesl_20200201_models.AddApDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ap_device_with_options(request, runtime)

    async def add_ap_device_async(
        self,
        request: cloudesl_20200201_models.AddApDeviceRequest,
    ) -> cloudesl_20200201_models.AddApDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ap_device_with_options_async(request, runtime)

    def add_planogram_shelf_with_options(
        self,
        request: cloudesl_20200201_models.AddPlanogramShelfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AddPlanogramShelfResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddPlanogramShelf',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AddPlanogramShelfResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_planogram_shelf_with_options_async(
        self,
        request: cloudesl_20200201_models.AddPlanogramShelfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AddPlanogramShelfResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddPlanogramShelf',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AddPlanogramShelfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_planogram_shelf(
        self,
        request: cloudesl_20200201_models.AddPlanogramShelfRequest,
    ) -> cloudesl_20200201_models.AddPlanogramShelfResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_planogram_shelf_with_options(request, runtime)

    async def add_planogram_shelf_async(
        self,
        request: cloudesl_20200201_models.AddPlanogramShelfRequest,
    ) -> cloudesl_20200201_models.AddPlanogramShelfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_planogram_shelf_with_options_async(request, runtime)

    def add_role_actions_with_options(
        self,
        request: cloudesl_20200201_models.AddRoleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AddRoleActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddRoleActions',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AddRoleActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_role_actions_with_options_async(
        self,
        request: cloudesl_20200201_models.AddRoleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AddRoleActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddRoleActions',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AddRoleActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_role_actions(
        self,
        request: cloudesl_20200201_models.AddRoleActionsRequest,
    ) -> cloudesl_20200201_models.AddRoleActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_role_actions_with_options(request, runtime)

    async def add_role_actions_async(
        self,
        request: cloudesl_20200201_models.AddRoleActionsRequest,
    ) -> cloudesl_20200201_models.AddRoleActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_role_actions_with_options_async(request, runtime)

    def add_user_with_options(
        self,
        request: cloudesl_20200201_models.AddUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AddUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AddUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_with_options_async(
        self,
        request: cloudesl_20200201_models.AddUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AddUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AddUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user(
        self,
        request: cloudesl_20200201_models.AddUserRequest,
    ) -> cloudesl_20200201_models.AddUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_with_options(request, runtime)

    async def add_user_async(
        self,
        request: cloudesl_20200201_models.AddUserRequest,
    ) -> cloudesl_20200201_models.AddUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_with_options_async(request, runtime)

    def assign_user_with_options(
        self,
        request: cloudesl_20200201_models.AssignUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AssignUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AssignUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AssignUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_user_with_options_async(
        self,
        request: cloudesl_20200201_models.AssignUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AssignUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AssignUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AssignUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_user(
        self,
        request: cloudesl_20200201_models.AssignUserRequest,
    ) -> cloudesl_20200201_models.AssignUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.assign_user_with_options(request, runtime)

    async def assign_user_async(
        self,
        request: cloudesl_20200201_models.AssignUserRequest,
    ) -> cloudesl_20200201_models.AssignUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_user_with_options_async(request, runtime)

    def associate_planogram_rail_with_options(
        self,
        request: cloudesl_20200201_models.AssociatePlanogramRailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AssociatePlanogramRailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AssociatePlanogramRail',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AssociatePlanogramRailResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_planogram_rail_with_options_async(
        self,
        request: cloudesl_20200201_models.AssociatePlanogramRailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.AssociatePlanogramRailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AssociatePlanogramRail',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AssociatePlanogramRailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_planogram_rail(
        self,
        request: cloudesl_20200201_models.AssociatePlanogramRailRequest,
    ) -> cloudesl_20200201_models.AssociatePlanogramRailResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_planogram_rail_with_options(request, runtime)

    async def associate_planogram_rail_async(
        self,
        request: cloudesl_20200201_models.AssociatePlanogramRailRequest,
    ) -> cloudesl_20200201_models.AssociatePlanogramRailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_planogram_rail_with_options_async(request, runtime)

    def batch_insert_items_with_options(
        self,
        request: cloudesl_20200201_models.BatchInsertItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.BatchInsertItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchInsertItems',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.BatchInsertItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_insert_items_with_options_async(
        self,
        request: cloudesl_20200201_models.BatchInsertItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.BatchInsertItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchInsertItems',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.BatchInsertItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_insert_items(
        self,
        request: cloudesl_20200201_models.BatchInsertItemsRequest,
    ) -> cloudesl_20200201_models.BatchInsertItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_insert_items_with_options(request, runtime)

    async def batch_insert_items_async(
        self,
        request: cloudesl_20200201_models.BatchInsertItemsRequest,
    ) -> cloudesl_20200201_models.BatchInsertItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_insert_items_with_options_async(request, runtime)

    def bind_esl_device_with_options(
        self,
        request: cloudesl_20200201_models.BindEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.BindEslDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindEslDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.BindEslDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_esl_device_with_options_async(
        self,
        request: cloudesl_20200201_models.BindEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.BindEslDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindEslDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.BindEslDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_esl_device(
        self,
        request: cloudesl_20200201_models.BindEslDeviceRequest,
    ) -> cloudesl_20200201_models.BindEslDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_esl_device_with_options(request, runtime)

    async def bind_esl_device_async(
        self,
        request: cloudesl_20200201_models.BindEslDeviceRequest,
    ) -> cloudesl_20200201_models.BindEslDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_esl_device_with_options_async(request, runtime)

    def compose_planogram_positions_with_options(
        self,
        request: cloudesl_20200201_models.ComposePlanogramPositionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.ComposePlanogramPositionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ComposePlanogramPositions',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.ComposePlanogramPositionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def compose_planogram_positions_with_options_async(
        self,
        request: cloudesl_20200201_models.ComposePlanogramPositionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.ComposePlanogramPositionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ComposePlanogramPositions',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.ComposePlanogramPositionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compose_planogram_positions(
        self,
        request: cloudesl_20200201_models.ComposePlanogramPositionsRequest,
    ) -> cloudesl_20200201_models.ComposePlanogramPositionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.compose_planogram_positions_with_options(request, runtime)

    async def compose_planogram_positions_async(
        self,
        request: cloudesl_20200201_models.ComposePlanogramPositionsRequest,
    ) -> cloudesl_20200201_models.ComposePlanogramPositionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.compose_planogram_positions_with_options_async(request, runtime)

    def create_store_with_options(
        self,
        request: cloudesl_20200201_models.CreateStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.CreateStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateStore',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.CreateStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_store_with_options_async(
        self,
        request: cloudesl_20200201_models.CreateStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.CreateStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateStore',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.CreateStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_store(
        self,
        request: cloudesl_20200201_models.CreateStoreRequest,
    ) -> cloudesl_20200201_models.CreateStoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_store_with_options(request, runtime)

    async def create_store_async(
        self,
        request: cloudesl_20200201_models.CreateStoreRequest,
    ) -> cloudesl_20200201_models.CreateStoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_store_with_options_async(request, runtime)

    def delete_ap_device_with_options(
        self,
        request: cloudesl_20200201_models.DeleteApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DeleteApDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteApDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ap_device_with_options_async(
        self,
        request: cloudesl_20200201_models.DeleteApDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DeleteApDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteApDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ap_device(
        self,
        request: cloudesl_20200201_models.DeleteApDeviceRequest,
    ) -> cloudesl_20200201_models.DeleteApDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ap_device_with_options(request, runtime)

    async def delete_ap_device_async(
        self,
        request: cloudesl_20200201_models.DeleteApDeviceRequest,
    ) -> cloudesl_20200201_models.DeleteApDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ap_device_with_options_async(request, runtime)

    def delete_planogram_shelf_with_options(
        self,
        request: cloudesl_20200201_models.DeletePlanogramShelfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DeletePlanogramShelfResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePlanogramShelf',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeletePlanogramShelfResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_planogram_shelf_with_options_async(
        self,
        request: cloudesl_20200201_models.DeletePlanogramShelfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DeletePlanogramShelfResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePlanogramShelf',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeletePlanogramShelfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_planogram_shelf(
        self,
        request: cloudesl_20200201_models.DeletePlanogramShelfRequest,
    ) -> cloudesl_20200201_models.DeletePlanogramShelfResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_planogram_shelf_with_options(request, runtime)

    async def delete_planogram_shelf_async(
        self,
        request: cloudesl_20200201_models.DeletePlanogramShelfRequest,
    ) -> cloudesl_20200201_models.DeletePlanogramShelfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_planogram_shelf_with_options_async(request, runtime)

    def delete_role_actions_with_options(
        self,
        request: cloudesl_20200201_models.DeleteRoleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DeleteRoleActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRoleActions',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteRoleActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_actions_with_options_async(
        self,
        request: cloudesl_20200201_models.DeleteRoleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DeleteRoleActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRoleActions',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteRoleActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role_actions(
        self,
        request: cloudesl_20200201_models.DeleteRoleActionsRequest,
    ) -> cloudesl_20200201_models.DeleteRoleActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_role_actions_with_options(request, runtime)

    async def delete_role_actions_async(
        self,
        request: cloudesl_20200201_models.DeleteRoleActionsRequest,
    ) -> cloudesl_20200201_models.DeleteRoleActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_role_actions_with_options_async(request, runtime)

    def delete_store_with_options(
        self,
        request: cloudesl_20200201_models.DeleteStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DeleteStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteStore',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_store_with_options_async(
        self,
        request: cloudesl_20200201_models.DeleteStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DeleteStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteStore',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_store(
        self,
        request: cloudesl_20200201_models.DeleteStoreRequest,
    ) -> cloudesl_20200201_models.DeleteStoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_store_with_options(request, runtime)

    async def delete_store_async(
        self,
        request: cloudesl_20200201_models.DeleteStoreRequest,
    ) -> cloudesl_20200201_models.DeleteStoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_store_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: cloudesl_20200201_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: cloudesl_20200201_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: cloudesl_20200201_models.DeleteUserRequest,
    ) -> cloudesl_20200201_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: cloudesl_20200201_models.DeleteUserRequest,
    ) -> cloudesl_20200201_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def describe_alarms_with_options(
        self,
        request: cloudesl_20200201_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeAlarmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAlarms',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarms_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeAlarmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAlarms',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarms(
        self,
        request: cloudesl_20200201_models.DescribeAlarmsRequest,
    ) -> cloudesl_20200201_models.DescribeAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alarms_with_options(request, runtime)

    async def describe_alarms_async(
        self,
        request: cloudesl_20200201_models.DescribeAlarmsRequest,
    ) -> cloudesl_20200201_models.DescribeAlarmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarms_with_options_async(request, runtime)

    def describe_ap_devices_with_options(
        self,
        request: cloudesl_20200201_models.DescribeApDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeApDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApDevices',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeApDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ap_devices_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribeApDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeApDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApDevices',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeApDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ap_devices(
        self,
        request: cloudesl_20200201_models.DescribeApDevicesRequest,
    ) -> cloudesl_20200201_models.DescribeApDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ap_devices_with_options(request, runtime)

    async def describe_ap_devices_async(
        self,
        request: cloudesl_20200201_models.DescribeApDevicesRequest,
    ) -> cloudesl_20200201_models.DescribeApDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ap_devices_with_options_async(request, runtime)

    def describe_binders_with_options(
        self,
        request: cloudesl_20200201_models.DescribeBindersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeBindersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBinders',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeBindersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_binders_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribeBindersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeBindersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBinders',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeBindersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_binders(
        self,
        request: cloudesl_20200201_models.DescribeBindersRequest,
    ) -> cloudesl_20200201_models.DescribeBindersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_binders_with_options(request, runtime)

    async def describe_binders_async(
        self,
        request: cloudesl_20200201_models.DescribeBindersRequest,
    ) -> cloudesl_20200201_models.DescribeBindersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_binders_with_options_async(request, runtime)

    def describe_client_package_with_options(
        self,
        request: cloudesl_20200201_models.DescribeClientPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeClientPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClientPackage',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeClientPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_package_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribeClientPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeClientPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClientPackage',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeClientPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_client_package(
        self,
        request: cloudesl_20200201_models.DescribeClientPackageRequest,
    ) -> cloudesl_20200201_models.DescribeClientPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_client_package_with_options(request, runtime)

    async def describe_client_package_async(
        self,
        request: cloudesl_20200201_models.DescribeClientPackageRequest,
    ) -> cloudesl_20200201_models.DescribeClientPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_client_package_with_options_async(request, runtime)

    def describe_esl_devices_with_options(
        self,
        request: cloudesl_20200201_models.DescribeEslDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeEslDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEslDevices',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeEslDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_esl_devices_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribeEslDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeEslDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEslDevices',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeEslDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_esl_devices(
        self,
        request: cloudesl_20200201_models.DescribeEslDevicesRequest,
    ) -> cloudesl_20200201_models.DescribeEslDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_esl_devices_with_options(request, runtime)

    async def describe_esl_devices_async(
        self,
        request: cloudesl_20200201_models.DescribeEslDevicesRequest,
    ) -> cloudesl_20200201_models.DescribeEslDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_esl_devices_with_options_async(request, runtime)

    def describe_items_with_options(
        self,
        request: cloudesl_20200201_models.DescribeItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeItems',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_items_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribeItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeItems',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_items(
        self,
        request: cloudesl_20200201_models.DescribeItemsRequest,
    ) -> cloudesl_20200201_models.DescribeItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_items_with_options(request, runtime)

    async def describe_items_async(
        self,
        request: cloudesl_20200201_models.DescribeItemsRequest,
    ) -> cloudesl_20200201_models.DescribeItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_items_with_options_async(request, runtime)

    def describe_planogram_esl_devices_with_options(
        self,
        request: cloudesl_20200201_models.DescribePlanogramEslDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribePlanogramEslDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePlanogramEslDevices',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribePlanogramEslDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_planogram_esl_devices_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribePlanogramEslDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribePlanogramEslDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePlanogramEslDevices',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribePlanogramEslDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_planogram_esl_devices(
        self,
        request: cloudesl_20200201_models.DescribePlanogramEslDevicesRequest,
    ) -> cloudesl_20200201_models.DescribePlanogramEslDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_planogram_esl_devices_with_options(request, runtime)

    async def describe_planogram_esl_devices_async(
        self,
        request: cloudesl_20200201_models.DescribePlanogramEslDevicesRequest,
    ) -> cloudesl_20200201_models.DescribePlanogramEslDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_planogram_esl_devices_with_options_async(request, runtime)

    def describe_planogram_positions_with_options(
        self,
        request: cloudesl_20200201_models.DescribePlanogramPositionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribePlanogramPositionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePlanogramPositions',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribePlanogramPositionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_planogram_positions_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribePlanogramPositionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribePlanogramPositionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePlanogramPositions',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribePlanogramPositionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_planogram_positions(
        self,
        request: cloudesl_20200201_models.DescribePlanogramPositionsRequest,
    ) -> cloudesl_20200201_models.DescribePlanogramPositionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_planogram_positions_with_options(request, runtime)

    async def describe_planogram_positions_async(
        self,
        request: cloudesl_20200201_models.DescribePlanogramPositionsRequest,
    ) -> cloudesl_20200201_models.DescribePlanogramPositionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_planogram_positions_with_options_async(request, runtime)

    def describe_planogram_rails_with_options(
        self,
        request: cloudesl_20200201_models.DescribePlanogramRailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribePlanogramRailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePlanogramRails',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribePlanogramRailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_planogram_rails_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribePlanogramRailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribePlanogramRailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePlanogramRails',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribePlanogramRailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_planogram_rails(
        self,
        request: cloudesl_20200201_models.DescribePlanogramRailsRequest,
    ) -> cloudesl_20200201_models.DescribePlanogramRailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_planogram_rails_with_options(request, runtime)

    async def describe_planogram_rails_async(
        self,
        request: cloudesl_20200201_models.DescribePlanogramRailsRequest,
    ) -> cloudesl_20200201_models.DescribePlanogramRailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_planogram_rails_with_options_async(request, runtime)

    def describe_planogram_shelves_with_options(
        self,
        request: cloudesl_20200201_models.DescribePlanogramShelvesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribePlanogramShelvesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePlanogramShelves',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribePlanogramShelvesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_planogram_shelves_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribePlanogramShelvesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribePlanogramShelvesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePlanogramShelves',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribePlanogramShelvesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_planogram_shelves(
        self,
        request: cloudesl_20200201_models.DescribePlanogramShelvesRequest,
    ) -> cloudesl_20200201_models.DescribePlanogramShelvesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_planogram_shelves_with_options(request, runtime)

    async def describe_planogram_shelves_async(
        self,
        request: cloudesl_20200201_models.DescribePlanogramShelvesRequest,
    ) -> cloudesl_20200201_models.DescribePlanogramShelvesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_planogram_shelves_with_options_async(request, runtime)

    def describe_role_actions_with_options(
        self,
        request: cloudesl_20200201_models.DescribeRoleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeRoleActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRoleActions',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeRoleActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_role_actions_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribeRoleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeRoleActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRoleActions',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeRoleActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_role_actions(
        self,
        request: cloudesl_20200201_models.DescribeRoleActionsRequest,
    ) -> cloudesl_20200201_models.DescribeRoleActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_role_actions_with_options(request, runtime)

    async def describe_role_actions_async(
        self,
        request: cloudesl_20200201_models.DescribeRoleActionsRequest,
    ) -> cloudesl_20200201_models.DescribeRoleActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_role_actions_with_options_async(request, runtime)

    def describe_store_config_with_options(
        self,
        request: cloudesl_20200201_models.DescribeStoreConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeStoreConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeStoreConfig',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeStoreConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_store_config_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribeStoreConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeStoreConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeStoreConfig',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeStoreConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_store_config(
        self,
        request: cloudesl_20200201_models.DescribeStoreConfigRequest,
    ) -> cloudesl_20200201_models.DescribeStoreConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_store_config_with_options(request, runtime)

    async def describe_store_config_async(
        self,
        request: cloudesl_20200201_models.DescribeStoreConfigRequest,
    ) -> cloudesl_20200201_models.DescribeStoreConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_store_config_with_options_async(request, runtime)

    def describe_stores_with_options(
        self,
        request: cloudesl_20200201_models.DescribeStoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeStoresResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeStores',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeStoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_stores_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribeStoresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeStoresResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeStores',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeStoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_stores(
        self,
        request: cloudesl_20200201_models.DescribeStoresRequest,
    ) -> cloudesl_20200201_models.DescribeStoresResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_stores_with_options(request, runtime)

    async def describe_stores_async(
        self,
        request: cloudesl_20200201_models.DescribeStoresRequest,
    ) -> cloudesl_20200201_models.DescribeStoresResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_stores_with_options_async(request, runtime)

    def describe_user_log_with_options(
        self,
        request: cloudesl_20200201_models.DescribeUserLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeUserLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUserLog',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeUserLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_log_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribeUserLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeUserLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUserLog',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeUserLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_log(
        self,
        request: cloudesl_20200201_models.DescribeUserLogRequest,
    ) -> cloudesl_20200201_models.DescribeUserLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_log_with_options(request, runtime)

    async def describe_user_log_async(
        self,
        request: cloudesl_20200201_models.DescribeUserLogRequest,
    ) -> cloudesl_20200201_models.DescribeUserLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_log_with_options_async(request, runtime)

    def describe_users_with_options(
        self,
        request: cloudesl_20200201_models.DescribeUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUsers',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_users_with_options_async(
        self,
        request: cloudesl_20200201_models.DescribeUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DescribeUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUsers',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_users(
        self,
        request: cloudesl_20200201_models.DescribeUsersRequest,
    ) -> cloudesl_20200201_models.DescribeUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_users_with_options(request, runtime)

    async def describe_users_async(
        self,
        request: cloudesl_20200201_models.DescribeUsersRequest,
    ) -> cloudesl_20200201_models.DescribeUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_users_with_options_async(request, runtime)

    def dissociate_planogram_rail_with_options(
        self,
        request: cloudesl_20200201_models.DissociatePlanogramRailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DissociatePlanogramRailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DissociatePlanogramRail',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DissociatePlanogramRailResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_planogram_rail_with_options_async(
        self,
        request: cloudesl_20200201_models.DissociatePlanogramRailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.DissociatePlanogramRailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DissociatePlanogramRail',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DissociatePlanogramRailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_planogram_rail(
        self,
        request: cloudesl_20200201_models.DissociatePlanogramRailRequest,
    ) -> cloudesl_20200201_models.DissociatePlanogramRailResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_planogram_rail_with_options(request, runtime)

    async def dissociate_planogram_rail_async(
        self,
        request: cloudesl_20200201_models.DissociatePlanogramRailRequest,
    ) -> cloudesl_20200201_models.DissociatePlanogramRailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_planogram_rail_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: cloudesl_20200201_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: cloudesl_20200201_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: cloudesl_20200201_models.GetUserRequest,
    ) -> cloudesl_20200201_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: cloudesl_20200201_models.GetUserRequest,
    ) -> cloudesl_20200201_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def unassign_user_with_options(
        self,
        request: cloudesl_20200201_models.UnassignUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UnassignUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnassignUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UnassignUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unassign_user_with_options_async(
        self,
        request: cloudesl_20200201_models.UnassignUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UnassignUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnassignUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UnassignUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unassign_user(
        self,
        request: cloudesl_20200201_models.UnassignUserRequest,
    ) -> cloudesl_20200201_models.UnassignUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassign_user_with_options(request, runtime)

    async def unassign_user_async(
        self,
        request: cloudesl_20200201_models.UnassignUserRequest,
    ) -> cloudesl_20200201_models.UnassignUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassign_user_with_options_async(request, runtime)

    def unbind_esl_device_with_options(
        self,
        request: cloudesl_20200201_models.UnbindEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UnbindEslDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindEslDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UnbindEslDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_esl_device_with_options_async(
        self,
        request: cloudesl_20200201_models.UnbindEslDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UnbindEslDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindEslDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UnbindEslDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_esl_device(
        self,
        request: cloudesl_20200201_models.UnbindEslDeviceRequest,
    ) -> cloudesl_20200201_models.UnbindEslDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_esl_device_with_options(request, runtime)

    async def unbind_esl_device_async(
        self,
        request: cloudesl_20200201_models.UnbindEslDeviceRequest,
    ) -> cloudesl_20200201_models.UnbindEslDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_esl_device_with_options_async(request, runtime)

    def update_esl_device_light_with_options(
        self,
        request: cloudesl_20200201_models.UpdateEslDeviceLightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UpdateEslDeviceLightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEslDeviceLight',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UpdateEslDeviceLightResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_esl_device_light_with_options_async(
        self,
        request: cloudesl_20200201_models.UpdateEslDeviceLightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UpdateEslDeviceLightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEslDeviceLight',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UpdateEslDeviceLightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_esl_device_light(
        self,
        request: cloudesl_20200201_models.UpdateEslDeviceLightRequest,
    ) -> cloudesl_20200201_models.UpdateEslDeviceLightResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_esl_device_light_with_options(request, runtime)

    async def update_esl_device_light_async(
        self,
        request: cloudesl_20200201_models.UpdateEslDeviceLightRequest,
    ) -> cloudesl_20200201_models.UpdateEslDeviceLightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_esl_device_light_with_options_async(request, runtime)

    def update_store_with_options(
        self,
        request: cloudesl_20200201_models.UpdateStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UpdateStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateStore',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UpdateStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_store_with_options_async(
        self,
        request: cloudesl_20200201_models.UpdateStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UpdateStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateStore',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UpdateStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_store(
        self,
        request: cloudesl_20200201_models.UpdateStoreRequest,
    ) -> cloudesl_20200201_models.UpdateStoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_store_with_options(request, runtime)

    async def update_store_async(
        self,
        request: cloudesl_20200201_models.UpdateStoreRequest,
    ) -> cloudesl_20200201_models.UpdateStoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_store_with_options_async(request, runtime)

    def update_store_config_with_options(
        self,
        request: cloudesl_20200201_models.UpdateStoreConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UpdateStoreConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateStoreConfig',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UpdateStoreConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_store_config_with_options_async(
        self,
        request: cloudesl_20200201_models.UpdateStoreConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UpdateStoreConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateStoreConfig',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UpdateStoreConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_store_config(
        self,
        request: cloudesl_20200201_models.UpdateStoreConfigRequest,
    ) -> cloudesl_20200201_models.UpdateStoreConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_store_config_with_options(request, runtime)

    async def update_store_config_async(
        self,
        request: cloudesl_20200201_models.UpdateStoreConfigRequest,
    ) -> cloudesl_20200201_models.UpdateStoreConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_store_config_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: cloudesl_20200201_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: cloudesl_20200201_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudesl_20200201_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: cloudesl_20200201_models.UpdateUserRequest,
    ) -> cloudesl_20200201_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: cloudesl_20200201_models.UpdateUserRequest,
    ) -> cloudesl_20200201_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)
