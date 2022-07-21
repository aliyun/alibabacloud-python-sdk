# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_msccommonquery20210407 import models as msc_common_query_20210407_models
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
        self._endpoint = self.get_endpoint('msccommonquery', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_messages_with_options(
        self,
        request: msc_common_query_20210407_models.ListMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_common_query_20210407_models.ListMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.end_timestamp):
            body['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            body['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMessages',
            version='2021-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_common_query_20210407_models.ListMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_messages_with_options_async(
        self,
        request: msc_common_query_20210407_models.ListMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> msc_common_query_20210407_models.ListMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.end_timestamp):
            body['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            body['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMessages',
            version='2021-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            msc_common_query_20210407_models.ListMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_messages(
        self,
        request: msc_common_query_20210407_models.ListMessagesRequest,
    ) -> msc_common_query_20210407_models.ListMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_messages_with_options(request, runtime)

    async def list_messages_async(
        self,
        request: msc_common_query_20210407_models.ListMessagesRequest,
    ) -> msc_common_query_20210407_models.ListMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_messages_with_options_async(request, runtime)
