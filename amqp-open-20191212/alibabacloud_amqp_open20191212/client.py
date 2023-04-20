# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

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

    def create_account_with_options(
        self,
        request: amqp_open_20191212_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_access_key):
            query['accountAccessKey'] = request.account_access_key
        if not UtilClient.is_unset(request.create_timestamp):
            query['createTimestamp'] = request.create_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_sign):
            query['secretSign'] = request.secret_sign
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.user_name):
            query['userName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: amqp_open_20191212_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_access_key):
            query['accountAccessKey'] = request.account_access_key
        if not UtilClient.is_unset(request.create_timestamp):
            query['createTimestamp'] = request.create_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_sign):
            query['secretSign'] = request.secret_sign
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.user_name):
            query['userName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: amqp_open_20191212_models.CreateAccountRequest,
    ) -> amqp_open_20191212_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: amqp_open_20191212_models.CreateAccountRequest,
    ) -> amqp_open_20191212_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_binding_with_options(
        self,
        request: amqp_open_20191212_models.CreateBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateBindingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.argument):
            body['Argument'] = request.argument
        if not UtilClient.is_unset(request.binding_key):
            body['BindingKey'] = request.binding_key
        if not UtilClient.is_unset(request.binding_type):
            body['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.destination_name):
            body['DestinationName'] = request.destination_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_exchange):
            body['SourceExchange'] = request.source_exchange
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBinding',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_binding_with_options_async(
        self,
        request: amqp_open_20191212_models.CreateBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateBindingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.argument):
            body['Argument'] = request.argument
        if not UtilClient.is_unset(request.binding_key):
            body['BindingKey'] = request.binding_key
        if not UtilClient.is_unset(request.binding_type):
            body['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.destination_name):
            body['DestinationName'] = request.destination_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_exchange):
            body['SourceExchange'] = request.source_exchange
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBinding',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateBindingResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.alternate_exchange):
            body['AlternateExchange'] = request.alternate_exchange
        if not UtilClient.is_unset(request.auto_delete_state):
            body['AutoDeleteState'] = request.auto_delete_state
        if not UtilClient.is_unset(request.exchange_name):
            body['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_type):
            body['ExchangeType'] = request.exchange_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.internal):
            body['Internal'] = request.internal
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExchange',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_exchange_with_options_async(
        self,
        request: amqp_open_20191212_models.CreateExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateExchangeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alternate_exchange):
            body['AlternateExchange'] = request.alternate_exchange
        if not UtilClient.is_unset(request.auto_delete_state):
            body['AutoDeleteState'] = request.auto_delete_state
        if not UtilClient.is_unset(request.exchange_name):
            body['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_type):
            body['ExchangeType'] = request.exchange_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.internal):
            body['Internal'] = request.internal
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExchange',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateExchangeResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.auto_delete_state):
            body['AutoDeleteState'] = request.auto_delete_state
        if not UtilClient.is_unset(request.auto_expire_state):
            body['AutoExpireState'] = request.auto_expire_state
        if not UtilClient.is_unset(request.dead_letter_exchange):
            body['DeadLetterExchange'] = request.dead_letter_exchange
        if not UtilClient.is_unset(request.dead_letter_routing_key):
            body['DeadLetterRoutingKey'] = request.dead_letter_routing_key
        if not UtilClient.is_unset(request.exclusive_state):
            body['ExclusiveState'] = request.exclusive_state
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_length):
            body['MaxLength'] = request.max_length
        if not UtilClient.is_unset(request.maximum_priority):
            body['MaximumPriority'] = request.maximum_priority
        if not UtilClient.is_unset(request.message_ttl):
            body['MessageTTL'] = request.message_ttl
        if not UtilClient.is_unset(request.queue_name):
            body['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQueue',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_queue_with_options_async(
        self,
        request: amqp_open_20191212_models.CreateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateQueueResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_delete_state):
            body['AutoDeleteState'] = request.auto_delete_state
        if not UtilClient.is_unset(request.auto_expire_state):
            body['AutoExpireState'] = request.auto_expire_state
        if not UtilClient.is_unset(request.dead_letter_exchange):
            body['DeadLetterExchange'] = request.dead_letter_exchange
        if not UtilClient.is_unset(request.dead_letter_routing_key):
            body['DeadLetterRoutingKey'] = request.dead_letter_routing_key
        if not UtilClient.is_unset(request.exclusive_state):
            body['ExclusiveState'] = request.exclusive_state
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_length):
            body['MaxLength'] = request.max_length
        if not UtilClient.is_unset(request.maximum_priority):
            body['MaximumPriority'] = request.maximum_priority
        if not UtilClient.is_unset(request.message_ttl):
            body['MessageTTL'] = request.message_ttl
        if not UtilClient.is_unset(request.queue_name):
            body['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQueue',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateQueueResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVirtualHost',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateVirtualHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_virtual_host_with_options_async(
        self,
        request: amqp_open_20191212_models.CreateVirtualHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateVirtualHostResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVirtualHost',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateVirtualHostResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_account_with_options(
        self,
        request: amqp_open_20191212_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_timestamp):
            query['CreateTimestamp'] = request.create_timestamp
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: amqp_open_20191212_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_timestamp):
            query['CreateTimestamp'] = request.create_timestamp
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: amqp_open_20191212_models.DeleteAccountRequest,
    ) -> amqp_open_20191212_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: amqp_open_20191212_models.DeleteAccountRequest,
    ) -> amqp_open_20191212_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_binding_with_options(
        self,
        request: amqp_open_20191212_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteBindingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.binding_key):
            body['BindingKey'] = request.binding_key
        if not UtilClient.is_unset(request.binding_type):
            body['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.destination_name):
            body['DestinationName'] = request.destination_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_exchange):
            body['SourceExchange'] = request.source_exchange
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBinding',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_binding_with_options_async(
        self,
        request: amqp_open_20191212_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteBindingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.binding_key):
            body['BindingKey'] = request.binding_key
        if not UtilClient.is_unset(request.binding_type):
            body['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.destination_name):
            body['DestinationName'] = request.destination_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_exchange):
            body['SourceExchange'] = request.source_exchange
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBinding',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteBindingResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.exchange_name):
            body['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteExchange',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_exchange_with_options_async(
        self,
        request: amqp_open_20191212_models.DeleteExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteExchangeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exchange_name):
            body['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteExchange',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteExchangeResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.queue_name):
            body['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQueue',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_queue_with_options_async(
        self,
        request: amqp_open_20191212_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteQueueResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.queue_name):
            body['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQueue',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteQueueResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVirtualHost',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteVirtualHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_virtual_host_with_options_async(
        self,
        request: amqp_open_20191212_models.DeleteVirtualHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteVirtualHostResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVirtualHost',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteVirtualHostResponse(),
            await self.call_api_async(params, req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetadataAmount',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.GetMetadataAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_metadata_amount_with_options_async(
        self,
        request: amqp_open_20191212_models.GetMetadataAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.GetMetadataAmountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetadataAmount',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.GetMetadataAmountResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_accounts_with_options(
        self,
        request: amqp_open_20191212_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_with_options_async(
        self,
        request: amqp_open_20191212_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts(
        self,
        request: amqp_open_20191212_models.ListAccountsRequest,
    ) -> amqp_open_20191212_models.ListAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    async def list_accounts_async(
        self,
        request: amqp_open_20191212_models.ListAccountsRequest,
    ) -> amqp_open_20191212_models.ListAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_with_options_async(request, runtime)

    def list_bindings_with_options(
        self,
        request: amqp_open_20191212_models.ListBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bindings_with_options_async(
        self,
        request: amqp_open_20191212_models.ListBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListBindingsResponse(),
            await self.call_api_async(params, req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownStreamBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListDownStreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_down_stream_bindings_with_options_async(
        self,
        request: amqp_open_20191212_models.ListDownStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListDownStreamBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownStreamBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListDownStreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_exchange_up_stream_bindings_with_options(
        self,
        request: amqp_open_20191212_models.ListExchangeUpStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchangeUpStreamBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_exchange_up_stream_bindings_with_options_async(
        self,
        request: amqp_open_20191212_models.ListExchangeUpStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchangeUpStreamBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_exchanges_with_options(
        self,
        request: amqp_open_20191212_models.ListExchangesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListExchangesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchanges',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListExchangesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_exchanges_with_options_async(
        self,
        request: amqp_open_20191212_models.ListExchangesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListExchangesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchanges',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListExchangesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_instances_with_options(
        self,
        request: amqp_open_20191212_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: amqp_open_20191212_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueueConsumers',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListQueueConsumersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queue_consumers_with_options_async(
        self,
        request: amqp_open_20191212_models.ListQueueConsumersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueueConsumersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueueConsumers',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListQueueConsumersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_queue_up_stream_bindings_with_options(
        self,
        request: amqp_open_20191212_models.ListQueueUpStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueueUpStreamBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueueUpStreamBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListQueueUpStreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queue_up_stream_bindings_with_options_async(
        self,
        request: amqp_open_20191212_models.ListQueueUpStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueueUpStreamBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueueUpStreamBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListQueueUpStreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_queues_with_options(
        self,
        request: amqp_open_20191212_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueues',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queues_with_options_async(
        self,
        request: amqp_open_20191212_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueues',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListQueuesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_virtual_hosts_with_options(
        self,
        request: amqp_open_20191212_models.ListVirtualHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListVirtualHostsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVirtualHosts',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListVirtualHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_virtual_hosts_with_options_async(
        self,
        request: amqp_open_20191212_models.ListVirtualHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListVirtualHostsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVirtualHosts',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListVirtualHostsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_instance_name_with_options(
        self,
        request: amqp_open_20191212_models.UpdateInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.UpdateInstanceNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.UpdateInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_name_with_options_async(
        self,
        request: amqp_open_20191212_models.UpdateInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.UpdateInstanceNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.UpdateInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_name(
        self,
        request: amqp_open_20191212_models.UpdateInstanceNameRequest,
    ) -> amqp_open_20191212_models.UpdateInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_name_with_options(request, runtime)

    async def update_instance_name_async(
        self,
        request: amqp_open_20191212_models.UpdateInstanceNameRequest,
    ) -> amqp_open_20191212_models.UpdateInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_name_with_options_async(request, runtime)
