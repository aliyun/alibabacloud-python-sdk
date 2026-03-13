# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sophonsoar20220728 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
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

    def compare_playbooks_with_options(
        self,
        request: main_models.ComparePlaybooksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ComparePlaybooksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_playbook_release_id):
            query['NewPlaybookReleaseId'] = request.new_playbook_release_id
        if not DaraCore.is_null(request.old_playbook_release_id):
            query['OldPlaybookReleaseId'] = request.old_playbook_release_id
        if not DaraCore.is_null(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ComparePlaybooks',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ComparePlaybooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_playbooks_with_options_async(
        self,
        request: main_models.ComparePlaybooksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ComparePlaybooksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_playbook_release_id):
            query['NewPlaybookReleaseId'] = request.new_playbook_release_id
        if not DaraCore.is_null(request.old_playbook_release_id):
            query['OldPlaybookReleaseId'] = request.old_playbook_release_id
        if not DaraCore.is_null(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ComparePlaybooks',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ComparePlaybooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_playbooks(
        self,
        request: main_models.ComparePlaybooksRequest,
    ) -> main_models.ComparePlaybooksResponse:
        runtime = RuntimeOptions()
        return self.compare_playbooks_with_options(request, runtime)

    async def compare_playbooks_async(
        self,
        request: main_models.ComparePlaybooksRequest,
    ) -> main_models.ComparePlaybooksResponse:
        runtime = RuntimeOptions()
        return await self.compare_playbooks_with_options_async(request, runtime)

    def convert_playbook_with_options(
        self,
        request: main_models.ConvertPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertPlaybookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            query['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        body = {}
        if not DaraCore.is_null(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConvertPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_playbook_with_options_async(
        self,
        request: main_models.ConvertPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertPlaybookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            query['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        body = {}
        if not DaraCore.is_null(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConvertPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_playbook(
        self,
        request: main_models.ConvertPlaybookRequest,
    ) -> main_models.ConvertPlaybookResponse:
        runtime = RuntimeOptions()
        return self.convert_playbook_with_options(request, runtime)

    async def convert_playbook_async(
        self,
        request: main_models.ConvertPlaybookRequest,
    ) -> main_models.ConvertPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.convert_playbook_with_options_async(request, runtime)

    def copy_playbook_with_options(
        self,
        request: main_models.CopyPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyPlaybookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            query['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.release_version):
            body['ReleaseVersion'] = request.release_version
        if not DaraCore.is_null(request.source_playbook_uuid):
            body['SourcePlaybookUuid'] = request.source_playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CopyPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_playbook_with_options_async(
        self,
        request: main_models.CopyPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyPlaybookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            query['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.release_version):
            body['ReleaseVersion'] = request.release_version
        if not DaraCore.is_null(request.source_playbook_uuid):
            body['SourcePlaybookUuid'] = request.source_playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CopyPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_playbook(
        self,
        request: main_models.CopyPlaybookRequest,
    ) -> main_models.CopyPlaybookResponse:
        runtime = RuntimeOptions()
        return self.copy_playbook_with_options(request, runtime)

    async def copy_playbook_async(
        self,
        request: main_models.CopyPlaybookRequest,
    ) -> main_models.CopyPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.copy_playbook_with_options_async(request, runtime)

    def create_playbook_with_options(
        self,
        request: main_models.CreatePlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.input_params):
            body['InputParams'] = request.input_params
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.output_params):
            body['OutputParams'] = request.output_params
        if not DaraCore.is_null(request.taskflow_type):
            body['TaskflowType'] = request.taskflow_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePlaybook',
            version = '2022-07-28',
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
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.input_params):
            body['InputParams'] = request.input_params
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.output_params):
            body['OutputParams'] = request.output_params
        if not DaraCore.is_null(request.taskflow_type):
            body['TaskflowType'] = request.taskflow_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePlaybook',
            version = '2022-07-28',
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

    def debug_playbook_with_options(
        self,
        request: main_models.DebugPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DebugPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.record):
            body['Record'] = request.record
        if not DaraCore.is_null(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DebugPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_playbook_with_options_async(
        self,
        request: main_models.DebugPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DebugPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.record):
            body['Record'] = request.record
        if not DaraCore.is_null(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DebugPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_playbook(
        self,
        request: main_models.DebugPlaybookRequest,
    ) -> main_models.DebugPlaybookResponse:
        runtime = RuntimeOptions()
        return self.debug_playbook_with_options(request, runtime)

    async def debug_playbook_async(
        self,
        request: main_models.DebugPlaybookRequest,
    ) -> main_models.DebugPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.debug_playbook_with_options_async(request, runtime)

    def delete_component_asset_with_options(
        self,
        request: main_models.DeleteComponentAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComponentAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponentAsset',
            version = '2022-07-28',
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
        query = {}
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponentAsset',
            version = '2022-07-28',
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
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePlaybook',
            version = '2022-07-28',
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
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePlaybook',
            version = '2022-07-28',
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

    def describe_component_asset_form_with_options(
        self,
        request: main_models.DescribeComponentAssetFormRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentAssetFormResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentAssetForm',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentAssetFormResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_asset_form_with_options_async(
        self,
        request: main_models.DescribeComponentAssetFormRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentAssetFormResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentAssetForm',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentAssetFormResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component_asset_form(
        self,
        request: main_models.DescribeComponentAssetFormRequest,
    ) -> main_models.DescribeComponentAssetFormResponse:
        runtime = RuntimeOptions()
        return self.describe_component_asset_form_with_options(request, runtime)

    async def describe_component_asset_form_async(
        self,
        request: main_models.DescribeComponentAssetFormRequest,
    ) -> main_models.DescribeComponentAssetFormResponse:
        runtime = RuntimeOptions()
        return await self.describe_component_asset_form_with_options_async(request, runtime)

    def describe_component_assets_with_options(
        self,
        request: main_models.DescribeComponentAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentAssetsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentAssets',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_assets_with_options_async(
        self,
        request: main_models.DescribeComponentAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentAssetsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentAssets',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component_assets(
        self,
        request: main_models.DescribeComponentAssetsRequest,
    ) -> main_models.DescribeComponentAssetsResponse:
        runtime = RuntimeOptions()
        return self.describe_component_assets_with_options(request, runtime)

    async def describe_component_assets_async(
        self,
        request: main_models.DescribeComponentAssetsRequest,
    ) -> main_models.DescribeComponentAssetsResponse:
        runtime = RuntimeOptions()
        return await self.describe_component_assets_with_options_async(request, runtime)

    def describe_component_list_with_options(
        self,
        request: main_models.DescribeComponentListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentList',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_list_with_options_async(
        self,
        request: main_models.DescribeComponentListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentList',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component_list(
        self,
        request: main_models.DescribeComponentListRequest,
    ) -> main_models.DescribeComponentListResponse:
        runtime = RuntimeOptions()
        return self.describe_component_list_with_options(request, runtime)

    async def describe_component_list_async(
        self,
        request: main_models.DescribeComponentListRequest,
    ) -> main_models.DescribeComponentListResponse:
        runtime = RuntimeOptions()
        return await self.describe_component_list_with_options_async(request, runtime)

    def describe_component_playbook_with_options(
        self,
        request: main_models.DescribeComponentPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentPlaybookResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_playbook_with_options_async(
        self,
        request: main_models.DescribeComponentPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentPlaybookResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component_playbook(
        self,
        request: main_models.DescribeComponentPlaybookRequest,
    ) -> main_models.DescribeComponentPlaybookResponse:
        runtime = RuntimeOptions()
        return self.describe_component_playbook_with_options(request, runtime)

    async def describe_component_playbook_async(
        self,
        request: main_models.DescribeComponentPlaybookRequest,
    ) -> main_models.DescribeComponentPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.describe_component_playbook_with_options_async(request, runtime)

    def describe_components_js_with_options(
        self,
        request: main_models.DescribeComponentsJsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentsJsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentsJs',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentsJsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_components_js_with_options_async(
        self,
        request: main_models.DescribeComponentsJsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentsJsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentsJs',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentsJsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_components_js(
        self,
        request: main_models.DescribeComponentsJsRequest,
    ) -> main_models.DescribeComponentsJsResponse:
        runtime = RuntimeOptions()
        return self.describe_components_js_with_options(request, runtime)

    async def describe_components_js_async(
        self,
        request: main_models.DescribeComponentsJsRequest,
    ) -> main_models.DescribeComponentsJsResponse:
        runtime = RuntimeOptions()
        return await self.describe_components_js_with_options_async(request, runtime)

    def describe_distinct_releases_with_options(
        self,
        request: main_models.DescribeDistinctReleasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDistinctReleasesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDistinctReleases',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDistinctReleasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_distinct_releases_with_options_async(
        self,
        request: main_models.DescribeDistinctReleasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDistinctReleasesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDistinctReleases',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDistinctReleasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_distinct_releases(
        self,
        request: main_models.DescribeDistinctReleasesRequest,
    ) -> main_models.DescribeDistinctReleasesResponse:
        runtime = RuntimeOptions()
        return self.describe_distinct_releases_with_options(request, runtime)

    async def describe_distinct_releases_async(
        self,
        request: main_models.DescribeDistinctReleasesRequest,
    ) -> main_models.DescribeDistinctReleasesResponse:
        runtime = RuntimeOptions()
        return await self.describe_distinct_releases_with_options_async(request, runtime)

    def describe_enum_items_with_options(
        self,
        request: main_models.DescribeEnumItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnumItemsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnumItems',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnumItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_enum_items_with_options_async(
        self,
        request: main_models.DescribeEnumItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnumItemsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnumItems',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnumItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_enum_items(
        self,
        request: main_models.DescribeEnumItemsRequest,
    ) -> main_models.DescribeEnumItemsResponse:
        runtime = RuntimeOptions()
        return self.describe_enum_items_with_options(request, runtime)

    async def describe_enum_items_async(
        self,
        request: main_models.DescribeEnumItemsRequest,
    ) -> main_models.DescribeEnumItemsResponse:
        runtime = RuntimeOptions()
        return await self.describe_enum_items_with_options_async(request, runtime)

    def describe_execute_playbooks_with_options(
        self,
        request: main_models.DescribeExecutePlaybooksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExecutePlaybooksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExecutePlaybooks',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExecutePlaybooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_execute_playbooks_with_options_async(
        self,
        request: main_models.DescribeExecutePlaybooksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExecutePlaybooksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExecutePlaybooks',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExecutePlaybooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_execute_playbooks(
        self,
        request: main_models.DescribeExecutePlaybooksRequest,
    ) -> main_models.DescribeExecutePlaybooksResponse:
        runtime = RuntimeOptions()
        return self.describe_execute_playbooks_with_options(request, runtime)

    async def describe_execute_playbooks_async(
        self,
        request: main_models.DescribeExecutePlaybooksRequest,
    ) -> main_models.DescribeExecutePlaybooksResponse:
        runtime = RuntimeOptions()
        return await self.describe_execute_playbooks_with_options_async(request, runtime)

    def describe_field_with_options(
        self,
        request: main_models.DescribeFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFieldResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeField',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_field_with_options_async(
        self,
        request: main_models.DescribeFieldRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFieldResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeField',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_field(
        self,
        request: main_models.DescribeFieldRequest,
    ) -> main_models.DescribeFieldResponse:
        runtime = RuntimeOptions()
        return self.describe_field_with_options(request, runtime)

    async def describe_field_async(
        self,
        request: main_models.DescribeFieldRequest,
    ) -> main_models.DescribeFieldResponse:
        runtime = RuntimeOptions()
        return await self.describe_field_with_options_async(request, runtime)

    def describe_group_productions_with_options(
        self,
        request: main_models.DescribeGroupProductionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupProductionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupProductions',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupProductionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_productions_with_options_async(
        self,
        request: main_models.DescribeGroupProductionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupProductionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupProductions',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupProductionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_productions(
        self,
        request: main_models.DescribeGroupProductionsRequest,
    ) -> main_models.DescribeGroupProductionsResponse:
        runtime = RuntimeOptions()
        return self.describe_group_productions_with_options(request, runtime)

    async def describe_group_productions_async(
        self,
        request: main_models.DescribeGroupProductionsRequest,
    ) -> main_models.DescribeGroupProductionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_productions_with_options_async(request, runtime)

    def describe_latest_record_schema_with_options(
        self,
        request: main_models.DescribeLatestRecordSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLatestRecordSchemaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLatestRecordSchema',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLatestRecordSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_latest_record_schema_with_options_async(
        self,
        request: main_models.DescribeLatestRecordSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLatestRecordSchemaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLatestRecordSchema',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLatestRecordSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_latest_record_schema(
        self,
        request: main_models.DescribeLatestRecordSchemaRequest,
    ) -> main_models.DescribeLatestRecordSchemaResponse:
        runtime = RuntimeOptions()
        return self.describe_latest_record_schema_with_options(request, runtime)

    async def describe_latest_record_schema_async(
        self,
        request: main_models.DescribeLatestRecordSchemaRequest,
    ) -> main_models.DescribeLatestRecordSchemaResponse:
        runtime = RuntimeOptions()
        return await self.describe_latest_record_schema_with_options_async(request, runtime)

    def describe_node_param_tags_with_options(
        self,
        request: main_models.DescribeNodeParamTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeParamTagsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodeParamTags',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeParamTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_param_tags_with_options_async(
        self,
        request: main_models.DescribeNodeParamTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeParamTagsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodeParamTags',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeParamTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_param_tags(
        self,
        request: main_models.DescribeNodeParamTagsRequest,
    ) -> main_models.DescribeNodeParamTagsResponse:
        runtime = RuntimeOptions()
        return self.describe_node_param_tags_with_options(request, runtime)

    async def describe_node_param_tags_async(
        self,
        request: main_models.DescribeNodeParamTagsRequest,
    ) -> main_models.DescribeNodeParamTagsResponse:
        runtime = RuntimeOptions()
        return await self.describe_node_param_tags_with_options_async(request, runtime)

    def describe_notify_template_list_with_options(
        self,
        request: main_models.DescribeNotifyTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNotifyTemplateListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNotifyTemplateList',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNotifyTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_notify_template_list_with_options_async(
        self,
        request: main_models.DescribeNotifyTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNotifyTemplateListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNotifyTemplateList',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNotifyTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_notify_template_list(
        self,
        request: main_models.DescribeNotifyTemplateListRequest,
    ) -> main_models.DescribeNotifyTemplateListResponse:
        runtime = RuntimeOptions()
        return self.describe_notify_template_list_with_options(request, runtime)

    async def describe_notify_template_list_async(
        self,
        request: main_models.DescribeNotifyTemplateListRequest,
    ) -> main_models.DescribeNotifyTemplateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_notify_template_list_with_options_async(request, runtime)

    def describe_open_api_info_with_options(
        self,
        request: main_models.DescribeOpenApiInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpenApiInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpenApiInfo',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpenApiInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_open_api_info_with_options_async(
        self,
        request: main_models.DescribeOpenApiInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpenApiInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpenApiInfo',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpenApiInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_open_api_info(
        self,
        request: main_models.DescribeOpenApiInfoRequest,
    ) -> main_models.DescribeOpenApiInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_open_api_info_with_options(request, runtime)

    async def describe_open_api_info_async(
        self,
        request: main_models.DescribeOpenApiInfoRequest,
    ) -> main_models.DescribeOpenApiInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_open_api_info_with_options_async(request, runtime)

    def describe_open_api_list_with_options(
        self,
        request: main_models.DescribeOpenApiListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpenApiListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpenApiList',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpenApiListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_open_api_list_with_options_async(
        self,
        request: main_models.DescribeOpenApiListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpenApiListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpenApiList',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpenApiListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_open_api_list(
        self,
        request: main_models.DescribeOpenApiListRequest,
    ) -> main_models.DescribeOpenApiListResponse:
        runtime = RuntimeOptions()
        return self.describe_open_api_list_with_options(request, runtime)

    async def describe_open_api_list_async(
        self,
        request: main_models.DescribeOpenApiListRequest,
    ) -> main_models.DescribeOpenApiListResponse:
        runtime = RuntimeOptions()
        return await self.describe_open_api_list_with_options_async(request, runtime)

    def describe_playbook_with_options(
        self,
        request: main_models.DescribePlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_with_options_async(
        self,
        request: main_models.DescribePlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook(
        self,
        request: main_models.DescribePlaybookRequest,
    ) -> main_models.DescribePlaybookResponse:
        runtime = RuntimeOptions()
        return self.describe_playbook_with_options(request, runtime)

    async def describe_playbook_async(
        self,
        request: main_models.DescribePlaybookRequest,
    ) -> main_models.DescribePlaybookResponse:
        runtime = RuntimeOptions()
        return await self.describe_playbook_with_options_async(request, runtime)

    def describe_playbook_input_output_with_options(
        self,
        request: main_models.DescribePlaybookInputOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookInputOutputResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybookInputOutput',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookInputOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_input_output_with_options_async(
        self,
        request: main_models.DescribePlaybookInputOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookInputOutputResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybookInputOutput',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookInputOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook_input_output(
        self,
        request: main_models.DescribePlaybookInputOutputRequest,
    ) -> main_models.DescribePlaybookInputOutputResponse:
        runtime = RuntimeOptions()
        return self.describe_playbook_input_output_with_options(request, runtime)

    async def describe_playbook_input_output_async(
        self,
        request: main_models.DescribePlaybookInputOutputRequest,
    ) -> main_models.DescribePlaybookInputOutputResponse:
        runtime = RuntimeOptions()
        return await self.describe_playbook_input_output_with_options_async(request, runtime)

    def describe_playbook_metrics_with_options(
        self,
        request: main_models.DescribePlaybookMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookMetricsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybookMetrics',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_metrics_with_options_async(
        self,
        request: main_models.DescribePlaybookMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookMetricsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybookMetrics',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook_metrics(
        self,
        request: main_models.DescribePlaybookMetricsRequest,
    ) -> main_models.DescribePlaybookMetricsResponse:
        runtime = RuntimeOptions()
        return self.describe_playbook_metrics_with_options(request, runtime)

    async def describe_playbook_metrics_async(
        self,
        request: main_models.DescribePlaybookMetricsRequest,
    ) -> main_models.DescribePlaybookMetricsResponse:
        runtime = RuntimeOptions()
        return await self.describe_playbook_metrics_with_options_async(request, runtime)

    def describe_playbook_nodes_output_with_options(
        self,
        request: main_models.DescribePlaybookNodesOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookNodesOutputResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybookNodesOutput',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookNodesOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_nodes_output_with_options_async(
        self,
        request: main_models.DescribePlaybookNodesOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookNodesOutputResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybookNodesOutput',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookNodesOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook_nodes_output(
        self,
        request: main_models.DescribePlaybookNodesOutputRequest,
    ) -> main_models.DescribePlaybookNodesOutputResponse:
        runtime = RuntimeOptions()
        return self.describe_playbook_nodes_output_with_options(request, runtime)

    async def describe_playbook_nodes_output_async(
        self,
        request: main_models.DescribePlaybookNodesOutputRequest,
    ) -> main_models.DescribePlaybookNodesOutputResponse:
        runtime = RuntimeOptions()
        return await self.describe_playbook_nodes_output_with_options_async(request, runtime)

    def describe_playbook_number_metrics_with_options(
        self,
        request: main_models.DescribePlaybookNumberMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookNumberMetricsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybookNumberMetrics',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookNumberMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_number_metrics_with_options_async(
        self,
        request: main_models.DescribePlaybookNumberMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookNumberMetricsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybookNumberMetrics',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookNumberMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook_number_metrics(
        self,
        request: main_models.DescribePlaybookNumberMetricsRequest,
    ) -> main_models.DescribePlaybookNumberMetricsResponse:
        runtime = RuntimeOptions()
        return self.describe_playbook_number_metrics_with_options(request, runtime)

    async def describe_playbook_number_metrics_async(
        self,
        request: main_models.DescribePlaybookNumberMetricsRequest,
    ) -> main_models.DescribePlaybookNumberMetricsResponse:
        runtime = RuntimeOptions()
        return await self.describe_playbook_number_metrics_with_options_async(request, runtime)

    def describe_playbook_releases_with_options(
        self,
        request: main_models.DescribePlaybookReleasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookReleasesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybookReleases',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookReleasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_releases_with_options_async(
        self,
        request: main_models.DescribePlaybookReleasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybookReleasesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybookReleases',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybookReleasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook_releases(
        self,
        request: main_models.DescribePlaybookReleasesRequest,
    ) -> main_models.DescribePlaybookReleasesResponse:
        runtime = RuntimeOptions()
        return self.describe_playbook_releases_with_options(request, runtime)

    async def describe_playbook_releases_async(
        self,
        request: main_models.DescribePlaybookReleasesRequest,
    ) -> main_models.DescribePlaybookReleasesResponse:
        runtime = RuntimeOptions()
        return await self.describe_playbook_releases_with_options_async(request, runtime)

    def describe_playbooks_with_options(
        self,
        request: main_models.DescribePlaybooksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybooksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybooks',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbooks_with_options_async(
        self,
        request: main_models.DescribePlaybooksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlaybooksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlaybooks',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlaybooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbooks(
        self,
        request: main_models.DescribePlaybooksRequest,
    ) -> main_models.DescribePlaybooksResponse:
        runtime = RuntimeOptions()
        return self.describe_playbooks_with_options(request, runtime)

    async def describe_playbooks_async(
        self,
        request: main_models.DescribePlaybooksRequest,
    ) -> main_models.DescribePlaybooksResponse:
        runtime = RuntimeOptions()
        return await self.describe_playbooks_with_options_async(request, runtime)

    def describe_pop_api_with_options(
        self,
        request: main_models.DescribePopApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePopApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.api_version):
            query['ApiVersion'] = request.api_version
        if not DaraCore.is_null(request.pop_code):
            query['PopCode'] = request.pop_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePopApi',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePopApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pop_api_with_options_async(
        self,
        request: main_models.DescribePopApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePopApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.api_version):
            query['ApiVersion'] = request.api_version
        if not DaraCore.is_null(request.pop_code):
            query['PopCode'] = request.pop_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePopApi',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePopApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pop_api(
        self,
        request: main_models.DescribePopApiRequest,
    ) -> main_models.DescribePopApiResponse:
        runtime = RuntimeOptions()
        return self.describe_pop_api_with_options(request, runtime)

    async def describe_pop_api_async(
        self,
        request: main_models.DescribePopApiRequest,
    ) -> main_models.DescribePopApiResponse:
        runtime = RuntimeOptions()
        return await self.describe_pop_api_with_options_async(request, runtime)

    def describe_process_statistics_with_options(
        self,
        request: main_models.DescribeProcessStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProcessStatisticsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProcessStatistics',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProcessStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_process_statistics_with_options_async(
        self,
        request: main_models.DescribeProcessStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProcessStatisticsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProcessStatistics',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProcessStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_process_statistics(
        self,
        request: main_models.DescribeProcessStatisticsRequest,
    ) -> main_models.DescribeProcessStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_process_statistics_with_options(request, runtime)

    async def describe_process_statistics_async(
        self,
        request: main_models.DescribeProcessStatisticsRequest,
    ) -> main_models.DescribeProcessStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_process_statistics_with_options_async(request, runtime)

    def describe_process_task_count_with_options(
        self,
        request: main_models.DescribeProcessTaskCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProcessTaskCountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProcessTaskCount',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProcessTaskCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_process_task_count_with_options_async(
        self,
        request: main_models.DescribeProcessTaskCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProcessTaskCountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProcessTaskCount',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProcessTaskCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_process_task_count(
        self,
        request: main_models.DescribeProcessTaskCountRequest,
    ) -> main_models.DescribeProcessTaskCountResponse:
        runtime = RuntimeOptions()
        return self.describe_process_task_count_with_options(request, runtime)

    async def describe_process_task_count_async(
        self,
        request: main_models.DescribeProcessTaskCountRequest,
    ) -> main_models.DescribeProcessTaskCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_process_task_count_with_options_async(request, runtime)

    def describe_process_tasks_with_options(
        self,
        request: main_models.DescribeProcessTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProcessTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.entity_name):
            query['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.entity_uuid):
            query['EntityUuid'] = request.entity_uuid
        if not DaraCore.is_null(request.event_uuid):
            query['EventUuid'] = request.event_uuid
        if not DaraCore.is_null(request.order_field):
            query['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.param_content):
            query['ParamContent'] = request.param_content
        if not DaraCore.is_null(request.process_action_end):
            query['ProcessActionEnd'] = request.process_action_end
        if not DaraCore.is_null(request.process_action_start):
            query['ProcessActionStart'] = request.process_action_start
        if not DaraCore.is_null(request.process_remove_end):
            query['ProcessRemoveEnd'] = request.process_remove_end
        if not DaraCore.is_null(request.process_remove_start):
            query['ProcessRemoveStart'] = request.process_remove_start
        if not DaraCore.is_null(request.process_strategy_uuid):
            query['ProcessStrategyUuid'] = request.process_strategy_uuid
        if not DaraCore.is_null(request.req_uuid):
            query['ReqUuid'] = request.req_uuid
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.trigger_source):
            query['TriggerSource'] = request.trigger_source
        if not DaraCore.is_null(request.yun_code):
            query['YunCode'] = request.yun_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProcessTasks',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProcessTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_process_tasks_with_options_async(
        self,
        request: main_models.DescribeProcessTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProcessTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.entity_name):
            query['EntityName'] = request.entity_name
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.entity_uuid):
            query['EntityUuid'] = request.entity_uuid
        if not DaraCore.is_null(request.event_uuid):
            query['EventUuid'] = request.event_uuid
        if not DaraCore.is_null(request.order_field):
            query['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.param_content):
            query['ParamContent'] = request.param_content
        if not DaraCore.is_null(request.process_action_end):
            query['ProcessActionEnd'] = request.process_action_end
        if not DaraCore.is_null(request.process_action_start):
            query['ProcessActionStart'] = request.process_action_start
        if not DaraCore.is_null(request.process_remove_end):
            query['ProcessRemoveEnd'] = request.process_remove_end
        if not DaraCore.is_null(request.process_remove_start):
            query['ProcessRemoveStart'] = request.process_remove_start
        if not DaraCore.is_null(request.process_strategy_uuid):
            query['ProcessStrategyUuid'] = request.process_strategy_uuid
        if not DaraCore.is_null(request.req_uuid):
            query['ReqUuid'] = request.req_uuid
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.trigger_source):
            query['TriggerSource'] = request.trigger_source
        if not DaraCore.is_null(request.yun_code):
            query['YunCode'] = request.yun_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProcessTasks',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProcessTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_process_tasks(
        self,
        request: main_models.DescribeProcessTasksRequest,
    ) -> main_models.DescribeProcessTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_process_tasks_with_options(request, runtime)

    async def describe_process_tasks_async(
        self,
        request: main_models.DescribeProcessTasksRequest,
    ) -> main_models.DescribeProcessTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_process_tasks_with_options_async(request, runtime)

    def describe_soar_record_action_output_list_with_options(
        self,
        request: main_models.DescribeSoarRecordActionOutputListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSoarRecordActionOutputListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSoarRecordActionOutputList',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSoarRecordActionOutputListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_soar_record_action_output_list_with_options_async(
        self,
        request: main_models.DescribeSoarRecordActionOutputListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSoarRecordActionOutputListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSoarRecordActionOutputList',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSoarRecordActionOutputListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_soar_record_action_output_list(
        self,
        request: main_models.DescribeSoarRecordActionOutputListRequest,
    ) -> main_models.DescribeSoarRecordActionOutputListResponse:
        runtime = RuntimeOptions()
        return self.describe_soar_record_action_output_list_with_options(request, runtime)

    async def describe_soar_record_action_output_list_async(
        self,
        request: main_models.DescribeSoarRecordActionOutputListRequest,
    ) -> main_models.DescribeSoarRecordActionOutputListResponse:
        runtime = RuntimeOptions()
        return await self.describe_soar_record_action_output_list_with_options_async(request, runtime)

    def describe_soar_record_in_output_with_options(
        self,
        request: main_models.DescribeSoarRecordInOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSoarRecordInOutputResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSoarRecordInOutput',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSoarRecordInOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_soar_record_in_output_with_options_async(
        self,
        request: main_models.DescribeSoarRecordInOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSoarRecordInOutputResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSoarRecordInOutput',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSoarRecordInOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_soar_record_in_output(
        self,
        request: main_models.DescribeSoarRecordInOutputRequest,
    ) -> main_models.DescribeSoarRecordInOutputResponse:
        runtime = RuntimeOptions()
        return self.describe_soar_record_in_output_with_options(request, runtime)

    async def describe_soar_record_in_output_async(
        self,
        request: main_models.DescribeSoarRecordInOutputRequest,
    ) -> main_models.DescribeSoarRecordInOutputResponse:
        runtime = RuntimeOptions()
        return await self.describe_soar_record_in_output_with_options_async(request, runtime)

    def describe_soar_records_with_options(
        self,
        request: main_models.DescribeSoarRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSoarRecordsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSoarRecords',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSoarRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_soar_records_with_options_async(
        self,
        request: main_models.DescribeSoarRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSoarRecordsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSoarRecords',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSoarRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_soar_records(
        self,
        request: main_models.DescribeSoarRecordsRequest,
    ) -> main_models.DescribeSoarRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_soar_records_with_options(request, runtime)

    async def describe_soar_records_async(
        self,
        request: main_models.DescribeSoarRecordsRequest,
    ) -> main_models.DescribeSoarRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_soar_records_with_options_async(request, runtime)

    def describe_soar_task_and_actions_with_options(
        self,
        request: main_models.DescribeSoarTaskAndActionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSoarTaskAndActionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSoarTaskAndActions',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSoarTaskAndActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_soar_task_and_actions_with_options_async(
        self,
        request: main_models.DescribeSoarTaskAndActionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSoarTaskAndActionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSoarTaskAndActions',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSoarTaskAndActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_soar_task_and_actions(
        self,
        request: main_models.DescribeSoarTaskAndActionsRequest,
    ) -> main_models.DescribeSoarTaskAndActionsResponse:
        runtime = RuntimeOptions()
        return self.describe_soar_task_and_actions_with_options(request, runtime)

    async def describe_soar_task_and_actions_async(
        self,
        request: main_models.DescribeSoarTaskAndActionsRequest,
    ) -> main_models.DescribeSoarTaskAndActionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_soar_task_and_actions_with_options_async(request, runtime)

    def describe_sophon_commands_with_options(
        self,
        request: main_models.DescribeSophonCommandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSophonCommandsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSophonCommands',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSophonCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sophon_commands_with_options_async(
        self,
        request: main_models.DescribeSophonCommandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSophonCommandsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSophonCommands',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSophonCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sophon_commands(
        self,
        request: main_models.DescribeSophonCommandsRequest,
    ) -> main_models.DescribeSophonCommandsResponse:
        runtime = RuntimeOptions()
        return self.describe_sophon_commands_with_options(request, runtime)

    async def describe_sophon_commands_async(
        self,
        request: main_models.DescribeSophonCommandsRequest,
    ) -> main_models.DescribeSophonCommandsResponse:
        runtime = RuntimeOptions()
        return await self.describe_sophon_commands_with_options_async(request, runtime)

    def describe_vendor_api_list_with_options(
        self,
        request: main_models.DescribeVendorApiListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVendorApiListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.vendor_code):
            query['VendorCode'] = request.vendor_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVendorApiList',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVendorApiListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vendor_api_list_with_options_async(
        self,
        request: main_models.DescribeVendorApiListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVendorApiListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.vendor_code):
            query['VendorCode'] = request.vendor_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVendorApiList',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVendorApiListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vendor_api_list(
        self,
        request: main_models.DescribeVendorApiListRequest,
    ) -> main_models.DescribeVendorApiListResponse:
        runtime = RuntimeOptions()
        return self.describe_vendor_api_list_with_options(request, runtime)

    async def describe_vendor_api_list_async(
        self,
        request: main_models.DescribeVendorApiListRequest,
    ) -> main_models.DescribeVendorApiListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vendor_api_list_with_options_async(request, runtime)

    def describer_python_3script_logs_with_options(
        self,
        request: main_models.DescriberPython3ScriptLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescriberPython3ScriptLogsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescriberPython3ScriptLogs',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescriberPython3ScriptLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describer_python_3script_logs_with_options_async(
        self,
        request: main_models.DescriberPython3ScriptLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescriberPython3ScriptLogsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescriberPython3ScriptLogs',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescriberPython3ScriptLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describer_python_3script_logs(
        self,
        request: main_models.DescriberPython3ScriptLogsRequest,
    ) -> main_models.DescriberPython3ScriptLogsResponse:
        runtime = RuntimeOptions()
        return self.describer_python_3script_logs_with_options(request, runtime)

    async def describer_python_3script_logs_async(
        self,
        request: main_models.DescriberPython3ScriptLogsRequest,
    ) -> main_models.DescriberPython3ScriptLogsResponse:
        runtime = RuntimeOptions()
        return await self.describer_python_3script_logs_with_options_async(request, runtime)

    def modify_component_asset_with_options(
        self,
        request: main_models.ModifyComponentAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyComponentAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_config):
            query['AssetConfig'] = request.asset_config
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyComponentAsset',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyComponentAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_component_asset_with_options_async(
        self,
        request: main_models.ModifyComponentAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyComponentAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_config):
            query['AssetConfig'] = request.asset_config
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyComponentAsset',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyComponentAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_component_asset(
        self,
        request: main_models.ModifyComponentAssetRequest,
    ) -> main_models.ModifyComponentAssetResponse:
        runtime = RuntimeOptions()
        return self.modify_component_asset_with_options(request, runtime)

    async def modify_component_asset_async(
        self,
        request: main_models.ModifyComponentAssetRequest,
    ) -> main_models.ModifyComponentAssetResponse:
        runtime = RuntimeOptions()
        return await self.modify_component_asset_with_options_async(request, runtime)

    def modify_playbook_with_options(
        self,
        request: main_models.ModifyPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_playbook_with_options_async(
        self,
        request: main_models.ModifyPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_playbook(
        self,
        request: main_models.ModifyPlaybookRequest,
    ) -> main_models.ModifyPlaybookResponse:
        runtime = RuntimeOptions()
        return self.modify_playbook_with_options(request, runtime)

    async def modify_playbook_async(
        self,
        request: main_models.ModifyPlaybookRequest,
    ) -> main_models.ModifyPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.modify_playbook_with_options_async(request, runtime)

    def modify_playbook_input_output_with_options(
        self,
        request: main_models.ModifyPlaybookInputOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPlaybookInputOutputResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.exe_config):
            body['ExeConfig'] = request.exe_config
        if not DaraCore.is_null(request.input_params):
            body['InputParams'] = request.input_params
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.output_params):
            body['OutputParams'] = request.output_params
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPlaybookInputOutput',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPlaybookInputOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_playbook_input_output_with_options_async(
        self,
        request: main_models.ModifyPlaybookInputOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPlaybookInputOutputResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.exe_config):
            body['ExeConfig'] = request.exe_config
        if not DaraCore.is_null(request.input_params):
            body['InputParams'] = request.input_params
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.output_params):
            body['OutputParams'] = request.output_params
        if not DaraCore.is_null(request.param_type):
            body['ParamType'] = request.param_type
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPlaybookInputOutput',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPlaybookInputOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_playbook_input_output(
        self,
        request: main_models.ModifyPlaybookInputOutputRequest,
    ) -> main_models.ModifyPlaybookInputOutputResponse:
        runtime = RuntimeOptions()
        return self.modify_playbook_input_output_with_options(request, runtime)

    async def modify_playbook_input_output_async(
        self,
        request: main_models.ModifyPlaybookInputOutputRequest,
    ) -> main_models.ModifyPlaybookInputOutputResponse:
        runtime = RuntimeOptions()
        return await self.modify_playbook_input_output_with_options_async(request, runtime)

    def publish_playbook_with_options(
        self,
        request: main_models.PublishPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_playbook_with_options_async(
        self,
        request: main_models.PublishPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_playbook(
        self,
        request: main_models.PublishPlaybookRequest,
    ) -> main_models.PublishPlaybookResponse:
        runtime = RuntimeOptions()
        return self.publish_playbook_with_options(request, runtime)

    async def publish_playbook_async(
        self,
        request: main_models.PublishPlaybookRequest,
    ) -> main_models.PublishPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.publish_playbook_with_options_async(request, runtime)

    def query_tree_data_with_options(
        self,
        request: main_models.QueryTreeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTreeDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTreeData',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTreeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tree_data_with_options_async(
        self,
        request: main_models.QueryTreeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTreeDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTreeData',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTreeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tree_data(
        self,
        request: main_models.QueryTreeDataRequest,
    ) -> main_models.QueryTreeDataResponse:
        runtime = RuntimeOptions()
        return self.query_tree_data_with_options(request, runtime)

    async def query_tree_data_async(
        self,
        request: main_models.QueryTreeDataRequest,
    ) -> main_models.QueryTreeDataResponse:
        runtime = RuntimeOptions()
        return await self.query_tree_data_with_options_async(request, runtime)

    def revert_playbook_release_with_options(
        self,
        request: main_models.RevertPlaybookReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevertPlaybookReleaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_publish):
            body['IsPublish'] = request.is_publish
        if not DaraCore.is_null(request.play_release_id):
            body['PlayReleaseId'] = request.play_release_id
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevertPlaybookRelease',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertPlaybookReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def revert_playbook_release_with_options_async(
        self,
        request: main_models.RevertPlaybookReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevertPlaybookReleaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_publish):
            body['IsPublish'] = request.is_publish
        if not DaraCore.is_null(request.play_release_id):
            body['PlayReleaseId'] = request.play_release_id
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevertPlaybookRelease',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertPlaybookReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revert_playbook_release(
        self,
        request: main_models.RevertPlaybookReleaseRequest,
    ) -> main_models.RevertPlaybookReleaseResponse:
        runtime = RuntimeOptions()
        return self.revert_playbook_release_with_options(request, runtime)

    async def revert_playbook_release_async(
        self,
        request: main_models.RevertPlaybookReleaseRequest,
    ) -> main_models.RevertPlaybookReleaseResponse:
        runtime = RuntimeOptions()
        return await self.revert_playbook_release_with_options_async(request, runtime)

    def run_notify_component_with_email_with_options(
        self,
        request: main_models.RunNotifyComponentWithEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunNotifyComponentWithEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.component_name):
            query['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.receivers):
            query['Receivers'] = request.receivers
        if not DaraCore.is_null(request.role_for):
            query['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunNotifyComponentWithEmail',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunNotifyComponentWithEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_notify_component_with_email_with_options_async(
        self,
        request: main_models.RunNotifyComponentWithEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunNotifyComponentWithEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.component_name):
            query['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.receivers):
            query['Receivers'] = request.receivers
        if not DaraCore.is_null(request.role_for):
            query['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunNotifyComponentWithEmail',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunNotifyComponentWithEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_notify_component_with_email(
        self,
        request: main_models.RunNotifyComponentWithEmailRequest,
    ) -> main_models.RunNotifyComponentWithEmailResponse:
        runtime = RuntimeOptions()
        return self.run_notify_component_with_email_with_options(request, runtime)

    async def run_notify_component_with_email_async(
        self,
        request: main_models.RunNotifyComponentWithEmailRequest,
    ) -> main_models.RunNotifyComponentWithEmailResponse:
        runtime = RuntimeOptions()
        return await self.run_notify_component_with_email_with_options_async(request, runtime)

    def run_notify_component_with_message_center_with_options(
        self,
        request: main_models.RunNotifyComponentWithMessageCenterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunNotifyComponentWithMessageCenterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.aliuid):
            query['Aliuid'] = request.aliuid
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.channel_type_list):
            query['ChannelTypeList'] = request.channel_type_list
        if not DaraCore.is_null(request.component_name):
            query['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.role_for):
            query['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunNotifyComponentWithMessageCenter',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunNotifyComponentWithMessageCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_notify_component_with_message_center_with_options_async(
        self,
        request: main_models.RunNotifyComponentWithMessageCenterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunNotifyComponentWithMessageCenterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.aliuid):
            query['Aliuid'] = request.aliuid
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.channel_type_list):
            query['ChannelTypeList'] = request.channel_type_list
        if not DaraCore.is_null(request.component_name):
            query['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.role_for):
            query['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunNotifyComponentWithMessageCenter',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunNotifyComponentWithMessageCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_notify_component_with_message_center(
        self,
        request: main_models.RunNotifyComponentWithMessageCenterRequest,
    ) -> main_models.RunNotifyComponentWithMessageCenterResponse:
        runtime = RuntimeOptions()
        return self.run_notify_component_with_message_center_with_options(request, runtime)

    async def run_notify_component_with_message_center_async(
        self,
        request: main_models.RunNotifyComponentWithMessageCenterRequest,
    ) -> main_models.RunNotifyComponentWithMessageCenterResponse:
        runtime = RuntimeOptions()
        return await self.run_notify_component_with_message_center_with_options_async(request, runtime)

    def run_notify_component_with_webhook_with_options(
        self,
        request: main_models.RunNotifyComponentWithWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunNotifyComponentWithWebhookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.component_name):
            query['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.msg_type):
            query['MsgType'] = request.msg_type
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.role_for):
            query['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        if not DaraCore.is_null(request.secret):
            query['Secret'] = request.secret
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunNotifyComponentWithWebhook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunNotifyComponentWithWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_notify_component_with_webhook_with_options_async(
        self,
        request: main_models.RunNotifyComponentWithWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunNotifyComponentWithWebhookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.component_name):
            query['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.msg_type):
            query['MsgType'] = request.msg_type
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.role_for):
            query['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        if not DaraCore.is_null(request.secret):
            query['Secret'] = request.secret
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunNotifyComponentWithWebhook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunNotifyComponentWithWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_notify_component_with_webhook(
        self,
        request: main_models.RunNotifyComponentWithWebhookRequest,
    ) -> main_models.RunNotifyComponentWithWebhookResponse:
        runtime = RuntimeOptions()
        return self.run_notify_component_with_webhook_with_options(request, runtime)

    async def run_notify_component_with_webhook_async(
        self,
        request: main_models.RunNotifyComponentWithWebhookRequest,
    ) -> main_models.RunNotifyComponentWithWebhookResponse:
        runtime = RuntimeOptions()
        return await self.run_notify_component_with_webhook_with_options_async(request, runtime)

    def run_python_3script_with_options(
        self,
        request: main_models.RunPython3ScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunPython3ScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.python_version):
            query['PythonVersion'] = request.python_version
        body = {}
        if not DaraCore.is_null(request.node_name):
            body['NodeName'] = request.node_name
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.python_script):
            body['PythonScript'] = request.python_script
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunPython3Script',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunPython3ScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_python_3script_with_options_async(
        self,
        request: main_models.RunPython3ScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunPython3ScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.python_version):
            query['PythonVersion'] = request.python_version
        body = {}
        if not DaraCore.is_null(request.node_name):
            body['NodeName'] = request.node_name
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.python_script):
            body['PythonScript'] = request.python_script
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunPython3Script',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunPython3ScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_python_3script(
        self,
        request: main_models.RunPython3ScriptRequest,
    ) -> main_models.RunPython3ScriptResponse:
        runtime = RuntimeOptions()
        return self.run_python_3script_with_options(request, runtime)

    async def run_python_3script_async(
        self,
        request: main_models.RunPython3ScriptRequest,
    ) -> main_models.RunPython3ScriptResponse:
        runtime = RuntimeOptions()
        return await self.run_python_3script_with_options_async(request, runtime)

    def trigger_playbook_with_options(
        self,
        request: main_models.TriggerPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input_param):
            body['InputParam'] = request.input_param
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_playbook_with_options_async(
        self,
        request: main_models.TriggerPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input_param):
            body['InputParam'] = request.input_param
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_playbook(
        self,
        request: main_models.TriggerPlaybookRequest,
    ) -> main_models.TriggerPlaybookResponse:
        runtime = RuntimeOptions()
        return self.trigger_playbook_with_options(request, runtime)

    async def trigger_playbook_async(
        self,
        request: main_models.TriggerPlaybookRequest,
    ) -> main_models.TriggerPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.trigger_playbook_with_options_async(request, runtime)

    def trigger_process_task_with_options(
        self,
        request: main_models.TriggerProcessTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerProcessTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerProcessTask',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerProcessTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_process_task_with_options_async(
        self,
        request: main_models.TriggerProcessTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerProcessTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerProcessTask',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerProcessTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_process_task(
        self,
        request: main_models.TriggerProcessTaskRequest,
    ) -> main_models.TriggerProcessTaskResponse:
        runtime = RuntimeOptions()
        return self.trigger_process_task_with_options(request, runtime)

    async def trigger_process_task_async(
        self,
        request: main_models.TriggerProcessTaskRequest,
    ) -> main_models.TriggerProcessTaskResponse:
        runtime = RuntimeOptions()
        return await self.trigger_process_task_with_options_async(request, runtime)

    def trigger_sophon_playbook_with_options(
        self,
        request: main_models.TriggerSophonPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerSophonPlaybookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_name):
            query['CommandName'] = request.command_name
        if not DaraCore.is_null(request.input_params):
            query['InputParams'] = request.input_params
        if not DaraCore.is_null(request.sophon_task_id):
            query['SophonTaskId'] = request.sophon_task_id
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TriggerSophonPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerSophonPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_sophon_playbook_with_options_async(
        self,
        request: main_models.TriggerSophonPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerSophonPlaybookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_name):
            query['CommandName'] = request.command_name
        if not DaraCore.is_null(request.input_params):
            query['InputParams'] = request.input_params
        if not DaraCore.is_null(request.sophon_task_id):
            query['SophonTaskId'] = request.sophon_task_id
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TriggerSophonPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerSophonPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_sophon_playbook(
        self,
        request: main_models.TriggerSophonPlaybookRequest,
    ) -> main_models.TriggerSophonPlaybookResponse:
        runtime = RuntimeOptions()
        return self.trigger_sophon_playbook_with_options(request, runtime)

    async def trigger_sophon_playbook_async(
        self,
        request: main_models.TriggerSophonPlaybookRequest,
    ) -> main_models.TriggerSophonPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.trigger_sophon_playbook_with_options_async(request, runtime)

    def verify_playbook_with_options(
        self,
        request: main_models.VerifyPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.task_flow):
            body['TaskFlow'] = request.task_flow
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VerifyPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_playbook_with_options_async(
        self,
        request: main_models.VerifyPlaybookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyPlaybookResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.task_flow):
            body['TaskFlow'] = request.task_flow
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VerifyPlaybook',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_playbook(
        self,
        request: main_models.VerifyPlaybookRequest,
    ) -> main_models.VerifyPlaybookResponse:
        runtime = RuntimeOptions()
        return self.verify_playbook_with_options(request, runtime)

    async def verify_playbook_async(
        self,
        request: main_models.VerifyPlaybookRequest,
    ) -> main_models.VerifyPlaybookResponse:
        runtime = RuntimeOptions()
        return await self.verify_playbook_with_options_async(request, runtime)

    def verify_python_file_with_options(
        self,
        request: main_models.VerifyPythonFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyPythonFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VerifyPythonFile',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyPythonFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_python_file_with_options_async(
        self,
        request: main_models.VerifyPythonFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyPythonFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VerifyPythonFile',
            version = '2022-07-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyPythonFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_python_file(
        self,
        request: main_models.VerifyPythonFileRequest,
    ) -> main_models.VerifyPythonFileResponse:
        runtime = RuntimeOptions()
        return self.verify_python_file_with_options(request, runtime)

    async def verify_python_file_async(
        self,
        request: main_models.VerifyPythonFileRequest,
    ) -> main_models.VerifyPythonFileResponse:
        runtime = RuntimeOptions()
        return await self.verify_python_file_with_options_async(request, runtime)
