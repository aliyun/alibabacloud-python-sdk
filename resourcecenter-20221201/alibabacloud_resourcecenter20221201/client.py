# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_resourcecenter20221201 import models as resource_center_20221201_models
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
        self._endpoint = self.get_endpoint('resourcecenter', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def disable_multi_account_resource_center_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DisableMultiAccountResourceCenterResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableMultiAccountResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DisableMultiAccountResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_multi_account_resource_center_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DisableMultiAccountResourceCenterResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableMultiAccountResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DisableMultiAccountResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_multi_account_resource_center(self) -> resource_center_20221201_models.DisableMultiAccountResourceCenterResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_multi_account_resource_center_with_options(runtime)

    async def disable_multi_account_resource_center_async(self) -> resource_center_20221201_models.DisableMultiAccountResourceCenterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_multi_account_resource_center_with_options_async(runtime)

    def disable_resource_center_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DisableResourceCenterResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DisableResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_resource_center_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DisableResourceCenterResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DisableResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_resource_center(self) -> resource_center_20221201_models.DisableResourceCenterResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_resource_center_with_options(runtime)

    async def disable_resource_center_async(self) -> resource_center_20221201_models.DisableResourceCenterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_resource_center_with_options_async(runtime)

    def enable_multi_account_resource_center_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.EnableMultiAccountResourceCenterResponse:
        """
        If you have created a resource directory for your enterprise, you can enable the cross-account resource search feature by using the management account of the resource directory or a delegated administrator account of Resource Center to view the resources of members in the resource directory. For more information about a resource directory, see [Resource Directory overview](~~200506~~).
        
        @param request: EnableMultiAccountResourceCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableMultiAccountResourceCenterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableMultiAccountResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.EnableMultiAccountResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_multi_account_resource_center_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.EnableMultiAccountResourceCenterResponse:
        """
        If you have created a resource directory for your enterprise, you can enable the cross-account resource search feature by using the management account of the resource directory or a delegated administrator account of Resource Center to view the resources of members in the resource directory. For more information about a resource directory, see [Resource Directory overview](~~200506~~).
        
        @param request: EnableMultiAccountResourceCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableMultiAccountResourceCenterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableMultiAccountResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.EnableMultiAccountResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_multi_account_resource_center(self) -> resource_center_20221201_models.EnableMultiAccountResourceCenterResponse:
        """
        If you have created a resource directory for your enterprise, you can enable the cross-account resource search feature by using the management account of the resource directory or a delegated administrator account of Resource Center to view the resources of members in the resource directory. For more information about a resource directory, see [Resource Directory overview](~~200506~~).
        
        @return: EnableMultiAccountResourceCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_multi_account_resource_center_with_options(runtime)

    async def enable_multi_account_resource_center_async(self) -> resource_center_20221201_models.EnableMultiAccountResourceCenterResponse:
        """
        If you have created a resource directory for your enterprise, you can enable the cross-account resource search feature by using the management account of the resource directory or a delegated administrator account of Resource Center to view the resources of members in the resource directory. For more information about a resource directory, see [Resource Directory overview](~~200506~~).
        
        @return: EnableMultiAccountResourceCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_multi_account_resource_center_with_options_async(runtime)

    def enable_resource_center_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.EnableResourceCenterResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.EnableResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_resource_center_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.EnableResourceCenterResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.EnableResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_resource_center(self) -> resource_center_20221201_models.EnableResourceCenterResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_resource_center_with_options(runtime)

    async def enable_resource_center_async(self) -> resource_center_20221201_models.EnableResourceCenterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_resource_center_with_options_async(runtime)

    def get_multi_account_resource_center_service_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMultiAccountResourceCenterServiceStatus',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_account_resource_center_service_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMultiAccountResourceCenterServiceStatus',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_account_resource_center_service_status(self) -> resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_multi_account_resource_center_service_status_with_options(runtime)

    async def get_multi_account_resource_center_service_status_async(self) -> resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_multi_account_resource_center_service_status_with_options_async(runtime)

    def get_multi_account_resource_configuration_with_options(
        self,
        request: resource_center_20221201_models.GetMultiAccountResourceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiAccountResourceConfiguration',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_account_resource_configuration_with_options_async(
        self,
        request: resource_center_20221201_models.GetMultiAccountResourceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiAccountResourceConfiguration',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_account_resource_configuration(
        self,
        request: resource_center_20221201_models.GetMultiAccountResourceConfigurationRequest,
    ) -> resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_multi_account_resource_configuration_with_options(request, runtime)

    async def get_multi_account_resource_configuration_async(
        self,
        request: resource_center_20221201_models.GetMultiAccountResourceConfigurationRequest,
    ) -> resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_multi_account_resource_configuration_with_options_async(request, runtime)

    def get_resource_center_service_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceCenterServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceCenterServiceStatus',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceCenterServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_center_service_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceCenterServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceCenterServiceStatus',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceCenterServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_center_service_status(self) -> resource_center_20221201_models.GetResourceCenterServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_center_service_status_with_options(runtime)

    async def get_resource_center_service_status_async(self) -> resource_center_20221201_models.GetResourceCenterServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_center_service_status_with_options_async(runtime)

    def get_resource_configuration_with_options(
        self,
        request: resource_center_20221201_models.GetResourceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceConfiguration',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_configuration_with_options_async(
        self,
        request: resource_center_20221201_models.GetResourceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceConfiguration',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_configuration(
        self,
        request: resource_center_20221201_models.GetResourceConfigurationRequest,
    ) -> resource_center_20221201_models.GetResourceConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_configuration_with_options(request, runtime)

    async def get_resource_configuration_async(
        self,
        request: resource_center_20221201_models.GetResourceConfigurationRequest,
    ) -> resource_center_20221201_models.GetResourceConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_configuration_with_options_async(request, runtime)

    def get_resource_counts_with_options(
        self,
        request: resource_center_20221201_models.GetResourceCountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceCountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.group_by_key):
            query['GroupByKey'] = request.group_by_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceCounts',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceCountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_counts_with_options_async(
        self,
        request: resource_center_20221201_models.GetResourceCountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceCountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.group_by_key):
            query['GroupByKey'] = request.group_by_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceCounts',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceCountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_counts(
        self,
        request: resource_center_20221201_models.GetResourceCountsRequest,
    ) -> resource_center_20221201_models.GetResourceCountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_counts_with_options(request, runtime)

    async def get_resource_counts_async(
        self,
        request: resource_center_20221201_models.GetResourceCountsRequest,
    ) -> resource_center_20221201_models.GetResourceCountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_counts_with_options_async(request, runtime)

    def list_multi_account_resource_groups_with_options(
        self,
        request: resource_center_20221201_models.ListMultiAccountResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountResourceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountResourceGroups',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_account_resource_groups_with_options_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountResourceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountResourceGroups',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_account_resource_groups(
        self,
        request: resource_center_20221201_models.ListMultiAccountResourceGroupsRequest,
    ) -> resource_center_20221201_models.ListMultiAccountResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_multi_account_resource_groups_with_options(request, runtime)

    async def list_multi_account_resource_groups_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountResourceGroupsRequest,
    ) -> resource_center_20221201_models.ListMultiAccountResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_multi_account_resource_groups_with_options_async(request, runtime)

    def list_multi_account_tag_keys_with_options(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountTagKeys',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_account_tag_keys_with_options_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountTagKeys',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_account_tag_keys(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagKeysRequest,
    ) -> resource_center_20221201_models.ListMultiAccountTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_multi_account_tag_keys_with_options(request, runtime)

    async def list_multi_account_tag_keys_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagKeysRequest,
    ) -> resource_center_20221201_models.ListMultiAccountTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_multi_account_tag_keys_with_options_async(request, runtime)

    def list_multi_account_tag_values_with_options(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountTagValues',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_account_tag_values_with_options_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountTagValues',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_account_tag_values(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagValuesRequest,
    ) -> resource_center_20221201_models.ListMultiAccountTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_multi_account_tag_values_with_options(request, runtime)

    async def list_multi_account_tag_values_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagValuesRequest,
    ) -> resource_center_20221201_models.ListMultiAccountTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_multi_account_tag_values_with_options_async(request, runtime)

    def list_resource_types_with_options(
        self,
        request: resource_center_20221201_models.ListResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListResourceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        request: resource_center_20221201_models.ListResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListResourceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_types(
        self,
        request: resource_center_20221201_models.ListResourceTypesRequest,
    ) -> resource_center_20221201_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_types_with_options(request, runtime)

    async def list_resource_types_async(
        self,
        request: resource_center_20221201_models.ListResourceTypesRequest,
    ) -> resource_center_20221201_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_types_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: resource_center_20221201_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: resource_center_20221201_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: resource_center_20221201_models.ListTagKeysRequest,
    ) -> resource_center_20221201_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: resource_center_20221201_models.ListTagKeysRequest,
    ) -> resource_center_20221201_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: resource_center_20221201_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: resource_center_20221201_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: resource_center_20221201_models.ListTagValuesRequest,
    ) -> resource_center_20221201_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: resource_center_20221201_models.ListTagValuesRequest,
    ) -> resource_center_20221201_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def search_multi_account_resources_with_options(
        self,
        request: resource_center_20221201_models.SearchMultiAccountResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.SearchMultiAccountResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMultiAccountResources',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.SearchMultiAccountResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_multi_account_resources_with_options_async(
        self,
        request: resource_center_20221201_models.SearchMultiAccountResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.SearchMultiAccountResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMultiAccountResources',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.SearchMultiAccountResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_multi_account_resources(
        self,
        request: resource_center_20221201_models.SearchMultiAccountResourcesRequest,
    ) -> resource_center_20221201_models.SearchMultiAccountResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_multi_account_resources_with_options(request, runtime)

    async def search_multi_account_resources_async(
        self,
        request: resource_center_20221201_models.SearchMultiAccountResourcesRequest,
    ) -> resource_center_20221201_models.SearchMultiAccountResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_multi_account_resources_with_options_async(request, runtime)

    def search_resources_with_options(
        self,
        request: resource_center_20221201_models.SearchResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.SearchResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchResources',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.SearchResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_resources_with_options_async(
        self,
        request: resource_center_20221201_models.SearchResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.SearchResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchResources',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.SearchResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_resources(
        self,
        request: resource_center_20221201_models.SearchResourcesRequest,
    ) -> resource_center_20221201_models.SearchResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_resources_with_options(request, runtime)

    async def search_resources_async(
        self,
        request: resource_center_20221201_models.SearchResourcesRequest,
    ) -> resource_center_20221201_models.SearchResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_resources_with_options_async(request, runtime)
