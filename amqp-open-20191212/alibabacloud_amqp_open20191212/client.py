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
        """
        @summary Creates a pair of static username and password. If you access an ApsaraMQ for RabbitMQ broker from an open source RabbitMQ client, you must use a pair of username and password for authentication. You can access the ApsaraMQ for RabbitMQ broker only after the authentication is passed. ApsaraMQ for RabbitMQ allows you to generate usernames and passwords by using AccessKey pairs provided by Alibaba Cloud Resource Access Management (RAM).
        
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
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
        """
        @summary Creates a pair of static username and password. If you access an ApsaraMQ for RabbitMQ broker from an open source RabbitMQ client, you must use a pair of username and password for authentication. You can access the ApsaraMQ for RabbitMQ broker only after the authentication is passed. ApsaraMQ for RabbitMQ allows you to generate usernames and passwords by using AccessKey pairs provided by Alibaba Cloud Resource Access Management (RAM).
        
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
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
        """
        @summary Creates a pair of static username and password. If you access an ApsaraMQ for RabbitMQ broker from an open source RabbitMQ client, you must use a pair of username and password for authentication. You can access the ApsaraMQ for RabbitMQ broker only after the authentication is passed. ApsaraMQ for RabbitMQ allows you to generate usernames and passwords by using AccessKey pairs provided by Alibaba Cloud Resource Access Management (RAM).
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: amqp_open_20191212_models.CreateAccountRequest,
    ) -> amqp_open_20191212_models.CreateAccountResponse:
        """
        @summary Creates a pair of static username and password. If you access an ApsaraMQ for RabbitMQ broker from an open source RabbitMQ client, you must use a pair of username and password for authentication. You can access the ApsaraMQ for RabbitMQ broker only after the authentication is passed. ApsaraMQ for RabbitMQ allows you to generate usernames and passwords by using AccessKey pairs provided by Alibaba Cloud Resource Access Management (RAM).
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_binding_with_options(
        self,
        request: amqp_open_20191212_models.CreateBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateBindingResponse:
        """
        @summary Creates a binding. In ApsaraMQ for RabbitMQ, after a producer sends a message to an exchange, the exchange routes the message to a queue or another exchange based on the binding relationship and the routing rule.
        
        @param request: CreateBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBindingResponse
        """
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
        """
        @summary Creates a binding. In ApsaraMQ for RabbitMQ, after a producer sends a message to an exchange, the exchange routes the message to a queue or another exchange based on the binding relationship and the routing rule.
        
        @param request: CreateBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBindingResponse
        """
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
        """
        @summary Creates a binding. In ApsaraMQ for RabbitMQ, after a producer sends a message to an exchange, the exchange routes the message to a queue or another exchange based on the binding relationship and the routing rule.
        
        @param request: CreateBindingRequest
        @return: CreateBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_binding_with_options(request, runtime)

    async def create_binding_async(
        self,
        request: amqp_open_20191212_models.CreateBindingRequest,
    ) -> amqp_open_20191212_models.CreateBindingResponse:
        """
        @summary Creates a binding. In ApsaraMQ for RabbitMQ, after a producer sends a message to an exchange, the exchange routes the message to a queue or another exchange based on the binding relationship and the routing rule.
        
        @param request: CreateBindingRequest
        @return: CreateBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_binding_with_options_async(request, runtime)

    def create_exchange_with_options(
        self,
        request: amqp_open_20191212_models.CreateExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateExchangeResponse:
        """
        @summary Creates an exchange. In ApsaraMQ for RabbitMQ, an exchange is used to route a message that is received from a producer to one or more queues or to discard the message. An exchange routes a message to queues by using the routing key and binding keys.
        
        @param request: CreateExchangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExchangeResponse
        """
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
        if not UtilClient.is_unset(request.xdelayed_type):
            body['XDelayedType'] = request.xdelayed_type
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
        """
        @summary Creates an exchange. In ApsaraMQ for RabbitMQ, an exchange is used to route a message that is received from a producer to one or more queues or to discard the message. An exchange routes a message to queues by using the routing key and binding keys.
        
        @param request: CreateExchangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExchangeResponse
        """
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
        if not UtilClient.is_unset(request.xdelayed_type):
            body['XDelayedType'] = request.xdelayed_type
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
        """
        @summary Creates an exchange. In ApsaraMQ for RabbitMQ, an exchange is used to route a message that is received from a producer to one or more queues or to discard the message. An exchange routes a message to queues by using the routing key and binding keys.
        
        @param request: CreateExchangeRequest
        @return: CreateExchangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_exchange_with_options(request, runtime)

    async def create_exchange_async(
        self,
        request: amqp_open_20191212_models.CreateExchangeRequest,
    ) -> amqp_open_20191212_models.CreateExchangeResponse:
        """
        @summary Creates an exchange. In ApsaraMQ for RabbitMQ, an exchange is used to route a message that is received from a producer to one or more queues or to discard the message. An exchange routes a message to queues by using the routing key and binding keys.
        
        @param request: CreateExchangeRequest
        @return: CreateExchangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_exchange_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: amqp_open_20191212_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateInstanceResponse:
        """
        @summary 创建实例-基于 openAPI 构建南天门购买工单信息数据
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_connections):
            query['MaxConnections'] = request.max_connections
        if not UtilClient.is_unset(request.max_eip_tps):
            query['MaxEipTps'] = request.max_eip_tps
        if not UtilClient.is_unset(request.max_private_tps):
            query['MaxPrivateTps'] = request.max_private_tps
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_cycle):
            query['PeriodCycle'] = request.period_cycle
        if not UtilClient.is_unset(request.queue_capacity):
            query['QueueCapacity'] = request.queue_capacity
        if not UtilClient.is_unset(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not UtilClient.is_unset(request.renewal_duration_unit):
            query['RenewalDurationUnit'] = request.renewal_duration_unit
        if not UtilClient.is_unset(request.serverless_charge_type):
            query['ServerlessChargeType'] = request.serverless_charge_type
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.support_eip):
            query['SupportEip'] = request.support_eip
        if not UtilClient.is_unset(request.support_tracing):
            query['SupportTracing'] = request.support_tracing
        if not UtilClient.is_unset(request.tracing_storage_time):
            query['TracingStorageTime'] = request.tracing_storage_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
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
            amqp_open_20191212_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: amqp_open_20191212_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateInstanceResponse:
        """
        @summary 创建实例-基于 openAPI 构建南天门购买工单信息数据
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_connections):
            query['MaxConnections'] = request.max_connections
        if not UtilClient.is_unset(request.max_eip_tps):
            query['MaxEipTps'] = request.max_eip_tps
        if not UtilClient.is_unset(request.max_private_tps):
            query['MaxPrivateTps'] = request.max_private_tps
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_cycle):
            query['PeriodCycle'] = request.period_cycle
        if not UtilClient.is_unset(request.queue_capacity):
            query['QueueCapacity'] = request.queue_capacity
        if not UtilClient.is_unset(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not UtilClient.is_unset(request.renewal_duration_unit):
            query['RenewalDurationUnit'] = request.renewal_duration_unit
        if not UtilClient.is_unset(request.serverless_charge_type):
            query['ServerlessChargeType'] = request.serverless_charge_type
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.support_eip):
            query['SupportEip'] = request.support_eip
        if not UtilClient.is_unset(request.support_tracing):
            query['SupportTracing'] = request.support_tracing
        if not UtilClient.is_unset(request.tracing_storage_time):
            query['TracingStorageTime'] = request.tracing_storage_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
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
            amqp_open_20191212_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: amqp_open_20191212_models.CreateInstanceRequest,
    ) -> amqp_open_20191212_models.CreateInstanceResponse:
        """
        @summary 创建实例-基于 openAPI 构建南天门购买工单信息数据
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: amqp_open_20191212_models.CreateInstanceRequest,
    ) -> amqp_open_20191212_models.CreateInstanceResponse:
        """
        @summary 创建实例-基于 openAPI 构建南天门购买工单信息数据
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_queue_with_options(
        self,
        request: amqp_open_20191212_models.CreateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateQueueResponse:
        """
        @summary Creates a queue. In ApsaraMQ for RabbitMQ, a queue is a message queue. All messages in ApsaraMQ for RabbitMQ are sent to a specific exchange and then routed to a bound queue by the exchange.
        
        @param request: CreateQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueueResponse
        """
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
        """
        @summary Creates a queue. In ApsaraMQ for RabbitMQ, a queue is a message queue. All messages in ApsaraMQ for RabbitMQ are sent to a specific exchange and then routed to a bound queue by the exchange.
        
        @param request: CreateQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueueResponse
        """
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
        """
        @summary Creates a queue. In ApsaraMQ for RabbitMQ, a queue is a message queue. All messages in ApsaraMQ for RabbitMQ are sent to a specific exchange and then routed to a bound queue by the exchange.
        
        @param request: CreateQueueRequest
        @return: CreateQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_queue_with_options(request, runtime)

    async def create_queue_async(
        self,
        request: amqp_open_20191212_models.CreateQueueRequest,
    ) -> amqp_open_20191212_models.CreateQueueResponse:
        """
        @summary Creates a queue. In ApsaraMQ for RabbitMQ, a queue is a message queue. All messages in ApsaraMQ for RabbitMQ are sent to a specific exchange and then routed to a bound queue by the exchange.
        
        @param request: CreateQueueRequest
        @return: CreateQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_queue_with_options_async(request, runtime)

    def create_virtual_host_with_options(
        self,
        request: amqp_open_20191212_models.CreateVirtualHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.CreateVirtualHostResponse:
        """
        @summary Creates a vhost. A vhost is used to logically isolate resources. Each vhost manages its own exchanges, queues, and bindings. Applications can run on independent vhosts in a secure manner. This way, the business of an application is not affected by other applications. Before you connect producers and consumers to an ApsaraMQ for RabbitMQ instance, you must specify vhosts for the producers and consumers.
        
        @param request: CreateVirtualHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVirtualHostResponse
        """
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
        """
        @summary Creates a vhost. A vhost is used to logically isolate resources. Each vhost manages its own exchanges, queues, and bindings. Applications can run on independent vhosts in a secure manner. This way, the business of an application is not affected by other applications. Before you connect producers and consumers to an ApsaraMQ for RabbitMQ instance, you must specify vhosts for the producers and consumers.
        
        @param request: CreateVirtualHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVirtualHostResponse
        """
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
        """
        @summary Creates a vhost. A vhost is used to logically isolate resources. Each vhost manages its own exchanges, queues, and bindings. Applications can run on independent vhosts in a secure manner. This way, the business of an application is not affected by other applications. Before you connect producers and consumers to an ApsaraMQ for RabbitMQ instance, you must specify vhosts for the producers and consumers.
        
        @param request: CreateVirtualHostRequest
        @return: CreateVirtualHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_host_with_options(request, runtime)

    async def create_virtual_host_async(
        self,
        request: amqp_open_20191212_models.CreateVirtualHostRequest,
    ) -> amqp_open_20191212_models.CreateVirtualHostResponse:
        """
        @summary Creates a vhost. A vhost is used to logically isolate resources. Each vhost manages its own exchanges, queues, and bindings. Applications can run on independent vhosts in a secure manner. This way, the business of an application is not affected by other applications. Before you connect producers and consumers to an ApsaraMQ for RabbitMQ instance, you must specify vhosts for the producers and consumers.
        
        @param request: CreateVirtualHostRequest
        @return: CreateVirtualHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_host_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: amqp_open_20191212_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteAccountResponse:
        """
        @summary Deletes a pair of username and password.
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
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
        """
        @summary Deletes a pair of username and password.
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
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
        """
        @summary Deletes a pair of username and password.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: amqp_open_20191212_models.DeleteAccountRequest,
    ) -> amqp_open_20191212_models.DeleteAccountResponse:
        """
        @summary Deletes a pair of username and password.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_binding_with_options(
        self,
        request: amqp_open_20191212_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteBindingResponse:
        """
        @summary Deletes a binding to unbind a queue or an exchange from a source exchange.
        
        @param request: DeleteBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBindingResponse
        """
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
        """
        @summary Deletes a binding to unbind a queue or an exchange from a source exchange.
        
        @param request: DeleteBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBindingResponse
        """
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
        """
        @summary Deletes a binding to unbind a queue or an exchange from a source exchange.
        
        @param request: DeleteBindingRequest
        @return: DeleteBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_binding_with_options(request, runtime)

    async def delete_binding_async(
        self,
        request: amqp_open_20191212_models.DeleteBindingRequest,
    ) -> amqp_open_20191212_models.DeleteBindingResponse:
        """
        @summary Deletes a binding to unbind a queue or an exchange from a source exchange.
        
        @param request: DeleteBindingRequest
        @return: DeleteBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_binding_with_options_async(request, runtime)

    def delete_exchange_with_options(
        self,
        request: amqp_open_20191212_models.DeleteExchangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteExchangeResponse:
        """
        @summary Deletes an exchange.
        
        @description ## [](#)Usage notes
        You cannot delete exchanges of the **headers** and **x-jms-topic** types.
        You cannot delete built-in exchanges in a vhost. These exchanges are amq.direct, amq.topic, and amq.fanout.
        
        @param request: DeleteExchangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExchangeResponse
        """
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
        """
        @summary Deletes an exchange.
        
        @description ## [](#)Usage notes
        You cannot delete exchanges of the **headers** and **x-jms-topic** types.
        You cannot delete built-in exchanges in a vhost. These exchanges are amq.direct, amq.topic, and amq.fanout.
        
        @param request: DeleteExchangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExchangeResponse
        """
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
        """
        @summary Deletes an exchange.
        
        @description ## [](#)Usage notes
        You cannot delete exchanges of the **headers** and **x-jms-topic** types.
        You cannot delete built-in exchanges in a vhost. These exchanges are amq.direct, amq.topic, and amq.fanout.
        
        @param request: DeleteExchangeRequest
        @return: DeleteExchangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_exchange_with_options(request, runtime)

    async def delete_exchange_async(
        self,
        request: amqp_open_20191212_models.DeleteExchangeRequest,
    ) -> amqp_open_20191212_models.DeleteExchangeResponse:
        """
        @summary Deletes an exchange.
        
        @description ## [](#)Usage notes
        You cannot delete exchanges of the **headers** and **x-jms-topic** types.
        You cannot delete built-in exchanges in a vhost. These exchanges are amq.direct, amq.topic, and amq.fanout.
        
        @param request: DeleteExchangeRequest
        @return: DeleteExchangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_exchange_with_options_async(request, runtime)

    def delete_queue_with_options(
        self,
        request: amqp_open_20191212_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteQueueResponse:
        """
        @summary Deletes a queue.
        
        @param request: DeleteQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQueueResponse
        """
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
        """
        @summary Deletes a queue.
        
        @param request: DeleteQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQueueResponse
        """
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
        """
        @summary Deletes a queue.
        
        @param request: DeleteQueueRequest
        @return: DeleteQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    async def delete_queue_async(
        self,
        request: amqp_open_20191212_models.DeleteQueueRequest,
    ) -> amqp_open_20191212_models.DeleteQueueResponse:
        """
        @summary Deletes a queue.
        
        @param request: DeleteQueueRequest
        @return: DeleteQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_queue_with_options_async(request, runtime)

    def delete_virtual_host_with_options(
        self,
        request: amqp_open_20191212_models.DeleteVirtualHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.DeleteVirtualHostResponse:
        """
        @summary Deletes a virtual host (vhost).
        
        @description Before you delete a vhost, make sure that all exchanges and queues in the vhost are deleted.
        
        @param request: DeleteVirtualHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVirtualHostResponse
        """
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
        """
        @summary Deletes a virtual host (vhost).
        
        @description Before you delete a vhost, make sure that all exchanges and queues in the vhost are deleted.
        
        @param request: DeleteVirtualHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVirtualHostResponse
        """
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
        """
        @summary Deletes a virtual host (vhost).
        
        @description Before you delete a vhost, make sure that all exchanges and queues in the vhost are deleted.
        
        @param request: DeleteVirtualHostRequest
        @return: DeleteVirtualHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_host_with_options(request, runtime)

    async def delete_virtual_host_async(
        self,
        request: amqp_open_20191212_models.DeleteVirtualHostRequest,
    ) -> amqp_open_20191212_models.DeleteVirtualHostResponse:
        """
        @summary Deletes a virtual host (vhost).
        
        @description Before you delete a vhost, make sure that all exchanges and queues in the vhost are deleted.
        
        @param request: DeleteVirtualHostRequest
        @return: DeleteVirtualHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_host_with_options_async(request, runtime)

    def get_metadata_amount_with_options(
        self,
        request: amqp_open_20191212_models.GetMetadataAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.GetMetadataAmountResponse:
        """
        @summary Queries the maximum number of vhosts, exchanges, and queues that you can create and the number of created vhosts, exchanges, and queues on an ApsaraMQ for RabbitMQ instance.
        
        @param request: GetMetadataAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMetadataAmountResponse
        """
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
        """
        @summary Queries the maximum number of vhosts, exchanges, and queues that you can create and the number of created vhosts, exchanges, and queues on an ApsaraMQ for RabbitMQ instance.
        
        @param request: GetMetadataAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMetadataAmountResponse
        """
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
        """
        @summary Queries the maximum number of vhosts, exchanges, and queues that you can create and the number of created vhosts, exchanges, and queues on an ApsaraMQ for RabbitMQ instance.
        
        @param request: GetMetadataAmountRequest
        @return: GetMetadataAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_metadata_amount_with_options(request, runtime)

    async def get_metadata_amount_async(
        self,
        request: amqp_open_20191212_models.GetMetadataAmountRequest,
    ) -> amqp_open_20191212_models.GetMetadataAmountResponse:
        """
        @summary Queries the maximum number of vhosts, exchanges, and queues that you can create and the number of created vhosts, exchanges, and queues on an ApsaraMQ for RabbitMQ instance.
        
        @param request: GetMetadataAmountRequest
        @return: GetMetadataAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_metadata_amount_with_options_async(request, runtime)

    def list_accounts_with_options(
        self,
        request: amqp_open_20191212_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListAccountsResponse:
        """
        @summary Queries the static username and password of an ApsaraMQ for RabbitMQ.
        
        @param request: ListAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountsResponse
        """
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
        """
        @summary Queries the static username and password of an ApsaraMQ for RabbitMQ.
        
        @param request: ListAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountsResponse
        """
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
        """
        @summary Queries the static username and password of an ApsaraMQ for RabbitMQ.
        
        @param request: ListAccountsRequest
        @return: ListAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    async def list_accounts_async(
        self,
        request: amqp_open_20191212_models.ListAccountsRequest,
    ) -> amqp_open_20191212_models.ListAccountsResponse:
        """
        @summary Queries the static username and password of an ApsaraMQ for RabbitMQ.
        
        @param request: ListAccountsRequest
        @return: ListAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_with_options_async(request, runtime)

    def list_bindings_with_options(
        self,
        request: amqp_open_20191212_models.ListBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListBindingsResponse:
        """
        @summary Queries all bindings of a virtual host (vhost) on an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindingsResponse
        """
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
        """
        @summary Queries all bindings of a virtual host (vhost) on an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindingsResponse
        """
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
        """
        @summary Queries all bindings of a virtual host (vhost) on an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListBindingsRequest
        @return: ListBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_bindings_with_options(request, runtime)

    async def list_bindings_async(
        self,
        request: amqp_open_20191212_models.ListBindingsRequest,
    ) -> amqp_open_20191212_models.ListBindingsResponse:
        """
        @summary Queries all bindings of a virtual host (vhost) on an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListBindingsRequest
        @return: ListBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_bindings_with_options_async(request, runtime)

    def list_down_stream_bindings_with_options(
        self,
        request: amqp_open_20191212_models.ListDownStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListDownStreamBindingsResponse:
        """
        @summary Queries all exchanges or queues to which an exchange is bound.
        
        @param request: ListDownStreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDownStreamBindingsResponse
        """
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
        """
        @summary Queries all exchanges or queues to which an exchange is bound.
        
        @param request: ListDownStreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDownStreamBindingsResponse
        """
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
        """
        @summary Queries all exchanges or queues to which an exchange is bound.
        
        @param request: ListDownStreamBindingsRequest
        @return: ListDownStreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_down_stream_bindings_with_options(request, runtime)

    async def list_down_stream_bindings_async(
        self,
        request: amqp_open_20191212_models.ListDownStreamBindingsRequest,
    ) -> amqp_open_20191212_models.ListDownStreamBindingsResponse:
        """
        @summary Queries all exchanges or queues to which an exchange is bound.
        
        @param request: ListDownStreamBindingsRequest
        @return: ListDownStreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_down_stream_bindings_with_options_async(request, runtime)

    def list_exchange_up_stream_bindings_with_options(
        self,
        request: amqp_open_20191212_models.ListExchangeUpStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse:
        """
        @summary Queries all queues or exchanges that are bound to an exchange.
        
        @param request: ListExchangeUpStreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExchangeUpStreamBindingsResponse
        """
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
        """
        @summary Queries all queues or exchanges that are bound to an exchange.
        
        @param request: ListExchangeUpStreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExchangeUpStreamBindingsResponse
        """
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
        """
        @summary Queries all queues or exchanges that are bound to an exchange.
        
        @param request: ListExchangeUpStreamBindingsRequest
        @return: ListExchangeUpStreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_exchange_up_stream_bindings_with_options(request, runtime)

    async def list_exchange_up_stream_bindings_async(
        self,
        request: amqp_open_20191212_models.ListExchangeUpStreamBindingsRequest,
    ) -> amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse:
        """
        @summary Queries all queues or exchanges that are bound to an exchange.
        
        @param request: ListExchangeUpStreamBindingsRequest
        @return: ListExchangeUpStreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_exchange_up_stream_bindings_with_options_async(request, runtime)

    def list_exchanges_with_options(
        self,
        request: amqp_open_20191212_models.ListExchangesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListExchangesResponse:
        """
        @summary Queries all exchanges that are created in a virtual host (vhost).
        
        @param request: ListExchangesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExchangesResponse
        """
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
        """
        @summary Queries all exchanges that are created in a virtual host (vhost).
        
        @param request: ListExchangesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExchangesResponse
        """
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
        """
        @summary Queries all exchanges that are created in a virtual host (vhost).
        
        @param request: ListExchangesRequest
        @return: ListExchangesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_exchanges_with_options(request, runtime)

    async def list_exchanges_async(
        self,
        request: amqp_open_20191212_models.ListExchangesRequest,
    ) -> amqp_open_20191212_models.ListExchangesResponse:
        """
        @summary Queries all exchanges that are created in a virtual host (vhost).
        
        @param request: ListExchangesRequest
        @return: ListExchangesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_exchanges_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: amqp_open_20191212_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListInstancesResponse:
        """
        @summary Queries all AparaMQ for RabbitMQ instances in a region. The returned data includes the basic information, endpoint, and specification limits of each instance.
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
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
        """
        @summary Queries all AparaMQ for RabbitMQ instances in a region. The returned data includes the basic information, endpoint, and specification limits of each instance.
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
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
        """
        @summary Queries all AparaMQ for RabbitMQ instances in a region. The returned data includes the basic information, endpoint, and specification limits of each instance.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: amqp_open_20191212_models.ListInstancesRequest,
    ) -> amqp_open_20191212_models.ListInstancesResponse:
        """
        @summary Queries all AparaMQ for RabbitMQ instances in a region. The returned data includes the basic information, endpoint, and specification limits of each instance.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_queue_consumers_with_options(
        self,
        request: amqp_open_20191212_models.ListQueueConsumersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueueConsumersResponse:
        """
        @summary Queries the online consumers of a queue.
        
        @description ApsaraMQ for RabbitMQ allows you to query only online consumers.
        
        @param request: ListQueueConsumersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueueConsumersResponse
        """
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
        """
        @summary Queries the online consumers of a queue.
        
        @description ApsaraMQ for RabbitMQ allows you to query only online consumers.
        
        @param request: ListQueueConsumersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueueConsumersResponse
        """
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
        """
        @summary Queries the online consumers of a queue.
        
        @description ApsaraMQ for RabbitMQ allows you to query only online consumers.
        
        @param request: ListQueueConsumersRequest
        @return: ListQueueConsumersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_queue_consumers_with_options(request, runtime)

    async def list_queue_consumers_async(
        self,
        request: amqp_open_20191212_models.ListQueueConsumersRequest,
    ) -> amqp_open_20191212_models.ListQueueConsumersResponse:
        """
        @summary Queries the online consumers of a queue.
        
        @description ApsaraMQ for RabbitMQ allows you to query only online consumers.
        
        @param request: ListQueueConsumersRequest
        @return: ListQueueConsumersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_queue_consumers_with_options_async(request, runtime)

    def list_queue_up_stream_bindings_with_options(
        self,
        request: amqp_open_20191212_models.ListQueueUpStreamBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueueUpStreamBindingsResponse:
        """
        @summary Queries the exchanges that are bound to a queue.
        
        @param request: ListQueueUpStreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueueUpStreamBindingsResponse
        """
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
        """
        @summary Queries the exchanges that are bound to a queue.
        
        @param request: ListQueueUpStreamBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueueUpStreamBindingsResponse
        """
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
        """
        @summary Queries the exchanges that are bound to a queue.
        
        @param request: ListQueueUpStreamBindingsRequest
        @return: ListQueueUpStreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_queue_up_stream_bindings_with_options(request, runtime)

    async def list_queue_up_stream_bindings_async(
        self,
        request: amqp_open_20191212_models.ListQueueUpStreamBindingsRequest,
    ) -> amqp_open_20191212_models.ListQueueUpStreamBindingsResponse:
        """
        @summary Queries the exchanges that are bound to a queue.
        
        @param request: ListQueueUpStreamBindingsRequest
        @return: ListQueueUpStreamBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_queue_up_stream_bindings_with_options_async(request, runtime)

    def list_queues_with_options(
        self,
        request: amqp_open_20191212_models.ListQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListQueuesResponse:
        """
        @summary Queries all queues in a vhost of an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListQueuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueuesResponse
        """
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
        """
        @summary Queries all queues in a vhost of an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListQueuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueuesResponse
        """
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
        """
        @summary Queries all queues in a vhost of an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListQueuesRequest
        @return: ListQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_queues_with_options(request, runtime)

    async def list_queues_async(
        self,
        request: amqp_open_20191212_models.ListQueuesRequest,
    ) -> amqp_open_20191212_models.ListQueuesResponse:
        """
        @summary Queries all queues in a vhost of an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListQueuesRequest
        @return: ListQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_queues_with_options_async(request, runtime)

    def list_virtual_hosts_with_options(
        self,
        request: amqp_open_20191212_models.ListVirtualHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.ListVirtualHostsResponse:
        """
        @summary Queries all virtual hosts (vhosts) on an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListVirtualHostsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualHostsResponse
        """
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
        """
        @summary Queries all virtual hosts (vhosts) on an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListVirtualHostsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualHostsResponse
        """
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
        """
        @summary Queries all virtual hosts (vhosts) on an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListVirtualHostsRequest
        @return: ListVirtualHostsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_hosts_with_options(request, runtime)

    async def list_virtual_hosts_async(
        self,
        request: amqp_open_20191212_models.ListVirtualHostsRequest,
    ) -> amqp_open_20191212_models.ListVirtualHostsResponse:
        """
        @summary Queries all virtual hosts (vhosts) on an ApsaraMQ for RabbitMQ instance.
        
        @param request: ListVirtualHostsRequest
        @return: ListVirtualHostsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_virtual_hosts_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: amqp_open_20191212_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.UpdateInstanceResponse:
        """
        @summary 变更实例，升降配
        
        @param request: UpdateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_connections):
            query['MaxConnections'] = request.max_connections
        if not UtilClient.is_unset(request.max_eip_tps):
            query['MaxEipTps'] = request.max_eip_tps
        if not UtilClient.is_unset(request.max_private_tps):
            query['MaxPrivateTps'] = request.max_private_tps
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.queue_capacity):
            query['QueueCapacity'] = request.queue_capacity
        if not UtilClient.is_unset(request.serverless_charge_type):
            query['ServerlessChargeType'] = request.serverless_charge_type
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.support_eip):
            query['SupportEip'] = request.support_eip
        if not UtilClient.is_unset(request.support_tracing):
            query['SupportTracing'] = request.support_tracing
        if not UtilClient.is_unset(request.tracing_storage_time):
            query['TracingStorageTime'] = request.tracing_storage_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
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
            amqp_open_20191212_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: amqp_open_20191212_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.UpdateInstanceResponse:
        """
        @summary 变更实例，升降配
        
        @param request: UpdateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_connections):
            query['MaxConnections'] = request.max_connections
        if not UtilClient.is_unset(request.max_eip_tps):
            query['MaxEipTps'] = request.max_eip_tps
        if not UtilClient.is_unset(request.max_private_tps):
            query['MaxPrivateTps'] = request.max_private_tps
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.queue_capacity):
            query['QueueCapacity'] = request.queue_capacity
        if not UtilClient.is_unset(request.serverless_charge_type):
            query['ServerlessChargeType'] = request.serverless_charge_type
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.support_eip):
            query['SupportEip'] = request.support_eip
        if not UtilClient.is_unset(request.support_tracing):
            query['SupportTracing'] = request.support_tracing
        if not UtilClient.is_unset(request.tracing_storage_time):
            query['TracingStorageTime'] = request.tracing_storage_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
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
            amqp_open_20191212_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: amqp_open_20191212_models.UpdateInstanceRequest,
    ) -> amqp_open_20191212_models.UpdateInstanceResponse:
        """
        @summary 变更实例，升降配
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: amqp_open_20191212_models.UpdateInstanceRequest,
    ) -> amqp_open_20191212_models.UpdateInstanceResponse:
        """
        @summary 变更实例，升降配
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_instance_name_with_options(
        self,
        request: amqp_open_20191212_models.UpdateInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amqp_open_20191212_models.UpdateInstanceNameResponse:
        """
        @summary Updates the name of an ApsaraMQ for RabbitMQ instance. After an ApsaraMQ for RabbitMQ instance is created, the ID of the instance is used as its name by default. You can specify a custom name for an instance to facilitate instance identification.
        
        @param request: UpdateInstanceNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceNameResponse
        """
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
        """
        @summary Updates the name of an ApsaraMQ for RabbitMQ instance. After an ApsaraMQ for RabbitMQ instance is created, the ID of the instance is used as its name by default. You can specify a custom name for an instance to facilitate instance identification.
        
        @param request: UpdateInstanceNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceNameResponse
        """
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
        """
        @summary Updates the name of an ApsaraMQ for RabbitMQ instance. After an ApsaraMQ for RabbitMQ instance is created, the ID of the instance is used as its name by default. You can specify a custom name for an instance to facilitate instance identification.
        
        @param request: UpdateInstanceNameRequest
        @return: UpdateInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_name_with_options(request, runtime)

    async def update_instance_name_async(
        self,
        request: amqp_open_20191212_models.UpdateInstanceNameRequest,
    ) -> amqp_open_20191212_models.UpdateInstanceNameResponse:
        """
        @summary Updates the name of an ApsaraMQ for RabbitMQ instance. After an ApsaraMQ for RabbitMQ instance is created, the ID of the instance is used as its name by default. You can specify a custom name for an instance to facilitate instance identification.
        
        @param request: UpdateInstanceNameRequest
        @return: UpdateInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_name_with_options_async(request, runtime)
