# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cms_export20211101 import models as cms_export_20211101_models
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
        self._endpoint = self.get_endpoint('cms-export', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_get_with_options(
        self,
        request: cms_export_20211101_models.BatchGetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_export_20211101_models.BatchGetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compression_type):
            body['CompressionType'] = request.compression_type
        if not UtilClient.is_unset(request.cursor):
            body['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.length):
            body['Length'] = request.length
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.record_key_white_list):
            body['RecordKeyWhiteList'] = request.record_key_white_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGet',
            version='2021-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_export_20211101_models.BatchGetResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_with_options_async(
        self,
        request: cms_export_20211101_models.BatchGetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_export_20211101_models.BatchGetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compression_type):
            body['CompressionType'] = request.compression_type
        if not UtilClient.is_unset(request.cursor):
            body['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.length):
            body['Length'] = request.length
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.record_key_white_list):
            body['RecordKeyWhiteList'] = request.record_key_white_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGet',
            version='2021-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_export_20211101_models.BatchGetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get(
        self,
        request: cms_export_20211101_models.BatchGetRequest,
    ) -> cms_export_20211101_models.BatchGetResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_get_with_options(request, runtime)

    async def batch_get_async(
        self,
        request: cms_export_20211101_models.BatchGetRequest,
    ) -> cms_export_20211101_models.BatchGetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_with_options_async(request, runtime)

    def cursor_with_options(
        self,
        tmp_req: cms_export_20211101_models.CursorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_export_20211101_models.CursorResponse:
        UtilClient.validate_model(tmp_req)
        request = cms_export_20211101_models.CursorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.matchers):
            request.matchers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.matchers, 'Matchers', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.matchers_shrink):
            body['Matchers'] = request.matchers_shrink
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Cursor',
            version='2021-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_export_20211101_models.CursorResponse(),
            self.call_api(params, req, runtime)
        )

    async def cursor_with_options_async(
        self,
        tmp_req: cms_export_20211101_models.CursorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_export_20211101_models.CursorResponse:
        UtilClient.validate_model(tmp_req)
        request = cms_export_20211101_models.CursorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.matchers):
            request.matchers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.matchers, 'Matchers', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.matchers_shrink):
            body['Matchers'] = request.matchers_shrink
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Cursor',
            version='2021-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_export_20211101_models.CursorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cursor(
        self,
        request: cms_export_20211101_models.CursorRequest,
    ) -> cms_export_20211101_models.CursorResponse:
        runtime = util_models.RuntimeOptions()
        return self.cursor_with_options(request, runtime)

    async def cursor_async(
        self,
        request: cms_export_20211101_models.CursorRequest,
    ) -> cms_export_20211101_models.CursorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cursor_with_options_async(request, runtime)
