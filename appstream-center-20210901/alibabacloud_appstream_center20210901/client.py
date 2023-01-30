# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_appstream_center20210901 import models as appstream_center_20210901_models
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
        self._endpoint = self.get_endpoint('appstream-center', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def approve_ota_task_with_options(
        self,
        request: appstream_center_20210901_models.ApproveOtaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ApproveOtaTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.ota_type):
            body['OtaType'] = request.ota_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApproveOtaTask',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ApproveOtaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_ota_task_with_options_async(
        self,
        request: appstream_center_20210901_models.ApproveOtaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ApproveOtaTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.ota_type):
            body['OtaType'] = request.ota_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApproveOtaTask',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ApproveOtaTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_ota_task(
        self,
        request: appstream_center_20210901_models.ApproveOtaTaskRequest,
    ) -> appstream_center_20210901_models.ApproveOtaTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_ota_task_with_options(request, runtime)

    async def approve_ota_task_async(
        self,
        request: appstream_center_20210901_models.ApproveOtaTaskRequest,
    ) -> appstream_center_20210901_models.ApproveOtaTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_ota_task_with_options_async(request, runtime)

    def authorize_instance_group_with_options(
        self,
        request: appstream_center_20210901_models.AuthorizeInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.AuthorizeInstanceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.authorize_user_ids):
            body['AuthorizeUserIds'] = request.authorize_user_ids
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.un_authorize_user_ids):
            body['UnAuthorizeUserIds'] = request.un_authorize_user_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AuthorizeInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.AuthorizeInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_instance_group_with_options_async(
        self,
        request: appstream_center_20210901_models.AuthorizeInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.AuthorizeInstanceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.authorize_user_ids):
            body['AuthorizeUserIds'] = request.authorize_user_ids
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.un_authorize_user_ids):
            body['UnAuthorizeUserIds'] = request.un_authorize_user_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AuthorizeInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.AuthorizeInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_instance_group(
        self,
        request: appstream_center_20210901_models.AuthorizeInstanceGroupRequest,
    ) -> appstream_center_20210901_models.AuthorizeInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.authorize_instance_group_with_options(request, runtime)

    async def authorize_instance_group_async(
        self,
        request: appstream_center_20210901_models.AuthorizeInstanceGroupRequest,
    ) -> appstream_center_20210901_models.AuthorizeInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.authorize_instance_group_with_options_async(request, runtime)

    def cancel_ota_task_with_options(
        self,
        request: appstream_center_20210901_models.CancelOtaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.CancelOtaTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelOtaTask',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.CancelOtaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_ota_task_with_options_async(
        self,
        request: appstream_center_20210901_models.CancelOtaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.CancelOtaTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelOtaTask',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.CancelOtaTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_ota_task(
        self,
        request: appstream_center_20210901_models.CancelOtaTaskRequest,
    ) -> appstream_center_20210901_models.CancelOtaTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_ota_task_with_options(request, runtime)

    async def cancel_ota_task_async(
        self,
        request: appstream_center_20210901_models.CancelOtaTaskRequest,
    ) -> appstream_center_20210901_models.CancelOtaTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_ota_task_with_options_async(request, runtime)

    def create_app_instance_group_with_options(
        self,
        tmp_req: appstream_center_20210901_models.CreateAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.CreateAppInstanceGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.CreateAppInstanceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network):
            request.network_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not UtilClient.is_unset(tmp_req.node_pool):
            request.node_pool_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_center_image_id):
            body['AppCenterImageId'] = request.app_center_image_id
        if not UtilClient.is_unset(request.app_instance_group_name):
            body['AppInstanceGroupName'] = request.app_instance_group_name
        if not UtilClient.is_unset(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_resource_mode):
            body['ChargeResourceMode'] = request.charge_resource_mode
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.network_shrink):
            body['Network'] = request.network_shrink
        if not UtilClient.is_unset(request.node_pool_shrink):
            body['NodePool'] = request.node_pool_shrink
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.pre_open_app_id):
            body['PreOpenAppId'] = request.pre_open_app_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.promotion_id):
            body['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.session_timeout):
            body['SessionTimeout'] = request.session_timeout
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.CreateAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_instance_group_with_options_async(
        self,
        tmp_req: appstream_center_20210901_models.CreateAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.CreateAppInstanceGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.CreateAppInstanceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network):
            request.network_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not UtilClient.is_unset(tmp_req.node_pool):
            request.node_pool_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_center_image_id):
            body['AppCenterImageId'] = request.app_center_image_id
        if not UtilClient.is_unset(request.app_instance_group_name):
            body['AppInstanceGroupName'] = request.app_instance_group_name
        if not UtilClient.is_unset(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_resource_mode):
            body['ChargeResourceMode'] = request.charge_resource_mode
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.network_shrink):
            body['Network'] = request.network_shrink
        if not UtilClient.is_unset(request.node_pool_shrink):
            body['NodePool'] = request.node_pool_shrink
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.pre_open_app_id):
            body['PreOpenAppId'] = request.pre_open_app_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.promotion_id):
            body['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.session_timeout):
            body['SessionTimeout'] = request.session_timeout
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.CreateAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_instance_group(
        self,
        request: appstream_center_20210901_models.CreateAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.CreateAppInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_instance_group_with_options(request, runtime)

    async def create_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.CreateAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.CreateAppInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_instance_group_with_options_async(request, runtime)

    def delete_app_instance_group_with_options(
        self,
        request: appstream_center_20210901_models.DeleteAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.DeleteAppInstanceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.DeleteAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_instance_group_with_options_async(
        self,
        request: appstream_center_20210901_models.DeleteAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.DeleteAppInstanceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.DeleteAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_instance_group(
        self,
        request: appstream_center_20210901_models.DeleteAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.DeleteAppInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_instance_group_with_options(request, runtime)

    async def delete_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.DeleteAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.DeleteAppInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_instance_group_with_options_async(request, runtime)

    def get_ota_task_by_task_id_with_options(
        self,
        request: appstream_center_20210901_models.GetOtaTaskByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetOtaTaskByTaskIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOtaTaskByTaskId',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.GetOtaTaskByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ota_task_by_task_id_with_options_async(
        self,
        request: appstream_center_20210901_models.GetOtaTaskByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetOtaTaskByTaskIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOtaTaskByTaskId',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.GetOtaTaskByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ota_task_by_task_id(
        self,
        request: appstream_center_20210901_models.GetOtaTaskByTaskIdRequest,
    ) -> appstream_center_20210901_models.GetOtaTaskByTaskIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ota_task_by_task_id_with_options(request, runtime)

    async def get_ota_task_by_task_id_async(
        self,
        request: appstream_center_20210901_models.GetOtaTaskByTaskIdRequest,
    ) -> appstream_center_20210901_models.GetOtaTaskByTaskIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ota_task_by_task_id_with_options_async(request, runtime)

    def get_resource_price_with_options(
        self,
        request: appstream_center_20210901_models.GetResourcePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetResourcePriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourcePrice',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.GetResourcePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_price_with_options_async(
        self,
        request: appstream_center_20210901_models.GetResourcePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetResourcePriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourcePrice',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.GetResourcePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_price(
        self,
        request: appstream_center_20210901_models.GetResourcePriceRequest,
    ) -> appstream_center_20210901_models.GetResourcePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_price_with_options(request, runtime)

    async def get_resource_price_async(
        self,
        request: appstream_center_20210901_models.GetResourcePriceRequest,
    ) -> appstream_center_20210901_models.GetResourcePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_price_with_options_async(request, runtime)

    def get_resource_renew_price_with_options(
        self,
        request: appstream_center_20210901_models.GetResourceRenewPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetResourceRenewPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceRenewPrice',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.GetResourceRenewPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_renew_price_with_options_async(
        self,
        request: appstream_center_20210901_models.GetResourceRenewPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetResourceRenewPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceRenewPrice',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.GetResourceRenewPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_renew_price(
        self,
        request: appstream_center_20210901_models.GetResourceRenewPriceRequest,
    ) -> appstream_center_20210901_models.GetResourceRenewPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_renew_price_with_options(request, runtime)

    async def get_resource_renew_price_async(
        self,
        request: appstream_center_20210901_models.GetResourceRenewPriceRequest,
    ) -> appstream_center_20210901_models.GetResourceRenewPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_renew_price_with_options_async(request, runtime)

    def list_app_instance_group_with_options(
        self,
        request: appstream_center_20210901_models.ListAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListAppInstanceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_center_image_id):
            query['AppCenterImageId'] = request.app_center_image_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_group_name):
            query['AppInstanceGroupName'] = request.app_instance_group_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ListAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_instance_group_with_options_async(
        self,
        request: appstream_center_20210901_models.ListAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListAppInstanceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_center_image_id):
            query['AppCenterImageId'] = request.app_center_image_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_group_name):
            query['AppInstanceGroupName'] = request.app_instance_group_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ListAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_instance_group(
        self,
        request: appstream_center_20210901_models.ListAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.ListAppInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_instance_group_with_options(request, runtime)

    async def list_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.ListAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.ListAppInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_instance_group_with_options_async(request, runtime)

    def list_node_instance_type_with_options(
        self,
        request: appstream_center_20210901_models.ListNodeInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListNodeInstanceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeInstanceType',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ListNodeInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_instance_type_with_options_async(
        self,
        request: appstream_center_20210901_models.ListNodeInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListNodeInstanceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeInstanceType',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ListNodeInstanceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_instance_type(
        self,
        request: appstream_center_20210901_models.ListNodeInstanceTypeRequest,
    ) -> appstream_center_20210901_models.ListNodeInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_node_instance_type_with_options(request, runtime)

    async def list_node_instance_type_async(
        self,
        request: appstream_center_20210901_models.ListNodeInstanceTypeRequest,
    ) -> appstream_center_20210901_models.ListNodeInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_node_instance_type_with_options_async(request, runtime)

    def list_ota_task_with_options(
        self,
        request: appstream_center_20210901_models.ListOtaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListOtaTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.ota_type):
            body['OtaType'] = request.ota_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListOtaTask',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ListOtaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ota_task_with_options_async(
        self,
        request: appstream_center_20210901_models.ListOtaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListOtaTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.ota_type):
            body['OtaType'] = request.ota_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListOtaTask',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ListOtaTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ota_task(
        self,
        request: appstream_center_20210901_models.ListOtaTaskRequest,
    ) -> appstream_center_20210901_models.ListOtaTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ota_task_with_options(request, runtime)

    async def list_ota_task_async(
        self,
        request: appstream_center_20210901_models.ListOtaTaskRequest,
    ) -> appstream_center_20210901_models.ListOtaTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ota_task_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> appstream_center_20210901_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> appstream_center_20210901_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_tenant_config_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListTenantConfigResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListTenantConfig',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ListTenantConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tenant_config_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListTenantConfigResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListTenantConfig',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ListTenantConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tenant_config(self) -> appstream_center_20210901_models.ListTenantConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tenant_config_with_options(runtime)

    async def list_tenant_config_async(self) -> appstream_center_20210901_models.ListTenantConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tenant_config_with_options_async(runtime)

    def log_off_all_sessions_in_app_instance_group_with_options(
        self,
        request: appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LogOffAllSessionsInAppInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def log_off_all_sessions_in_app_instance_group_with_options_async(
        self,
        request: appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LogOffAllSessionsInAppInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def log_off_all_sessions_in_app_instance_group(
        self,
        request: appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.log_off_all_sessions_in_app_instance_group_with_options(request, runtime)

    async def log_off_all_sessions_in_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.log_off_all_sessions_in_app_instance_group_with_options_async(request, runtime)

    def modify_app_instance_group_attribute_with_options(
        self,
        tmp_req: appstream_center_20210901_models.ModifyAppInstanceGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyAppInstanceGroupAttributeResponse:
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.ModifyAppInstanceGroupAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_pool):
            request.node_pool_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_group_name):
            query['AppInstanceGroupName'] = request.app_instance_group_name
        if not UtilClient.is_unset(request.node_pool_shrink):
            query['NodePool'] = request.node_pool_shrink
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppInstanceGroupAttribute',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ModifyAppInstanceGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_instance_group_attribute_with_options_async(
        self,
        tmp_req: appstream_center_20210901_models.ModifyAppInstanceGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyAppInstanceGroupAttributeResponse:
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.ModifyAppInstanceGroupAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_pool):
            request.node_pool_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_group_name):
            query['AppInstanceGroupName'] = request.app_instance_group_name
        if not UtilClient.is_unset(request.node_pool_shrink):
            query['NodePool'] = request.node_pool_shrink
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppInstanceGroupAttribute',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ModifyAppInstanceGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_instance_group_attribute(
        self,
        request: appstream_center_20210901_models.ModifyAppInstanceGroupAttributeRequest,
    ) -> appstream_center_20210901_models.ModifyAppInstanceGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_app_instance_group_attribute_with_options(request, runtime)

    async def modify_app_instance_group_attribute_async(
        self,
        request: appstream_center_20210901_models.ModifyAppInstanceGroupAttributeRequest,
    ) -> appstream_center_20210901_models.ModifyAppInstanceGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_instance_group_attribute_with_options_async(request, runtime)

    def modify_node_pool_attribute_with_options(
        self,
        tmp_req: appstream_center_20210901_models.ModifyNodePoolAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyNodePoolAttributeResponse:
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.ModifyNodePoolAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_pool_strategy):
            request.node_pool_strategy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool_strategy, 'NodePoolStrategy', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.node_capacity):
            body['NodeCapacity'] = request.node_capacity
        if not UtilClient.is_unset(request.node_pool_strategy_shrink):
            body['NodePoolStrategy'] = request.node_pool_strategy_shrink
        if not UtilClient.is_unset(request.pool_id):
            body['PoolId'] = request.pool_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNodePoolAttribute',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ModifyNodePoolAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_pool_attribute_with_options_async(
        self,
        tmp_req: appstream_center_20210901_models.ModifyNodePoolAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyNodePoolAttributeResponse:
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.ModifyNodePoolAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_pool_strategy):
            request.node_pool_strategy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool_strategy, 'NodePoolStrategy', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.node_capacity):
            body['NodeCapacity'] = request.node_capacity
        if not UtilClient.is_unset(request.node_pool_strategy_shrink):
            body['NodePoolStrategy'] = request.node_pool_strategy_shrink
        if not UtilClient.is_unset(request.pool_id):
            body['PoolId'] = request.pool_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNodePoolAttribute',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ModifyNodePoolAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_pool_attribute(
        self,
        request: appstream_center_20210901_models.ModifyNodePoolAttributeRequest,
    ) -> appstream_center_20210901_models.ModifyNodePoolAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_node_pool_attribute_with_options(request, runtime)

    async def modify_node_pool_attribute_async(
        self,
        request: appstream_center_20210901_models.ModifyNodePoolAttributeRequest,
    ) -> appstream_center_20210901_models.ModifyNodePoolAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_node_pool_attribute_with_options_async(request, runtime)

    def modify_tenant_config_with_options(
        self,
        request: appstream_center_20210901_models.ModifyTenantConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyTenantConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_expire_remind):
            body['AppInstanceGroupExpireRemind'] = request.app_instance_group_expire_remind
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantConfig',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ModifyTenantConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tenant_config_with_options_async(
        self,
        request: appstream_center_20210901_models.ModifyTenantConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyTenantConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_expire_remind):
            body['AppInstanceGroupExpireRemind'] = request.app_instance_group_expire_remind
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantConfig',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.ModifyTenantConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tenant_config(
        self,
        request: appstream_center_20210901_models.ModifyTenantConfigRequest,
    ) -> appstream_center_20210901_models.ModifyTenantConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_config_with_options(request, runtime)

    async def modify_tenant_config_async(
        self,
        request: appstream_center_20210901_models.ModifyTenantConfigRequest,
    ) -> appstream_center_20210901_models.ModifyTenantConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_config_with_options_async(request, runtime)

    def page_list_app_instance_group_user_with_options(
        self,
        request: appstream_center_20210901_models.PageListAppInstanceGroupUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.PageListAppInstanceGroupUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageListAppInstanceGroupUser',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.PageListAppInstanceGroupUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_list_app_instance_group_user_with_options_async(
        self,
        request: appstream_center_20210901_models.PageListAppInstanceGroupUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.PageListAppInstanceGroupUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageListAppInstanceGroupUser',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.PageListAppInstanceGroupUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_list_app_instance_group_user(
        self,
        request: appstream_center_20210901_models.PageListAppInstanceGroupUserRequest,
    ) -> appstream_center_20210901_models.PageListAppInstanceGroupUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.page_list_app_instance_group_user_with_options(request, runtime)

    async def page_list_app_instance_group_user_async(
        self,
        request: appstream_center_20210901_models.PageListAppInstanceGroupUserRequest,
    ) -> appstream_center_20210901_models.PageListAppInstanceGroupUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.page_list_app_instance_group_user_with_options_async(request, runtime)

    def renew_app_instance_group_with_options(
        self,
        request: appstream_center_20210901_models.RenewAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.RenewAppInstanceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewAppInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.RenewAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_app_instance_group_with_options_async(
        self,
        request: appstream_center_20210901_models.RenewAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.RenewAppInstanceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewAppInstanceGroup',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.RenewAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_app_instance_group(
        self,
        request: appstream_center_20210901_models.RenewAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.RenewAppInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_app_instance_group_with_options(request, runtime)

    async def renew_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.RenewAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.RenewAppInstanceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_app_instance_group_with_options_async(request, runtime)

    def update_app_instance_group_image_with_options(
        self,
        request: appstream_center_20210901_models.UpdateAppInstanceGroupImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.UpdateAppInstanceGroupImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_center_image_id):
            query['AppCenterImageId'] = request.app_center_image_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.update_mode):
            query['UpdateMode'] = request.update_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppInstanceGroupImage',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.UpdateAppInstanceGroupImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_instance_group_image_with_options_async(
        self,
        request: appstream_center_20210901_models.UpdateAppInstanceGroupImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.UpdateAppInstanceGroupImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_center_image_id):
            query['AppCenterImageId'] = request.app_center_image_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.update_mode):
            query['UpdateMode'] = request.update_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppInstanceGroupImage',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210901_models.UpdateAppInstanceGroupImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_instance_group_image(
        self,
        request: appstream_center_20210901_models.UpdateAppInstanceGroupImageRequest,
    ) -> appstream_center_20210901_models.UpdateAppInstanceGroupImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_instance_group_image_with_options(request, runtime)

    async def update_app_instance_group_image_async(
        self,
        request: appstream_center_20210901_models.UpdateAppInstanceGroupImageRequest,
    ) -> appstream_center_20210901_models.UpdateAppInstanceGroupImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_instance_group_image_with_options_async(request, runtime)
