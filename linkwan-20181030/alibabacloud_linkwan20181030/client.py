# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkwan20181030 import models as link_wan20181030_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('linkwan', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_kpm_encrypted_node_tuples_by_order_id_with_options(
        self,
        request: link_wan20181030_models.GetKpmEncryptedNodeTuplesByOrderIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_wan20181030_models.GetKpmEncryptedNodeTuplesByOrderIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return link_wan20181030_models.GetKpmEncryptedNodeTuplesByOrderIdResponse().from_map(
            self.do_rpcrequest('GetKpmEncryptedNodeTuplesByOrderId', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_kpm_encrypted_node_tuples_by_order_id_with_options_async(
        self,
        request: link_wan20181030_models.GetKpmEncryptedNodeTuplesByOrderIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_wan20181030_models.GetKpmEncryptedNodeTuplesByOrderIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return link_wan20181030_models.GetKpmEncryptedNodeTuplesByOrderIdResponse().from_map(
            await self.do_rpcrequest_async('GetKpmEncryptedNodeTuplesByOrderId', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_kpm_encrypted_node_tuples_by_order_id(
        self,
        request: link_wan20181030_models.GetKpmEncryptedNodeTuplesByOrderIdRequest,
    ) -> link_wan20181030_models.GetKpmEncryptedNodeTuplesByOrderIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_kpm_encrypted_node_tuples_by_order_id_with_options(request, runtime)

    async def get_kpm_encrypted_node_tuples_by_order_id_async(
        self,
        request: link_wan20181030_models.GetKpmEncryptedNodeTuplesByOrderIdRequest,
    ) -> link_wan20181030_models.GetKpmEncryptedNodeTuplesByOrderIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_kpm_encrypted_node_tuples_by_order_id_with_options_async(request, runtime)

    def submit_kpm_encrypted_node_tuple_order_with_options(
        self,
        request: link_wan20181030_models.SubmitKpmEncryptedNodeTupleOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_wan20181030_models.SubmitKpmEncryptedNodeTupleOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return link_wan20181030_models.SubmitKpmEncryptedNodeTupleOrderResponse().from_map(
            self.do_rpcrequest('SubmitKpmEncryptedNodeTupleOrder', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_kpm_encrypted_node_tuple_order_with_options_async(
        self,
        request: link_wan20181030_models.SubmitKpmEncryptedNodeTupleOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_wan20181030_models.SubmitKpmEncryptedNodeTupleOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return link_wan20181030_models.SubmitKpmEncryptedNodeTupleOrderResponse().from_map(
            await self.do_rpcrequest_async('SubmitKpmEncryptedNodeTupleOrder', '2018-10-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_kpm_encrypted_node_tuple_order(
        self,
        request: link_wan20181030_models.SubmitKpmEncryptedNodeTupleOrderRequest,
    ) -> link_wan20181030_models.SubmitKpmEncryptedNodeTupleOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_kpm_encrypted_node_tuple_order_with_options(request, runtime)

    async def submit_kpm_encrypted_node_tuple_order_async(
        self,
        request: link_wan20181030_models.SubmitKpmEncryptedNodeTupleOrderRequest,
    ) -> link_wan20181030_models.SubmitKpmEncryptedNodeTupleOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_kpm_encrypted_node_tuple_order_with_options_async(request, runtime)
