# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dybaseapi20170525 import models as dybaseapi_20170525_models
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
        self._endpoint = self.get_endpoint('dybaseapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_token_for_mns_queue_with_options(
        self,
        request: dybaseapi_20170525_models.QueryTokenForMnsQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dybaseapi_20170525_models.QueryTokenForMnsQueueResponse:
        """
        @param request: QueryTokenForMnsQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTokenForMnsQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTokenForMnsQueue',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dybaseapi_20170525_models.QueryTokenForMnsQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_token_for_mns_queue_with_options_async(
        self,
        request: dybaseapi_20170525_models.QueryTokenForMnsQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dybaseapi_20170525_models.QueryTokenForMnsQueueResponse:
        """
        @param request: QueryTokenForMnsQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTokenForMnsQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTokenForMnsQueue',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dybaseapi_20170525_models.QueryTokenForMnsQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_token_for_mns_queue(
        self,
        request: dybaseapi_20170525_models.QueryTokenForMnsQueueRequest,
    ) -> dybaseapi_20170525_models.QueryTokenForMnsQueueResponse:
        """
        @param request: QueryTokenForMnsQueueRequest
        @return: QueryTokenForMnsQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_token_for_mns_queue_with_options(request, runtime)

    async def query_token_for_mns_queue_async(
        self,
        request: dybaseapi_20170525_models.QueryTokenForMnsQueueRequest,
    ) -> dybaseapi_20170525_models.QueryTokenForMnsQueueResponse:
        """
        @param request: QueryTokenForMnsQueueRequest
        @return: QueryTokenForMnsQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_token_for_mns_queue_with_options_async(request, runtime)
