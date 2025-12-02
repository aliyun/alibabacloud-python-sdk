# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sophonsoar20250903 import models as sophonsoar_20250903_models
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

    def create_component_asset_with_options(
        self,
        request: sophonsoar_20250903_models.CreateComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.CreateComponentAssetResponse:
        """
        @summary Create Component Asset.
        
        @description Please ensure that you fully understand the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the response orchestration product (i.e., Threat Analysis and Response Log Ingress Traffic) before using this interface.
        
        @param request: CreateComponentAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateComponentAssetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_asset_name):
            body['ComponentAssetName'] = request.component_asset_name
        body_flat = {}
        if not UtilClient.is_unset(request.component_asset_values):
            body_flat['ComponentAssetValues'] = request.component_asset_values
        if not UtilClient.is_unset(request.component_name):
            body['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComponentAsset',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.CreateComponentAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_component_asset_with_options_async(
        self,
        request: sophonsoar_20250903_models.CreateComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.CreateComponentAssetResponse:
        """
        @summary Create Component Asset.
        
        @description Please ensure that you fully understand the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the response orchestration product (i.e., Threat Analysis and Response Log Ingress Traffic) before using this interface.
        
        @param request: CreateComponentAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateComponentAssetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_asset_name):
            body['ComponentAssetName'] = request.component_asset_name
        body_flat = {}
        if not UtilClient.is_unset(request.component_asset_values):
            body_flat['ComponentAssetValues'] = request.component_asset_values
        if not UtilClient.is_unset(request.component_name):
            body['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComponentAsset',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.CreateComponentAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_component_asset(
        self,
        request: sophonsoar_20250903_models.CreateComponentAssetRequest,
    ) -> sophonsoar_20250903_models.CreateComponentAssetResponse:
        """
        @summary Create Component Asset.
        
        @description Please ensure that you fully understand the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the response orchestration product (i.e., Threat Analysis and Response Log Ingress Traffic) before using this interface.
        
        @param request: CreateComponentAssetRequest
        @return: CreateComponentAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_component_asset_with_options(request, runtime)

    async def create_component_asset_async(
        self,
        request: sophonsoar_20250903_models.CreateComponentAssetRequest,
    ) -> sophonsoar_20250903_models.CreateComponentAssetResponse:
        """
        @summary Create Component Asset.
        
        @description Please ensure that you fully understand the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the response orchestration product (i.e., Threat Analysis and Response Log Ingress Traffic) before using this interface.
        
        @param request: CreateComponentAssetRequest
        @return: CreateComponentAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_component_asset_with_options_async(request, runtime)

    def create_playbook_with_options(
        self,
        request: sophonsoar_20250903_models.CreatePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.CreatePlaybookResponse:
        """
        @summary Create Playbook.
        
        @param request: CreatePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_description):
            body['PlaybookDescription'] = request.playbook_description
        body_flat = {}
        if not UtilClient.is_unset(request.playbook_input_configs):
            body_flat['PlaybookInputConfigs'] = request.playbook_input_configs
        if not UtilClient.is_unset(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not UtilClient.is_unset(request.playbook_output_configs):
            body_flat['PlaybookOutputConfigs'] = request.playbook_output_configs
        if not UtilClient.is_unset(request.playbook_param_type):
            body['PlaybookParamType'] = request.playbook_param_type
        if not UtilClient.is_unset(request.playbook_task_flow):
            body['PlaybookTaskFlow'] = request.playbook_task_flow
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.src_playbook_uuid):
            body['SrcPlaybookUuid'] = request.src_playbook_uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlaybook',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.CreatePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_playbook_with_options_async(
        self,
        request: sophonsoar_20250903_models.CreatePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.CreatePlaybookResponse:
        """
        @summary Create Playbook.
        
        @param request: CreatePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_description):
            body['PlaybookDescription'] = request.playbook_description
        body_flat = {}
        if not UtilClient.is_unset(request.playbook_input_configs):
            body_flat['PlaybookInputConfigs'] = request.playbook_input_configs
        if not UtilClient.is_unset(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not UtilClient.is_unset(request.playbook_output_configs):
            body_flat['PlaybookOutputConfigs'] = request.playbook_output_configs
        if not UtilClient.is_unset(request.playbook_param_type):
            body['PlaybookParamType'] = request.playbook_param_type
        if not UtilClient.is_unset(request.playbook_task_flow):
            body['PlaybookTaskFlow'] = request.playbook_task_flow
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.src_playbook_uuid):
            body['SrcPlaybookUuid'] = request.src_playbook_uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlaybook',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.CreatePlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_playbook(
        self,
        request: sophonsoar_20250903_models.CreatePlaybookRequest,
    ) -> sophonsoar_20250903_models.CreatePlaybookResponse:
        """
        @summary Create Playbook.
        
        @param request: CreatePlaybookRequest
        @return: CreatePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_playbook_with_options(request, runtime)

    async def create_playbook_async(
        self,
        request: sophonsoar_20250903_models.CreatePlaybookRequest,
    ) -> sophonsoar_20250903_models.CreatePlaybookResponse:
        """
        @summary Create Playbook.
        
        @param request: CreatePlaybookRequest
        @return: CreatePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_playbook_with_options_async(request, runtime)

    def delete_component_asset_with_options(
        self,
        request: sophonsoar_20250903_models.DeleteComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.DeleteComponentAssetResponse:
        """
        @summary Delete Component Asset.
        
        @description Please ensure that before using this interface, you have fully understood the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the response orchestration product (i.e., Threat Analysis and Response Log Access Traffic).
        
        @param request: DeleteComponentAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteComponentAssetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteComponentAsset',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.DeleteComponentAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_component_asset_with_options_async(
        self,
        request: sophonsoar_20250903_models.DeleteComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.DeleteComponentAssetResponse:
        """
        @summary Delete Component Asset.
        
        @description Please ensure that before using this interface, you have fully understood the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the response orchestration product (i.e., Threat Analysis and Response Log Access Traffic).
        
        @param request: DeleteComponentAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteComponentAssetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteComponentAsset',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.DeleteComponentAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_component_asset(
        self,
        request: sophonsoar_20250903_models.DeleteComponentAssetRequest,
    ) -> sophonsoar_20250903_models.DeleteComponentAssetResponse:
        """
        @summary Delete Component Asset.
        
        @description Please ensure that before using this interface, you have fully understood the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the response orchestration product (i.e., Threat Analysis and Response Log Access Traffic).
        
        @param request: DeleteComponentAssetRequest
        @return: DeleteComponentAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_component_asset_with_options(request, runtime)

    async def delete_component_asset_async(
        self,
        request: sophonsoar_20250903_models.DeleteComponentAssetRequest,
    ) -> sophonsoar_20250903_models.DeleteComponentAssetResponse:
        """
        @summary Delete Component Asset.
        
        @description Please ensure that before using this interface, you have fully understood the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the response orchestration product (i.e., Threat Analysis and Response Log Access Traffic).
        
        @param request: DeleteComponentAssetRequest
        @return: DeleteComponentAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_component_asset_with_options_async(request, runtime)

    def delete_playbook_with_options(
        self,
        request: sophonsoar_20250903_models.DeletePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.DeletePlaybookResponse:
        """
        @summary Delete Playbook.
        
        @param request: DeletePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePlaybook',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.DeletePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_playbook_with_options_async(
        self,
        request: sophonsoar_20250903_models.DeletePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.DeletePlaybookResponse:
        """
        @summary Delete Playbook.
        
        @param request: DeletePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePlaybook',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.DeletePlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_playbook(
        self,
        request: sophonsoar_20250903_models.DeletePlaybookRequest,
    ) -> sophonsoar_20250903_models.DeletePlaybookResponse:
        """
        @summary Delete Playbook.
        
        @param request: DeletePlaybookRequest
        @return: DeletePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_playbook_with_options(request, runtime)

    async def delete_playbook_async(
        self,
        request: sophonsoar_20250903_models.DeletePlaybookRequest,
    ) -> sophonsoar_20250903_models.DeletePlaybookResponse:
        """
        @summary Delete Playbook.
        
        @param request: DeletePlaybookRequest
        @return: DeletePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_playbook_with_options_async(request, runtime)

    def get_playbook_with_options(
        self,
        request: sophonsoar_20250903_models.GetPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.GetPlaybookResponse:
        """
        @summary Get playbook details.
        
        @param request: GetPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.playbook_version):
            body['PlaybookVersion'] = request.playbook_version
        if not UtilClient.is_unset(request.playbook_version_type):
            body['PlaybookVersionType'] = request.playbook_version_type
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPlaybook',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.GetPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_playbook_with_options_async(
        self,
        request: sophonsoar_20250903_models.GetPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.GetPlaybookResponse:
        """
        @summary Get playbook details.
        
        @param request: GetPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.playbook_version):
            body['PlaybookVersion'] = request.playbook_version
        if not UtilClient.is_unset(request.playbook_version_type):
            body['PlaybookVersionType'] = request.playbook_version_type
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPlaybook',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.GetPlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_playbook(
        self,
        request: sophonsoar_20250903_models.GetPlaybookRequest,
    ) -> sophonsoar_20250903_models.GetPlaybookResponse:
        """
        @summary Get playbook details.
        
        @param request: GetPlaybookRequest
        @return: GetPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_playbook_with_options(request, runtime)

    async def get_playbook_async(
        self,
        request: sophonsoar_20250903_models.GetPlaybookRequest,
    ) -> sophonsoar_20250903_models.GetPlaybookResponse:
        """
        @summary Get playbook details.
        
        @param request: GetPlaybookRequest
        @return: GetPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_playbook_with_options_async(request, runtime)

    def list_component_assets_with_options(
        self,
        request: sophonsoar_20250903_models.ListComponentAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.ListComponentAssetsResponse:
        """
        @summary Get the list of assets configured for a component.
        
        @param request: ListComponentAssetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComponentAssetsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        if not UtilClient.is_unset(request.component_name):
            body['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComponentAssets',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.ListComponentAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_component_assets_with_options_async(
        self,
        request: sophonsoar_20250903_models.ListComponentAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.ListComponentAssetsResponse:
        """
        @summary Get the list of assets configured for a component.
        
        @param request: ListComponentAssetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComponentAssetsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        if not UtilClient.is_unset(request.component_name):
            body['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComponentAssets',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.ListComponentAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_component_assets(
        self,
        request: sophonsoar_20250903_models.ListComponentAssetsRequest,
    ) -> sophonsoar_20250903_models.ListComponentAssetsResponse:
        """
        @summary Get the list of assets configured for a component.
        
        @param request: ListComponentAssetsRequest
        @return: ListComponentAssetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_component_assets_with_options(request, runtime)

    async def list_component_assets_async(
        self,
        request: sophonsoar_20250903_models.ListComponentAssetsRequest,
    ) -> sophonsoar_20250903_models.ListComponentAssetsResponse:
        """
        @summary Get the list of assets configured for a component.
        
        @param request: ListComponentAssetsRequest
        @return: ListComponentAssetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_component_assets_with_options_async(request, runtime)

    def list_components_with_options(
        self,
        request: sophonsoar_20250903_models.ListComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.ListComponentsResponse:
        """
        @summary Get Component List.
        
        @param request: ListComponentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComponentsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_name):
            body['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: sophonsoar_20250903_models.ListComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.ListComponentsResponse:
        """
        @summary Get Component List.
        
        @param request: ListComponentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComponentsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_name):
            body['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(
        self,
        request: sophonsoar_20250903_models.ListComponentsRequest,
    ) -> sophonsoar_20250903_models.ListComponentsResponse:
        """
        @summary Get Component List.
        
        @param request: ListComponentsRequest
        @return: ListComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_components_with_options(request, runtime)

    async def list_components_async(
        self,
        request: sophonsoar_20250903_models.ListComponentsRequest,
    ) -> sophonsoar_20250903_models.ListComponentsResponse:
        """
        @summary Get Component List.
        
        @param request: ListComponentsRequest
        @return: ListComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_components_with_options_async(request, runtime)

    def list_playbooks_with_options(
        self,
        tmp_req: sophonsoar_20250903_models.ListPlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.ListPlaybooksResponse:
        """
        @summary Get Playbook List.
        
        @param tmp_req: ListPlaybooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPlaybooksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sophonsoar_20250903_models.ListPlaybooksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.playbook_param_types):
            request.playbook_param_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.playbook_param_types, 'PlaybookParamTypes', 'simple')
        if not UtilClient.is_unset(tmp_req.playbook_uuids):
            request.playbook_uuids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.playbook_uuids, 'PlaybookUuids', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.playbook_execution_end_time):
            body['PlaybookExecutionEndTime'] = request.playbook_execution_end_time
        if not UtilClient.is_unset(request.playbook_execution_start_time):
            body['PlaybookExecutionStartTime'] = request.playbook_execution_start_time
        if not UtilClient.is_unset(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not UtilClient.is_unset(request.playbook_param_types_shrink):
            body['PlaybookParamTypes'] = request.playbook_param_types_shrink
        if not UtilClient.is_unset(request.playbook_status):
            body['PlaybookStatus'] = request.playbook_status
        if not UtilClient.is_unset(request.playbook_type):
            body['PlaybookType'] = request.playbook_type
        if not UtilClient.is_unset(request.playbook_uuids_shrink):
            body['PlaybookUuids'] = request.playbook_uuids_shrink
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPlaybooks',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.ListPlaybooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_playbooks_with_options_async(
        self,
        tmp_req: sophonsoar_20250903_models.ListPlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.ListPlaybooksResponse:
        """
        @summary Get Playbook List.
        
        @param tmp_req: ListPlaybooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPlaybooksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sophonsoar_20250903_models.ListPlaybooksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.playbook_param_types):
            request.playbook_param_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.playbook_param_types, 'PlaybookParamTypes', 'simple')
        if not UtilClient.is_unset(tmp_req.playbook_uuids):
            request.playbook_uuids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.playbook_uuids, 'PlaybookUuids', 'simple')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.playbook_execution_end_time):
            body['PlaybookExecutionEndTime'] = request.playbook_execution_end_time
        if not UtilClient.is_unset(request.playbook_execution_start_time):
            body['PlaybookExecutionStartTime'] = request.playbook_execution_start_time
        if not UtilClient.is_unset(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not UtilClient.is_unset(request.playbook_param_types_shrink):
            body['PlaybookParamTypes'] = request.playbook_param_types_shrink
        if not UtilClient.is_unset(request.playbook_status):
            body['PlaybookStatus'] = request.playbook_status
        if not UtilClient.is_unset(request.playbook_type):
            body['PlaybookType'] = request.playbook_type
        if not UtilClient.is_unset(request.playbook_uuids_shrink):
            body['PlaybookUuids'] = request.playbook_uuids_shrink
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPlaybooks',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.ListPlaybooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_playbooks(
        self,
        request: sophonsoar_20250903_models.ListPlaybooksRequest,
    ) -> sophonsoar_20250903_models.ListPlaybooksResponse:
        """
        @summary Get Playbook List.
        
        @param request: ListPlaybooksRequest
        @return: ListPlaybooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_playbooks_with_options(request, runtime)

    async def list_playbooks_async(
        self,
        request: sophonsoar_20250903_models.ListPlaybooksRequest,
    ) -> sophonsoar_20250903_models.ListPlaybooksResponse:
        """
        @summary Get Playbook List.
        
        @param request: ListPlaybooksRequest
        @return: ListPlaybooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_playbooks_with_options_async(request, runtime)

    def update_component_asset_with_options(
        self,
        request: sophonsoar_20250903_models.UpdateComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.UpdateComponentAssetResponse:
        """
        @summary Update Component Asset.
        
        @param request: UpdateComponentAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateComponentAssetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_asset_name):
            body['ComponentAssetName'] = request.component_asset_name
        if not UtilClient.is_unset(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        body_flat = {}
        if not UtilClient.is_unset(request.component_asset_values):
            body_flat['ComponentAssetValues'] = request.component_asset_values
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateComponentAsset',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.UpdateComponentAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_component_asset_with_options_async(
        self,
        request: sophonsoar_20250903_models.UpdateComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.UpdateComponentAssetResponse:
        """
        @summary Update Component Asset.
        
        @param request: UpdateComponentAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateComponentAssetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_asset_name):
            body['ComponentAssetName'] = request.component_asset_name
        if not UtilClient.is_unset(request.component_asset_uuid):
            body['ComponentAssetUuid'] = request.component_asset_uuid
        body_flat = {}
        if not UtilClient.is_unset(request.component_asset_values):
            body_flat['ComponentAssetValues'] = request.component_asset_values
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateComponentAsset',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.UpdateComponentAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_component_asset(
        self,
        request: sophonsoar_20250903_models.UpdateComponentAssetRequest,
    ) -> sophonsoar_20250903_models.UpdateComponentAssetResponse:
        """
        @summary Update Component Asset.
        
        @param request: UpdateComponentAssetRequest
        @return: UpdateComponentAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_component_asset_with_options(request, runtime)

    async def update_component_asset_async(
        self,
        request: sophonsoar_20250903_models.UpdateComponentAssetRequest,
    ) -> sophonsoar_20250903_models.UpdateComponentAssetResponse:
        """
        @summary Update Component Asset.
        
        @param request: UpdateComponentAssetRequest
        @return: UpdateComponentAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_component_asset_with_options_async(request, runtime)

    def update_playbook_with_options(
        self,
        tmp_req: sophonsoar_20250903_models.UpdatePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.UpdatePlaybookResponse:
        """
        @summary Update Playbook.
        
        @param tmp_req: UpdatePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePlaybookResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sophonsoar_20250903_models.UpdatePlaybookShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.playbook_input_configs):
            request.playbook_input_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.playbook_input_configs, 'PlaybookInputConfigs', 'json')
        if not UtilClient.is_unset(tmp_req.playbook_output_configs):
            request.playbook_output_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.playbook_output_configs, 'PlaybookOutputConfigs', 'json')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_description):
            body['PlaybookDescription'] = request.playbook_description
        if not UtilClient.is_unset(request.playbook_input_configs_shrink):
            body['PlaybookInputConfigs'] = request.playbook_input_configs_shrink
        if not UtilClient.is_unset(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not UtilClient.is_unset(request.playbook_output_configs_shrink):
            body['PlaybookOutputConfigs'] = request.playbook_output_configs_shrink
        if not UtilClient.is_unset(request.playbook_param_type):
            body['PlaybookParamType'] = request.playbook_param_type
        if not UtilClient.is_unset(request.playbook_task_flow):
            body['PlaybookTaskFlow'] = request.playbook_task_flow
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePlaybook',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.UpdatePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_playbook_with_options_async(
        self,
        tmp_req: sophonsoar_20250903_models.UpdatePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20250903_models.UpdatePlaybookResponse:
        """
        @summary Update Playbook.
        
        @param tmp_req: UpdatePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePlaybookResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sophonsoar_20250903_models.UpdatePlaybookShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.playbook_input_configs):
            request.playbook_input_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.playbook_input_configs, 'PlaybookInputConfigs', 'json')
        if not UtilClient.is_unset(tmp_req.playbook_output_configs):
            request.playbook_output_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.playbook_output_configs, 'PlaybookOutputConfigs', 'json')
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_description):
            body['PlaybookDescription'] = request.playbook_description
        if not UtilClient.is_unset(request.playbook_input_configs_shrink):
            body['PlaybookInputConfigs'] = request.playbook_input_configs_shrink
        if not UtilClient.is_unset(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not UtilClient.is_unset(request.playbook_output_configs_shrink):
            body['PlaybookOutputConfigs'] = request.playbook_output_configs_shrink
        if not UtilClient.is_unset(request.playbook_param_type):
            body['PlaybookParamType'] = request.playbook_param_type
        if not UtilClient.is_unset(request.playbook_task_flow):
            body['PlaybookTaskFlow'] = request.playbook_task_flow
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePlaybook',
            version='2025-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20250903_models.UpdatePlaybookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_playbook(
        self,
        request: sophonsoar_20250903_models.UpdatePlaybookRequest,
    ) -> sophonsoar_20250903_models.UpdatePlaybookResponse:
        """
        @summary Update Playbook.
        
        @param request: UpdatePlaybookRequest
        @return: UpdatePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_playbook_with_options(request, runtime)

    async def update_playbook_async(
        self,
        request: sophonsoar_20250903_models.UpdatePlaybookRequest,
    ) -> sophonsoar_20250903_models.UpdatePlaybookResponse:
        """
        @summary Update Playbook.
        
        @param request: UpdatePlaybookRequest
        @return: UpdatePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_playbook_with_options_async(request, runtime)
