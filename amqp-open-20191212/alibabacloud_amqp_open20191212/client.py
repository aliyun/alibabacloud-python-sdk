# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_amqp_open20191212 import models as amqp_open_20191212_models
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
        self._endpoint = self.get_endpoint('amqp-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_binding_with_options(
        self,
        request: amqp_open_20191212_models.CreateBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateBindingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.CreateBindingResponse().from_map(
            self.do_rpcrequest('CreateBinding', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_binding_with_options_async(
        self,
        request: amqp_open_20191212_models.CreateBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateBindingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.CreateBindingResponse().from_map(
            await self.do_rpcrequest_async('CreateBinding', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_binding(
        self,
        request: amqp_open_20191212_models.CreateBindingRequest,
    ) -> amqp_open_20191212_models.CreateBindingResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_binding_with_options(request, runtime)

    async def create_binding_async(
        self,
        request: amqp_open_20191212_models.CreateBindingRequest,
    ) -> amqp_open_20191212_models.CreateBindingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_binding_with_options_async(request, runtime)

    def create_exchange_with_options(
        self,
        request: amqp_open_20191212_models.CreateExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateExchangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.CreateExchangeResponse().from_map(
            self.do_rpcrequest('CreateExchange', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_exchange_with_options_async(
        self,
        request: amqp_open_20191212_models.CreateExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateExchangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.CreateExchangeResponse().from_map(
            await self.do_rpcrequest_async('CreateExchange', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_exchange(
        self,
        request: amqp_open_20191212_models.CreateExchangeRequest,
    ) -> amqp_open_20191212_models.CreateExchangeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_exchange_with_options(request, runtime)

    async def create_exchange_async(
        self,
        request: amqp_open_20191212_models.CreateExchangeRequest,
    ) -> amqp_open_20191212_models.CreateExchangeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_exchange_with_options_async(request, runtime)

    def create_queue_with_options(
        self,
        request: amqp_open_20191212_models.CreateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.CreateQueueResponse().from_map(
            self.do_rpcrequest('CreateQueue', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_queue_with_options_async(
        self,
        request: amqp_open_20191212_models.CreateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.CreateQueueResponse().from_map(
            await self.do_rpcrequest_async('CreateQueue', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_queue(
        self,
        request: amqp_open_20191212_models.CreateQueueRequest,
    ) -> amqp_open_20191212_models.CreateQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_queue_with_options(request, runtime)

    async def create_queue_async(
        self,
        request: amqp_open_20191212_models.CreateQueueRequest,
    ) -> amqp_open_20191212_models.CreateQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_queue_with_options_async(request, runtime)

    def create_virtual_host_with_options(
        self,
        request: amqp_open_20191212_models.CreateVirtualHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateVirtualHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.CreateVirtualHostResponse().from_map(
            self.do_rpcrequest('CreateVirtualHost', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_virtual_host_with_options_async(
        self,
        request: amqp_open_20191212_models.CreateVirtualHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateVirtualHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.CreateVirtualHostResponse().from_map(
            await self.do_rpcrequest_async('CreateVirtualHost', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_virtual_host(
        self,
        request: amqp_open_20191212_models.CreateVirtualHostRequest,
    ) -> amqp_open_20191212_models.CreateVirtualHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_host_with_options(request, runtime)

    async def create_virtual_host_async(
        self,
        request: amqp_open_20191212_models.CreateVirtualHostRequest,
    ) -> amqp_open_20191212_models.CreateVirtualHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_host_with_options_async(request, runtime)

    def delete_binding_with_options(
        self,
        request: amqp_open_20191212_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteBindingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.DeleteBindingResponse().from_map(
            self.do_rpcrequest('DeleteBinding', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_binding_with_options_async(
        self,
        request: amqp_open_20191212_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteBindingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.DeleteBindingResponse().from_map(
            await self.do_rpcrequest_async('DeleteBinding', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_binding(
        self,
        request: amqp_open_20191212_models.DeleteBindingRequest,
    ) -> amqp_open_20191212_models.DeleteBindingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_binding_with_options(request, runtime)

    async def delete_binding_async(
        self,
        request: amqp_open_20191212_models.DeleteBindingRequest,
    ) -> amqp_open_20191212_models.DeleteBindingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_binding_with_options_async(request, runtime)

    def delete_exchange_with_options(
        self,
        request: amqp_open_20191212_models.DeleteExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteExchangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.DeleteExchangeResponse().from_map(
            self.do_rpcrequest('DeleteExchange', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_exchange_with_options_async(
        self,
        request: amqp_open_20191212_models.DeleteExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteExchangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.DeleteExchangeResponse().from_map(
            await self.do_rpcrequest_async('DeleteExchange', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_exchange(
        self,
        request: amqp_open_20191212_models.DeleteExchangeRequest,
    ) -> amqp_open_20191212_models.DeleteExchangeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_exchange_with_options(request, runtime)

    async def delete_exchange_async(
        self,
        request: amqp_open_20191212_models.DeleteExchangeRequest,
    ) -> amqp_open_20191212_models.DeleteExchangeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_exchange_with_options_async(request, runtime)

    def delete_queue_with_options(
        self,
        request: amqp_open_20191212_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.DeleteQueueResponse().from_map(
            self.do_rpcrequest('DeleteQueue', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_queue_with_options_async(
        self,
        request: amqp_open_20191212_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.DeleteQueueResponse().from_map(
            await self.do_rpcrequest_async('DeleteQueue', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_queue(
        self,
        request: amqp_open_20191212_models.DeleteQueueRequest,
    ) -> amqp_open_20191212_models.DeleteQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    async def delete_queue_async(
        self,
        request: amqp_open_20191212_models.DeleteQueueRequest,
    ) -> amqp_open_20191212_models.DeleteQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_queue_with_options_async(request, runtime)

    def delete_virtual_host_with_options(
        self,
        request: amqp_open_20191212_models.DeleteVirtualHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteVirtualHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.DeleteVirtualHostResponse().from_map(
            self.do_rpcrequest('DeleteVirtualHost', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_virtual_host_with_options_async(
        self,
        request: amqp_open_20191212_models.DeleteVirtualHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteVirtualHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return amqp_open_20191212_models.DeleteVirtualHostResponse().from_map(
            await self.do_rpcrequest_async('DeleteVirtualHost', '2019-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_virtual_host(
        self,
        request: amqp_open_20191212_models.DeleteVirtualHostRequest,
    ) -> amqp_open_20191212_models.DeleteVirtualHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_host_with_options(request, runtime)

    async def delete_virtual_host_async(
        self,
        request: amqp_open_20191212_models.DeleteVirtualHostRequest,
    ) -> amqp_open_20191212_models.DeleteVirtualHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_host_with_options_async(request, runtime)

    def get_metadata_amount_with_options(
        self,
        request: amqp_open_20191212_models.GetMetadataAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.GetMetadataAmountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.GetMetadataAmountResponse().from_map(
            self.do_rpcrequest('GetMetadataAmount', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_metadata_amount_with_options_async(
        self,
        request: amqp_open_20191212_models.GetMetadataAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.GetMetadataAmountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.GetMetadataAmountResponse().from_map(
            await self.do_rpcrequest_async('GetMetadataAmount', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_metadata_amount(
        self,
        request: amqp_open_20191212_models.GetMetadataAmountRequest,
    ) -> amqp_open_20191212_models.GetMetadataAmountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_metadata_amount_with_options(request, runtime)

    async def get_metadata_amount_async(
        self,
        request: amqp_open_20191212_models.GetMetadataAmountRequest,
    ) -> amqp_open_20191212_models.GetMetadataAmountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_metadata_amount_with_options_async(request, runtime)

    def list_bindings_with_options(
        self,
        request: amqp_open_20191212_models.ListBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListBindingsResponse().from_map(
            self.do_rpcrequest('ListBindings', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_bindings_with_options_async(
        self,
        request: amqp_open_20191212_models.ListBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListBindingsResponse().from_map(
            await self.do_rpcrequest_async('ListBindings', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_bindings(
        self,
        request: amqp_open_20191212_models.ListBindingsRequest,
    ) -> amqp_open_20191212_models.ListBindingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bindings_with_options(request, runtime)

    async def list_bindings_async(
        self,
        request: amqp_open_20191212_models.ListBindingsRequest,
    ) -> amqp_open_20191212_models.ListBindingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bindings_with_options_async(request, runtime)

    def list_down_stream_bindings_with_options(
        self,
        request: amqp_open_20191212_models.ListDownStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListDownStreamBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListDownStreamBindingsResponse().from_map(
            self.do_rpcrequest('ListDownStreamBindings', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_down_stream_bindings_with_options_async(
        self,
        request: amqp_open_20191212_models.ListDownStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListDownStreamBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListDownStreamBindingsResponse().from_map(
            await self.do_rpcrequest_async('ListDownStreamBindings', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_down_stream_bindings(
        self,
        request: amqp_open_20191212_models.ListDownStreamBindingsRequest,
    ) -> amqp_open_20191212_models.ListDownStreamBindingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_down_stream_bindings_with_options(request, runtime)

    async def list_down_stream_bindings_async(
        self,
        request: amqp_open_20191212_models.ListDownStreamBindingsRequest,
    ) -> amqp_open_20191212_models.ListDownStreamBindingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_down_stream_bindings_with_options_async(request, runtime)

    def list_exchanges_with_options(
        self,
        request: amqp_open_20191212_models.ListExchangesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListExchangesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListExchangesResponse().from_map(
            self.do_rpcrequest('ListExchanges', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_exchanges_with_options_async(
        self,
        request: amqp_open_20191212_models.ListExchangesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListExchangesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListExchangesResponse().from_map(
            await self.do_rpcrequest_async('ListExchanges', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_exchanges(
        self,
        request: amqp_open_20191212_models.ListExchangesRequest,
    ) -> amqp_open_20191212_models.ListExchangesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_exchanges_with_options(request, runtime)

    async def list_exchanges_async(
        self,
        request: amqp_open_20191212_models.ListExchangesRequest,
    ) -> amqp_open_20191212_models.ListExchangesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_exchanges_with_options_async(request, runtime)

    def list_exchange_up_stream_bindings_with_options(
        self,
        request: amqp_open_20191212_models.ListExchangeUpStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse().from_map(
            self.do_rpcrequest('ListExchangeUpStreamBindings', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_exchange_up_stream_bindings_with_options_async(
        self,
        request: amqp_open_20191212_models.ListExchangeUpStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse().from_map(
            await self.do_rpcrequest_async('ListExchangeUpStreamBindings', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_exchange_up_stream_bindings(
        self,
        request: amqp_open_20191212_models.ListExchangeUpStreamBindingsRequest,
    ) -> amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_exchange_up_stream_bindings_with_options(request, runtime)

    async def list_exchange_up_stream_bindings_async(
        self,
        request: amqp_open_20191212_models.ListExchangeUpStreamBindingsRequest,
    ) -> amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_exchange_up_stream_bindings_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: amqp_open_20191212_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListInstancesResponse().from_map(
            self.do_rpcrequest('ListInstances', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: amqp_open_20191212_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListInstancesResponse().from_map(
            await self.do_rpcrequest_async('ListInstances', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_instances(
        self,
        request: amqp_open_20191212_models.ListInstancesRequest,
    ) -> amqp_open_20191212_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: amqp_open_20191212_models.ListInstancesRequest,
    ) -> amqp_open_20191212_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_queue_consumers_with_options(
        self,
        request: amqp_open_20191212_models.ListQueueConsumersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueueConsumersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListQueueConsumersResponse().from_map(
            self.do_rpcrequest('ListQueueConsumers', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_queue_consumers_with_options_async(
        self,
        request: amqp_open_20191212_models.ListQueueConsumersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueueConsumersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListQueueConsumersResponse().from_map(
            await self.do_rpcrequest_async('ListQueueConsumers', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_queue_consumers(
        self,
        request: amqp_open_20191212_models.ListQueueConsumersRequest,
    ) -> amqp_open_20191212_models.ListQueueConsumersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_queue_consumers_with_options(request, runtime)

    async def list_queue_consumers_async(
        self,
        request: amqp_open_20191212_models.ListQueueConsumersRequest,
    ) -> amqp_open_20191212_models.ListQueueConsumersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_queue_consumers_with_options_async(request, runtime)

    def list_queues_with_options(
        self,
        request: amqp_open_20191212_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListQueuesResponse().from_map(
            self.do_rpcrequest('ListQueues', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_queues_with_options_async(
        self,
        request: amqp_open_20191212_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListQueuesResponse().from_map(
            await self.do_rpcrequest_async('ListQueues', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_queues(
        self,
        request: amqp_open_20191212_models.ListQueuesRequest,
    ) -> amqp_open_20191212_models.ListQueuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_queues_with_options(request, runtime)

    async def list_queues_async(
        self,
        request: amqp_open_20191212_models.ListQueuesRequest,
    ) -> amqp_open_20191212_models.ListQueuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_queues_with_options_async(request, runtime)

    def list_queue_up_stream_bindings_with_options(
        self,
        request: amqp_open_20191212_models.ListQueueUpStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueueUpStreamBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListQueueUpStreamBindingsResponse().from_map(
            self.do_rpcrequest('ListQueueUpStreamBindings', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_queue_up_stream_bindings_with_options_async(
        self,
        request: amqp_open_20191212_models.ListQueueUpStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueueUpStreamBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListQueueUpStreamBindingsResponse().from_map(
            await self.do_rpcrequest_async('ListQueueUpStreamBindings', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_queue_up_stream_bindings(
        self,
        request: amqp_open_20191212_models.ListQueueUpStreamBindingsRequest,
    ) -> amqp_open_20191212_models.ListQueueUpStreamBindingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_queue_up_stream_bindings_with_options(request, runtime)

    async def list_queue_up_stream_bindings_async(
        self,
        request: amqp_open_20191212_models.ListQueueUpStreamBindingsRequest,
    ) -> amqp_open_20191212_models.ListQueueUpStreamBindingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_queue_up_stream_bindings_with_options_async(request, runtime)

    def list_virtual_hosts_with_options(
        self,
        request: amqp_open_20191212_models.ListVirtualHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListVirtualHostsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListVirtualHostsResponse().from_map(
            self.do_rpcrequest('ListVirtualHosts', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_virtual_hosts_with_options_async(
        self,
        request: amqp_open_20191212_models.ListVirtualHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListVirtualHostsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return amqp_open_20191212_models.ListVirtualHostsResponse().from_map(
            await self.do_rpcrequest_async('ListVirtualHosts', '2019-12-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_virtual_hosts(
        self,
        request: amqp_open_20191212_models.ListVirtualHostsRequest,
    ) -> amqp_open_20191212_models.ListVirtualHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_hosts_with_options(request, runtime)

    async def list_virtual_hosts_async(
        self,
        request: amqp_open_20191212_models.ListVirtualHostsRequest,
    ) -> amqp_open_20191212_models.ListVirtualHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_virtual_hosts_with_options_async(request, runtime)
