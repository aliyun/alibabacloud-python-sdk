# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ecdbiz20240929 import models as main_models
from alibabacloud_gateway_pop.client import Client as GatewayClientClient
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
        self._product_id = 'EcdBiz'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ecdbiz', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def active_rights_with_options(
        self,
        request: main_models.ActiveRightsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveRightsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not DaraCore.is_null(request.desktop_type):
            query['DesktopType'] = request.desktop_type
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.root_disk_size):
            query['RootDiskSize'] = request.root_disk_size
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not DaraCore.is_null(request.wyid_list):
            query['WyidList'] = request.wyid_list
        body = {}
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.custom_image_id):
            body['CustomImageId'] = request.custom_image_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.hibernate):
            body['Hibernate'] = request.hibernate
        if not DaraCore.is_null(request.office_site_id):
            body['OfficeSiteId'] = request.office_site_id
        body_flat = {}
        if not DaraCore.is_null(request.rights_assigned_user):
            body_flat['RightsAssignedUser'] = request.rights_assigned_user
        if not DaraCore.is_null(request.rights_gpu_spec):
            body['RightsGpuSpec'] = request.rights_gpu_spec
        if not DaraCore.is_null(request.rights_ids):
            body_flat['RightsIds'] = request.rights_ids
        if not DaraCore.is_null(request.rights_resource_area):
            body['RightsResourceArea'] = request.rights_resource_area
        if not DaraCore.is_null(request.rights_resource_image_os):
            body['RightsResourceImageOs'] = request.rights_resource_image_os
        if not DaraCore.is_null(request.rights_resource_region):
            body['RightsResourceRegion'] = request.rights_resource_region
        if not DaraCore.is_null(request.rights_resource_type):
            body['RightsResourceType'] = request.rights_resource_type
        if not DaraCore.is_null(request.rights_spec):
            body['RightsSpec'] = request.rights_spec
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActiveRights',
            version = '2024-09-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveRightsResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_rights_with_options_async(
        self,
        request: main_models.ActiveRightsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveRightsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not DaraCore.is_null(request.desktop_type):
            query['DesktopType'] = request.desktop_type
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.root_disk_size):
            query['RootDiskSize'] = request.root_disk_size
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not DaraCore.is_null(request.wyid_list):
            query['WyidList'] = request.wyid_list
        body = {}
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.custom_image_id):
            body['CustomImageId'] = request.custom_image_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.hibernate):
            body['Hibernate'] = request.hibernate
        if not DaraCore.is_null(request.office_site_id):
            body['OfficeSiteId'] = request.office_site_id
        body_flat = {}
        if not DaraCore.is_null(request.rights_assigned_user):
            body_flat['RightsAssignedUser'] = request.rights_assigned_user
        if not DaraCore.is_null(request.rights_gpu_spec):
            body['RightsGpuSpec'] = request.rights_gpu_spec
        if not DaraCore.is_null(request.rights_ids):
            body_flat['RightsIds'] = request.rights_ids
        if not DaraCore.is_null(request.rights_resource_area):
            body['RightsResourceArea'] = request.rights_resource_area
        if not DaraCore.is_null(request.rights_resource_image_os):
            body['RightsResourceImageOs'] = request.rights_resource_image_os
        if not DaraCore.is_null(request.rights_resource_region):
            body['RightsResourceRegion'] = request.rights_resource_region
        if not DaraCore.is_null(request.rights_resource_type):
            body['RightsResourceType'] = request.rights_resource_type
        if not DaraCore.is_null(request.rights_spec):
            body['RightsSpec'] = request.rights_spec
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActiveRights',
            version = '2024-09-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveRightsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_rights(
        self,
        request: main_models.ActiveRightsRequest,
    ) -> main_models.ActiveRightsResponse:
        runtime = RuntimeOptions()
        return self.active_rights_with_options(request, runtime)

    async def active_rights_async(
        self,
        request: main_models.ActiveRightsRequest,
    ) -> main_models.ActiveRightsResponse:
        runtime = RuntimeOptions()
        return await self.active_rights_with_options_async(request, runtime)

    def list_rights_with_options(
        self,
        request: main_models.ListRightsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRightsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_scene_code):
            query['BusinessSceneCode'] = request.business_scene_code
        if not DaraCore.is_null(request.rights_ids):
            query['RightsIds'] = request.rights_ids
        body = {}
        if not DaraCore.is_null(request.ai_desktop):
            body['AiDesktop'] = request.ai_desktop
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.order_type):
            body['OrderType'] = request.order_type
        if not DaraCore.is_null(request.overseas):
            body['Overseas'] = request.overseas
        if not DaraCore.is_null(request.rights_active_status):
            body['RightsActiveStatus'] = request.rights_active_status
        if not DaraCore.is_null(request.rights_assigned_user):
            body['RightsAssignedUser'] = request.rights_assigned_user
        if not DaraCore.is_null(request.rights_period):
            body['RightsPeriod'] = request.rights_period
        if not DaraCore.is_null(request.rights_resource_id):
            body['RightsResourceId'] = request.rights_resource_id
        if not DaraCore.is_null(request.rights_resource_type):
            body['RightsResourceType'] = request.rights_resource_type
        body_flat = {}
        if not DaraCore.is_null(request.rights_resource_types):
            body_flat['RightsResourceTypes'] = request.rights_resource_types
        if not DaraCore.is_null(request.rights_spec):
            body['RightsSpec'] = request.rights_spec
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRights',
            version = '2024-09-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRightsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rights_with_options_async(
        self,
        request: main_models.ListRightsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRightsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_scene_code):
            query['BusinessSceneCode'] = request.business_scene_code
        if not DaraCore.is_null(request.rights_ids):
            query['RightsIds'] = request.rights_ids
        body = {}
        if not DaraCore.is_null(request.ai_desktop):
            body['AiDesktop'] = request.ai_desktop
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.order_type):
            body['OrderType'] = request.order_type
        if not DaraCore.is_null(request.overseas):
            body['Overseas'] = request.overseas
        if not DaraCore.is_null(request.rights_active_status):
            body['RightsActiveStatus'] = request.rights_active_status
        if not DaraCore.is_null(request.rights_assigned_user):
            body['RightsAssignedUser'] = request.rights_assigned_user
        if not DaraCore.is_null(request.rights_period):
            body['RightsPeriod'] = request.rights_period
        if not DaraCore.is_null(request.rights_resource_id):
            body['RightsResourceId'] = request.rights_resource_id
        if not DaraCore.is_null(request.rights_resource_type):
            body['RightsResourceType'] = request.rights_resource_type
        body_flat = {}
        if not DaraCore.is_null(request.rights_resource_types):
            body_flat['RightsResourceTypes'] = request.rights_resource_types
        if not DaraCore.is_null(request.rights_spec):
            body['RightsSpec'] = request.rights_spec
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRights',
            version = '2024-09-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRightsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rights(
        self,
        request: main_models.ListRightsRequest,
    ) -> main_models.ListRightsResponse:
        runtime = RuntimeOptions()
        return self.list_rights_with_options(request, runtime)

    async def list_rights_async(
        self,
        request: main_models.ListRightsRequest,
    ) -> main_models.ListRightsResponse:
        runtime = RuntimeOptions()
        return await self.list_rights_with_options_async(request, runtime)
