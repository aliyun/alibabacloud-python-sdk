# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_viapi_oxs_cross20200701 import models as viapi_oxs_cross_20200701_models
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
        self._endpoint = self.get_endpoint('viapi-oxs-cross', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_sdkinstance_with_options(
        self,
        request: viapi_oxs_cross_20200701_models.CreateSDKInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_oxs_cross_20200701_models.CreateSDKInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.recipe):
            query['Recipe'] = request.recipe
        if not UtilClient.is_unset(request.valid_from):
            query['ValidFrom'] = request.valid_from
        if not UtilClient.is_unset(request.valid_to):
            query['ValidTo'] = request.valid_to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSDKInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_oxs_cross_20200701_models.CreateSDKInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sdkinstance_with_options_async(
        self,
        request: viapi_oxs_cross_20200701_models.CreateSDKInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_oxs_cross_20200701_models.CreateSDKInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.recipe):
            query['Recipe'] = request.recipe
        if not UtilClient.is_unset(request.valid_from):
            query['ValidFrom'] = request.valid_from
        if not UtilClient.is_unset(request.valid_to):
            query['ValidTo'] = request.valid_to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSDKInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_oxs_cross_20200701_models.CreateSDKInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sdkinstance(
        self,
        request: viapi_oxs_cross_20200701_models.CreateSDKInstanceRequest,
    ) -> viapi_oxs_cross_20200701_models.CreateSDKInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sdkinstance_with_options(request, runtime)

    async def create_sdkinstance_async(
        self,
        request: viapi_oxs_cross_20200701_models.CreateSDKInstanceRequest,
    ) -> viapi_oxs_cross_20200701_models.CreateSDKInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sdkinstance_with_options_async(request, runtime)

    def get_sdkinstance_debug_info_with_options(
        self,
        request: viapi_oxs_cross_20200701_models.GetSDKInstanceDebugInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_oxs_cross_20200701_models.GetSDKInstanceDebugInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSDKInstanceDebugInfo',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_oxs_cross_20200701_models.GetSDKInstanceDebugInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sdkinstance_debug_info_with_options_async(
        self,
        request: viapi_oxs_cross_20200701_models.GetSDKInstanceDebugInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_oxs_cross_20200701_models.GetSDKInstanceDebugInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSDKInstanceDebugInfo',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_oxs_cross_20200701_models.GetSDKInstanceDebugInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sdkinstance_debug_info(
        self,
        request: viapi_oxs_cross_20200701_models.GetSDKInstanceDebugInfoRequest,
    ) -> viapi_oxs_cross_20200701_models.GetSDKInstanceDebugInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sdkinstance_debug_info_with_options(request, runtime)

    async def get_sdkinstance_debug_info_async(
        self,
        request: viapi_oxs_cross_20200701_models.GetSDKInstanceDebugInfoRequest,
    ) -> viapi_oxs_cross_20200701_models.GetSDKInstanceDebugInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sdkinstance_debug_info_with_options_async(request, runtime)

    def query_sdkinstances_with_options(
        self,
        request: viapi_oxs_cross_20200701_models.QuerySDKInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_oxs_cross_20200701_models.QuerySDKInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code_list):
            query['CodeList'] = request.code_list
        if not UtilClient.is_unset(request.created_after_date):
            query['CreatedAfterDate'] = request.created_after_date
        if not UtilClient.is_unset(request.created_before_date):
            query['CreatedBeforeDate'] = request.created_before_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySDKInstances',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_oxs_cross_20200701_models.QuerySDKInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sdkinstances_with_options_async(
        self,
        request: viapi_oxs_cross_20200701_models.QuerySDKInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_oxs_cross_20200701_models.QuerySDKInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code_list):
            query['CodeList'] = request.code_list
        if not UtilClient.is_unset(request.created_after_date):
            query['CreatedAfterDate'] = request.created_after_date
        if not UtilClient.is_unset(request.created_before_date):
            query['CreatedBeforeDate'] = request.created_before_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySDKInstances',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_oxs_cross_20200701_models.QuerySDKInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sdkinstances(
        self,
        request: viapi_oxs_cross_20200701_models.QuerySDKInstancesRequest,
    ) -> viapi_oxs_cross_20200701_models.QuerySDKInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sdkinstances_with_options(request, runtime)

    async def query_sdkinstances_async(
        self,
        request: viapi_oxs_cross_20200701_models.QuerySDKInstancesRequest,
    ) -> viapi_oxs_cross_20200701_models.QuerySDKInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sdkinstances_with_options_async(request, runtime)

    def start_sdkinstance_production_with_options(
        self,
        request: viapi_oxs_cross_20200701_models.StartSDKInstanceProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_oxs_cross_20200701_models.StartSDKInstanceProductionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSDKInstanceProduction',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_oxs_cross_20200701_models.StartSDKInstanceProductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_sdkinstance_production_with_options_async(
        self,
        request: viapi_oxs_cross_20200701_models.StartSDKInstanceProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_oxs_cross_20200701_models.StartSDKInstanceProductionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSDKInstanceProduction',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_oxs_cross_20200701_models.StartSDKInstanceProductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_sdkinstance_production(
        self,
        request: viapi_oxs_cross_20200701_models.StartSDKInstanceProductionRequest,
    ) -> viapi_oxs_cross_20200701_models.StartSDKInstanceProductionResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_sdkinstance_production_with_options(request, runtime)

    async def start_sdkinstance_production_async(
        self,
        request: viapi_oxs_cross_20200701_models.StartSDKInstanceProductionRequest,
    ) -> viapi_oxs_cross_20200701_models.StartSDKInstanceProductionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_sdkinstance_production_with_options_async(request, runtime)
