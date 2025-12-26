# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_appstream_center20210901 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def approve_ota_task_with_options(
        self,
        request: main_models.ApproveOtaTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveOtaTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.ota_type):
            body['OtaType'] = request.ota_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApproveOtaTask',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveOtaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_ota_task_with_options_async(
        self,
        request: main_models.ApproveOtaTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveOtaTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.ota_type):
            body['OtaType'] = request.ota_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApproveOtaTask',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveOtaTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_ota_task(
        self,
        request: main_models.ApproveOtaTaskRequest,
    ) -> main_models.ApproveOtaTaskResponse:
        runtime = RuntimeOptions()
        return self.approve_ota_task_with_options(request, runtime)

    async def approve_ota_task_async(
        self,
        request: main_models.ApproveOtaTaskRequest,
    ) -> main_models.ApproveOtaTaskResponse:
        runtime = RuntimeOptions()
        return await self.approve_ota_task_with_options_async(request, runtime)

    def authorize_instance_group_with_options(
        self,
        tmp_req: main_models.AuthorizeInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeInstanceGroupResponse:
        tmp_req.validate()
        request = main_models.AuthorizeInstanceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_meta):
            request.user_meta_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_meta, 'UserMeta', 'json')
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        body_flat = {}
        if not DaraCore.is_null(request.authorize_user_group_ids):
            body_flat['AuthorizeUserGroupIds'] = request.authorize_user_group_ids
        if not DaraCore.is_null(request.authorize_user_ids):
            body_flat['AuthorizeUserIds'] = request.authorize_user_ids
        if not DaraCore.is_null(request.avatar_id):
            body['AvatarId'] = request.avatar_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.un_authorize_user_group_ids):
            body_flat['UnAuthorizeUserGroupIds'] = request.un_authorize_user_group_ids
        if not DaraCore.is_null(request.un_authorize_user_ids):
            body_flat['UnAuthorizeUserIds'] = request.un_authorize_user_ids
        if not DaraCore.is_null(request.user_meta_shrink):
            body['UserMeta'] = request.user_meta_shrink
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_instance_group_with_options_async(
        self,
        tmp_req: main_models.AuthorizeInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeInstanceGroupResponse:
        tmp_req.validate()
        request = main_models.AuthorizeInstanceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_meta):
            request.user_meta_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_meta, 'UserMeta', 'json')
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        body_flat = {}
        if not DaraCore.is_null(request.authorize_user_group_ids):
            body_flat['AuthorizeUserGroupIds'] = request.authorize_user_group_ids
        if not DaraCore.is_null(request.authorize_user_ids):
            body_flat['AuthorizeUserIds'] = request.authorize_user_ids
        if not DaraCore.is_null(request.avatar_id):
            body['AvatarId'] = request.avatar_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.un_authorize_user_group_ids):
            body_flat['UnAuthorizeUserGroupIds'] = request.un_authorize_user_group_ids
        if not DaraCore.is_null(request.un_authorize_user_ids):
            body_flat['UnAuthorizeUserIds'] = request.un_authorize_user_ids
        if not DaraCore.is_null(request.user_meta_shrink):
            body['UserMeta'] = request.user_meta_shrink
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_instance_group(
        self,
        request: main_models.AuthorizeInstanceGroupRequest,
    ) -> main_models.AuthorizeInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.authorize_instance_group_with_options(request, runtime)

    async def authorize_instance_group_async(
        self,
        request: main_models.AuthorizeInstanceGroupRequest,
    ) -> main_models.AuthorizeInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.authorize_instance_group_with_options_async(request, runtime)

    def create_app_instance_group_with_options(
        self,
        tmp_req: main_models.CreateAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceGroupResponse:
        tmp_req.validate()
        request = main_models.CreateAppInstanceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network):
            request.network_shrink = Utils.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not DaraCore.is_null(tmp_req.node_pool):
            request.node_pool_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        if not DaraCore.is_null(tmp_req.runtime_policy):
            request.runtime_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_policy, 'RuntimePolicy', 'json')
        if not DaraCore.is_null(tmp_req.security_policy):
            request.security_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not DaraCore.is_null(tmp_req.storage_policy):
            request.storage_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.storage_policy, 'StoragePolicy', 'json')
        if not DaraCore.is_null(tmp_req.user_define_policy):
            request.user_define_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_define_policy, 'UserDefinePolicy', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        if not DaraCore.is_null(tmp_req.video_policy):
            request.video_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_policy, 'VideoPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.user_define_policy_shrink):
            query['UserDefinePolicy'] = request.user_define_policy_shrink
        body = {}
        if not DaraCore.is_null(request.app_center_image_id):
            body['AppCenterImageId'] = request.app_center_image_id
        if not DaraCore.is_null(request.app_instance_group_name):
            body['AppInstanceGroupName'] = request.app_instance_group_name
        if not DaraCore.is_null(request.app_package_type):
            body['AppPackageType'] = request.app_package_type
        if not DaraCore.is_null(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not DaraCore.is_null(request.auth_mode):
            body['AuthMode'] = request.auth_mode
        if not DaraCore.is_null(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_resource_mode):
            body['ChargeResourceMode'] = request.charge_resource_mode
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.network_shrink):
            body['Network'] = request.network_shrink
        if not DaraCore.is_null(request.node_pool_shrink):
            body['NodePool'] = request.node_pool_shrink
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.pre_open_app_id):
            body['PreOpenAppId'] = request.pre_open_app_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.promotion_id):
            body['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.runtime_policy_shrink):
            body['RuntimePolicy'] = request.runtime_policy_shrink
        if not DaraCore.is_null(request.security_policy_shrink):
            body['SecurityPolicy'] = request.security_policy_shrink
        if not DaraCore.is_null(request.session_timeout):
            body['SessionTimeout'] = request.session_timeout
        if not DaraCore.is_null(request.storage_policy_shrink):
            body['StoragePolicy'] = request.storage_policy_shrink
        if not DaraCore.is_null(request.sub_pay_type):
            body['SubPayType'] = request.sub_pay_type
        if not DaraCore.is_null(request.user_group_ids):
            body['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        if not DaraCore.is_null(request.video_policy_shrink):
            body['VideoPolicy'] = request.video_policy_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_instance_group_with_options_async(
        self,
        tmp_req: main_models.CreateAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceGroupResponse:
        tmp_req.validate()
        request = main_models.CreateAppInstanceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network):
            request.network_shrink = Utils.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not DaraCore.is_null(tmp_req.node_pool):
            request.node_pool_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        if not DaraCore.is_null(tmp_req.runtime_policy):
            request.runtime_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.runtime_policy, 'RuntimePolicy', 'json')
        if not DaraCore.is_null(tmp_req.security_policy):
            request.security_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not DaraCore.is_null(tmp_req.storage_policy):
            request.storage_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.storage_policy, 'StoragePolicy', 'json')
        if not DaraCore.is_null(tmp_req.user_define_policy):
            request.user_define_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_define_policy, 'UserDefinePolicy', 'json')
        if not DaraCore.is_null(tmp_req.user_info):
            request.user_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        if not DaraCore.is_null(tmp_req.video_policy):
            request.video_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_policy, 'VideoPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.user_define_policy_shrink):
            query['UserDefinePolicy'] = request.user_define_policy_shrink
        body = {}
        if not DaraCore.is_null(request.app_center_image_id):
            body['AppCenterImageId'] = request.app_center_image_id
        if not DaraCore.is_null(request.app_instance_group_name):
            body['AppInstanceGroupName'] = request.app_instance_group_name
        if not DaraCore.is_null(request.app_package_type):
            body['AppPackageType'] = request.app_package_type
        if not DaraCore.is_null(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not DaraCore.is_null(request.auth_mode):
            body['AuthMode'] = request.auth_mode
        if not DaraCore.is_null(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_resource_mode):
            body['ChargeResourceMode'] = request.charge_resource_mode
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.network_shrink):
            body['Network'] = request.network_shrink
        if not DaraCore.is_null(request.node_pool_shrink):
            body['NodePool'] = request.node_pool_shrink
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.pre_open_app_id):
            body['PreOpenAppId'] = request.pre_open_app_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.promotion_id):
            body['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.runtime_policy_shrink):
            body['RuntimePolicy'] = request.runtime_policy_shrink
        if not DaraCore.is_null(request.security_policy_shrink):
            body['SecurityPolicy'] = request.security_policy_shrink
        if not DaraCore.is_null(request.session_timeout):
            body['SessionTimeout'] = request.session_timeout
        if not DaraCore.is_null(request.storage_policy_shrink):
            body['StoragePolicy'] = request.storage_policy_shrink
        if not DaraCore.is_null(request.sub_pay_type):
            body['SubPayType'] = request.sub_pay_type
        if not DaraCore.is_null(request.user_group_ids):
            body['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        if not DaraCore.is_null(request.video_policy_shrink):
            body['VideoPolicy'] = request.video_policy_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_instance_group(
        self,
        request: main_models.CreateAppInstanceGroupRequest,
    ) -> main_models.CreateAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.create_app_instance_group_with_options(request, runtime)

    async def create_app_instance_group_async(
        self,
        request: main_models.CreateAppInstanceGroupRequest,
    ) -> main_models.CreateAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_app_instance_group_with_options_async(request, runtime)

    def create_image_by_instance_with_options(
        self,
        request: main_models.CreateImageByInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageByInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_clean_userdata):
            body['AutoCleanUserdata'] = request.auto_clean_userdata
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.disk_type):
            body['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.image_name):
            body['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.sub_instance_id):
            body['SubInstanceId'] = request.sub_instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageByInstance',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageByInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_by_instance_with_options_async(
        self,
        request: main_models.CreateImageByInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageByInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_clean_userdata):
            body['AutoCleanUserdata'] = request.auto_clean_userdata
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.disk_type):
            body['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.image_name):
            body['ImageName'] = request.image_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.sub_instance_id):
            body['SubInstanceId'] = request.sub_instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageByInstance',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageByInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_by_instance(
        self,
        request: main_models.CreateImageByInstanceRequest,
    ) -> main_models.CreateImageByInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_image_by_instance_with_options(request, runtime)

    async def create_image_by_instance_async(
        self,
        request: main_models.CreateImageByInstanceRequest,
    ) -> main_models.CreateImageByInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_image_by_instance_with_options_async(request, runtime)

    def create_image_from_app_instance_group_with_options(
        self,
        request: main_models.CreateImageFromAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageFromAppInstanceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_center_image_name):
            body['AppCenterImageName'] = request.app_center_image_name
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageFromAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageFromAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_from_app_instance_group_with_options_async(
        self,
        request: main_models.CreateImageFromAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageFromAppInstanceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_center_image_name):
            body['AppCenterImageName'] = request.app_center_image_name
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageFromAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageFromAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_from_app_instance_group(
        self,
        request: main_models.CreateImageFromAppInstanceGroupRequest,
    ) -> main_models.CreateImageFromAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.create_image_from_app_instance_group_with_options(request, runtime)

    async def create_image_from_app_instance_group_async(
        self,
        request: main_models.CreateImageFromAppInstanceGroupRequest,
    ) -> main_models.CreateImageFromAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_image_from_app_instance_group_with_options_async(request, runtime)

    def create_wuying_server_with_options(
        self,
        request: main_models.CreateWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWuyingServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amount):
            body['Amount'] = request.amount
        if not DaraCore.is_null(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        body_flat = {}
        if not DaraCore.is_null(request.data_disk):
            body_flat['DataDisk'] = request.data_disk
        if not DaraCore.is_null(request.host_name):
            body['HostName'] = request.host_name
        if not DaraCore.is_null(request.idempotence_token):
            body['IdempotenceToken'] = request.idempotence_token
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.max_price):
            body['MaxPrice'] = request.max_price
        if not DaraCore.is_null(request.network_strategy_type):
            body['NetworkStrategyType'] = request.network_strategy_type
        if not DaraCore.is_null(request.office_site_id):
            body['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.promotion_id):
            body['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.saving_plan_id):
            body['SavingPlanId'] = request.saving_plan_id
        if not DaraCore.is_null(request.server_instance_type):
            body['ServerInstanceType'] = request.server_instance_type
        if not DaraCore.is_null(request.server_port_range):
            body['ServerPortRange'] = request.server_port_range
        if not DaraCore.is_null(request.sub_pay_type):
            body['SubPayType'] = request.sub_pay_type
        if not DaraCore.is_null(request.system_disk_category):
            body['SystemDiskCategory'] = request.system_disk_category
        if not DaraCore.is_null(request.system_disk_performance_level):
            body['SystemDiskPerformanceLevel'] = request.system_disk_performance_level
        if not DaraCore.is_null(request.system_disk_size):
            body['SystemDiskSize'] = request.system_disk_size
        if not DaraCore.is_null(request.v_switch_ids):
            body['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.virtual_node_pool_id):
            body['VirtualNodePoolId'] = request.virtual_node_pool_id
        if not DaraCore.is_null(request.wuying_server_name):
            body['WuyingServerName'] = request.wuying_server_name
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWuyingServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wuying_server_with_options_async(
        self,
        request: main_models.CreateWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWuyingServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amount):
            body['Amount'] = request.amount
        if not DaraCore.is_null(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        body_flat = {}
        if not DaraCore.is_null(request.data_disk):
            body_flat['DataDisk'] = request.data_disk
        if not DaraCore.is_null(request.host_name):
            body['HostName'] = request.host_name
        if not DaraCore.is_null(request.idempotence_token):
            body['IdempotenceToken'] = request.idempotence_token
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.max_price):
            body['MaxPrice'] = request.max_price
        if not DaraCore.is_null(request.network_strategy_type):
            body['NetworkStrategyType'] = request.network_strategy_type
        if not DaraCore.is_null(request.office_site_id):
            body['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.promotion_id):
            body['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.saving_plan_id):
            body['SavingPlanId'] = request.saving_plan_id
        if not DaraCore.is_null(request.server_instance_type):
            body['ServerInstanceType'] = request.server_instance_type
        if not DaraCore.is_null(request.server_port_range):
            body['ServerPortRange'] = request.server_port_range
        if not DaraCore.is_null(request.sub_pay_type):
            body['SubPayType'] = request.sub_pay_type
        if not DaraCore.is_null(request.system_disk_category):
            body['SystemDiskCategory'] = request.system_disk_category
        if not DaraCore.is_null(request.system_disk_performance_level):
            body['SystemDiskPerformanceLevel'] = request.system_disk_performance_level
        if not DaraCore.is_null(request.system_disk_size):
            body['SystemDiskSize'] = request.system_disk_size
        if not DaraCore.is_null(request.v_switch_ids):
            body['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.virtual_node_pool_id):
            body['VirtualNodePoolId'] = request.virtual_node_pool_id
        if not DaraCore.is_null(request.wuying_server_name):
            body['WuyingServerName'] = request.wuying_server_name
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWuyingServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wuying_server(
        self,
        request: main_models.CreateWuyingServerRequest,
    ) -> main_models.CreateWuyingServerResponse:
        runtime = RuntimeOptions()
        return self.create_wuying_server_with_options(request, runtime)

    async def create_wuying_server_async(
        self,
        request: main_models.CreateWuyingServerRequest,
    ) -> main_models.CreateWuyingServerResponse:
        runtime = RuntimeOptions()
        return await self.create_wuying_server_with_options_async(request, runtime)

    def delete_app_instance_group_with_options(
        self,
        request: main_models.DeleteAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppInstanceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_instance_group_with_options_async(
        self,
        request: main_models.DeleteAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppInstanceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_instance_group(
        self,
        request: main_models.DeleteAppInstanceGroupRequest,
    ) -> main_models.DeleteAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_app_instance_group_with_options(request, runtime)

    async def delete_app_instance_group_async(
        self,
        request: main_models.DeleteAppInstanceGroupRequest,
    ) -> main_models.DeleteAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_instance_group_with_options_async(request, runtime)

    def delete_app_instances_with_options(
        self,
        request: main_models.DeleteAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_ids):
            body['AppInstanceIds'] = request.app_instance_ids
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppInstances',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_instances_with_options_async(
        self,
        request: main_models.DeleteAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_ids):
            body['AppInstanceIds'] = request.app_instance_ids
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppInstances',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_instances(
        self,
        request: main_models.DeleteAppInstancesRequest,
    ) -> main_models.DeleteAppInstancesResponse:
        runtime = RuntimeOptions()
        return self.delete_app_instances_with_options(request, runtime)

    async def delete_app_instances_async(
        self,
        request: main_models.DeleteAppInstancesRequest,
    ) -> main_models.DeleteAppInstancesResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_instances_with_options_async(request, runtime)

    def delete_image_with_options(
        self,
        request: main_models.DeleteImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImage',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: main_models.DeleteImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImage',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image(
        self,
        request: main_models.DeleteImageRequest,
    ) -> main_models.DeleteImageResponse:
        runtime = RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: main_models.DeleteImageRequest,
    ) -> main_models.DeleteImageResponse:
        runtime = RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def delete_wuying_server_with_options(
        self,
        request: main_models.DeleteWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWuyingServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWuyingServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_wuying_server_with_options_async(
        self,
        request: main_models.DeleteWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWuyingServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWuyingServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_wuying_server(
        self,
        request: main_models.DeleteWuyingServerRequest,
    ) -> main_models.DeleteWuyingServerResponse:
        runtime = RuntimeOptions()
        return self.delete_wuying_server_with_options(request, runtime)

    async def delete_wuying_server_async(
        self,
        request: main_models.DeleteWuyingServerRequest,
    ) -> main_models.DeleteWuyingServerResponse:
        runtime = RuntimeOptions()
        return await self.delete_wuying_server_with_options_async(request, runtime)

    def describe_wuying_server_eip_info_with_options(
        self,
        request: main_models.DescribeWuyingServerEipInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWuyingServerEipInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.isp):
            body['Isp'] = request.isp
        if not DaraCore.is_null(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWuyingServerEipInfo',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWuyingServerEipInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_wuying_server_eip_info_with_options_async(
        self,
        request: main_models.DescribeWuyingServerEipInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWuyingServerEipInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.isp):
            body['Isp'] = request.isp
        if not DaraCore.is_null(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWuyingServerEipInfo',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWuyingServerEipInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_wuying_server_eip_info(
        self,
        request: main_models.DescribeWuyingServerEipInfoRequest,
    ) -> main_models.DescribeWuyingServerEipInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_wuying_server_eip_info_with_options(request, runtime)

    async def describe_wuying_server_eip_info_async(
        self,
        request: main_models.DescribeWuyingServerEipInfoRequest,
    ) -> main_models.DescribeWuyingServerEipInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_wuying_server_eip_info_with_options_async(request, runtime)

    def get_app_instance_group_with_options(
        self,
        request: main_models.GetAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_instance_group_with_options_async(
        self,
        request: main_models.GetAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_instance_group(
        self,
        request: main_models.GetAppInstanceGroupRequest,
    ) -> main_models.GetAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.get_app_instance_group_with_options(request, runtime)

    async def get_app_instance_group_async(
        self,
        request: main_models.GetAppInstanceGroupRequest,
    ) -> main_models.GetAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_app_instance_group_with_options_async(request, runtime)

    def get_connection_ticket_with_options(
        self,
        request: main_models.GetConnectionTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectionTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_type):
            body['AccessType'] = request.access_type
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_instance_group_id_list):
            body['AppInstanceGroupIdList'] = request.app_instance_group_id_list
        if not DaraCore.is_null(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        if not DaraCore.is_null(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not DaraCore.is_null(request.app_start_param):
            body['AppStartParam'] = request.app_start_param
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.environment_config):
            body['EnvironmentConfig'] = request.environment_config
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetConnectionTicket',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectionTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_connection_ticket_with_options_async(
        self,
        request: main_models.GetConnectionTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectionTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_type):
            body['AccessType'] = request.access_type
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_instance_group_id_list):
            body['AppInstanceGroupIdList'] = request.app_instance_group_id_list
        if not DaraCore.is_null(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        if not DaraCore.is_null(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not DaraCore.is_null(request.app_start_param):
            body['AppStartParam'] = request.app_start_param
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.environment_config):
            body['EnvironmentConfig'] = request.environment_config
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetConnectionTicket',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectionTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_connection_ticket(
        self,
        request: main_models.GetConnectionTicketRequest,
    ) -> main_models.GetConnectionTicketResponse:
        runtime = RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    async def get_connection_ticket_async(
        self,
        request: main_models.GetConnectionTicketRequest,
    ) -> main_models.GetConnectionTicketResponse:
        runtime = RuntimeOptions()
        return await self.get_connection_ticket_with_options_async(request, runtime)

    def get_debug_app_instance_with_options(
        self,
        request: main_models.GetDebugAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDebugAppInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDebugAppInstance',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDebugAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_debug_app_instance_with_options_async(
        self,
        request: main_models.GetDebugAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDebugAppInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDebugAppInstance',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDebugAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_debug_app_instance(
        self,
        request: main_models.GetDebugAppInstanceRequest,
    ) -> main_models.GetDebugAppInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_debug_app_instance_with_options(request, runtime)

    async def get_debug_app_instance_async(
        self,
        request: main_models.GetDebugAppInstanceRequest,
    ) -> main_models.GetDebugAppInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_debug_app_instance_with_options_async(request, runtime)

    def get_ota_task_by_task_id_with_options(
        self,
        request: main_models.GetOtaTaskByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOtaTaskByTaskIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOtaTaskByTaskId',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOtaTaskByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ota_task_by_task_id_with_options_async(
        self,
        request: main_models.GetOtaTaskByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOtaTaskByTaskIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOtaTaskByTaskId',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOtaTaskByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ota_task_by_task_id(
        self,
        request: main_models.GetOtaTaskByTaskIdRequest,
    ) -> main_models.GetOtaTaskByTaskIdResponse:
        runtime = RuntimeOptions()
        return self.get_ota_task_by_task_id_with_options(request, runtime)

    async def get_ota_task_by_task_id_async(
        self,
        request: main_models.GetOtaTaskByTaskIdRequest,
    ) -> main_models.GetOtaTaskByTaskIdResponse:
        runtime = RuntimeOptions()
        return await self.get_ota_task_by_task_id_with_options_async(request, runtime)

    def get_resource_price_with_options(
        self,
        request: main_models.GetResourcePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourcePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.app_instance_type):
            query['AppInstanceType'] = request.app_instance_type
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourcePrice',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourcePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_price_with_options_async(
        self,
        request: main_models.GetResourcePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourcePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.app_instance_type):
            query['AppInstanceType'] = request.app_instance_type
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourcePrice',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourcePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_price(
        self,
        request: main_models.GetResourcePriceRequest,
    ) -> main_models.GetResourcePriceResponse:
        runtime = RuntimeOptions()
        return self.get_resource_price_with_options(request, runtime)

    async def get_resource_price_async(
        self,
        request: main_models.GetResourcePriceRequest,
    ) -> main_models.GetResourcePriceResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_price_with_options_async(request, runtime)

    def get_resource_renew_price_with_options(
        self,
        request: main_models.GetResourceRenewPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceRenewPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceRenewPrice',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceRenewPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_renew_price_with_options_async(
        self,
        request: main_models.GetResourceRenewPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceRenewPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceRenewPrice',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceRenewPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_renew_price(
        self,
        request: main_models.GetResourceRenewPriceRequest,
    ) -> main_models.GetResourceRenewPriceResponse:
        runtime = RuntimeOptions()
        return self.get_resource_renew_price_with_options(request, runtime)

    async def get_resource_renew_price_async(
        self,
        request: main_models.GetResourceRenewPriceRequest,
    ) -> main_models.GetResourceRenewPriceResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_renew_price_with_options_async(request, runtime)

    def list_app_instance_group_with_options(
        self,
        request: main_models.ListAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_center_image_id):
            query['AppCenterImageId'] = request.app_center_image_id
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_group_name):
            query['AppInstanceGroupName'] = request.app_instance_group_name
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.excluded_user_group_ids):
            body['ExcludedUserGroupIds'] = request.excluded_user_group_ids
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.user_group_ids):
            body['UserGroupIds'] = request.user_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_instance_group_with_options_async(
        self,
        request: main_models.ListAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstanceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_center_image_id):
            query['AppCenterImageId'] = request.app_center_image_id
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_group_name):
            query['AppInstanceGroupName'] = request.app_instance_group_name
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not DaraCore.is_null(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.excluded_user_group_ids):
            body['ExcludedUserGroupIds'] = request.excluded_user_group_ids
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.user_group_ids):
            body['UserGroupIds'] = request.user_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_instance_group(
        self,
        request: main_models.ListAppInstanceGroupRequest,
    ) -> main_models.ListAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.list_app_instance_group_with_options(request, runtime)

    async def list_app_instance_group_async(
        self,
        request: main_models.ListAppInstanceGroupRequest,
    ) -> main_models.ListAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_app_instance_group_with_options_async(request, runtime)

    def list_app_instances_with_options(
        self,
        request: main_models.ListAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.include_deleted):
            query['IncludeDeleted'] = request.include_deleted
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        body = {}
        if not DaraCore.is_null(request.app_instance_id_list):
            body['AppInstanceIdList'] = request.app_instance_id_list
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstances',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_instances_with_options_async(
        self,
        request: main_models.ListAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.include_deleted):
            query['IncludeDeleted'] = request.include_deleted
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        body = {}
        if not DaraCore.is_null(request.app_instance_id_list):
            body['AppInstanceIdList'] = request.app_instance_id_list
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstances',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_instances(
        self,
        request: main_models.ListAppInstancesRequest,
    ) -> main_models.ListAppInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_app_instances_with_options(request, runtime)

    async def list_app_instances_async(
        self,
        request: main_models.ListAppInstancesRequest,
    ) -> main_models.ListAppInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_app_instances_with_options_async(request, runtime)

    def list_authorized_user_groups_with_options(
        self,
        request: main_models.ListAuthorizedUserGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedUserGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            body['GroupName'] = request.group_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedUserGroups',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorized_user_groups_with_options_async(
        self,
        request: main_models.ListAuthorizedUserGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedUserGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            body['GroupName'] = request.group_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedUserGroups',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorized_user_groups(
        self,
        request: main_models.ListAuthorizedUserGroupsRequest,
    ) -> main_models.ListAuthorizedUserGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_authorized_user_groups_with_options(request, runtime)

    async def list_authorized_user_groups_async(
        self,
        request: main_models.ListAuthorizedUserGroupsRequest,
    ) -> main_models.ListAuthorizedUserGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_authorized_user_groups_with_options_async(request, runtime)

    def list_bind_info_with_options(
        self,
        request: main_models.ListBindInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id_list):
            body['AppIdList'] = request.app_id_list
        if not DaraCore.is_null(request.app_instance_group_id_list):
            body['AppInstanceGroupIdList'] = request.app_instance_group_id_list
        if not DaraCore.is_null(request.app_instance_id_list):
            body['AppInstanceIdList'] = request.app_instance_id_list
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id_list):
            body['UserIdList'] = request.user_id_list
        if not DaraCore.is_null(request.wy_id_list):
            body['WyIdList'] = request.wy_id_list
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBindInfo',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bind_info_with_options_async(
        self,
        request: main_models.ListBindInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id_list):
            body['AppIdList'] = request.app_id_list
        if not DaraCore.is_null(request.app_instance_group_id_list):
            body['AppInstanceGroupIdList'] = request.app_instance_group_id_list
        if not DaraCore.is_null(request.app_instance_id_list):
            body['AppInstanceIdList'] = request.app_instance_id_list
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id_list):
            body['UserIdList'] = request.user_id_list
        if not DaraCore.is_null(request.wy_id_list):
            body['WyIdList'] = request.wy_id_list
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBindInfo',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bind_info(
        self,
        request: main_models.ListBindInfoRequest,
    ) -> main_models.ListBindInfoResponse:
        runtime = RuntimeOptions()
        return self.list_bind_info_with_options(request, runtime)

    async def list_bind_info_async(
        self,
        request: main_models.ListBindInfoRequest,
    ) -> main_models.ListBindInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_bind_info_with_options_async(request, runtime)

    def list_image_with_options(
        self,
        request: main_models.ListImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_list):
            query['TagList'] = request.tag_list
        body = {}
        if not DaraCore.is_null(request.biz_region_id_list):
            body['BizRegionIdList'] = request.biz_region_id_list
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.biz_type_list):
            body['BizTypeList'] = request.biz_type_list
        if not DaraCore.is_null(request.feature_list):
            body['FeatureList'] = request.feature_list
        if not DaraCore.is_null(request.fota_version):
            body['FotaVersion'] = request.fota_version
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_name):
            body['ImageName'] = request.image_name
        if not DaraCore.is_null(request.image_type):
            body['ImageType'] = request.image_type
        if not DaraCore.is_null(request.language_type):
            body['LanguageType'] = request.language_type
        if not DaraCore.is_null(request.os_type):
            body['OsType'] = request.os_type
        if not DaraCore.is_null(request.package_type):
            body['PackageType'] = request.package_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.platform_name):
            body['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.platform_name_list):
            body['PlatformNameList'] = request.platform_name_list
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.product_type_list):
            body['ProductTypeList'] = request.product_type_list
        if not DaraCore.is_null(request.protocol_type):
            body['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.resource_instance_type):
            body['ResourceInstanceType'] = request.resource_instance_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListImage',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_image_with_options_async(
        self,
        request: main_models.ListImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_list):
            query['TagList'] = request.tag_list
        body = {}
        if not DaraCore.is_null(request.biz_region_id_list):
            body['BizRegionIdList'] = request.biz_region_id_list
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.biz_type_list):
            body['BizTypeList'] = request.biz_type_list
        if not DaraCore.is_null(request.feature_list):
            body['FeatureList'] = request.feature_list
        if not DaraCore.is_null(request.fota_version):
            body['FotaVersion'] = request.fota_version
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.image_name):
            body['ImageName'] = request.image_name
        if not DaraCore.is_null(request.image_type):
            body['ImageType'] = request.image_type
        if not DaraCore.is_null(request.language_type):
            body['LanguageType'] = request.language_type
        if not DaraCore.is_null(request.os_type):
            body['OsType'] = request.os_type
        if not DaraCore.is_null(request.package_type):
            body['PackageType'] = request.package_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.platform_name):
            body['PlatformName'] = request.platform_name
        if not DaraCore.is_null(request.platform_name_list):
            body['PlatformNameList'] = request.platform_name_list
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.product_type_list):
            body['ProductTypeList'] = request.product_type_list
        if not DaraCore.is_null(request.protocol_type):
            body['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.resource_instance_type):
            body['ResourceInstanceType'] = request.resource_instance_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListImage',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_image(
        self,
        request: main_models.ListImageRequest,
    ) -> main_models.ListImageResponse:
        runtime = RuntimeOptions()
        return self.list_image_with_options(request, runtime)

    async def list_image_async(
        self,
        request: main_models.ListImageRequest,
    ) -> main_models.ListImageResponse:
        runtime = RuntimeOptions()
        return await self.list_image_with_options_async(request, runtime)

    def list_node_instance_type_with_options(
        self,
        request: main_models.ListNodeInstanceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodeInstanceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.gpu):
            query['Gpu'] = request.gpu
        if not DaraCore.is_null(request.gpu_memory):
            query['GpuMemory'] = request.gpu_memory
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not DaraCore.is_null(request.node_instance_type_family):
            query['NodeInstanceTypeFamily'] = request.node_instance_type_family
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeInstanceType',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodeInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_instance_type_with_options_async(
        self,
        request: main_models.ListNodeInstanceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodeInstanceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.gpu):
            query['Gpu'] = request.gpu
        if not DaraCore.is_null(request.gpu_memory):
            query['GpuMemory'] = request.gpu_memory
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not DaraCore.is_null(request.node_instance_type_family):
            query['NodeInstanceTypeFamily'] = request.node_instance_type_family
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeInstanceType',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodeInstanceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_instance_type(
        self,
        request: main_models.ListNodeInstanceTypeRequest,
    ) -> main_models.ListNodeInstanceTypeResponse:
        runtime = RuntimeOptions()
        return self.list_node_instance_type_with_options(request, runtime)

    async def list_node_instance_type_async(
        self,
        request: main_models.ListNodeInstanceTypeRequest,
    ) -> main_models.ListNodeInstanceTypeResponse:
        runtime = RuntimeOptions()
        return await self.list_node_instance_type_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: main_models.ListNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: main_models.ListNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_ota_task_with_options(
        self,
        request: main_models.ListOtaTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOtaTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.ota_type):
            body['OtaType'] = request.ota_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListOtaTask',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOtaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ota_task_with_options_async(
        self,
        request: main_models.ListOtaTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOtaTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.ota_type):
            body['OtaType'] = request.ota_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListOtaTask',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOtaTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ota_task(
        self,
        request: main_models.ListOtaTaskRequest,
    ) -> main_models.ListOtaTaskResponse:
        runtime = RuntimeOptions()
        return self.list_ota_task_with_options(request, runtime)

    async def list_ota_task_async(
        self,
        request: main_models.ListOtaTaskRequest,
    ) -> main_models.ListOtaTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_ota_task_with_options_async(request, runtime)

    def list_persistent_app_instances_with_options(
        self,
        request: main_models.ListPersistentAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPersistentAppInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_persistent_ids):
            query['AppInstancePersistentIds'] = request.app_instance_persistent_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPersistentAppInstances',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPersistentAppInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_persistent_app_instances_with_options_async(
        self,
        request: main_models.ListPersistentAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPersistentAppInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_persistent_ids):
            query['AppInstancePersistentIds'] = request.app_instance_persistent_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPersistentAppInstances',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPersistentAppInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_persistent_app_instances(
        self,
        request: main_models.ListPersistentAppInstancesRequest,
    ) -> main_models.ListPersistentAppInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_persistent_app_instances_with_options(request, runtime)

    async def list_persistent_app_instances_async(
        self,
        request: main_models.ListPersistentAppInstancesRequest,
    ) -> main_models.ListPersistentAppInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_persistent_app_instances_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: main_models.ListRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_source):
            query['BizSource'] = request.biz_source
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        request: main_models.ListRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_source):
            query['BizSource'] = request.biz_source
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(
        self,
        request: main_models.ListRegionsRequest,
    ) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: main_models.ListRegionsRequest,
    ) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_tag_cloud_resources_with_options(
        self,
        request: main_models.ListTagCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagCloudResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scope):
            body['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagCloudResources',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_cloud_resources_with_options_async(
        self,
        request: main_models.ListTagCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagCloudResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scope):
            body['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagCloudResources',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_cloud_resources(
        self,
        request: main_models.ListTagCloudResourcesRequest,
    ) -> main_models.ListTagCloudResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_cloud_resources_with_options(request, runtime)

    async def list_tag_cloud_resources_async(
        self,
        request: main_models.ListTagCloudResourcesRequest,
    ) -> main_models.ListTagCloudResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_cloud_resources_with_options_async(request, runtime)

    def list_tenant_config_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListTenantConfigResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListTenantConfig',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTenantConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tenant_config_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListTenantConfigResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListTenantConfig',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTenantConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tenant_config(self) -> main_models.ListTenantConfigResponse:
        runtime = RuntimeOptions()
        return self.list_tenant_config_with_options(runtime)

    async def list_tenant_config_async(self) -> main_models.ListTenantConfigResponse:
        runtime = RuntimeOptions()
        return await self.list_tenant_config_with_options_async(runtime)

    def list_wuying_server_with_options(
        self,
        request: main_models.ListWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWuyingServerResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.add_virtual_node_pool_status_list):
            body_flat['AddVirtualNodePoolStatusList'] = request.add_virtual_node_pool_status_list
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.office_site_id):
            body['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.server_instance_type):
            body['ServerInstanceType'] = request.server_instance_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.virtual_node_pool_id):
            body['VirtualNodePoolId'] = request.virtual_node_pool_id
        if not DaraCore.is_null(request.wuying_server_id_list):
            body_flat['WuyingServerIdList'] = request.wuying_server_id_list
        if not DaraCore.is_null(request.wuying_server_name_or_id):
            body['WuyingServerNameOrId'] = request.wuying_server_name_or_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWuyingServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_wuying_server_with_options_async(
        self,
        request: main_models.ListWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWuyingServerResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.add_virtual_node_pool_status_list):
            body_flat['AddVirtualNodePoolStatusList'] = request.add_virtual_node_pool_status_list
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.office_site_id):
            body['OfficeSiteId'] = request.office_site_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.server_instance_type):
            body['ServerInstanceType'] = request.server_instance_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.virtual_node_pool_id):
            body['VirtualNodePoolId'] = request.virtual_node_pool_id
        if not DaraCore.is_null(request.wuying_server_id_list):
            body_flat['WuyingServerIdList'] = request.wuying_server_id_list
        if not DaraCore.is_null(request.wuying_server_name_or_id):
            body['WuyingServerNameOrId'] = request.wuying_server_name_or_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWuyingServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_wuying_server(
        self,
        request: main_models.ListWuyingServerRequest,
    ) -> main_models.ListWuyingServerResponse:
        runtime = RuntimeOptions()
        return self.list_wuying_server_with_options(request, runtime)

    async def list_wuying_server_async(
        self,
        request: main_models.ListWuyingServerRequest,
    ) -> main_models.ListWuyingServerResponse:
        runtime = RuntimeOptions()
        return await self.list_wuying_server_with_options_async(request, runtime)

    def log_off_all_sessions_in_app_instance_group_with_options(
        self,
        request: main_models.LogOffAllSessionsInAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LogOffAllSessionsInAppInstanceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LogOffAllSessionsInAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LogOffAllSessionsInAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def log_off_all_sessions_in_app_instance_group_with_options_async(
        self,
        request: main_models.LogOffAllSessionsInAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LogOffAllSessionsInAppInstanceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LogOffAllSessionsInAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LogOffAllSessionsInAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def log_off_all_sessions_in_app_instance_group(
        self,
        request: main_models.LogOffAllSessionsInAppInstanceGroupRequest,
    ) -> main_models.LogOffAllSessionsInAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.log_off_all_sessions_in_app_instance_group_with_options(request, runtime)

    async def log_off_all_sessions_in_app_instance_group_async(
        self,
        request: main_models.LogOffAllSessionsInAppInstanceGroupRequest,
    ) -> main_models.LogOffAllSessionsInAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.log_off_all_sessions_in_app_instance_group_with_options_async(request, runtime)

    def modify_app_instance_group_attribute_with_options(
        self,
        tmp_req: main_models.ModifyAppInstanceGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppInstanceGroupAttributeResponse:
        tmp_req.validate()
        request = main_models.ModifyAppInstanceGroupAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network):
            request.network_shrink = Utils.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not DaraCore.is_null(tmp_req.node_pool):
            request.node_pool_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        if not DaraCore.is_null(tmp_req.security_policy):
            request.security_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not DaraCore.is_null(tmp_req.storage_policy):
            request.storage_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.storage_policy, 'StoragePolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_group_name):
            query['AppInstanceGroupName'] = request.app_instance_group_name
        if not DaraCore.is_null(request.node_pool_shrink):
            query['NodePool'] = request.node_pool_shrink
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        body = {}
        if not DaraCore.is_null(request.network_shrink):
            body['Network'] = request.network_shrink
        if not DaraCore.is_null(request.per_session_per_app):
            body['PerSessionPerApp'] = request.per_session_per_app
        if not DaraCore.is_null(request.pre_open_app_id):
            body['PreOpenAppId'] = request.pre_open_app_id
        if not DaraCore.is_null(request.pre_open_mode):
            body['PreOpenMode'] = request.pre_open_mode
        if not DaraCore.is_null(request.security_policy_shrink):
            body['SecurityPolicy'] = request.security_policy_shrink
        if not DaraCore.is_null(request.storage_policy_shrink):
            body['StoragePolicy'] = request.storage_policy_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppInstanceGroupAttribute',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppInstanceGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_instance_group_attribute_with_options_async(
        self,
        tmp_req: main_models.ModifyAppInstanceGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppInstanceGroupAttributeResponse:
        tmp_req.validate()
        request = main_models.ModifyAppInstanceGroupAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network):
            request.network_shrink = Utils.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not DaraCore.is_null(tmp_req.node_pool):
            request.node_pool_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        if not DaraCore.is_null(tmp_req.security_policy):
            request.security_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not DaraCore.is_null(tmp_req.storage_policy):
            request.storage_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.storage_policy, 'StoragePolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_group_name):
            query['AppInstanceGroupName'] = request.app_instance_group_name
        if not DaraCore.is_null(request.node_pool_shrink):
            query['NodePool'] = request.node_pool_shrink
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        body = {}
        if not DaraCore.is_null(request.network_shrink):
            body['Network'] = request.network_shrink
        if not DaraCore.is_null(request.per_session_per_app):
            body['PerSessionPerApp'] = request.per_session_per_app
        if not DaraCore.is_null(request.pre_open_app_id):
            body['PreOpenAppId'] = request.pre_open_app_id
        if not DaraCore.is_null(request.pre_open_mode):
            body['PreOpenMode'] = request.pre_open_mode
        if not DaraCore.is_null(request.security_policy_shrink):
            body['SecurityPolicy'] = request.security_policy_shrink
        if not DaraCore.is_null(request.storage_policy_shrink):
            body['StoragePolicy'] = request.storage_policy_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppInstanceGroupAttribute',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppInstanceGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_instance_group_attribute(
        self,
        request: main_models.ModifyAppInstanceGroupAttributeRequest,
    ) -> main_models.ModifyAppInstanceGroupAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_app_instance_group_attribute_with_options(request, runtime)

    async def modify_app_instance_group_attribute_async(
        self,
        request: main_models.ModifyAppInstanceGroupAttributeRequest,
    ) -> main_models.ModifyAppInstanceGroupAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_instance_group_attribute_with_options_async(request, runtime)

    def modify_app_policy_with_options(
        self,
        tmp_req: main_models.ModifyAppPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppPolicyResponse:
        tmp_req.validate()
        request = main_models.ModifyAppPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.video_policy):
            request.video_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_policy, 'VideoPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.app_policy_id):
            query['AppPolicyId'] = request.app_policy_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.video_policy_shrink):
            query['VideoPolicy'] = request.video_policy_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppPolicy',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_policy_with_options_async(
        self,
        tmp_req: main_models.ModifyAppPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppPolicyResponse:
        tmp_req.validate()
        request = main_models.ModifyAppPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.video_policy):
            request.video_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_policy, 'VideoPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.app_policy_id):
            query['AppPolicyId'] = request.app_policy_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.video_policy_shrink):
            query['VideoPolicy'] = request.video_policy_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppPolicy',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_policy(
        self,
        request: main_models.ModifyAppPolicyRequest,
    ) -> main_models.ModifyAppPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_app_policy_with_options(request, runtime)

    async def modify_app_policy_async(
        self,
        request: main_models.ModifyAppPolicyRequest,
    ) -> main_models.ModifyAppPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_policy_with_options_async(request, runtime)

    def modify_browser_instance_group_with_options(
        self,
        tmp_req: main_models.ModifyBrowserInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBrowserInstanceGroupResponse:
        tmp_req.validate()
        request = main_models.ModifyBrowserInstanceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.browser_config):
            request.browser_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.browser_config, 'BrowserConfig', 'json')
        if not DaraCore.is_null(tmp_req.network):
            request.network_shrink = Utils.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        if not DaraCore.is_null(tmp_req.timers):
            request.timers_shrink = Utils.array_to_string_with_specified_style(tmp_req.timers, 'Timers', 'json')
        query = {}
        if not DaraCore.is_null(request.browser_config_shrink):
            query['BrowserConfig'] = request.browser_config_shrink
        if not DaraCore.is_null(request.browser_instance_group_id):
            query['BrowserInstanceGroupId'] = request.browser_instance_group_id
        if not DaraCore.is_null(request.policy_shrink):
            query['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.timers_shrink):
            query['Timers'] = request.timers_shrink
        body = {}
        if not DaraCore.is_null(request.cloud_browser_name):
            body['CloudBrowserName'] = request.cloud_browser_name
        if not DaraCore.is_null(request.network_shrink):
            body['Network'] = request.network_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBrowserInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBrowserInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_browser_instance_group_with_options_async(
        self,
        tmp_req: main_models.ModifyBrowserInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBrowserInstanceGroupResponse:
        tmp_req.validate()
        request = main_models.ModifyBrowserInstanceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.browser_config):
            request.browser_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.browser_config, 'BrowserConfig', 'json')
        if not DaraCore.is_null(tmp_req.network):
            request.network_shrink = Utils.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        if not DaraCore.is_null(tmp_req.timers):
            request.timers_shrink = Utils.array_to_string_with_specified_style(tmp_req.timers, 'Timers', 'json')
        query = {}
        if not DaraCore.is_null(request.browser_config_shrink):
            query['BrowserConfig'] = request.browser_config_shrink
        if not DaraCore.is_null(request.browser_instance_group_id):
            query['BrowserInstanceGroupId'] = request.browser_instance_group_id
        if not DaraCore.is_null(request.policy_shrink):
            query['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.timers_shrink):
            query['Timers'] = request.timers_shrink
        body = {}
        if not DaraCore.is_null(request.cloud_browser_name):
            body['CloudBrowserName'] = request.cloud_browser_name
        if not DaraCore.is_null(request.network_shrink):
            body['Network'] = request.network_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBrowserInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBrowserInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_browser_instance_group(
        self,
        request: main_models.ModifyBrowserInstanceGroupRequest,
    ) -> main_models.ModifyBrowserInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_browser_instance_group_with_options(request, runtime)

    async def modify_browser_instance_group_async(
        self,
        request: main_models.ModifyBrowserInstanceGroupRequest,
    ) -> main_models.ModifyBrowserInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_browser_instance_group_with_options_async(request, runtime)

    def modify_node_pool_amount_with_options(
        self,
        tmp_req: main_models.ModifyNodePoolAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodePoolAmountResponse:
        tmp_req.validate()
        request = main_models.ModifyNodePoolAmountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_pool):
            request.node_pool_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.node_pool_shrink):
            body['NodePool'] = request.node_pool_shrink
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodePoolAmount',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodePoolAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_pool_amount_with_options_async(
        self,
        tmp_req: main_models.ModifyNodePoolAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodePoolAmountResponse:
        tmp_req.validate()
        request = main_models.ModifyNodePoolAmountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_pool):
            request.node_pool_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.node_pool_shrink):
            body['NodePool'] = request.node_pool_shrink
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodePoolAmount',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodePoolAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_pool_amount(
        self,
        request: main_models.ModifyNodePoolAmountRequest,
    ) -> main_models.ModifyNodePoolAmountResponse:
        runtime = RuntimeOptions()
        return self.modify_node_pool_amount_with_options(request, runtime)

    async def modify_node_pool_amount_async(
        self,
        request: main_models.ModifyNodePoolAmountRequest,
    ) -> main_models.ModifyNodePoolAmountResponse:
        runtime = RuntimeOptions()
        return await self.modify_node_pool_amount_with_options_async(request, runtime)

    def modify_node_pool_attribute_with_options(
        self,
        tmp_req: main_models.ModifyNodePoolAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodePoolAttributeResponse:
        tmp_req.validate()
        request = main_models.ModifyNodePoolAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_pool_strategy):
            request.node_pool_strategy_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_pool_strategy, 'NodePoolStrategy', 'json')
        body = {}
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.node_capacity):
            body['NodeCapacity'] = request.node_capacity
        if not DaraCore.is_null(request.node_pool_strategy_shrink):
            body['NodePoolStrategy'] = request.node_pool_strategy_shrink
        if not DaraCore.is_null(request.pool_id):
            body['PoolId'] = request.pool_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodePoolAttribute',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodePoolAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_pool_attribute_with_options_async(
        self,
        tmp_req: main_models.ModifyNodePoolAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodePoolAttributeResponse:
        tmp_req.validate()
        request = main_models.ModifyNodePoolAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_pool_strategy):
            request.node_pool_strategy_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_pool_strategy, 'NodePoolStrategy', 'json')
        body = {}
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.node_capacity):
            body['NodeCapacity'] = request.node_capacity
        if not DaraCore.is_null(request.node_pool_strategy_shrink):
            body['NodePoolStrategy'] = request.node_pool_strategy_shrink
        if not DaraCore.is_null(request.pool_id):
            body['PoolId'] = request.pool_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodePoolAttribute',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodePoolAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_pool_attribute(
        self,
        request: main_models.ModifyNodePoolAttributeRequest,
    ) -> main_models.ModifyNodePoolAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_node_pool_attribute_with_options(request, runtime)

    async def modify_node_pool_attribute_async(
        self,
        request: main_models.ModifyNodePoolAttributeRequest,
    ) -> main_models.ModifyNodePoolAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_node_pool_attribute_with_options_async(request, runtime)

    def modify_tenant_config_with_options(
        self,
        request: main_models.ModifyTenantConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTenantConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_expire_remind):
            body['AppInstanceGroupExpireRemind'] = request.app_instance_group_expire_remind
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTenantConfig',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTenantConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tenant_config_with_options_async(
        self,
        request: main_models.ModifyTenantConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTenantConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_expire_remind):
            body['AppInstanceGroupExpireRemind'] = request.app_instance_group_expire_remind
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTenantConfig',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTenantConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tenant_config(
        self,
        request: main_models.ModifyTenantConfigRequest,
    ) -> main_models.ModifyTenantConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_tenant_config_with_options(request, runtime)

    async def modify_tenant_config_async(
        self,
        request: main_models.ModifyTenantConfigRequest,
    ) -> main_models.ModifyTenantConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_tenant_config_with_options_async(request, runtime)

    def modify_wuying_server_attribute_with_options(
        self,
        request: main_models.ModifyWuyingServerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWuyingServerAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        if not DaraCore.is_null(request.wuying_server_name):
            body['WuyingServerName'] = request.wuying_server_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWuyingServerAttribute',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWuyingServerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_wuying_server_attribute_with_options_async(
        self,
        request: main_models.ModifyWuyingServerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWuyingServerAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        if not DaraCore.is_null(request.wuying_server_name):
            body['WuyingServerName'] = request.wuying_server_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWuyingServerAttribute',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWuyingServerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_wuying_server_attribute(
        self,
        request: main_models.ModifyWuyingServerAttributeRequest,
    ) -> main_models.ModifyWuyingServerAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_wuying_server_attribute_with_options(request, runtime)

    async def modify_wuying_server_attribute_async(
        self,
        request: main_models.ModifyWuyingServerAttributeRequest,
    ) -> main_models.ModifyWuyingServerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_wuying_server_attribute_with_options_async(request, runtime)

    def page_list_app_instance_group_user_with_options(
        self,
        request: main_models.PageListAppInstanceGroupUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PageListAppInstanceGroupUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PageListAppInstanceGroupUser',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PageListAppInstanceGroupUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_list_app_instance_group_user_with_options_async(
        self,
        request: main_models.PageListAppInstanceGroupUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PageListAppInstanceGroupUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PageListAppInstanceGroupUser',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PageListAppInstanceGroupUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_list_app_instance_group_user(
        self,
        request: main_models.PageListAppInstanceGroupUserRequest,
    ) -> main_models.PageListAppInstanceGroupUserResponse:
        runtime = RuntimeOptions()
        return self.page_list_app_instance_group_user_with_options(request, runtime)

    async def page_list_app_instance_group_user_async(
        self,
        request: main_models.PageListAppInstanceGroupUserRequest,
    ) -> main_models.PageListAppInstanceGroupUserResponse:
        runtime = RuntimeOptions()
        return await self.page_list_app_instance_group_user_with_options_async(request, runtime)

    def renew_app_instance_group_with_options(
        self,
        tmp_req: main_models.RenewAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAppInstanceGroupResponse:
        tmp_req.validate()
        request = main_models.RenewAppInstanceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.renew_nodes):
            request.renew_nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.renew_nodes, 'RenewNodes', 'json')
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.renew_amount):
            query['RenewAmount'] = request.renew_amount
        if not DaraCore.is_null(request.renew_mode):
            query['RenewMode'] = request.renew_mode
        if not DaraCore.is_null(request.renew_nodes_shrink):
            query['RenewNodes'] = request.renew_nodes_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_app_instance_group_with_options_async(
        self,
        tmp_req: main_models.RenewAppInstanceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAppInstanceGroupResponse:
        tmp_req.validate()
        request = main_models.RenewAppInstanceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.renew_nodes):
            request.renew_nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.renew_nodes, 'RenewNodes', 'json')
        query = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.renew_amount):
            query['RenewAmount'] = request.renew_amount
        if not DaraCore.is_null(request.renew_mode):
            query['RenewMode'] = request.renew_mode
        if not DaraCore.is_null(request.renew_nodes_shrink):
            query['RenewNodes'] = request.renew_nodes_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAppInstanceGroup',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_app_instance_group(
        self,
        request: main_models.RenewAppInstanceGroupRequest,
    ) -> main_models.RenewAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return self.renew_app_instance_group_with_options(request, runtime)

    async def renew_app_instance_group_async(
        self,
        request: main_models.RenewAppInstanceGroupRequest,
    ) -> main_models.RenewAppInstanceGroupResponse:
        runtime = RuntimeOptions()
        return await self.renew_app_instance_group_with_options_async(request, runtime)

    def renew_wuying_server_with_options(
        self,
        request: main_models.RenewWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewWuyingServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.promotion_id):
            body['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenewWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewWuyingServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_wuying_server_with_options_async(
        self,
        request: main_models.RenewWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewWuyingServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.promotion_id):
            body['PromotionId'] = request.promotion_id
        if not DaraCore.is_null(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenewWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewWuyingServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_wuying_server(
        self,
        request: main_models.RenewWuyingServerRequest,
    ) -> main_models.RenewWuyingServerResponse:
        runtime = RuntimeOptions()
        return self.renew_wuying_server_with_options(request, runtime)

    async def renew_wuying_server_async(
        self,
        request: main_models.RenewWuyingServerRequest,
    ) -> main_models.RenewWuyingServerResponse:
        runtime = RuntimeOptions()
        return await self.renew_wuying_server_with_options_async(request, runtime)

    def restart_wuying_server_with_options(
        self,
        request: main_models.RestartWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartWuyingServerResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.wuying_server_id_list):
            body_flat['WuyingServerIdList'] = request.wuying_server_id_list
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartWuyingServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_wuying_server_with_options_async(
        self,
        request: main_models.RestartWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartWuyingServerResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.wuying_server_id_list):
            body_flat['WuyingServerIdList'] = request.wuying_server_id_list
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartWuyingServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_wuying_server(
        self,
        request: main_models.RestartWuyingServerRequest,
    ) -> main_models.RestartWuyingServerResponse:
        runtime = RuntimeOptions()
        return self.restart_wuying_server_with_options(request, runtime)

    async def restart_wuying_server_async(
        self,
        request: main_models.RestartWuyingServerRequest,
    ) -> main_models.RestartWuyingServerResponse:
        runtime = RuntimeOptions()
        return await self.restart_wuying_server_with_options_async(request, runtime)

    def start_task_for_distribute_image_with_options(
        self,
        request: main_models.StartTaskForDistributeImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartTaskForDistributeImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_region_list):
            body['DestinationRegionList'] = request.destination_region_list
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.retry_type):
            body['RetryType'] = request.retry_type
        if not DaraCore.is_null(request.source_region):
            body['SourceRegion'] = request.source_region
        if not DaraCore.is_null(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartTaskForDistributeImage',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTaskForDistributeImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_task_for_distribute_image_with_options_async(
        self,
        request: main_models.StartTaskForDistributeImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartTaskForDistributeImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.destination_region_list):
            body['DestinationRegionList'] = request.destination_region_list
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.retry_type):
            body['RetryType'] = request.retry_type
        if not DaraCore.is_null(request.source_region):
            body['SourceRegion'] = request.source_region
        if not DaraCore.is_null(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartTaskForDistributeImage',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTaskForDistributeImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_task_for_distribute_image(
        self,
        request: main_models.StartTaskForDistributeImageRequest,
    ) -> main_models.StartTaskForDistributeImageResponse:
        runtime = RuntimeOptions()
        return self.start_task_for_distribute_image_with_options(request, runtime)

    async def start_task_for_distribute_image_async(
        self,
        request: main_models.StartTaskForDistributeImageRequest,
    ) -> main_models.StartTaskForDistributeImageResponse:
        runtime = RuntimeOptions()
        return await self.start_task_for_distribute_image_with_options_async(request, runtime)

    def start_wuying_server_with_options(
        self,
        request: main_models.StartWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartWuyingServerResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.wuying_server_id_list):
            body_flat['WuyingServerIdList'] = request.wuying_server_id_list
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartWuyingServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_wuying_server_with_options_async(
        self,
        request: main_models.StartWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartWuyingServerResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.wuying_server_id_list):
            body_flat['WuyingServerIdList'] = request.wuying_server_id_list
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartWuyingServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_wuying_server(
        self,
        request: main_models.StartWuyingServerRequest,
    ) -> main_models.StartWuyingServerResponse:
        runtime = RuntimeOptions()
        return self.start_wuying_server_with_options(request, runtime)

    async def start_wuying_server_async(
        self,
        request: main_models.StartWuyingServerRequest,
    ) -> main_models.StartWuyingServerResponse:
        runtime = RuntimeOptions()
        return await self.start_wuying_server_with_options_async(request, runtime)

    def stop_wuying_server_with_options(
        self,
        request: main_models.StopWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopWuyingServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.force):
            body['Force'] = request.force
        body_flat = {}
        if not DaraCore.is_null(request.wuying_server_id_list):
            body_flat['WuyingServerIdList'] = request.wuying_server_id_list
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopWuyingServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_wuying_server_with_options_async(
        self,
        request: main_models.StopWuyingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopWuyingServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.force):
            body['Force'] = request.force
        body_flat = {}
        if not DaraCore.is_null(request.wuying_server_id_list):
            body_flat['WuyingServerIdList'] = request.wuying_server_id_list
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopWuyingServer',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopWuyingServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_wuying_server(
        self,
        request: main_models.StopWuyingServerRequest,
    ) -> main_models.StopWuyingServerResponse:
        runtime = RuntimeOptions()
        return self.stop_wuying_server_with_options(request, runtime)

    async def stop_wuying_server_async(
        self,
        request: main_models.StopWuyingServerRequest,
    ) -> main_models.StopWuyingServerResponse:
        runtime = RuntimeOptions()
        return await self.stop_wuying_server_with_options_async(request, runtime)

    def tag_cloud_resources_with_options(
        self,
        request: main_models.TagCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagCloudResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagCloudResources',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_cloud_resources_with_options_async(
        self,
        request: main_models.TagCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagCloudResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagCloudResources',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_cloud_resources(
        self,
        request: main_models.TagCloudResourcesRequest,
    ) -> main_models.TagCloudResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_cloud_resources_with_options(request, runtime)

    async def tag_cloud_resources_async(
        self,
        request: main_models.TagCloudResourcesRequest,
    ) -> main_models.TagCloudResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_cloud_resources_with_options_async(request, runtime)

    def unbind_with_options(
        self,
        request: main_models.UnbindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Unbind',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_with_options_async(
        self,
        request: main_models.UnbindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Unbind',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind(
        self,
        request: main_models.UnbindRequest,
    ) -> main_models.UnbindResponse:
        runtime = RuntimeOptions()
        return self.unbind_with_options(request, runtime)

    async def unbind_async(
        self,
        request: main_models.UnbindRequest,
    ) -> main_models.UnbindResponse:
        runtime = RuntimeOptions()
        return await self.unbind_with_options_async(request, runtime)

    def untag_cloud_resources_with_options(
        self,
        request: main_models.UntagCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagCloudResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            body['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagCloudResources',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_cloud_resources_with_options_async(
        self,
        request: main_models.UntagCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagCloudResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            body['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagCloudResources',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_cloud_resources(
        self,
        request: main_models.UntagCloudResourcesRequest,
    ) -> main_models.UntagCloudResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_cloud_resources_with_options(request, runtime)

    async def untag_cloud_resources_async(
        self,
        request: main_models.UntagCloudResourcesRequest,
    ) -> main_models.UntagCloudResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_cloud_resources_with_options_async(request, runtime)

    def update_app_instance_group_image_with_options(
        self,
        request: main_models.UpdateAppInstanceGroupImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppInstanceGroupImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_center_image_id):
            query['AppCenterImageId'] = request.app_center_image_id
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppInstanceGroupImage',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppInstanceGroupImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_instance_group_image_with_options_async(
        self,
        request: main_models.UpdateAppInstanceGroupImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppInstanceGroupImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_center_image_id):
            query['AppCenterImageId'] = request.app_center_image_id
        if not DaraCore.is_null(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppInstanceGroupImage',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppInstanceGroupImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_instance_group_image(
        self,
        request: main_models.UpdateAppInstanceGroupImageRequest,
    ) -> main_models.UpdateAppInstanceGroupImageResponse:
        runtime = RuntimeOptions()
        return self.update_app_instance_group_image_with_options(request, runtime)

    async def update_app_instance_group_image_async(
        self,
        request: main_models.UpdateAppInstanceGroupImageRequest,
    ) -> main_models.UpdateAppInstanceGroupImageResponse:
        runtime = RuntimeOptions()
        return await self.update_app_instance_group_image_with_options_async(request, runtime)

    def update_wuying_server_image_with_options(
        self,
        request: main_models.UpdateWuyingServerImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWuyingServerImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWuyingServerImage',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWuyingServerImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_wuying_server_image_with_options_async(
        self,
        request: main_models.UpdateWuyingServerImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWuyingServerImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.wuying_server_id):
            body['WuyingServerId'] = request.wuying_server_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWuyingServerImage',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWuyingServerImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_wuying_server_image(
        self,
        request: main_models.UpdateWuyingServerImageRequest,
    ) -> main_models.UpdateWuyingServerImageResponse:
        runtime = RuntimeOptions()
        return self.update_wuying_server_image_with_options(request, runtime)

    async def update_wuying_server_image_async(
        self,
        request: main_models.UpdateWuyingServerImageRequest,
    ) -> main_models.UpdateWuyingServerImageResponse:
        runtime = RuntimeOptions()
        return await self.update_wuying_server_image_with_options_async(request, runtime)
