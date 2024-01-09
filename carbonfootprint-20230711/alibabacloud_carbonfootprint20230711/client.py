# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_carbonfootprint20230711 import models as carbon_footprint_20230711_models
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
        self._endpoint = self.get_endpoint('carbonfootprint', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allow_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> carbon_footprint_20230711_models.AllowResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='Allow',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.AllowResponse(),
            self.call_api(params, req, runtime)
        )

    async def allow_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> carbon_footprint_20230711_models.AllowResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='Allow',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.AllowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allow(self) -> carbon_footprint_20230711_models.AllowResponse:
        runtime = util_models.RuntimeOptions()
        return self.allow_with_options(runtime)

    async def allow_async(self) -> carbon_footprint_20230711_models.AllowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allow_with_options_async(runtime)

    def get_summary_data_with_options(
        self,
        request: carbon_footprint_20230711_models.GetSummaryDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> carbon_footprint_20230711_models.GetSummaryDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSummaryData',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.GetSummaryDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_summary_data_with_options_async(
        self,
        request: carbon_footprint_20230711_models.GetSummaryDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> carbon_footprint_20230711_models.GetSummaryDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSummaryData',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.GetSummaryDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_summary_data(
        self,
        request: carbon_footprint_20230711_models.GetSummaryDataRequest,
    ) -> carbon_footprint_20230711_models.GetSummaryDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_summary_data_with_options(request, runtime)

    async def get_summary_data_async(
        self,
        request: carbon_footprint_20230711_models.GetSummaryDataRequest,
    ) -> carbon_footprint_20230711_models.GetSummaryDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_summary_data_with_options_async(request, runtime)

    def query_carbon_track_with_options(
        self,
        request: carbon_footprint_20230711_models.QueryCarbonTrackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> carbon_footprint_20230711_models.QueryCarbonTrackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCarbonTrack',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.QueryCarbonTrackResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_carbon_track_with_options_async(
        self,
        request: carbon_footprint_20230711_models.QueryCarbonTrackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> carbon_footprint_20230711_models.QueryCarbonTrackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCarbonTrack',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.QueryCarbonTrackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_carbon_track(
        self,
        request: carbon_footprint_20230711_models.QueryCarbonTrackRequest,
    ) -> carbon_footprint_20230711_models.QueryCarbonTrackResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_carbon_track_with_options(request, runtime)

    async def query_carbon_track_async(
        self,
        request: carbon_footprint_20230711_models.QueryCarbonTrackRequest,
    ) -> carbon_footprint_20230711_models.QueryCarbonTrackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_carbon_track_with_options_async(request, runtime)

    def query_multi_account_carbon_track_with_options(
        self,
        request: carbon_footprint_20230711_models.QueryMultiAccountCarbonTrackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> carbon_footprint_20230711_models.QueryMultiAccountCarbonTrackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMultiAccountCarbonTrack',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.QueryMultiAccountCarbonTrackResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_multi_account_carbon_track_with_options_async(
        self,
        request: carbon_footprint_20230711_models.QueryMultiAccountCarbonTrackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> carbon_footprint_20230711_models.QueryMultiAccountCarbonTrackResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMultiAccountCarbonTrack',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.QueryMultiAccountCarbonTrackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_multi_account_carbon_track(
        self,
        request: carbon_footprint_20230711_models.QueryMultiAccountCarbonTrackRequest,
    ) -> carbon_footprint_20230711_models.QueryMultiAccountCarbonTrackResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_multi_account_carbon_track_with_options(request, runtime)

    async def query_multi_account_carbon_track_async(
        self,
        request: carbon_footprint_20230711_models.QueryMultiAccountCarbonTrackRequest,
    ) -> carbon_footprint_20230711_models.QueryMultiAccountCarbonTrackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_multi_account_carbon_track_with_options_async(request, runtime)

    def verify_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> carbon_footprint_20230711_models.VerifyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='Verify',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.VerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> carbon_footprint_20230711_models.VerifyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='Verify',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.VerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify(self) -> carbon_footprint_20230711_models.VerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_with_options(runtime)

    async def verify_async(self) -> carbon_footprint_20230711_models.VerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_with_options_async(runtime)
