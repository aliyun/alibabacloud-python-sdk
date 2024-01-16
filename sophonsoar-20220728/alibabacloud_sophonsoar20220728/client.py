# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sophonsoar20220728 import models as sophonsoar_20220728_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_modify_instance_status_with_options(
        self,
        request: sophonsoar_20220728_models.BatchModifyInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.BatchModifyInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchModifyInstanceStatus',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.BatchModifyInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_modify_instance_status_with_options_async(
        self,
        request: sophonsoar_20220728_models.BatchModifyInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.BatchModifyInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchModifyInstanceStatus',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.BatchModifyInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_modify_instance_status(
        self,
        request: sophonsoar_20220728_models.BatchModifyInstanceStatusRequest,
    ) -> sophonsoar_20220728_models.BatchModifyInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_modify_instance_status_with_options(request, runtime)

    async def batch_modify_instance_status_async(
        self,
        request: sophonsoar_20220728_models.BatchModifyInstanceStatusRequest,
    ) -> sophonsoar_20220728_models.BatchModifyInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_modify_instance_status_with_options_async(request, runtime)

    def compare_playbooks_with_options(
        self,
        request: sophonsoar_20220728_models.ComparePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ComparePlaybooksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_playbook_release_id):
            query['NewPlaybookReleaseId'] = request.new_playbook_release_id
        if not UtilClient.is_unset(request.old_playbook_release_id):
            query['OldPlaybookReleaseId'] = request.old_playbook_release_id
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ComparePlaybooks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ComparePlaybooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_playbooks_with_options_async(
        self,
        request: sophonsoar_20220728_models.ComparePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ComparePlaybooksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_playbook_release_id):
            query['NewPlaybookReleaseId'] = request.new_playbook_release_id
        if not UtilClient.is_unset(request.old_playbook_release_id):
            query['OldPlaybookReleaseId'] = request.old_playbook_release_id
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ComparePlaybooks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ComparePlaybooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_playbooks(
        self,
        request: sophonsoar_20220728_models.ComparePlaybooksRequest,
    ) -> sophonsoar_20220728_models.ComparePlaybooksResponse:
        runtime = util_models.RuntimeOptions()
        return self.compare_playbooks_with_options(request, runtime)

    async def compare_playbooks_async(
        self,
        request: sophonsoar_20220728_models.ComparePlaybooksRequest,
    ) -> sophonsoar_20220728_models.ComparePlaybooksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.compare_playbooks_with_options_async(request, runtime)

    def create_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.CreatePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.CreatePlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.CreatePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.CreatePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.CreatePlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.CreatePlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_playbook(
        self,
        request: sophonsoar_20220728_models.CreatePlaybookRequest,
    ) -> sophonsoar_20220728_models.CreatePlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_playbook_with_options(request, runtime)

    async def create_playbook_async(
        self,
        request: sophonsoar_20220728_models.CreatePlaybookRequest,
    ) -> sophonsoar_20220728_models.CreatePlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_playbook_with_options_async(request, runtime)

    def debug_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.DebugPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DebugPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.record):
            body['Record'] = request.record
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DebugPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DebugPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.DebugPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DebugPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.record):
            body['Record'] = request.record
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DebugPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DebugPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_playbook(
        self,
        request: sophonsoar_20220728_models.DebugPlaybookRequest,
    ) -> sophonsoar_20220728_models.DebugPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return self.debug_playbook_with_options(request, runtime)

    async def debug_playbook_async(
        self,
        request: sophonsoar_20220728_models.DebugPlaybookRequest,
    ) -> sophonsoar_20220728_models.DebugPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.debug_playbook_with_options_async(request, runtime)

    def delete_component_asset_with_options(
        self,
        request: sophonsoar_20220728_models.DeleteComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DeleteComponentAssetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteComponentAsset',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DeleteComponentAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_component_asset_with_options_async(
        self,
        request: sophonsoar_20220728_models.DeleteComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DeleteComponentAssetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteComponentAsset',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DeleteComponentAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_component_asset(
        self,
        request: sophonsoar_20220728_models.DeleteComponentAssetRequest,
    ) -> sophonsoar_20220728_models.DeleteComponentAssetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_component_asset_with_options(request, runtime)

    async def delete_component_asset_async(
        self,
        request: sophonsoar_20220728_models.DeleteComponentAssetRequest,
    ) -> sophonsoar_20220728_models.DeleteComponentAssetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_component_asset_with_options_async(request, runtime)

    def delete_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.DeletePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DeletePlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DeletePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.DeletePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DeletePlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DeletePlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_playbook(
        self,
        request: sophonsoar_20220728_models.DeletePlaybookRequest,
    ) -> sophonsoar_20220728_models.DeletePlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_playbook_with_options(request, runtime)

    async def delete_playbook_async(
        self,
        request: sophonsoar_20220728_models.DeletePlaybookRequest,
    ) -> sophonsoar_20220728_models.DeletePlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_playbook_with_options_async(request, runtime)

    def describe_api_list_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeApiListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeApiListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeApiListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_list_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeApiListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeApiListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeApiListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_list(
        self,
        request: sophonsoar_20220728_models.DescribeApiListRequest,
    ) -> sophonsoar_20220728_models.DescribeApiListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_list_with_options(request, runtime)

    async def describe_api_list_async(
        self,
        request: sophonsoar_20220728_models.DescribeApiListRequest,
    ) -> sophonsoar_20220728_models.DescribeApiListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_list_with_options_async(request, runtime)

    def describe_component_asset_form_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetFormResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentAssetForm',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentAssetFormResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_asset_form_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetFormResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentAssetForm',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentAssetFormResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component_asset_form(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetFormRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetFormResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_component_asset_form_with_options(request, runtime)

    async def describe_component_asset_form_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetFormRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetFormResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_component_asset_form_with_options_async(request, runtime)

    def describe_component_assets_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentAssets',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_assets_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentAssets',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component_assets(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetsRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_component_assets_with_options(request, runtime)

    async def describe_component_assets_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetsRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_component_assets_with_options_async(request, runtime)

    def describe_component_list_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeComponentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_list_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component_list(
        self,
        request: sophonsoar_20220728_models.DescribeComponentListRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_component_list_with_options(request, runtime)

    async def describe_component_list_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentListRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_component_list_with_options_async(request, runtime)

    def describe_component_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeComponentPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentPlaybookResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentPlaybookResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component_playbook(
        self,
        request: sophonsoar_20220728_models.DescribeComponentPlaybookRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_component_playbook_with_options(request, runtime)

    async def describe_component_playbook_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentPlaybookRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_component_playbook_with_options_async(request, runtime)

    def describe_components_js_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeComponentsJsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentsJsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentsJs',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentsJsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_components_js_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentsJsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentsJsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentsJs',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentsJsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_components_js(
        self,
        request: sophonsoar_20220728_models.DescribeComponentsJsRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentsJsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_components_js_with_options(request, runtime)

    async def describe_components_js_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentsJsRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentsJsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_components_js_with_options_async(request, runtime)

    def describe_distinct_releases_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeDistinctReleasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeDistinctReleasesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDistinctReleases',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeDistinctReleasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_distinct_releases_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeDistinctReleasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeDistinctReleasesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDistinctReleases',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeDistinctReleasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_distinct_releases(
        self,
        request: sophonsoar_20220728_models.DescribeDistinctReleasesRequest,
    ) -> sophonsoar_20220728_models.DescribeDistinctReleasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_distinct_releases_with_options(request, runtime)

    async def describe_distinct_releases_async(
        self,
        request: sophonsoar_20220728_models.DescribeDistinctReleasesRequest,
    ) -> sophonsoar_20220728_models.DescribeDistinctReleasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_distinct_releases_with_options_async(request, runtime)

    def describe_enum_items_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeEnumItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeEnumItemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnumItems',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeEnumItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_enum_items_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeEnumItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeEnumItemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnumItems',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeEnumItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_enum_items(
        self,
        request: sophonsoar_20220728_models.DescribeEnumItemsRequest,
    ) -> sophonsoar_20220728_models.DescribeEnumItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_enum_items_with_options(request, runtime)

    async def describe_enum_items_async(
        self,
        request: sophonsoar_20220728_models.DescribeEnumItemsRequest,
    ) -> sophonsoar_20220728_models.DescribeEnumItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_enum_items_with_options_async(request, runtime)

    def describe_execute_playbooks_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeExecutePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeExecutePlaybooksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExecutePlaybooks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeExecutePlaybooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_execute_playbooks_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeExecutePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeExecutePlaybooksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExecutePlaybooks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeExecutePlaybooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_execute_playbooks(
        self,
        request: sophonsoar_20220728_models.DescribeExecutePlaybooksRequest,
    ) -> sophonsoar_20220728_models.DescribeExecutePlaybooksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_execute_playbooks_with_options(request, runtime)

    async def describe_execute_playbooks_async(
        self,
        request: sophonsoar_20220728_models.DescribeExecutePlaybooksRequest,
    ) -> sophonsoar_20220728_models.DescribeExecutePlaybooksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_execute_playbooks_with_options_async(request, runtime)

    def describe_field_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeFieldResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeField',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_field_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeFieldResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeField',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_field(
        self,
        request: sophonsoar_20220728_models.DescribeFieldRequest,
    ) -> sophonsoar_20220728_models.DescribeFieldResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_field_with_options(request, runtime)

    async def describe_field_async(
        self,
        request: sophonsoar_20220728_models.DescribeFieldRequest,
    ) -> sophonsoar_20220728_models.DescribeFieldResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_field_with_options_async(request, runtime)

    def describe_latest_record_schema_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeLatestRecordSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLatestRecordSchema',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_latest_record_schema_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeLatestRecordSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLatestRecordSchema',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_latest_record_schema(
        self,
        request: sophonsoar_20220728_models.DescribeLatestRecordSchemaRequest,
    ) -> sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_latest_record_schema_with_options(request, runtime)

    async def describe_latest_record_schema_async(
        self,
        request: sophonsoar_20220728_models.DescribeLatestRecordSchemaRequest,
    ) -> sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_latest_record_schema_with_options_async(request, runtime)

    def describe_node_param_tags_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeNodeParamTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeNodeParamTagsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeParamTags',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeNodeParamTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_param_tags_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeNodeParamTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeNodeParamTagsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeParamTags',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeNodeParamTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_param_tags(
        self,
        request: sophonsoar_20220728_models.DescribeNodeParamTagsRequest,
    ) -> sophonsoar_20220728_models.DescribeNodeParamTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_node_param_tags_with_options(request, runtime)

    async def describe_node_param_tags_async(
        self,
        request: sophonsoar_20220728_models.DescribeNodeParamTagsRequest,
    ) -> sophonsoar_20220728_models.DescribeNodeParamTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_param_tags_with_options_async(request, runtime)

    def describe_node_used_infos_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeNodeUsedInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeNodeUsedInfosResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeUsedInfos',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeNodeUsedInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_used_infos_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeNodeUsedInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeNodeUsedInfosResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeUsedInfos',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeNodeUsedInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_used_infos(
        self,
        request: sophonsoar_20220728_models.DescribeNodeUsedInfosRequest,
    ) -> sophonsoar_20220728_models.DescribeNodeUsedInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_node_used_infos_with_options(request, runtime)

    async def describe_node_used_infos_async(
        self,
        request: sophonsoar_20220728_models.DescribeNodeUsedInfosRequest,
    ) -> sophonsoar_20220728_models.DescribeNodeUsedInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_used_infos_with_options_async(request, runtime)

    def describe_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_with_options(request, runtime)

    async def describe_playbook_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_with_options_async(request, runtime)

    def describe_playbook_input_output_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookInputOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookInputOutputResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookInputOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookInputOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_input_output_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookInputOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookInputOutputResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookInputOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookInputOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook_input_output(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookInputOutputRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookInputOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_input_output_with_options(request, runtime)

    async def describe_playbook_input_output_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookInputOutputRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookInputOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_input_output_with_options_async(request, runtime)

    def describe_playbook_metrics_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookMetricsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookMetrics',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_metrics_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookMetricsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookMetrics',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook_metrics(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookMetricsRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_metrics_with_options(request, runtime)

    async def describe_playbook_metrics_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookMetricsRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_metrics_with_options_async(request, runtime)

    def describe_playbook_nodes_output_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNodesOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookNodesOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_nodes_output_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNodesOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookNodesOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook_nodes_output(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNodesOutputRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_nodes_output_with_options(request, runtime)

    async def describe_playbook_nodes_output_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNodesOutputRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_nodes_output_with_options_async(request, runtime)

    def describe_playbook_number_metrics_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNumberMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookNumberMetrics',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_number_metrics_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNumberMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookNumberMetrics',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook_number_metrics(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNumberMetricsRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_number_metrics_with_options(request, runtime)

    async def describe_playbook_number_metrics_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNumberMetricsRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_number_metrics_with_options_async(request, runtime)

    def describe_playbook_releases_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookReleasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookReleasesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookReleases',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookReleasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbook_releases_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookReleasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookReleasesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookReleases',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookReleasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbook_releases(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookReleasesRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookReleasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_releases_with_options(request, runtime)

    async def describe_playbook_releases_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookReleasesRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookReleasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_releases_with_options_async(request, runtime)

    def describe_playbooks_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybooksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybooks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_playbooks_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybooksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybooks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_playbooks(
        self,
        request: sophonsoar_20220728_models.DescribePlaybooksRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybooksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_playbooks_with_options(request, runtime)

    async def describe_playbooks_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybooksRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybooksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbooks_with_options_async(request, runtime)

    def describe_pop_api_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePopApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePopApiResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApi',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePopApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pop_api_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePopApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePopApiResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApi',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePopApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pop_api(
        self,
        request: sophonsoar_20220728_models.DescribePopApiRequest,
    ) -> sophonsoar_20220728_models.DescribePopApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pop_api_with_options(request, runtime)

    async def describe_pop_api_async(
        self,
        request: sophonsoar_20220728_models.DescribePopApiRequest,
    ) -> sophonsoar_20220728_models.DescribePopApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pop_api_with_options_async(request, runtime)

    def describe_pop_api_item_list_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePopApiItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePopApiItemListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApiItemList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePopApiItemListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pop_api_item_list_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePopApiItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePopApiItemListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApiItemList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePopApiItemListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pop_api_item_list(
        self,
        request: sophonsoar_20220728_models.DescribePopApiItemListRequest,
    ) -> sophonsoar_20220728_models.DescribePopApiItemListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pop_api_item_list_with_options(request, runtime)

    async def describe_pop_api_item_list_async(
        self,
        request: sophonsoar_20220728_models.DescribePopApiItemListRequest,
    ) -> sophonsoar_20220728_models.DescribePopApiItemListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pop_api_item_list_with_options_async(request, runtime)

    def describe_pop_api_version_list_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePopApiVersionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePopApiVersionListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApiVersionList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePopApiVersionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pop_api_version_list_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePopApiVersionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePopApiVersionListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApiVersionList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePopApiVersionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pop_api_version_list(
        self,
        request: sophonsoar_20220728_models.DescribePopApiVersionListRequest,
    ) -> sophonsoar_20220728_models.DescribePopApiVersionListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pop_api_version_list_with_options(request, runtime)

    async def describe_pop_api_version_list_async(
        self,
        request: sophonsoar_20220728_models.DescribePopApiVersionListRequest,
    ) -> sophonsoar_20220728_models.DescribePopApiVersionListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pop_api_version_list_with_options_async(request, runtime)

    def describe_process_tasks_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeProcessTasksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessTasks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeProcessTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_process_tasks_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeProcessTasksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessTasks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeProcessTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_process_tasks(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTasksRequest,
    ) -> sophonsoar_20220728_models.DescribeProcessTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_process_tasks_with_options(request, runtime)

    async def describe_process_tasks_async(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTasksRequest,
    ) -> sophonsoar_20220728_models.DescribeProcessTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_process_tasks_with_options_async(request, runtime)

    def describe_soar_record_action_output_list_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordActionOutputListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecordActionOutputList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_soar_record_action_output_list_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordActionOutputListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecordActionOutputList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_soar_record_action_output_list(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordActionOutputListRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_record_action_output_list_with_options(request, runtime)

    async def describe_soar_record_action_output_list_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordActionOutputListRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_soar_record_action_output_list_with_options_async(request, runtime)

    def describe_soar_record_in_output_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordInOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecordInOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_soar_record_in_output_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordInOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecordInOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_soar_record_in_output(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordInOutputRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_record_in_output_with_options(request, runtime)

    async def describe_soar_record_in_output_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordInOutputRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_soar_record_in_output_with_options_async(request, runtime)

    def describe_soar_records_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecords',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_soar_records_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecords',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_soar_records(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordsRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_records_with_options(request, runtime)

    async def describe_soar_records_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordsRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_soar_records_with_options_async(request, runtime)

    def describe_soar_task_and_actions_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeSoarTaskAndActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarTaskAndActions',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_soar_task_and_actions_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarTaskAndActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarTaskAndActions',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_soar_task_and_actions(
        self,
        request: sophonsoar_20220728_models.DescribeSoarTaskAndActionsRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_task_and_actions_with_options(request, runtime)

    async def describe_soar_task_and_actions_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarTaskAndActionsRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_soar_task_and_actions_with_options_async(request, runtime)

    def describe_sophon_commands_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeSophonCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSophonCommandsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSophonCommands',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSophonCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sophon_commands_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeSophonCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSophonCommandsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSophonCommands',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSophonCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sophon_commands(
        self,
        request: sophonsoar_20220728_models.DescribeSophonCommandsRequest,
    ) -> sophonsoar_20220728_models.DescribeSophonCommandsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sophon_commands_with_options(request, runtime)

    async def describe_sophon_commands_async(
        self,
        request: sophonsoar_20220728_models.DescribeSophonCommandsRequest,
    ) -> sophonsoar_20220728_models.DescribeSophonCommandsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sophon_commands_with_options_async(request, runtime)

    def describer_python_3script_logs_with_options(
        self,
        request: sophonsoar_20220728_models.DescriberPython3ScriptLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescriberPython3ScriptLogs',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describer_python_3script_logs_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescriberPython3ScriptLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescriberPython3ScriptLogs',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describer_python_3script_logs(
        self,
        request: sophonsoar_20220728_models.DescriberPython3ScriptLogsRequest,
    ) -> sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describer_python_3script_logs_with_options(request, runtime)

    async def describer_python_3script_logs_async(
        self,
        request: sophonsoar_20220728_models.DescriberPython3ScriptLogsRequest,
    ) -> sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describer_python_3script_logs_with_options_async(request, runtime)

    def modify_component_asset_with_options(
        self,
        request: sophonsoar_20220728_models.ModifyComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyComponentAssetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_config):
            query['AssetConfig'] = request.asset_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyComponentAsset',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyComponentAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_component_asset_with_options_async(
        self,
        request: sophonsoar_20220728_models.ModifyComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyComponentAssetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_config):
            query['AssetConfig'] = request.asset_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyComponentAsset',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyComponentAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_component_asset(
        self,
        request: sophonsoar_20220728_models.ModifyComponentAssetRequest,
    ) -> sophonsoar_20220728_models.ModifyComponentAssetResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_component_asset_with_options(request, runtime)

    async def modify_component_asset_async(
        self,
        request: sophonsoar_20220728_models.ModifyComponentAssetRequest,
    ) -> sophonsoar_20220728_models.ModifyComponentAssetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_component_asset_with_options_async(request, runtime)

    def modify_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_playbook(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_playbook_with_options(request, runtime)

    async def modify_playbook_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_playbook_with_options_async(request, runtime)

    def modify_playbook_input_output_with_options(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInputOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exe_config):
            body['ExeConfig'] = request.exe_config
        if not UtilClient.is_unset(request.input_params):
            body['InputParams'] = request.input_params
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.output_params):
            body['OutputParams'] = request.output_params
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybookInputOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_playbook_input_output_with_options_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInputOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exe_config):
            body['ExeConfig'] = request.exe_config
        if not UtilClient.is_unset(request.input_params):
            body['InputParams'] = request.input_params
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.output_params):
            body['OutputParams'] = request.output_params
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybookInputOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_playbook_input_output(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInputOutputRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_playbook_input_output_with_options(request, runtime)

    async def modify_playbook_input_output_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInputOutputRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_playbook_input_output_with_options_async(request, runtime)

    def modify_playbook_instance_status_with_options(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybookInstanceStatus',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_playbook_instance_status_with_options_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybookInstanceStatus',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_playbook_instance_status(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInstanceStatusRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_playbook_instance_status_with_options(request, runtime)

    async def modify_playbook_instance_status_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInstanceStatusRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_playbook_instance_status_with_options_async(request, runtime)

    def publish_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.PublishPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.PublishPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.PublishPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.PublishPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.PublishPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.PublishPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_playbook(
        self,
        request: sophonsoar_20220728_models.PublishPlaybookRequest,
    ) -> sophonsoar_20220728_models.PublishPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_playbook_with_options(request, runtime)

    async def publish_playbook_async(
        self,
        request: sophonsoar_20220728_models.PublishPlaybookRequest,
    ) -> sophonsoar_20220728_models.PublishPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_playbook_with_options_async(request, runtime)

    def query_tree_data_with_options(
        self,
        request: sophonsoar_20220728_models.QueryTreeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.QueryTreeDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTreeData',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.QueryTreeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tree_data_with_options_async(
        self,
        request: sophonsoar_20220728_models.QueryTreeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.QueryTreeDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTreeData',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.QueryTreeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tree_data(
        self,
        request: sophonsoar_20220728_models.QueryTreeDataRequest,
    ) -> sophonsoar_20220728_models.QueryTreeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_tree_data_with_options(request, runtime)

    async def query_tree_data_async(
        self,
        request: sophonsoar_20220728_models.QueryTreeDataRequest,
    ) -> sophonsoar_20220728_models.QueryTreeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_tree_data_with_options_async(request, runtime)

    def rename_playbook_node_with_options(
        self,
        request: sophonsoar_20220728_models.RenamePlaybookNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RenamePlaybookNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_node_name):
            query['NewNodeName'] = request.new_node_name
        if not UtilClient.is_unset(request.old_node_name):
            query['OldNodeName'] = request.old_node_name
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenamePlaybookNode',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.RenamePlaybookNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_playbook_node_with_options_async(
        self,
        request: sophonsoar_20220728_models.RenamePlaybookNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RenamePlaybookNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_node_name):
            query['NewNodeName'] = request.new_node_name
        if not UtilClient.is_unset(request.old_node_name):
            query['OldNodeName'] = request.old_node_name
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenamePlaybookNode',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.RenamePlaybookNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_playbook_node(
        self,
        request: sophonsoar_20220728_models.RenamePlaybookNodeRequest,
    ) -> sophonsoar_20220728_models.RenamePlaybookNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.rename_playbook_node_with_options(request, runtime)

    async def rename_playbook_node_async(
        self,
        request: sophonsoar_20220728_models.RenamePlaybookNodeRequest,
    ) -> sophonsoar_20220728_models.RenamePlaybookNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rename_playbook_node_with_options_async(request, runtime)

    def revert_playbook_release_with_options(
        self,
        request: sophonsoar_20220728_models.RevertPlaybookReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RevertPlaybookReleaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_publish):
            body['IsPublish'] = request.is_publish
        if not UtilClient.is_unset(request.play_release_id):
            body['PlayReleaseId'] = request.play_release_id
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevertPlaybookRelease',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.RevertPlaybookReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def revert_playbook_release_with_options_async(
        self,
        request: sophonsoar_20220728_models.RevertPlaybookReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RevertPlaybookReleaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_publish):
            body['IsPublish'] = request.is_publish
        if not UtilClient.is_unset(request.play_release_id):
            body['PlayReleaseId'] = request.play_release_id
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevertPlaybookRelease',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.RevertPlaybookReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revert_playbook_release(
        self,
        request: sophonsoar_20220728_models.RevertPlaybookReleaseRequest,
    ) -> sophonsoar_20220728_models.RevertPlaybookReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.revert_playbook_release_with_options(request, runtime)

    async def revert_playbook_release_async(
        self,
        request: sophonsoar_20220728_models.RevertPlaybookReleaseRequest,
    ) -> sophonsoar_20220728_models.RevertPlaybookReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revert_playbook_release_with_options_async(request, runtime)

    def run_python_3script_with_options(
        self,
        request: sophonsoar_20220728_models.RunPython3ScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RunPython3ScriptResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: RunPython3ScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunPython3ScriptResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.python_script):
            body['PythonScript'] = request.python_script
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunPython3Script',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.RunPython3ScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_python_3script_with_options_async(
        self,
        request: sophonsoar_20220728_models.RunPython3ScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RunPython3ScriptResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: RunPython3ScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunPython3ScriptResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.python_script):
            body['PythonScript'] = request.python_script
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunPython3Script',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.RunPython3ScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_python_3script(
        self,
        request: sophonsoar_20220728_models.RunPython3ScriptRequest,
    ) -> sophonsoar_20220728_models.RunPython3ScriptResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: RunPython3ScriptRequest
        @return: RunPython3ScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_python_3script_with_options(request, runtime)

    async def run_python_3script_async(
        self,
        request: sophonsoar_20220728_models.RunPython3ScriptRequest,
    ) -> sophonsoar_20220728_models.RunPython3ScriptResponse:
        """
        Before you call this operation, make sure that you understand the billing method and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: RunPython3ScriptRequest
        @return: RunPython3ScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_python_3script_with_options_async(request, runtime)

    def trigger_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.TriggerPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerPlaybookResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: TriggerPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input_param):
            body['InputParam'] = request.input_param
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.TriggerPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.TriggerPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerPlaybookResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: TriggerPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input_param):
            body['InputParam'] = request.input_param
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.TriggerPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_playbook(
        self,
        request: sophonsoar_20220728_models.TriggerPlaybookRequest,
    ) -> sophonsoar_20220728_models.TriggerPlaybookResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: TriggerPlaybookRequest
        @return: TriggerPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_playbook_with_options(request, runtime)

    async def trigger_playbook_async(
        self,
        request: sophonsoar_20220728_models.TriggerPlaybookRequest,
    ) -> sophonsoar_20220728_models.TriggerPlaybookResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: TriggerPlaybookRequest
        @return: TriggerPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.trigger_playbook_with_options_async(request, runtime)

    def trigger_process_task_with_options(
        self,
        request: sophonsoar_20220728_models.TriggerProcessTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerProcessTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerProcessTask',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.TriggerProcessTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_process_task_with_options_async(
        self,
        request: sophonsoar_20220728_models.TriggerProcessTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerProcessTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerProcessTask',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.TriggerProcessTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_process_task(
        self,
        request: sophonsoar_20220728_models.TriggerProcessTaskRequest,
    ) -> sophonsoar_20220728_models.TriggerProcessTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.trigger_process_task_with_options(request, runtime)

    async def trigger_process_task_async(
        self,
        request: sophonsoar_20220728_models.TriggerProcessTaskRequest,
    ) -> sophonsoar_20220728_models.TriggerProcessTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.trigger_process_task_with_options_async(request, runtime)

    def trigger_sophon_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.TriggerSophonPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerSophonPlaybookResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: TriggerSophonPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerSophonPlaybookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_name):
            query['CommandName'] = request.command_name
        if not UtilClient.is_unset(request.input_params):
            query['InputParams'] = request.input_params
        if not UtilClient.is_unset(request.sophon_task_id):
            query['SophonTaskId'] = request.sophon_task_id
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerSophonPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.TriggerSophonPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_sophon_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.TriggerSophonPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerSophonPlaybookResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: TriggerSophonPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerSophonPlaybookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_name):
            query['CommandName'] = request.command_name
        if not UtilClient.is_unset(request.input_params):
            query['InputParams'] = request.input_params
        if not UtilClient.is_unset(request.sophon_task_id):
            query['SophonTaskId'] = request.sophon_task_id
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerSophonPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.TriggerSophonPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_sophon_playbook(
        self,
        request: sophonsoar_20220728_models.TriggerSophonPlaybookRequest,
    ) -> sophonsoar_20220728_models.TriggerSophonPlaybookResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: TriggerSophonPlaybookRequest
        @return: TriggerSophonPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_sophon_playbook_with_options(request, runtime)

    async def trigger_sophon_playbook_async(
        self,
        request: sophonsoar_20220728_models.TriggerSophonPlaybookRequest,
    ) -> sophonsoar_20220728_models.TriggerSophonPlaybookResponse:
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        
        @param request: TriggerSophonPlaybookRequest
        @return: TriggerSophonPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.trigger_sophon_playbook_with_options_async(request, runtime)

    def verify_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.VerifyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.VerifyPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.task_flow):
            body['TaskFlow'] = request.task_flow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.VerifyPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.VerifyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.VerifyPlaybookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.task_flow):
            body['TaskFlow'] = request.task_flow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.VerifyPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_playbook(
        self,
        request: sophonsoar_20220728_models.VerifyPlaybookRequest,
    ) -> sophonsoar_20220728_models.VerifyPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_playbook_with_options(request, runtime)

    async def verify_playbook_async(
        self,
        request: sophonsoar_20220728_models.VerifyPlaybookRequest,
    ) -> sophonsoar_20220728_models.VerifyPlaybookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_playbook_with_options_async(request, runtime)

    def verify_python_file_with_options(
        self,
        request: sophonsoar_20220728_models.VerifyPythonFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.VerifyPythonFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyPythonFile',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.VerifyPythonFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_python_file_with_options_async(
        self,
        request: sophonsoar_20220728_models.VerifyPythonFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.VerifyPythonFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyPythonFile',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.VerifyPythonFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_python_file(
        self,
        request: sophonsoar_20220728_models.VerifyPythonFileRequest,
    ) -> sophonsoar_20220728_models.VerifyPythonFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_python_file_with_options(request, runtime)

    async def verify_python_file_async(
        self,
        request: sophonsoar_20220728_models.VerifyPythonFileRequest,
    ) -> sophonsoar_20220728_models.VerifyPythonFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_python_file_with_options_async(request, runtime)
