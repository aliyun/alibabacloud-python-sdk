# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sophonsoar20250903 import models as main_models
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
        self._endpoint = self.get_endpoint('sophonsoar', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_component_asset_with_options(
        self,
        request: main_models.CreateComponentAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComponentAssetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_asset_name):
            body['ComponentAssetName'] = request.component_asset_name
        body_flat = {}
        if not DaraCore.is_null(request.component_asset_values):
            body_flat['ComponentAssetValues'] = request.component_asset_values
        if not DaraCore.is_null(request.component_name):
            body['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComponentAsset',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComponentAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_component_asset_with_options_async(
        self,
        request: main_models.CreateComponentAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComponentAssetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_asset_name):
            body['ComponentAssetName'] = request.component_asset_name
        body_flat = {}
        if not DaraCore.is_null(request.component_asset_values):
            body_flat['ComponentAssetValues'] = request.component_asset_values
        if not DaraCore.is_null(request.component_name):
            body['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComponentAsset',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComponentAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_component_asset(
        self,
        request: main_models.CreateComponentAssetRequest,
    ) -> main_models.CreateComponentAssetResponse:
        runtime = RuntimeOptions()
        return self.create_component_asset_with_options(request, runtime)

    async def create_component_asset_async(
        self,
        request: main_models.CreateComponentAssetRequest,
    ) -> main_models.CreateComponentAssetResponse:
        runtime = RuntimeOptions()
        return await self.create_component_asset_with_options_async(request, runtime)

    def create_playbook_with_options(
        self,
        request: main_models.CreatePlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_description):
            body['PlaybookDescription'] = request.playbook_description
        body_flat = {}
        if not DaraCore.is_null(request.playbook_input_configs):
            body_flat['PlaybookInputConfigs'] = request.playbook_input_configs
        if not DaraCore.is_null(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not DaraCore.is_null(request.playbook_output_configs):
            body_flat['PlaybookOutputConfigs'] = request.playbook_output_configs
        if not DaraCore.is_null(request.playbook_param_type):
            body['PlaybookParamType'] = request.playbook_param_type
        if not DaraCore.is_null(request.playbook_task_flow):
            body['PlaybookTaskFlow'] = request.playbook_task_flow
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.src_playbook_uuid):
            body['SrcPlaybookUuid'] = request.src_playbook_uuid
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePlaybook',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_playbook_with_options_async(
        self,
        request: main_models.CreatePlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_description):
            body['PlaybookDescription'] = request.playbook_description
        body_flat = {}
        if not DaraCore.is_null(request.playbook_input_configs):
            body_flat['PlaybookInputConfigs'] = request.playbook_input_configs
        if not DaraCore.is_null(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not DaraCore.is_null(request.playbook_output_configs):
            body_flat['PlaybookOutputConfigs'] = request.playbook_output_configs
        if not DaraCore.is_null(request.playbook_param_type):
            body['PlaybookParamType'] = request.playbook_param_type
        if not DaraCore.is_null(request.playbook_task_flow):
            body['PlaybookTaskFlow'] = request.playbook_task_flow
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.src_playbook_uuid):
            body['SrcPlaybookUuid'] = request.src_playbook_uuid
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePlaybook',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_playbook(
        self,
        request: main_models.CreatePlaybookRequest,
    ) -> main_models.CreatePlaybookResponse:
        runtime = RuntimeOptions()
        return self.create_playbook_with_options(request, runtime)

    async def create_playbook_async(
        self,
        request: main_models.CreatePlaybookRequest,
    ) -> main_models.CreatePlaybookResponse:
        runtime = RuntimeOptions()
        return await self.create_playbook_with_options_async(request, runtime)

    def delete_component_asset_with_options(
        self,
        request: main_models.DeleteComponentAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComponentAssetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponentAsset',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComponentAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_component_asset_with_options_async(
        self,
        request: main_models.DeleteComponentAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComponentAssetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponentAsset',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComponentAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_component_asset(
        self,
        request: main_models.DeleteComponentAssetRequest,
    ) -> main_models.DeleteComponentAssetResponse:
        runtime = RuntimeOptions()
        return self.delete_component_asset_with_options(request, runtime)

    async def delete_component_asset_async(
        self,
        request: main_models.DeleteComponentAssetRequest,
    ) -> main_models.DeleteComponentAssetResponse:
        runtime = RuntimeOptions()
        return await self.delete_component_asset_with_options_async(request, runtime)

    def delete_playbook_with_options(
        self,
        request: main_models.DeletePlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePlaybook',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_playbook_with_options_async(
        self,
        request: main_models.DeletePlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePlaybook',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_playbook(
        self,
        request: main_models.DeletePlaybookRequest,
    ) -> main_models.DeletePlaybookResponse:
        runtime = RuntimeOptions()
        return self.delete_playbook_with_options(request, runtime)

    async def delete_playbook_async(
        self,
        request: main_models.DeletePlaybookRequest,
    ) -> main_models.DeletePlaybookResponse:
        runtime = RuntimeOptions()
        return await self.delete_playbook_with_options_async(request, runtime)

    def execute_component_with_options(
        self,
        request: main_models.ExecuteComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteComponentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_action_name):
            body['ComponentActionName'] = request.component_action_name
        if not DaraCore.is_null(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        if not DaraCore.is_null(request.component_input):
            body['ComponentInput'] = request.component_input
        if not DaraCore.is_null(request.component_name):
            body['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.play_book_node_name):
            body['PlayBookNodeName'] = request.play_book_node_name
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteComponent',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_component_with_options_async(
        self,
        request: main_models.ExecuteComponentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteComponentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_action_name):
            body['ComponentActionName'] = request.component_action_name
        if not DaraCore.is_null(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        if not DaraCore.is_null(request.component_input):
            body['ComponentInput'] = request.component_input
        if not DaraCore.is_null(request.component_name):
            body['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.play_book_node_name):
            body['PlayBookNodeName'] = request.play_book_node_name
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteComponent',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_component(
        self,
        request: main_models.ExecuteComponentRequest,
    ) -> main_models.ExecuteComponentResponse:
        runtime = RuntimeOptions()
        return self.execute_component_with_options(request, runtime)

    async def execute_component_async(
        self,
        request: main_models.ExecuteComponentRequest,
    ) -> main_models.ExecuteComponentResponse:
        runtime = RuntimeOptions()
        return await self.execute_component_with_options_async(request, runtime)

    def get_playbook_with_options(
        self,
        request: main_models.GetPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.playbook_version):
            body['PlaybookVersion'] = request.playbook_version
        if not DaraCore.is_null(request.playbook_version_type):
            body['PlaybookVersionType'] = request.playbook_version_type
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPlaybook',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_playbook_with_options_async(
        self,
        request: main_models.GetPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.playbook_version):
            body['PlaybookVersion'] = request.playbook_version
        if not DaraCore.is_null(request.playbook_version_type):
            body['PlaybookVersionType'] = request.playbook_version_type
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPlaybook',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_playbook(
        self,
        request: main_models.GetPlaybookRequest,
    ) -> main_models.GetPlaybookResponse:
        runtime = RuntimeOptions()
        return self.get_playbook_with_options(request, runtime)

    async def get_playbook_async(
        self,
        request: main_models.GetPlaybookRequest,
    ) -> main_models.GetPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.get_playbook_with_options_async(request, runtime)

    def list_component_assets_with_options(
        self,
        request: main_models.ListComponentAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentAssetsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        if not DaraCore.is_null(request.component_name):
            body['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListComponentAssets',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_component_assets_with_options_async(
        self,
        request: main_models.ListComponentAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentAssetsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        if not DaraCore.is_null(request.component_name):
            body['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListComponentAssets',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_component_assets(
        self,
        request: main_models.ListComponentAssetsRequest,
    ) -> main_models.ListComponentAssetsResponse:
        runtime = RuntimeOptions()
        return self.list_component_assets_with_options(request, runtime)

    async def list_component_assets_async(
        self,
        request: main_models.ListComponentAssetsRequest,
    ) -> main_models.ListComponentAssetsResponse:
        runtime = RuntimeOptions()
        return await self.list_component_assets_with_options_async(request, runtime)

    def list_components_with_options(
        self,
        request: main_models.ListComponentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_name):
            body['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListComponents',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: main_models.ListComponentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_name):
            body['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListComponents',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(
        self,
        request: main_models.ListComponentsRequest,
    ) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        return self.list_components_with_options(request, runtime)

    async def list_components_async(
        self,
        request: main_models.ListComponentsRequest,
    ) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        return await self.list_components_with_options_async(request, runtime)

    def list_playbooks_with_options(
        self,
        tmp_req: main_models.ListPlaybooksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPlaybooksResponse:
        tmp_req.validate()
        request = main_models.ListPlaybooksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.playbook_param_types):
            request.playbook_param_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.playbook_param_types, 'PlaybookParamTypes', 'simple')
        if not DaraCore.is_null(tmp_req.playbook_uuids):
            request.playbook_uuids_shrink = Utils.array_to_string_with_specified_style(tmp_req.playbook_uuids, 'PlaybookUuids', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.playbook_execution_end_time):
            body['PlaybookExecutionEndTime'] = request.playbook_execution_end_time
        if not DaraCore.is_null(request.playbook_execution_start_time):
            body['PlaybookExecutionStartTime'] = request.playbook_execution_start_time
        if not DaraCore.is_null(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not DaraCore.is_null(request.playbook_param_types_shrink):
            body['PlaybookParamTypes'] = request.playbook_param_types_shrink
        if not DaraCore.is_null(request.playbook_status):
            body['PlaybookStatus'] = request.playbook_status
        if not DaraCore.is_null(request.playbook_type):
            body['PlaybookType'] = request.playbook_type
        if not DaraCore.is_null(request.playbook_uuids_shrink):
            body['PlaybookUuids'] = request.playbook_uuids_shrink
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPlaybooks',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPlaybooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_playbooks_with_options_async(
        self,
        tmp_req: main_models.ListPlaybooksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPlaybooksResponse:
        tmp_req.validate()
        request = main_models.ListPlaybooksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.playbook_param_types):
            request.playbook_param_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.playbook_param_types, 'PlaybookParamTypes', 'simple')
        if not DaraCore.is_null(tmp_req.playbook_uuids):
            request.playbook_uuids_shrink = Utils.array_to_string_with_specified_style(tmp_req.playbook_uuids, 'PlaybookUuids', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.playbook_execution_end_time):
            body['PlaybookExecutionEndTime'] = request.playbook_execution_end_time
        if not DaraCore.is_null(request.playbook_execution_start_time):
            body['PlaybookExecutionStartTime'] = request.playbook_execution_start_time
        if not DaraCore.is_null(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not DaraCore.is_null(request.playbook_param_types_shrink):
            body['PlaybookParamTypes'] = request.playbook_param_types_shrink
        if not DaraCore.is_null(request.playbook_status):
            body['PlaybookStatus'] = request.playbook_status
        if not DaraCore.is_null(request.playbook_type):
            body['PlaybookType'] = request.playbook_type
        if not DaraCore.is_null(request.playbook_uuids_shrink):
            body['PlaybookUuids'] = request.playbook_uuids_shrink
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPlaybooks',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPlaybooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_playbooks(
        self,
        request: main_models.ListPlaybooksRequest,
    ) -> main_models.ListPlaybooksResponse:
        runtime = RuntimeOptions()
        return self.list_playbooks_with_options(request, runtime)

    async def list_playbooks_async(
        self,
        request: main_models.ListPlaybooksRequest,
    ) -> main_models.ListPlaybooksResponse:
        runtime = RuntimeOptions()
        return await self.list_playbooks_with_options_async(request, runtime)

    def update_component_asset_with_options(
        self,
        request: main_models.UpdateComponentAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComponentAssetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_asset_name):
            body['ComponentAssetName'] = request.component_asset_name
        if not DaraCore.is_null(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        body_flat = {}
        if not DaraCore.is_null(request.component_asset_values):
            body_flat['ComponentAssetValues'] = request.component_asset_values
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComponentAsset',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComponentAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_component_asset_with_options_async(
        self,
        request: main_models.UpdateComponentAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComponentAssetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_asset_name):
            body['ComponentAssetName'] = request.component_asset_name
        if not DaraCore.is_null(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        body_flat = {}
        if not DaraCore.is_null(request.component_asset_values):
            body_flat['ComponentAssetValues'] = request.component_asset_values
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComponentAsset',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComponentAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_component_asset(
        self,
        request: main_models.UpdateComponentAssetRequest,
    ) -> main_models.UpdateComponentAssetResponse:
        runtime = RuntimeOptions()
        return self.update_component_asset_with_options(request, runtime)

    async def update_component_asset_async(
        self,
        request: main_models.UpdateComponentAssetRequest,
    ) -> main_models.UpdateComponentAssetResponse:
        runtime = RuntimeOptions()
        return await self.update_component_asset_with_options_async(request, runtime)

    def update_playbook_with_options(
        self,
        tmp_req: main_models.UpdatePlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePlaybookResponse:
        tmp_req.validate()
        request = main_models.UpdatePlaybookShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.playbook_input_configs):
            request.playbook_input_configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.playbook_input_configs, 'PlaybookInputConfigs', 'json')
        if not DaraCore.is_null(tmp_req.playbook_output_configs):
            request.playbook_output_configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.playbook_output_configs, 'PlaybookOutputConfigs', 'json')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_description):
            body['PlaybookDescription'] = request.playbook_description
        if not DaraCore.is_null(request.playbook_input_configs_shrink):
            body['PlaybookInputConfigs'] = request.playbook_input_configs_shrink
        if not DaraCore.is_null(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not DaraCore.is_null(request.playbook_output_configs_shrink):
            body['PlaybookOutputConfigs'] = request.playbook_output_configs_shrink
        if not DaraCore.is_null(request.playbook_param_type):
            body['PlaybookParamType'] = request.playbook_param_type
        if not DaraCore.is_null(request.playbook_task_flow):
            body['PlaybookTaskFlow'] = request.playbook_task_flow
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePlaybook',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_playbook_with_options_async(
        self,
        tmp_req: main_models.UpdatePlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePlaybookResponse:
        tmp_req.validate()
        request = main_models.UpdatePlaybookShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.playbook_input_configs):
            request.playbook_input_configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.playbook_input_configs, 'PlaybookInputConfigs', 'json')
        if not DaraCore.is_null(tmp_req.playbook_output_configs):
            request.playbook_output_configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.playbook_output_configs, 'PlaybookOutputConfigs', 'json')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_description):
            body['PlaybookDescription'] = request.playbook_description
        if not DaraCore.is_null(request.playbook_input_configs_shrink):
            body['PlaybookInputConfigs'] = request.playbook_input_configs_shrink
        if not DaraCore.is_null(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not DaraCore.is_null(request.playbook_output_configs_shrink):
            body['PlaybookOutputConfigs'] = request.playbook_output_configs_shrink
        if not DaraCore.is_null(request.playbook_param_type):
            body['PlaybookParamType'] = request.playbook_param_type
        if not DaraCore.is_null(request.playbook_task_flow):
            body['PlaybookTaskFlow'] = request.playbook_task_flow
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePlaybook',
            version = '2025-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_playbook(
        self,
        request: main_models.UpdatePlaybookRequest,
    ) -> main_models.UpdatePlaybookResponse:
        runtime = RuntimeOptions()
        return self.update_playbook_with_options(request, runtime)

    async def update_playbook_async(
        self,
        request: main_models.UpdatePlaybookRequest,
    ) -> main_models.UpdatePlaybookResponse:
        runtime = RuntimeOptions()
        return await self.update_playbook_with_options_async(request, runtime)
