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
        self._signature_algorithm = 'v2'
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
        """
        @summary Sets the execution time of an over-the-air (OTA) update task.
        
        @param request: ApproveOtaTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApproveOtaTaskResponse
        """
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
        """
        @summary Sets the execution time of an over-the-air (OTA) update task.
        
        @param request: ApproveOtaTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApproveOtaTaskResponse
        """
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
        """
        @summary Sets the execution time of an over-the-air (OTA) update task.
        
        @param request: ApproveOtaTaskRequest
        @return: ApproveOtaTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.approve_ota_task_with_options(request, runtime)

    async def approve_ota_task_async(
        self,
        request: appstream_center_20210901_models.ApproveOtaTaskRequest,
    ) -> appstream_center_20210901_models.ApproveOtaTaskResponse:
        """
        @summary Sets the execution time of an over-the-air (OTA) update task.
        
        @param request: ApproveOtaTaskRequest
        @return: ApproveOtaTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.approve_ota_task_with_options_async(request, runtime)

    def authorize_instance_group_with_options(
        self,
        tmp_req: appstream_center_20210901_models.AuthorizeInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.AuthorizeInstanceGroupResponse:
        """
        @summary 授权用户
        
        @param tmp_req: AuthorizeInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeInstanceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.AuthorizeInstanceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_meta):
            request.user_meta_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_meta, 'UserMeta', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        body_flat = {}
        if not UtilClient.is_unset(request.authorize_user_group_ids):
            body_flat['AuthorizeUserGroupIds'] = request.authorize_user_group_ids
        if not UtilClient.is_unset(request.authorize_user_ids):
            body_flat['AuthorizeUserIds'] = request.authorize_user_ids
        if not UtilClient.is_unset(request.avatar_id):
            body['AvatarId'] = request.avatar_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.un_authorize_user_group_ids):
            body_flat['UnAuthorizeUserGroupIds'] = request.un_authorize_user_group_ids
        if not UtilClient.is_unset(request.un_authorize_user_ids):
            body_flat['UnAuthorizeUserIds'] = request.un_authorize_user_ids
        if not UtilClient.is_unset(request.user_meta_shrink):
            body['UserMeta'] = request.user_meta_shrink
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        tmp_req: appstream_center_20210901_models.AuthorizeInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.AuthorizeInstanceGroupResponse:
        """
        @summary 授权用户
        
        @param tmp_req: AuthorizeInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeInstanceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.AuthorizeInstanceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_meta):
            request.user_meta_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_meta, 'UserMeta', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        body_flat = {}
        if not UtilClient.is_unset(request.authorize_user_group_ids):
            body_flat['AuthorizeUserGroupIds'] = request.authorize_user_group_ids
        if not UtilClient.is_unset(request.authorize_user_ids):
            body_flat['AuthorizeUserIds'] = request.authorize_user_ids
        if not UtilClient.is_unset(request.avatar_id):
            body['AvatarId'] = request.avatar_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.un_authorize_user_group_ids):
            body_flat['UnAuthorizeUserGroupIds'] = request.un_authorize_user_group_ids
        if not UtilClient.is_unset(request.un_authorize_user_ids):
            body_flat['UnAuthorizeUserIds'] = request.un_authorize_user_ids
        if not UtilClient.is_unset(request.user_meta_shrink):
            body['UserMeta'] = request.user_meta_shrink
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary 授权用户
        
        @param request: AuthorizeInstanceGroupRequest
        @return: AuthorizeInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_instance_group_with_options(request, runtime)

    async def authorize_instance_group_async(
        self,
        request: appstream_center_20210901_models.AuthorizeInstanceGroupRequest,
    ) -> appstream_center_20210901_models.AuthorizeInstanceGroupResponse:
        """
        @summary 授权用户
        
        @param request: AuthorizeInstanceGroupRequest
        @return: AuthorizeInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_instance_group_with_options_async(request, runtime)

    def create_app_instance_group_with_options(
        self,
        tmp_req: appstream_center_20210901_models.CreateAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.CreateAppInstanceGroupResponse:
        """
        @summary 创建云应用交付组
        
        @param tmp_req: CreateAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppInstanceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.CreateAppInstanceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network):
            request.network_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not UtilClient.is_unset(tmp_req.node_pool):
            request.node_pool_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        if not UtilClient.is_unset(tmp_req.runtime_policy):
            request.runtime_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.runtime_policy, 'RuntimePolicy', 'json')
        if not UtilClient.is_unset(tmp_req.security_policy):
            request.security_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.storage_policy):
            request.storage_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage_policy, 'StoragePolicy', 'json')
        if not UtilClient.is_unset(tmp_req.user_define_policy):
            request.user_define_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_define_policy, 'UserDefinePolicy', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_policy):
            request.video_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_policy, 'VideoPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_define_policy_shrink):
            query['UserDefinePolicy'] = request.user_define_policy_shrink
        body = {}
        if not UtilClient.is_unset(request.app_center_image_id):
            body['AppCenterImageId'] = request.app_center_image_id
        if not UtilClient.is_unset(request.app_instance_group_name):
            body['AppInstanceGroupName'] = request.app_instance_group_name
        if not UtilClient.is_unset(request.app_package_type):
            body['AppPackageType'] = request.app_package_type
        if not UtilClient.is_unset(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not UtilClient.is_unset(request.auth_mode):
            body['AuthMode'] = request.auth_mode
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
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
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
        if not UtilClient.is_unset(request.runtime_policy_shrink):
            body['RuntimePolicy'] = request.runtime_policy_shrink
        if not UtilClient.is_unset(request.security_policy_shrink):
            body['SecurityPolicy'] = request.security_policy_shrink
        if not UtilClient.is_unset(request.session_timeout):
            body['SessionTimeout'] = request.session_timeout
        if not UtilClient.is_unset(request.storage_policy_shrink):
            body['StoragePolicy'] = request.storage_policy_shrink
        if not UtilClient.is_unset(request.sub_pay_type):
            body['SubPayType'] = request.sub_pay_type
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        if not UtilClient.is_unset(request.video_policy_shrink):
            body['VideoPolicy'] = request.video_policy_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        """
        @summary 创建云应用交付组
        
        @param tmp_req: CreateAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppInstanceGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.CreateAppInstanceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network):
            request.network_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not UtilClient.is_unset(tmp_req.node_pool):
            request.node_pool_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        if not UtilClient.is_unset(tmp_req.runtime_policy):
            request.runtime_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.runtime_policy, 'RuntimePolicy', 'json')
        if not UtilClient.is_unset(tmp_req.security_policy):
            request.security_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.storage_policy):
            request.storage_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage_policy, 'StoragePolicy', 'json')
        if not UtilClient.is_unset(tmp_req.user_define_policy):
            request.user_define_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_define_policy, 'UserDefinePolicy', 'json')
        if not UtilClient.is_unset(tmp_req.user_info):
            request.user_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_info, 'UserInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_policy):
            request.video_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_policy, 'VideoPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.user_define_policy_shrink):
            query['UserDefinePolicy'] = request.user_define_policy_shrink
        body = {}
        if not UtilClient.is_unset(request.app_center_image_id):
            body['AppCenterImageId'] = request.app_center_image_id
        if not UtilClient.is_unset(request.app_instance_group_name):
            body['AppInstanceGroupName'] = request.app_instance_group_name
        if not UtilClient.is_unset(request.app_package_type):
            body['AppPackageType'] = request.app_package_type
        if not UtilClient.is_unset(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not UtilClient.is_unset(request.auth_mode):
            body['AuthMode'] = request.auth_mode
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
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
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
        if not UtilClient.is_unset(request.runtime_policy_shrink):
            body['RuntimePolicy'] = request.runtime_policy_shrink
        if not UtilClient.is_unset(request.security_policy_shrink):
            body['SecurityPolicy'] = request.security_policy_shrink
        if not UtilClient.is_unset(request.session_timeout):
            body['SessionTimeout'] = request.session_timeout
        if not UtilClient.is_unset(request.storage_policy_shrink):
            body['StoragePolicy'] = request.storage_policy_shrink
        if not UtilClient.is_unset(request.sub_pay_type):
            body['SubPayType'] = request.sub_pay_type
        if not UtilClient.is_unset(request.user_info_shrink):
            body['UserInfo'] = request.user_info_shrink
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        if not UtilClient.is_unset(request.video_policy_shrink):
            body['VideoPolicy'] = request.video_policy_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        """
        @summary 创建云应用交付组
        
        @param request: CreateAppInstanceGroupRequest
        @return: CreateAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_instance_group_with_options(request, runtime)

    async def create_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.CreateAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.CreateAppInstanceGroupResponse:
        """
        @summary 创建云应用交付组
        
        @param request: CreateAppInstanceGroupRequest
        @return: CreateAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_instance_group_with_options_async(request, runtime)

    def create_image_from_app_instance_group_with_options(
        self,
        request: appstream_center_20210901_models.CreateImageFromAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.CreateImageFromAppInstanceGroupResponse:
        """
        @summary Creates a new image by debugging the delivery group.
        
        @param request: CreateImageFromAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageFromAppInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_center_image_name):
            body['AppCenterImageName'] = request.app_center_image_name
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateImageFromAppInstanceGroup',
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
            appstream_center_20210901_models.CreateImageFromAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_from_app_instance_group_with_options_async(
        self,
        request: appstream_center_20210901_models.CreateImageFromAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.CreateImageFromAppInstanceGroupResponse:
        """
        @summary Creates a new image by debugging the delivery group.
        
        @param request: CreateImageFromAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageFromAppInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_center_image_name):
            body['AppCenterImageName'] = request.app_center_image_name
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateImageFromAppInstanceGroup',
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
            appstream_center_20210901_models.CreateImageFromAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_from_app_instance_group(
        self,
        request: appstream_center_20210901_models.CreateImageFromAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.CreateImageFromAppInstanceGroupResponse:
        """
        @summary Creates a new image by debugging the delivery group.
        
        @param request: CreateImageFromAppInstanceGroupRequest
        @return: CreateImageFromAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_image_from_app_instance_group_with_options(request, runtime)

    async def create_image_from_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.CreateImageFromAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.CreateImageFromAppInstanceGroupResponse:
        """
        @summary Creates a new image by debugging the delivery group.
        
        @param request: CreateImageFromAppInstanceGroupRequest
        @return: CreateImageFromAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_image_from_app_instance_group_with_options_async(request, runtime)

    def delete_app_instance_group_with_options(
        self,
        request: appstream_center_20210901_models.DeleteAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.DeleteAppInstanceGroupResponse:
        """
        @summary Deletes a delivery group that uses the By Resource - Pay-as-you-go billing method.
        
        @description >  You cannot call this operation to delete a subscription delivery group.
        
        @param request: DeleteAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppInstanceGroupResponse
        """
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
        """
        @summary Deletes a delivery group that uses the By Resource - Pay-as-you-go billing method.
        
        @description >  You cannot call this operation to delete a subscription delivery group.
        
        @param request: DeleteAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppInstanceGroupResponse
        """
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
        """
        @summary Deletes a delivery group that uses the By Resource - Pay-as-you-go billing method.
        
        @description >  You cannot call this operation to delete a subscription delivery group.
        
        @param request: DeleteAppInstanceGroupRequest
        @return: DeleteAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_instance_group_with_options(request, runtime)

    async def delete_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.DeleteAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.DeleteAppInstanceGroupResponse:
        """
        @summary Deletes a delivery group that uses the By Resource - Pay-as-you-go billing method.
        
        @description >  You cannot call this operation to delete a subscription delivery group.
        
        @param request: DeleteAppInstanceGroupRequest
        @return: DeleteAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_instance_group_with_options_async(request, runtime)

    def delete_app_instances_with_options(
        self,
        request: appstream_center_20210901_models.DeleteAppInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.DeleteAppInstancesResponse:
        """
        @summary Deletes an application instance.
        
        @description Only application instances that are in the Initializing or Idle state can be deleted. The operation can be called only by specific customers.
        
        @param request: DeleteAppInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_ids):
            body['AppInstanceIds'] = request.app_instance_ids
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppInstances',
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
            appstream_center_20210901_models.DeleteAppInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_instances_with_options_async(
        self,
        request: appstream_center_20210901_models.DeleteAppInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.DeleteAppInstancesResponse:
        """
        @summary Deletes an application instance.
        
        @description Only application instances that are in the Initializing or Idle state can be deleted. The operation can be called only by specific customers.
        
        @param request: DeleteAppInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_ids):
            body['AppInstanceIds'] = request.app_instance_ids
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppInstances',
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
            appstream_center_20210901_models.DeleteAppInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_instances(
        self,
        request: appstream_center_20210901_models.DeleteAppInstancesRequest,
    ) -> appstream_center_20210901_models.DeleteAppInstancesResponse:
        """
        @summary Deletes an application instance.
        
        @description Only application instances that are in the Initializing or Idle state can be deleted. The operation can be called only by specific customers.
        
        @param request: DeleteAppInstancesRequest
        @return: DeleteAppInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_instances_with_options(request, runtime)

    async def delete_app_instances_async(
        self,
        request: appstream_center_20210901_models.DeleteAppInstancesRequest,
    ) -> appstream_center_20210901_models.DeleteAppInstancesResponse:
        """
        @summary Deletes an application instance.
        
        @description Only application instances that are in the Initializing or Idle state can be deleted. The operation can be called only by specific customers.
        
        @param request: DeleteAppInstancesRequest
        @return: DeleteAppInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_instances_with_options_async(request, runtime)

    def get_app_instance_group_with_options(
        self,
        request: appstream_center_20210901_models.GetAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetAppInstanceGroupResponse:
        """
        @summary 获取交付组详情
        
        @param request: GetAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppInstanceGroup',
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
            appstream_center_20210901_models.GetAppInstanceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_instance_group_with_options_async(
        self,
        request: appstream_center_20210901_models.GetAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetAppInstanceGroupResponse:
        """
        @summary 获取交付组详情
        
        @param request: GetAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppInstanceGroup',
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
            appstream_center_20210901_models.GetAppInstanceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_instance_group(
        self,
        request: appstream_center_20210901_models.GetAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.GetAppInstanceGroupResponse:
        """
        @summary 获取交付组详情
        
        @param request: GetAppInstanceGroupRequest
        @return: GetAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_instance_group_with_options(request, runtime)

    async def get_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.GetAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.GetAppInstanceGroupResponse:
        """
        @summary 获取交付组详情
        
        @param request: GetAppInstanceGroupRequest
        @return: GetAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_app_instance_group_with_options_async(request, runtime)

    def get_connection_ticket_with_options(
        self,
        request: appstream_center_20210901_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetConnectionTicketResponse:
        """
        @summary Queries the credential that is used to connect to App Streaming.
        
        @description You must call this operation at least twice to obtain a connection credential.
        The first time you call this operation, the system assigns an application instance to the specified convenience account and then starts the application. In this case, the ID of the started task, which is indicated by `TaskID`, is returned.
        In subsequent calls, you must configure `TaskID` to query whether the task is completed. If the value of `TaskStatus` in the response is `Finished`, the connection credential, which is indicated by `Ticket`, is returned.
        
        @param request: GetConnectionTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_type):
            body['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_instance_group_id_list):
            body['AppInstanceGroupIdList'] = request.app_instance_group_id_list
        if not UtilClient.is_unset(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        if not UtilClient.is_unset(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not UtilClient.is_unset(request.app_start_param):
            body['AppStartParam'] = request.app_start_param
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetConnectionTicket',
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
            appstream_center_20210901_models.GetConnectionTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_connection_ticket_with_options_async(
        self,
        request: appstream_center_20210901_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetConnectionTicketResponse:
        """
        @summary Queries the credential that is used to connect to App Streaming.
        
        @description You must call this operation at least twice to obtain a connection credential.
        The first time you call this operation, the system assigns an application instance to the specified convenience account and then starts the application. In this case, the ID of the started task, which is indicated by `TaskID`, is returned.
        In subsequent calls, you must configure `TaskID` to query whether the task is completed. If the value of `TaskStatus` in the response is `Finished`, the connection credential, which is indicated by `Ticket`, is returned.
        
        @param request: GetConnectionTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_type):
            body['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_instance_group_id_list):
            body['AppInstanceGroupIdList'] = request.app_instance_group_id_list
        if not UtilClient.is_unset(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        if not UtilClient.is_unset(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not UtilClient.is_unset(request.app_start_param):
            body['AppStartParam'] = request.app_start_param
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetConnectionTicket',
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
            appstream_center_20210901_models.GetConnectionTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_connection_ticket(
        self,
        request: appstream_center_20210901_models.GetConnectionTicketRequest,
    ) -> appstream_center_20210901_models.GetConnectionTicketResponse:
        """
        @summary Queries the credential that is used to connect to App Streaming.
        
        @description You must call this operation at least twice to obtain a connection credential.
        The first time you call this operation, the system assigns an application instance to the specified convenience account and then starts the application. In this case, the ID of the started task, which is indicated by `TaskID`, is returned.
        In subsequent calls, you must configure `TaskID` to query whether the task is completed. If the value of `TaskStatus` in the response is `Finished`, the connection credential, which is indicated by `Ticket`, is returned.
        
        @param request: GetConnectionTicketRequest
        @return: GetConnectionTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    async def get_connection_ticket_async(
        self,
        request: appstream_center_20210901_models.GetConnectionTicketRequest,
    ) -> appstream_center_20210901_models.GetConnectionTicketResponse:
        """
        @summary Queries the credential that is used to connect to App Streaming.
        
        @description You must call this operation at least twice to obtain a connection credential.
        The first time you call this operation, the system assigns an application instance to the specified convenience account and then starts the application. In this case, the ID of the started task, which is indicated by `TaskID`, is returned.
        In subsequent calls, you must configure `TaskID` to query whether the task is completed. If the value of `TaskStatus` in the response is `Finished`, the connection credential, which is indicated by `Ticket`, is returned.
        
        @param request: GetConnectionTicketRequest
        @return: GetConnectionTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_connection_ticket_with_options_async(request, runtime)

    def get_debug_app_instance_with_options(
        self,
        request: appstream_center_20210901_models.GetDebugAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetDebugAppInstanceResponse:
        """
        @summary Queries information that is used to debug an application instance.
        
        @param request: GetDebugAppInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDebugAppInstanceResponse
        """
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
            action='GetDebugAppInstance',
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
            appstream_center_20210901_models.GetDebugAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_debug_app_instance_with_options_async(
        self,
        request: appstream_center_20210901_models.GetDebugAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetDebugAppInstanceResponse:
        """
        @summary Queries information that is used to debug an application instance.
        
        @param request: GetDebugAppInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDebugAppInstanceResponse
        """
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
            action='GetDebugAppInstance',
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
            appstream_center_20210901_models.GetDebugAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_debug_app_instance(
        self,
        request: appstream_center_20210901_models.GetDebugAppInstanceRequest,
    ) -> appstream_center_20210901_models.GetDebugAppInstanceResponse:
        """
        @summary Queries information that is used to debug an application instance.
        
        @param request: GetDebugAppInstanceRequest
        @return: GetDebugAppInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_debug_app_instance_with_options(request, runtime)

    async def get_debug_app_instance_async(
        self,
        request: appstream_center_20210901_models.GetDebugAppInstanceRequest,
    ) -> appstream_center_20210901_models.GetDebugAppInstanceResponse:
        """
        @summary Queries information that is used to debug an application instance.
        
        @param request: GetDebugAppInstanceRequest
        @return: GetDebugAppInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_debug_app_instance_with_options_async(request, runtime)

    def get_ota_task_by_task_id_with_options(
        self,
        request: appstream_center_20210901_models.GetOtaTaskByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetOtaTaskByTaskIdResponse:
        """
        @summary Queries the details of an over-the-air (OTA) update task, including the available versions and version description.
        
        @param request: GetOtaTaskByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOtaTaskByTaskIdResponse
        """
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
        """
        @summary Queries the details of an over-the-air (OTA) update task, including the available versions and version description.
        
        @param request: GetOtaTaskByTaskIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOtaTaskByTaskIdResponse
        """
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
        """
        @summary Queries the details of an over-the-air (OTA) update task, including the available versions and version description.
        
        @param request: GetOtaTaskByTaskIdRequest
        @return: GetOtaTaskByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ota_task_by_task_id_with_options(request, runtime)

    async def get_ota_task_by_task_id_async(
        self,
        request: appstream_center_20210901_models.GetOtaTaskByTaskIdRequest,
    ) -> appstream_center_20210901_models.GetOtaTaskByTaskIdResponse:
        """
        @summary Queries the details of an over-the-air (OTA) update task, including the available versions and version description.
        
        @param request: GetOtaTaskByTaskIdRequest
        @return: GetOtaTaskByTaskIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ota_task_by_task_id_with_options_async(request, runtime)

    def get_resource_price_with_options(
        self,
        request: appstream_center_20210901_models.GetResourcePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetResourcePriceResponse:
        """
        @summary Queries resource prices.
        
        @param request: GetResourcePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourcePriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.app_instance_type):
            query['AppInstanceType'] = request.app_instance_type
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
        """
        @summary Queries resource prices.
        
        @param request: GetResourcePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourcePriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.app_instance_type):
            query['AppInstanceType'] = request.app_instance_type
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
        """
        @summary Queries resource prices.
        
        @param request: GetResourcePriceRequest
        @return: GetResourcePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_price_with_options(request, runtime)

    async def get_resource_price_async(
        self,
        request: appstream_center_20210901_models.GetResourcePriceRequest,
    ) -> appstream_center_20210901_models.GetResourcePriceResponse:
        """
        @summary Queries resource prices.
        
        @param request: GetResourcePriceRequest
        @return: GetResourcePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_price_with_options_async(request, runtime)

    def get_resource_renew_price_with_options(
        self,
        request: appstream_center_20210901_models.GetResourceRenewPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.GetResourceRenewPriceResponse:
        """
        @summary Queries the renewal prices of App Streaming resources.
        
        @param request: GetResourceRenewPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceRenewPriceResponse
        """
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
        """
        @summary Queries the renewal prices of App Streaming resources.
        
        @param request: GetResourceRenewPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceRenewPriceResponse
        """
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
        """
        @summary Queries the renewal prices of App Streaming resources.
        
        @param request: GetResourceRenewPriceRequest
        @return: GetResourceRenewPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_renew_price_with_options(request, runtime)

    async def get_resource_renew_price_async(
        self,
        request: appstream_center_20210901_models.GetResourceRenewPriceRequest,
    ) -> appstream_center_20210901_models.GetResourceRenewPriceResponse:
        """
        @summary Queries the renewal prices of App Streaming resources.
        
        @param request: GetResourceRenewPriceRequest
        @return: GetResourceRenewPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_renew_price_with_options_async(request, runtime)

    def list_app_instance_group_with_options(
        self,
        request: appstream_center_20210901_models.ListAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListAppInstanceGroupResponse:
        """
        @summary Queries the details of multiple delivery groups that meet the query conditions.
        
        @param request: ListAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_center_image_id):
            query['AppCenterImageId'] = request.app_center_image_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_group_name):
            query['AppInstanceGroupName'] = request.app_instance_group_name
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        @summary Queries the details of multiple delivery groups that meet the query conditions.
        
        @param request: ListAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppInstanceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_center_image_id):
            query['AppCenterImageId'] = request.app_center_image_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_group_name):
            query['AppInstanceGroupName'] = request.app_instance_group_name
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        @summary Queries the details of multiple delivery groups that meet the query conditions.
        
        @param request: ListAppInstanceGroupRequest
        @return: ListAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_instance_group_with_options(request, runtime)

    async def list_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.ListAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.ListAppInstanceGroupResponse:
        """
        @summary Queries the details of multiple delivery groups that meet the query conditions.
        
        @param request: ListAppInstanceGroupRequest
        @return: ListAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_app_instance_group_with_options_async(request, runtime)

    def list_app_instances_with_options(
        self,
        request: appstream_center_20210901_models.ListAppInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListAppInstancesResponse:
        """
        @summary Queries the details of application instances in a delivery group, including the IDs, status, creation time, update time, session status, and public IP addresses associated with the primary NICs of the instances.
        
        @param request: ListAppInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.include_deleted):
            query['IncludeDeleted'] = request.include_deleted
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        body = {}
        if not UtilClient.is_unset(request.app_instance_id_list):
            body['AppInstanceIdList'] = request.app_instance_id_list
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppInstances',
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
            appstream_center_20210901_models.ListAppInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_instances_with_options_async(
        self,
        request: appstream_center_20210901_models.ListAppInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListAppInstancesResponse:
        """
        @summary Queries the details of application instances in a delivery group, including the IDs, status, creation time, update time, session status, and public IP addresses associated with the primary NICs of the instances.
        
        @param request: ListAppInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.include_deleted):
            query['IncludeDeleted'] = request.include_deleted
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        body = {}
        if not UtilClient.is_unset(request.app_instance_id_list):
            body['AppInstanceIdList'] = request.app_instance_id_list
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppInstances',
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
            appstream_center_20210901_models.ListAppInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_instances(
        self,
        request: appstream_center_20210901_models.ListAppInstancesRequest,
    ) -> appstream_center_20210901_models.ListAppInstancesResponse:
        """
        @summary Queries the details of application instances in a delivery group, including the IDs, status, creation time, update time, session status, and public IP addresses associated with the primary NICs of the instances.
        
        @param request: ListAppInstancesRequest
        @return: ListAppInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_instances_with_options(request, runtime)

    async def list_app_instances_async(
        self,
        request: appstream_center_20210901_models.ListAppInstancesRequest,
    ) -> appstream_center_20210901_models.ListAppInstancesResponse:
        """
        @summary Queries the details of application instances in a delivery group, including the IDs, status, creation time, update time, session status, and public IP addresses associated with the primary NICs of the instances.
        
        @param request: ListAppInstancesRequest
        @return: ListAppInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_app_instances_with_options_async(request, runtime)

    def list_authorized_user_groups_with_options(
        self,
        request: appstream_center_20210901_models.ListAuthorizedUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListAuthorizedUserGroupsResponse:
        """
        @summary 通过交付组查询展示授权的用户组列表
        
        @param request: ListAuthorizedUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthorizedUserGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
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
            action='ListAuthorizedUserGroups',
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
            appstream_center_20210901_models.ListAuthorizedUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorized_user_groups_with_options_async(
        self,
        request: appstream_center_20210901_models.ListAuthorizedUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListAuthorizedUserGroupsResponse:
        """
        @summary 通过交付组查询展示授权的用户组列表
        
        @param request: ListAuthorizedUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthorizedUserGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
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
            action='ListAuthorizedUserGroups',
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
            appstream_center_20210901_models.ListAuthorizedUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorized_user_groups(
        self,
        request: appstream_center_20210901_models.ListAuthorizedUserGroupsRequest,
    ) -> appstream_center_20210901_models.ListAuthorizedUserGroupsResponse:
        """
        @summary 通过交付组查询展示授权的用户组列表
        
        @param request: ListAuthorizedUserGroupsRequest
        @return: ListAuthorizedUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_authorized_user_groups_with_options(request, runtime)

    async def list_authorized_user_groups_async(
        self,
        request: appstream_center_20210901_models.ListAuthorizedUserGroupsRequest,
    ) -> appstream_center_20210901_models.ListAuthorizedUserGroupsResponse:
        """
        @summary 通过交付组查询展示授权的用户组列表
        
        @param request: ListAuthorizedUserGroupsRequest
        @return: ListAuthorizedUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_authorized_user_groups_with_options_async(request, runtime)

    def list_bind_info_with_options(
        self,
        request: appstream_center_20210901_models.ListBindInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListBindInfoResponse:
        """
        @summary 查询绑定信息，支持分页
        
        @param request: ListBindInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id_list):
            body['AppIdList'] = request.app_id_list
        if not UtilClient.is_unset(request.app_instance_group_id_list):
            body['AppInstanceGroupIdList'] = request.app_instance_group_id_list
        if not UtilClient.is_unset(request.app_instance_id_list):
            body['AppInstanceIdList'] = request.app_instance_id_list
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id_list):
            body['UserIdList'] = request.user_id_list
        if not UtilClient.is_unset(request.wy_id_list):
            body['WyIdList'] = request.wy_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBindInfo',
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
            appstream_center_20210901_models.ListBindInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bind_info_with_options_async(
        self,
        request: appstream_center_20210901_models.ListBindInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListBindInfoResponse:
        """
        @summary 查询绑定信息，支持分页
        
        @param request: ListBindInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id_list):
            body['AppIdList'] = request.app_id_list
        if not UtilClient.is_unset(request.app_instance_group_id_list):
            body['AppInstanceGroupIdList'] = request.app_instance_group_id_list
        if not UtilClient.is_unset(request.app_instance_id_list):
            body['AppInstanceIdList'] = request.app_instance_id_list
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id_list):
            body['UserIdList'] = request.user_id_list
        if not UtilClient.is_unset(request.wy_id_list):
            body['WyIdList'] = request.wy_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBindInfo',
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
            appstream_center_20210901_models.ListBindInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bind_info(
        self,
        request: appstream_center_20210901_models.ListBindInfoRequest,
    ) -> appstream_center_20210901_models.ListBindInfoResponse:
        """
        @summary 查询绑定信息，支持分页
        
        @param request: ListBindInfoRequest
        @return: ListBindInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_bind_info_with_options(request, runtime)

    async def list_bind_info_async(
        self,
        request: appstream_center_20210901_models.ListBindInfoRequest,
    ) -> appstream_center_20210901_models.ListBindInfoResponse:
        """
        @summary 查询绑定信息，支持分页
        
        @param request: ListBindInfoRequest
        @return: ListBindInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_bind_info_with_options_async(request, runtime)

    def list_node_instance_type_with_options(
        self,
        request: appstream_center_20210901_models.ListNodeInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListNodeInstanceTypeResponse:
        """
        @summary Queries the resource types that are available for purchase when you create a delivery group.
        
        @param request: ListNodeInstanceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeInstanceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.gpu):
            query['Gpu'] = request.gpu
        if not UtilClient.is_unset(request.gpu_memory):
            query['GpuMemory'] = request.gpu_memory
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not UtilClient.is_unset(request.node_instance_type_family):
            query['NodeInstanceTypeFamily'] = request.node_instance_type_family
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
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
        """
        @summary Queries the resource types that are available for purchase when you create a delivery group.
        
        @param request: ListNodeInstanceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeInstanceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.gpu):
            query['Gpu'] = request.gpu
        if not UtilClient.is_unset(request.gpu_memory):
            query['GpuMemory'] = request.gpu_memory
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.node_instance_type):
            query['NodeInstanceType'] = request.node_instance_type
        if not UtilClient.is_unset(request.node_instance_type_family):
            query['NodeInstanceTypeFamily'] = request.node_instance_type_family
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
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
        """
        @summary Queries the resource types that are available for purchase when you create a delivery group.
        
        @param request: ListNodeInstanceTypeRequest
        @return: ListNodeInstanceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_node_instance_type_with_options(request, runtime)

    async def list_node_instance_type_async(
        self,
        request: appstream_center_20210901_models.ListNodeInstanceTypeRequest,
    ) -> appstream_center_20210901_models.ListNodeInstanceTypeResponse:
        """
        @summary Queries the resource types that are available for purchase when you create a delivery group.
        
        @param request: ListNodeInstanceTypeRequest
        @return: ListNodeInstanceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_node_instance_type_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: appstream_center_20210901_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListNodesResponse:
        """
        @summary Queries resource nodes.
        
        @param request: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
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
            action='ListNodes',
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
            appstream_center_20210901_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: appstream_center_20210901_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListNodesResponse:
        """
        @summary Queries resource nodes.
        
        @param request: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
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
            action='ListNodes',
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
            appstream_center_20210901_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: appstream_center_20210901_models.ListNodesRequest,
    ) -> appstream_center_20210901_models.ListNodesResponse:
        """
        @summary Queries resource nodes.
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: appstream_center_20210901_models.ListNodesRequest,
    ) -> appstream_center_20210901_models.ListNodesResponse:
        """
        @summary Queries resource nodes.
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_ota_task_with_options(
        self,
        request: appstream_center_20210901_models.ListOtaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListOtaTaskResponse:
        """
        @summary Queries the information about over-the-air (OTA) update tasks.
        
        @param request: ListOtaTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOtaTaskResponse
        """
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
        """
        @summary Queries the information about over-the-air (OTA) update tasks.
        
        @param request: ListOtaTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOtaTaskResponse
        """
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
        """
        @summary Queries the information about over-the-air (OTA) update tasks.
        
        @param request: ListOtaTaskRequest
        @return: ListOtaTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ota_task_with_options(request, runtime)

    async def list_ota_task_async(
        self,
        request: appstream_center_20210901_models.ListOtaTaskRequest,
    ) -> appstream_center_20210901_models.ListOtaTaskResponse:
        """
        @summary Queries the information about over-the-air (OTA) update tasks.
        
        @param request: ListOtaTaskRequest
        @return: ListOtaTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ota_task_with_options_async(request, runtime)

    def list_persistent_app_instances_with_options(
        self,
        request: appstream_center_20210901_models.ListPersistentAppInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListPersistentAppInstancesResponse:
        """
        @summary 查询交付组内持久会话列表
        
        @param request: ListPersistentAppInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPersistentAppInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_persistent_ids):
            query['AppInstancePersistentIds'] = request.app_instance_persistent_ids
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
            action='ListPersistentAppInstances',
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
            appstream_center_20210901_models.ListPersistentAppInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_persistent_app_instances_with_options_async(
        self,
        request: appstream_center_20210901_models.ListPersistentAppInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListPersistentAppInstancesResponse:
        """
        @summary 查询交付组内持久会话列表
        
        @param request: ListPersistentAppInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPersistentAppInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            query['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_persistent_ids):
            query['AppInstancePersistentIds'] = request.app_instance_persistent_ids
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
            action='ListPersistentAppInstances',
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
            appstream_center_20210901_models.ListPersistentAppInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_persistent_app_instances(
        self,
        request: appstream_center_20210901_models.ListPersistentAppInstancesRequest,
    ) -> appstream_center_20210901_models.ListPersistentAppInstancesResponse:
        """
        @summary 查询交付组内持久会话列表
        
        @param request: ListPersistentAppInstancesRequest
        @return: ListPersistentAppInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_persistent_app_instances_with_options(request, runtime)

    async def list_persistent_app_instances_async(
        self,
        request: appstream_center_20210901_models.ListPersistentAppInstancesRequest,
    ) -> appstream_center_20210901_models.ListPersistentAppInstancesResponse:
        """
        @summary 查询交付组内持久会话列表
        
        @param request: ListPersistentAppInstancesRequest
        @return: ListPersistentAppInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_persistent_app_instances_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: appstream_center_20210901_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListRegionsResponse:
        """
        @summary Queries the regions that are supported by App Streaming.
        
        @description >  All supported regions instead of available regions are returned by this operation. For more information, see [Supported regions](https://help.aliyun.com/document_detail/426036.html).
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_source):
            query['BizSource'] = request.biz_source
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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
        request: appstream_center_20210901_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListRegionsResponse:
        """
        @summary Queries the regions that are supported by App Streaming.
        
        @description >  All supported regions instead of available regions are returned by this operation. For more information, see [Supported regions](https://help.aliyun.com/document_detail/426036.html).
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_source):
            query['BizSource'] = request.biz_source
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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

    def list_regions(
        self,
        request: appstream_center_20210901_models.ListRegionsRequest,
    ) -> appstream_center_20210901_models.ListRegionsResponse:
        """
        @summary Queries the regions that are supported by App Streaming.
        
        @description >  All supported regions instead of available regions are returned by this operation. For more information, see [Supported regions](https://help.aliyun.com/document_detail/426036.html).
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: appstream_center_20210901_models.ListRegionsRequest,
    ) -> appstream_center_20210901_models.ListRegionsResponse:
        """
        @summary Queries the regions that are supported by App Streaming.
        
        @description >  All supported regions instead of available regions are returned by this operation. For more information, see [Supported regions](https://help.aliyun.com/document_detail/426036.html).
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_tag_cloud_resources_with_options(
        self,
        request: appstream_center_20210901_models.ListTagCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListTagCloudResourcesResponse:
        """
        @summary Queries the tags added to one or more cloud resources.
        
        @param request: ListTagCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scope):
            body['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagCloudResources',
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
            appstream_center_20210901_models.ListTagCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_cloud_resources_with_options_async(
        self,
        request: appstream_center_20210901_models.ListTagCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListTagCloudResourcesResponse:
        """
        @summary Queries the tags added to one or more cloud resources.
        
        @param request: ListTagCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scope):
            body['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagCloudResources',
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
            appstream_center_20210901_models.ListTagCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_cloud_resources(
        self,
        request: appstream_center_20210901_models.ListTagCloudResourcesRequest,
    ) -> appstream_center_20210901_models.ListTagCloudResourcesResponse:
        """
        @summary Queries the tags added to one or more cloud resources.
        
        @param request: ListTagCloudResourcesRequest
        @return: ListTagCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_cloud_resources_with_options(request, runtime)

    async def list_tag_cloud_resources_async(
        self,
        request: appstream_center_20210901_models.ListTagCloudResourcesRequest,
    ) -> appstream_center_20210901_models.ListTagCloudResourcesResponse:
        """
        @summary Queries the tags added to one or more cloud resources.
        
        @param request: ListTagCloudResourcesRequest
        @return: ListTagCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_cloud_resources_with_options_async(request, runtime)

    def list_tenant_config_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ListTenantConfigResponse:
        """
        @summary Queries the configurations of the administrator account, such as whether the resource expiration reminder feature is enabled.
        
        @param request: ListTenantConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTenantConfigResponse
        """
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
        """
        @summary Queries the configurations of the administrator account, such as whether the resource expiration reminder feature is enabled.
        
        @param request: ListTenantConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTenantConfigResponse
        """
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
        """
        @summary Queries the configurations of the administrator account, such as whether the resource expiration reminder feature is enabled.
        
        @return: ListTenantConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tenant_config_with_options(runtime)

    async def list_tenant_config_async(self) -> appstream_center_20210901_models.ListTenantConfigResponse:
        """
        @summary Queries the configurations of the administrator account, such as whether the resource expiration reminder feature is enabled.
        
        @return: ListTenantConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tenant_config_with_options_async(runtime)

    def log_off_all_sessions_in_app_instance_group_with_options(
        self,
        request: appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupResponse:
        """
        @summary Closes all sessions in a pay-as-you-go delivery group for which a scheduled scaling policy is used.
        
        @description >  This operation can be called only if you use a pay-as-you-go delivery group for which a scheduled scaling policy is used and if you call the operation at a time other than the scheduled time.
        
        @param request: LogOffAllSessionsInAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LogOffAllSessionsInAppInstanceGroupResponse
        """
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
        """
        @summary Closes all sessions in a pay-as-you-go delivery group for which a scheduled scaling policy is used.
        
        @description >  This operation can be called only if you use a pay-as-you-go delivery group for which a scheduled scaling policy is used and if you call the operation at a time other than the scheduled time.
        
        @param request: LogOffAllSessionsInAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LogOffAllSessionsInAppInstanceGroupResponse
        """
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
        """
        @summary Closes all sessions in a pay-as-you-go delivery group for which a scheduled scaling policy is used.
        
        @description >  This operation can be called only if you use a pay-as-you-go delivery group for which a scheduled scaling policy is used and if you call the operation at a time other than the scheduled time.
        
        @param request: LogOffAllSessionsInAppInstanceGroupRequest
        @return: LogOffAllSessionsInAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.log_off_all_sessions_in_app_instance_group_with_options(request, runtime)

    async def log_off_all_sessions_in_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.LogOffAllSessionsInAppInstanceGroupResponse:
        """
        @summary Closes all sessions in a pay-as-you-go delivery group for which a scheduled scaling policy is used.
        
        @description >  This operation can be called only if you use a pay-as-you-go delivery group for which a scheduled scaling policy is used and if you call the operation at a time other than the scheduled time.
        
        @param request: LogOffAllSessionsInAppInstanceGroupRequest
        @return: LogOffAllSessionsInAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.log_off_all_sessions_in_app_instance_group_with_options_async(request, runtime)

    def modify_app_instance_group_attribute_with_options(
        self,
        tmp_req: appstream_center_20210901_models.ModifyAppInstanceGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyAppInstanceGroupAttributeResponse:
        """
        @summary Modifies the general policies of a delivery group, including the number of concurrent sessions and the retention period of disconnected sessions.
        
        @param tmp_req: ModifyAppInstanceGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppInstanceGroupAttributeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.ModifyAppInstanceGroupAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network):
            request.network_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not UtilClient.is_unset(tmp_req.node_pool):
            request.node_pool_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        if not UtilClient.is_unset(tmp_req.security_policy):
            request.security_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.storage_policy):
            request.storage_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage_policy, 'StoragePolicy', 'json')
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
        body = {}
        if not UtilClient.is_unset(request.network_shrink):
            body['Network'] = request.network_shrink
        if not UtilClient.is_unset(request.per_session_per_app):
            body['PerSessionPerApp'] = request.per_session_per_app
        if not UtilClient.is_unset(request.pre_open_app_id):
            body['PreOpenAppId'] = request.pre_open_app_id
        if not UtilClient.is_unset(request.pre_open_mode):
            body['PreOpenMode'] = request.pre_open_mode
        if not UtilClient.is_unset(request.security_policy_shrink):
            body['SecurityPolicy'] = request.security_policy_shrink
        if not UtilClient.is_unset(request.storage_policy_shrink):
            body['StoragePolicy'] = request.storage_policy_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary Modifies the general policies of a delivery group, including the number of concurrent sessions and the retention period of disconnected sessions.
        
        @param tmp_req: ModifyAppInstanceGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppInstanceGroupAttributeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.ModifyAppInstanceGroupAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network):
            request.network_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network, 'Network', 'json')
        if not UtilClient.is_unset(tmp_req.node_pool):
            request.node_pool_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        if not UtilClient.is_unset(tmp_req.security_policy):
            request.security_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.storage_policy):
            request.storage_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage_policy, 'StoragePolicy', 'json')
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
        body = {}
        if not UtilClient.is_unset(request.network_shrink):
            body['Network'] = request.network_shrink
        if not UtilClient.is_unset(request.per_session_per_app):
            body['PerSessionPerApp'] = request.per_session_per_app
        if not UtilClient.is_unset(request.pre_open_app_id):
            body['PreOpenAppId'] = request.pre_open_app_id
        if not UtilClient.is_unset(request.pre_open_mode):
            body['PreOpenMode'] = request.pre_open_mode
        if not UtilClient.is_unset(request.security_policy_shrink):
            body['SecurityPolicy'] = request.security_policy_shrink
        if not UtilClient.is_unset(request.storage_policy_shrink):
            body['StoragePolicy'] = request.storage_policy_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary Modifies the general policies of a delivery group, including the number of concurrent sessions and the retention period of disconnected sessions.
        
        @param request: ModifyAppInstanceGroupAttributeRequest
        @return: ModifyAppInstanceGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_instance_group_attribute_with_options(request, runtime)

    async def modify_app_instance_group_attribute_async(
        self,
        request: appstream_center_20210901_models.ModifyAppInstanceGroupAttributeRequest,
    ) -> appstream_center_20210901_models.ModifyAppInstanceGroupAttributeResponse:
        """
        @summary Modifies the general policies of a delivery group, including the number of concurrent sessions and the retention period of disconnected sessions.
        
        @param request: ModifyAppInstanceGroupAttributeRequest
        @return: ModifyAppInstanceGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_instance_group_attribute_with_options_async(request, runtime)

    def modify_app_policy_with_options(
        self,
        tmp_req: appstream_center_20210901_models.ModifyAppPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyAppPolicyResponse:
        """
        @summary 修改策略信息
        
        @param tmp_req: ModifyAppPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.ModifyAppPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.video_policy):
            request.video_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_policy, 'VideoPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_policy_id):
            query['AppPolicyId'] = request.app_policy_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.video_policy_shrink):
            query['VideoPolicy'] = request.video_policy_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppPolicy',
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
            appstream_center_20210901_models.ModifyAppPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_policy_with_options_async(
        self,
        tmp_req: appstream_center_20210901_models.ModifyAppPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyAppPolicyResponse:
        """
        @summary 修改策略信息
        
        @param tmp_req: ModifyAppPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.ModifyAppPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.video_policy):
            request.video_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_policy, 'VideoPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_policy_id):
            query['AppPolicyId'] = request.app_policy_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.video_policy_shrink):
            query['VideoPolicy'] = request.video_policy_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppPolicy',
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
            appstream_center_20210901_models.ModifyAppPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_policy(
        self,
        request: appstream_center_20210901_models.ModifyAppPolicyRequest,
    ) -> appstream_center_20210901_models.ModifyAppPolicyResponse:
        """
        @summary 修改策略信息
        
        @param request: ModifyAppPolicyRequest
        @return: ModifyAppPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_policy_with_options(request, runtime)

    async def modify_app_policy_async(
        self,
        request: appstream_center_20210901_models.ModifyAppPolicyRequest,
    ) -> appstream_center_20210901_models.ModifyAppPolicyResponse:
        """
        @summary 修改策略信息
        
        @param request: ModifyAppPolicyRequest
        @return: ModifyAppPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_policy_with_options_async(request, runtime)

    def modify_node_pool_amount_with_options(
        self,
        tmp_req: appstream_center_20210901_models.ModifyNodePoolAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyNodePoolAmountResponse:
        """
        @summary Changes the number of nodes in a subscription delivery group.
        
        @param tmp_req: ModifyNodePoolAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodePoolAmountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.ModifyNodePoolAmountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_pool):
            request.node_pool_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.node_pool_shrink):
            body['NodePool'] = request.node_pool_shrink
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNodePoolAmount',
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
            appstream_center_20210901_models.ModifyNodePoolAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_pool_amount_with_options_async(
        self,
        tmp_req: appstream_center_20210901_models.ModifyNodePoolAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyNodePoolAmountResponse:
        """
        @summary Changes the number of nodes in a subscription delivery group.
        
        @param tmp_req: ModifyNodePoolAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodePoolAmountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = appstream_center_20210901_models.ModifyNodePoolAmountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_pool):
            request.node_pool_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_pool, 'NodePool', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.node_pool_shrink):
            body['NodePool'] = request.node_pool_shrink
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNodePoolAmount',
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
            appstream_center_20210901_models.ModifyNodePoolAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_pool_amount(
        self,
        request: appstream_center_20210901_models.ModifyNodePoolAmountRequest,
    ) -> appstream_center_20210901_models.ModifyNodePoolAmountResponse:
        """
        @summary Changes the number of nodes in a subscription delivery group.
        
        @param request: ModifyNodePoolAmountRequest
        @return: ModifyNodePoolAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_node_pool_amount_with_options(request, runtime)

    async def modify_node_pool_amount_async(
        self,
        request: appstream_center_20210901_models.ModifyNodePoolAmountRequest,
    ) -> appstream_center_20210901_models.ModifyNodePoolAmountResponse:
        """
        @summary Changes the number of nodes in a subscription delivery group.
        
        @param request: ModifyNodePoolAmountRequest
        @return: ModifyNodePoolAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_node_pool_amount_with_options_async(request, runtime)

    def modify_node_pool_attribute_with_options(
        self,
        tmp_req: appstream_center_20210901_models.ModifyNodePoolAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyNodePoolAttributeResponse:
        """
        @param tmp_req: ModifyNodePoolAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodePoolAttributeResponse
        """
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
        """
        @param tmp_req: ModifyNodePoolAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodePoolAttributeResponse
        """
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
        """
        @param request: ModifyNodePoolAttributeRequest
        @return: ModifyNodePoolAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_node_pool_attribute_with_options(request, runtime)

    async def modify_node_pool_attribute_async(
        self,
        request: appstream_center_20210901_models.ModifyNodePoolAttributeRequest,
    ) -> appstream_center_20210901_models.ModifyNodePoolAttributeResponse:
        """
        @param request: ModifyNodePoolAttributeRequest
        @return: ModifyNodePoolAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_node_pool_attribute_with_options_async(request, runtime)

    def modify_tenant_config_with_options(
        self,
        request: appstream_center_20210901_models.ModifyTenantConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.ModifyTenantConfigResponse:
        """
        @summary Modifies the configurations of the administrator account, such as whether to enable the resource expiration reminder feature.
        
        @param request: ModifyTenantConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantConfigResponse
        """
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
        """
        @summary Modifies the configurations of the administrator account, such as whether to enable the resource expiration reminder feature.
        
        @param request: ModifyTenantConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantConfigResponse
        """
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
        """
        @summary Modifies the configurations of the administrator account, such as whether to enable the resource expiration reminder feature.
        
        @param request: ModifyTenantConfigRequest
        @return: ModifyTenantConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_config_with_options(request, runtime)

    async def modify_tenant_config_async(
        self,
        request: appstream_center_20210901_models.ModifyTenantConfigRequest,
    ) -> appstream_center_20210901_models.ModifyTenantConfigResponse:
        """
        @summary Modifies the configurations of the administrator account, such as whether to enable the resource expiration reminder feature.
        
        @param request: ModifyTenantConfigRequest
        @return: ModifyTenantConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_config_with_options_async(request, runtime)

    def page_list_app_instance_group_user_with_options(
        self,
        request: appstream_center_20210901_models.PageListAppInstanceGroupUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.PageListAppInstanceGroupUserResponse:
        """
        @summary Queries the assigned users that are added to a delivery group by page.
        
        @param request: PageListAppInstanceGroupUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageListAppInstanceGroupUserResponse
        """
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
        """
        @summary Queries the assigned users that are added to a delivery group by page.
        
        @param request: PageListAppInstanceGroupUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageListAppInstanceGroupUserResponse
        """
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
        """
        @summary Queries the assigned users that are added to a delivery group by page.
        
        @param request: PageListAppInstanceGroupUserRequest
        @return: PageListAppInstanceGroupUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.page_list_app_instance_group_user_with_options(request, runtime)

    async def page_list_app_instance_group_user_async(
        self,
        request: appstream_center_20210901_models.PageListAppInstanceGroupUserRequest,
    ) -> appstream_center_20210901_models.PageListAppInstanceGroupUserResponse:
        """
        @summary Queries the assigned users that are added to a delivery group by page.
        
        @param request: PageListAppInstanceGroupUserRequest
        @return: PageListAppInstanceGroupUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.page_list_app_instance_group_user_with_options_async(request, runtime)

    def renew_app_instance_group_with_options(
        self,
        request: appstream_center_20210901_models.RenewAppInstanceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.RenewAppInstanceGroupResponse:
        """
        @summary Renews a delivery group.
        
        @description Before you call this operation, make sure that you fully understand the [billing methods and prices](https://help.aliyun.com/document_detail/426039.html) of App Streaming.
        
        @param request: RenewAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewAppInstanceGroupResponse
        """
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
        """
        @summary Renews a delivery group.
        
        @description Before you call this operation, make sure that you fully understand the [billing methods and prices](https://help.aliyun.com/document_detail/426039.html) of App Streaming.
        
        @param request: RenewAppInstanceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewAppInstanceGroupResponse
        """
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
        """
        @summary Renews a delivery group.
        
        @description Before you call this operation, make sure that you fully understand the [billing methods and prices](https://help.aliyun.com/document_detail/426039.html) of App Streaming.
        
        @param request: RenewAppInstanceGroupRequest
        @return: RenewAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_app_instance_group_with_options(request, runtime)

    async def renew_app_instance_group_async(
        self,
        request: appstream_center_20210901_models.RenewAppInstanceGroupRequest,
    ) -> appstream_center_20210901_models.RenewAppInstanceGroupResponse:
        """
        @summary Renews a delivery group.
        
        @description Before you call this operation, make sure that you fully understand the [billing methods and prices](https://help.aliyun.com/document_detail/426039.html) of App Streaming.
        
        @param request: RenewAppInstanceGroupRequest
        @return: RenewAppInstanceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_app_instance_group_with_options_async(request, runtime)

    def tag_cloud_resources_with_options(
        self,
        request: appstream_center_20210901_models.TagCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.TagCloudResourcesResponse:
        """
        @summary 为云资源创建并绑定标签
        
        @param request: TagCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagCloudResources',
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
            appstream_center_20210901_models.TagCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_cloud_resources_with_options_async(
        self,
        request: appstream_center_20210901_models.TagCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.TagCloudResourcesResponse:
        """
        @summary 为云资源创建并绑定标签
        
        @param request: TagCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagCloudResources',
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
            appstream_center_20210901_models.TagCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_cloud_resources(
        self,
        request: appstream_center_20210901_models.TagCloudResourcesRequest,
    ) -> appstream_center_20210901_models.TagCloudResourcesResponse:
        """
        @summary 为云资源创建并绑定标签
        
        @param request: TagCloudResourcesRequest
        @return: TagCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_cloud_resources_with_options(request, runtime)

    async def tag_cloud_resources_async(
        self,
        request: appstream_center_20210901_models.TagCloudResourcesRequest,
    ) -> appstream_center_20210901_models.TagCloudResourcesResponse:
        """
        @summary 为云资源创建并绑定标签
        
        @param request: TagCloudResourcesRequest
        @return: TagCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_cloud_resources_with_options_async(request, runtime)

    def unbind_with_options(
        self,
        request: appstream_center_20210901_models.UnbindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.UnbindResponse:
        """
        @summary Unbinds a user and a session.
        
        @param request: UnbindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Unbind',
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
            appstream_center_20210901_models.UnbindResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_with_options_async(
        self,
        request: appstream_center_20210901_models.UnbindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.UnbindResponse:
        """
        @summary Unbinds a user and a session.
        
        @param request: UnbindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Unbind',
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
            appstream_center_20210901_models.UnbindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind(
        self,
        request: appstream_center_20210901_models.UnbindRequest,
    ) -> appstream_center_20210901_models.UnbindResponse:
        """
        @summary Unbinds a user and a session.
        
        @param request: UnbindRequest
        @return: UnbindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_with_options(request, runtime)

    async def unbind_async(
        self,
        request: appstream_center_20210901_models.UnbindRequest,
    ) -> appstream_center_20210901_models.UnbindResponse:
        """
        @summary Unbinds a user and a session.
        
        @param request: UnbindRequest
        @return: UnbindResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_with_options_async(request, runtime)

    def untag_cloud_resources_with_options(
        self,
        request: appstream_center_20210901_models.UntagCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.UntagCloudResourcesResponse:
        """
        @summary Removes tags from cloud resources.
        
        @param request: UntagCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            body['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagCloudResources',
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
            appstream_center_20210901_models.UntagCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_cloud_resources_with_options_async(
        self,
        request: appstream_center_20210901_models.UntagCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.UntagCloudResourcesResponse:
        """
        @summary Removes tags from cloud resources.
        
        @param request: UntagCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            body['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagCloudResources',
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
            appstream_center_20210901_models.UntagCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_cloud_resources(
        self,
        request: appstream_center_20210901_models.UntagCloudResourcesRequest,
    ) -> appstream_center_20210901_models.UntagCloudResourcesResponse:
        """
        @summary Removes tags from cloud resources.
        
        @param request: UntagCloudResourcesRequest
        @return: UntagCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_cloud_resources_with_options(request, runtime)

    async def untag_cloud_resources_async(
        self,
        request: appstream_center_20210901_models.UntagCloudResourcesRequest,
    ) -> appstream_center_20210901_models.UntagCloudResourcesResponse:
        """
        @summary Removes tags from cloud resources.
        
        @param request: UntagCloudResourcesRequest
        @return: UntagCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_cloud_resources_with_options_async(request, runtime)

    def update_app_instance_group_image_with_options(
        self,
        request: appstream_center_20210901_models.UpdateAppInstanceGroupImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210901_models.UpdateAppInstanceGroupImageResponse:
        """
        @summary Updates the image of a delivery group.
        
        @description *\
        *Warning** After the image is updated, the end user session accessing the cloud application will be disconnected. Exercise caution to avoid end user data loss.
        >  After the image of the delivery group is updated, the change takes effect on the terminal in approximately 2 minutes.
        
        @param request: UpdateAppInstanceGroupImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppInstanceGroupImageResponse
        """
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
        """
        @summary Updates the image of a delivery group.
        
        @description *\
        *Warning** After the image is updated, the end user session accessing the cloud application will be disconnected. Exercise caution to avoid end user data loss.
        >  After the image of the delivery group is updated, the change takes effect on the terminal in approximately 2 minutes.
        
        @param request: UpdateAppInstanceGroupImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppInstanceGroupImageResponse
        """
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
        """
        @summary Updates the image of a delivery group.
        
        @description *\
        *Warning** After the image is updated, the end user session accessing the cloud application will be disconnected. Exercise caution to avoid end user data loss.
        >  After the image of the delivery group is updated, the change takes effect on the terminal in approximately 2 minutes.
        
        @param request: UpdateAppInstanceGroupImageRequest
        @return: UpdateAppInstanceGroupImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_app_instance_group_image_with_options(request, runtime)

    async def update_app_instance_group_image_async(
        self,
        request: appstream_center_20210901_models.UpdateAppInstanceGroupImageRequest,
    ) -> appstream_center_20210901_models.UpdateAppInstanceGroupImageResponse:
        """
        @summary Updates the image of a delivery group.
        
        @description *\
        *Warning** After the image is updated, the end user session accessing the cloud application will be disconnected. Exercise caution to avoid end user data loss.
        >  After the image of the delivery group is updated, the change takes effect on the terminal in approximately 2 minutes.
        
        @param request: UpdateAppInstanceGroupImageRequest
        @return: UpdateAppInstanceGroupImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_app_instance_group_image_with_options_async(request, runtime)
