# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cams20200606 import models as cams_20200606_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cams', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_contacts_with_options(
        self,
        request: cams_20200606_models.CheckContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CheckContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckContacts',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CheckContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_contacts_with_options_async(
        self,
        request: cams_20200606_models.CheckContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CheckContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckContacts',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CheckContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_contacts(
        self,
        request: cams_20200606_models.CheckContactsRequest,
    ) -> cams_20200606_models.CheckContactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_contacts_with_options(request, runtime)

    async def check_contacts_async(
        self,
        request: cams_20200606_models.CheckContactsRequest,
    ) -> cams_20200606_models.CheckContactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_contacts_with_options_async(request, runtime)

    def send_message_with_options(
        self,
        request: cams_20200606_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.SendMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        request: cams_20200606_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.SendMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: cams_20200606_models.SendMessageRequest,
    ) -> cams_20200606_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    async def send_message_async(
        self,
        request: cams_20200606_models.SendMessageRequest,
    ) -> cams_20200606_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_message_with_options_async(request, runtime)
