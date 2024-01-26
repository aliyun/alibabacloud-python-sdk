# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_status20200117 import models as status_20200117_models
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
        self._endpoint = self.get_endpoint('status', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_event_in_progress_with_options(
        self,
        tmp_req: status_20200117_models.ListEventInProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> status_20200117_models.ListEventInProgressResponse:
        UtilClient.validate_model(tmp_req)
        request = status_20200117_models.ListEventInProgressShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.region_ids_shrink):
            body['RegionIds'] = request.region_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEventInProgress',
            version='2020-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            status_20200117_models.ListEventInProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_in_progress_with_options_async(
        self,
        tmp_req: status_20200117_models.ListEventInProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> status_20200117_models.ListEventInProgressResponse:
        UtilClient.validate_model(tmp_req)
        request = status_20200117_models.ListEventInProgressShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.region_ids_shrink):
            body['RegionIds'] = request.region_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEventInProgress',
            version='2020-01-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            status_20200117_models.ListEventInProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_in_progress(
        self,
        request: status_20200117_models.ListEventInProgressRequest,
    ) -> status_20200117_models.ListEventInProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_in_progress_with_options(request, runtime)

    async def list_event_in_progress_async(
        self,
        request: status_20200117_models.ListEventInProgressRequest,
    ) -> status_20200117_models.ListEventInProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_in_progress_with_options_async(request, runtime)
