# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_amqp_open20191212 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_account_with_options(
        self,
        request: main_models.CreateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.account_access_key):
            query['accountAccessKey'] = request.account_access_key
        if not DaraCore.is_null(request.create_timestamp):
            query['createTimestamp'] = request.create_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_sign):
            query['secretSign'] = request.secret_sign
        if not DaraCore.is_null(request.signature):
            query['signature'] = request.signature
        if not DaraCore.is_null(request.user_name):
            query['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: main_models.CreateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.account_access_key):
            query['accountAccessKey'] = request.account_access_key
        if not DaraCore.is_null(request.create_timestamp):
            query['createTimestamp'] = request.create_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_sign):
            query['secretSign'] = request.secret_sign
        if not DaraCore.is_null(request.signature):
            query['signature'] = request.signature
        if not DaraCore.is_null(request.user_name):
            query['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: main_models.CreateAccountRequest,
    ) -> main_models.CreateAccountResponse:
        runtime = RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: main_models.CreateAccountRequest,
    ) -> main_models.CreateAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_binding_with_options(
        self,
        request: main_models.CreateBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBindingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.argument):
            body['Argument'] = request.argument
        if not DaraCore.is_null(request.binding_key):
            body['BindingKey'] = request.binding_key
        if not DaraCore.is_null(request.binding_type):
            body['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.destination_name):
            body['DestinationName'] = request.destination_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_exchange):
            body['SourceExchange'] = request.source_exchange
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBinding',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_binding_with_options_async(
        self,
        request: main_models.CreateBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBindingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.argument):
            body['Argument'] = request.argument
        if not DaraCore.is_null(request.binding_key):
            body['BindingKey'] = request.binding_key
        if not DaraCore.is_null(request.binding_type):
            body['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.destination_name):
            body['DestinationName'] = request.destination_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_exchange):
            body['SourceExchange'] = request.source_exchange
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBinding',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_binding(
        self,
        request: main_models.CreateBindingRequest,
    ) -> main_models.CreateBindingResponse:
        runtime = RuntimeOptions()
        return self.create_binding_with_options(request, runtime)

    async def create_binding_async(
        self,
        request: main_models.CreateBindingRequest,
    ) -> main_models.CreateBindingResponse:
        runtime = RuntimeOptions()
        return await self.create_binding_with_options_async(request, runtime)

    def create_exchange_with_options(
        self,
        request: main_models.CreateExchangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExchangeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alternate_exchange):
            body['AlternateExchange'] = request.alternate_exchange
        if not DaraCore.is_null(request.auto_delete_state):
            body['AutoDeleteState'] = request.auto_delete_state
        if not DaraCore.is_null(request.exchange_name):
            body['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.exchange_type):
            body['ExchangeType'] = request.exchange_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.internal):
            body['Internal'] = request.internal
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        if not DaraCore.is_null(request.xdelayed_type):
            body['XDelayedType'] = request.xdelayed_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExchange',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_exchange_with_options_async(
        self,
        request: main_models.CreateExchangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExchangeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alternate_exchange):
            body['AlternateExchange'] = request.alternate_exchange
        if not DaraCore.is_null(request.auto_delete_state):
            body['AutoDeleteState'] = request.auto_delete_state
        if not DaraCore.is_null(request.exchange_name):
            body['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.exchange_type):
            body['ExchangeType'] = request.exchange_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.internal):
            body['Internal'] = request.internal
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        if not DaraCore.is_null(request.xdelayed_type):
            body['XDelayedType'] = request.xdelayed_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExchange',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExchangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_exchange(
        self,
        request: main_models.CreateExchangeRequest,
    ) -> main_models.CreateExchangeResponse:
        runtime = RuntimeOptions()
        return self.create_exchange_with_options(request, runtime)

    async def create_exchange_async(
        self,
        request: main_models.CreateExchangeRequest,
    ) -> main_models.CreateExchangeResponse:
        runtime = RuntimeOptions()
        return await self.create_exchange_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        tmp_req: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.encrypted_instance):
            query['EncryptedInstance'] = request.encrypted_instance
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.max_connections):
            query['MaxConnections'] = request.max_connections
        if not DaraCore.is_null(request.max_eip_tps):
            query['MaxEipTps'] = request.max_eip_tps
        if not DaraCore.is_null(request.max_private_tps):
            query['MaxPrivateTps'] = request.max_private_tps
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_cycle):
            query['PeriodCycle'] = request.period_cycle
        if not DaraCore.is_null(request.provisioned_capacity):
            query['ProvisionedCapacity'] = request.provisioned_capacity
        if not DaraCore.is_null(request.queue_capacity):
            query['QueueCapacity'] = request.queue_capacity
        if not DaraCore.is_null(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not DaraCore.is_null(request.renewal_duration_unit):
            query['RenewalDurationUnit'] = request.renewal_duration_unit
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.serverless_charge_type):
            query['ServerlessChargeType'] = request.serverless_charge_type
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.support_eip):
            query['SupportEip'] = request.support_eip
        if not DaraCore.is_null(request.support_tracing):
            query['SupportTracing'] = request.support_tracing
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.tracing_storage_time):
            query['TracingStorageTime'] = request.tracing_storage_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        tmp_req: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.encrypted_instance):
            query['EncryptedInstance'] = request.encrypted_instance
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.max_connections):
            query['MaxConnections'] = request.max_connections
        if not DaraCore.is_null(request.max_eip_tps):
            query['MaxEipTps'] = request.max_eip_tps
        if not DaraCore.is_null(request.max_private_tps):
            query['MaxPrivateTps'] = request.max_private_tps
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_cycle):
            query['PeriodCycle'] = request.period_cycle
        if not DaraCore.is_null(request.provisioned_capacity):
            query['ProvisionedCapacity'] = request.provisioned_capacity
        if not DaraCore.is_null(request.queue_capacity):
            query['QueueCapacity'] = request.queue_capacity
        if not DaraCore.is_null(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not DaraCore.is_null(request.renewal_duration_unit):
            query['RenewalDurationUnit'] = request.renewal_duration_unit
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.serverless_charge_type):
            query['ServerlessChargeType'] = request.serverless_charge_type
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.support_eip):
            query['SupportEip'] = request.support_eip
        if not DaraCore.is_null(request.support_tracing):
            query['SupportTracing'] = request.support_tracing
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.tracing_storage_time):
            query['TracingStorageTime'] = request.tracing_storage_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_queue_with_options(
        self,
        request: main_models.CreateQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_delete_state):
            body['AutoDeleteState'] = request.auto_delete_state
        if not DaraCore.is_null(request.auto_expire_state):
            body['AutoExpireState'] = request.auto_expire_state
        if not DaraCore.is_null(request.dead_letter_exchange):
            body['DeadLetterExchange'] = request.dead_letter_exchange
        if not DaraCore.is_null(request.dead_letter_routing_key):
            body['DeadLetterRoutingKey'] = request.dead_letter_routing_key
        if not DaraCore.is_null(request.exclusive_state):
            body['ExclusiveState'] = request.exclusive_state
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_length):
            body['MaxLength'] = request.max_length
        if not DaraCore.is_null(request.maximum_priority):
            body['MaximumPriority'] = request.maximum_priority
        if not DaraCore.is_null(request.message_ttl):
            body['MessageTTL'] = request.message_ttl
        if not DaraCore.is_null(request.queue_name):
            body['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueue',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_queue_with_options_async(
        self,
        request: main_models.CreateQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_delete_state):
            body['AutoDeleteState'] = request.auto_delete_state
        if not DaraCore.is_null(request.auto_expire_state):
            body['AutoExpireState'] = request.auto_expire_state
        if not DaraCore.is_null(request.dead_letter_exchange):
            body['DeadLetterExchange'] = request.dead_letter_exchange
        if not DaraCore.is_null(request.dead_letter_routing_key):
            body['DeadLetterRoutingKey'] = request.dead_letter_routing_key
        if not DaraCore.is_null(request.exclusive_state):
            body['ExclusiveState'] = request.exclusive_state
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_length):
            body['MaxLength'] = request.max_length
        if not DaraCore.is_null(request.maximum_priority):
            body['MaximumPriority'] = request.maximum_priority
        if not DaraCore.is_null(request.message_ttl):
            body['MessageTTL'] = request.message_ttl
        if not DaraCore.is_null(request.queue_name):
            body['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueue',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_queue(
        self,
        request: main_models.CreateQueueRequest,
    ) -> main_models.CreateQueueResponse:
        runtime = RuntimeOptions()
        return self.create_queue_with_options(request, runtime)

    async def create_queue_async(
        self,
        request: main_models.CreateQueueRequest,
    ) -> main_models.CreateQueueResponse:
        runtime = RuntimeOptions()
        return await self.create_queue_with_options_async(request, runtime)

    def create_virtual_host_with_options(
        self,
        request: main_models.CreateVirtualHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVirtualHostResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVirtualHost',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVirtualHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_virtual_host_with_options_async(
        self,
        request: main_models.CreateVirtualHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVirtualHostResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVirtualHost',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVirtualHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_virtual_host(
        self,
        request: main_models.CreateVirtualHostRequest,
    ) -> main_models.CreateVirtualHostResponse:
        runtime = RuntimeOptions()
        return self.create_virtual_host_with_options(request, runtime)

    async def create_virtual_host_async(
        self,
        request: main_models.CreateVirtualHostRequest,
    ) -> main_models.CreateVirtualHostResponse:
        runtime = RuntimeOptions()
        return await self.create_virtual_host_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_timestamp):
            query['CreateTimestamp'] = request.create_timestamp
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_timestamp):
            query['CreateTimestamp'] = request.create_timestamp
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: main_models.DeleteAccountRequest,
    ) -> main_models.DeleteAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: main_models.DeleteAccountRequest,
    ) -> main_models.DeleteAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_binding_with_options(
        self,
        request: main_models.DeleteBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBindingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.binding_key):
            body['BindingKey'] = request.binding_key
        if not DaraCore.is_null(request.binding_type):
            body['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.destination_name):
            body['DestinationName'] = request.destination_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_exchange):
            body['SourceExchange'] = request.source_exchange
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBinding',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_binding_with_options_async(
        self,
        request: main_models.DeleteBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBindingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.binding_key):
            body['BindingKey'] = request.binding_key
        if not DaraCore.is_null(request.binding_type):
            body['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.destination_name):
            body['DestinationName'] = request.destination_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source_exchange):
            body['SourceExchange'] = request.source_exchange
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBinding',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_binding(
        self,
        request: main_models.DeleteBindingRequest,
    ) -> main_models.DeleteBindingResponse:
        runtime = RuntimeOptions()
        return self.delete_binding_with_options(request, runtime)

    async def delete_binding_async(
        self,
        request: main_models.DeleteBindingRequest,
    ) -> main_models.DeleteBindingResponse:
        runtime = RuntimeOptions()
        return await self.delete_binding_with_options_async(request, runtime)

    def delete_exchange_with_options(
        self,
        request: main_models.DeleteExchangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExchangeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.exchange_name):
            body['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExchange',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_exchange_with_options_async(
        self,
        request: main_models.DeleteExchangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExchangeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.exchange_name):
            body['ExchangeName'] = request.exchange_name
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExchange',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExchangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_exchange(
        self,
        request: main_models.DeleteExchangeRequest,
    ) -> main_models.DeleteExchangeResponse:
        runtime = RuntimeOptions()
        return self.delete_exchange_with_options(request, runtime)

    async def delete_exchange_async(
        self,
        request: main_models.DeleteExchangeRequest,
    ) -> main_models.DeleteExchangeResponse:
        runtime = RuntimeOptions()
        return await self.delete_exchange_with_options_async(request, runtime)

    def delete_queue_with_options(
        self,
        request: main_models.DeleteQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQueueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.queue_name):
            body['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQueue',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_queue_with_options_async(
        self,
        request: main_models.DeleteQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQueueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.queue_name):
            body['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQueue',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_queue(
        self,
        request: main_models.DeleteQueueRequest,
    ) -> main_models.DeleteQueueResponse:
        runtime = RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    async def delete_queue_async(
        self,
        request: main_models.DeleteQueueRequest,
    ) -> main_models.DeleteQueueResponse:
        runtime = RuntimeOptions()
        return await self.delete_queue_with_options_async(request, runtime)

    def delete_virtual_host_with_options(
        self,
        request: main_models.DeleteVirtualHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVirtualHostResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVirtualHost',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVirtualHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_virtual_host_with_options_async(
        self,
        request: main_models.DeleteVirtualHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVirtualHostResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVirtualHost',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVirtualHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_virtual_host(
        self,
        request: main_models.DeleteVirtualHostRequest,
    ) -> main_models.DeleteVirtualHostResponse:
        runtime = RuntimeOptions()
        return self.delete_virtual_host_with_options(request, runtime)

    async def delete_virtual_host_async(
        self,
        request: main_models.DeleteVirtualHostRequest,
    ) -> main_models.DeleteVirtualHostResponse:
        runtime = RuntimeOptions()
        return await self.delete_virtual_host_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_metadata_amount_with_options(
        self,
        request: main_models.GetMetadataAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMetadataAmountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMetadataAmount',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetadataAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_metadata_amount_with_options_async(
        self,
        request: main_models.GetMetadataAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMetadataAmountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMetadataAmount',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetadataAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_metadata_amount(
        self,
        request: main_models.GetMetadataAmountRequest,
    ) -> main_models.GetMetadataAmountResponse:
        runtime = RuntimeOptions()
        return self.get_metadata_amount_with_options(request, runtime)

    async def get_metadata_amount_async(
        self,
        request: main_models.GetMetadataAmountRequest,
    ) -> main_models.GetMetadataAmountResponse:
        runtime = RuntimeOptions()
        return await self.get_metadata_amount_with_options_async(request, runtime)

    def list_accounts_with_options(
        self,
        request: main_models.ListAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccounts',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_with_options_async(
        self,
        request: main_models.ListAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccounts',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts(
        self,
        request: main_models.ListAccountsRequest,
    ) -> main_models.ListAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    async def list_accounts_async(
        self,
        request: main_models.ListAccountsRequest,
    ) -> main_models.ListAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_accounts_with_options_async(request, runtime)

    def list_bindings_with_options(
        self,
        request: main_models.ListBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindingsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBindings',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bindings_with_options_async(
        self,
        request: main_models.ListBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindingsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBindings',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bindings(
        self,
        request: main_models.ListBindingsRequest,
    ) -> main_models.ListBindingsResponse:
        runtime = RuntimeOptions()
        return self.list_bindings_with_options(request, runtime)

    async def list_bindings_async(
        self,
        request: main_models.ListBindingsRequest,
    ) -> main_models.ListBindingsResponse:
        runtime = RuntimeOptions()
        return await self.list_bindings_with_options_async(request, runtime)

    def list_down_stream_bindings_with_options(
        self,
        request: main_models.ListDownStreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDownStreamBindingsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownStreamBindings',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownStreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_down_stream_bindings_with_options_async(
        self,
        request: main_models.ListDownStreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDownStreamBindingsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownStreamBindings',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownStreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_down_stream_bindings(
        self,
        request: main_models.ListDownStreamBindingsRequest,
    ) -> main_models.ListDownStreamBindingsResponse:
        runtime = RuntimeOptions()
        return self.list_down_stream_bindings_with_options(request, runtime)

    async def list_down_stream_bindings_async(
        self,
        request: main_models.ListDownStreamBindingsRequest,
    ) -> main_models.ListDownStreamBindingsResponse:
        runtime = RuntimeOptions()
        return await self.list_down_stream_bindings_with_options_async(request, runtime)

    def list_exchange_up_stream_bindings_with_options(
        self,
        request: main_models.ListExchangeUpStreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExchangeUpStreamBindingsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExchangeUpStreamBindings',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExchangeUpStreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_exchange_up_stream_bindings_with_options_async(
        self,
        request: main_models.ListExchangeUpStreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExchangeUpStreamBindingsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExchangeUpStreamBindings',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExchangeUpStreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_exchange_up_stream_bindings(
        self,
        request: main_models.ListExchangeUpStreamBindingsRequest,
    ) -> main_models.ListExchangeUpStreamBindingsResponse:
        runtime = RuntimeOptions()
        return self.list_exchange_up_stream_bindings_with_options(request, runtime)

    async def list_exchange_up_stream_bindings_async(
        self,
        request: main_models.ListExchangeUpStreamBindingsRequest,
    ) -> main_models.ListExchangeUpStreamBindingsResponse:
        runtime = RuntimeOptions()
        return await self.list_exchange_up_stream_bindings_with_options_async(request, runtime)

    def list_exchanges_with_options(
        self,
        request: main_models.ListExchangesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExchangesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExchanges',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExchangesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_exchanges_with_options_async(
        self,
        request: main_models.ListExchangesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExchangesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExchanges',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExchangesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_exchanges(
        self,
        request: main_models.ListExchangesRequest,
    ) -> main_models.ListExchangesResponse:
        runtime = RuntimeOptions()
        return self.list_exchanges_with_options(request, runtime)

    async def list_exchanges_async(
        self,
        request: main_models.ListExchangesRequest,
    ) -> main_models.ListExchangesResponse:
        runtime = RuntimeOptions()
        return await self.list_exchanges_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_queue_consumers_with_options(
        self,
        request: main_models.ListQueueConsumersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueueConsumersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueueConsumers',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueueConsumersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queue_consumers_with_options_async(
        self,
        request: main_models.ListQueueConsumersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueueConsumersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueueConsumers',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueueConsumersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_queue_consumers(
        self,
        request: main_models.ListQueueConsumersRequest,
    ) -> main_models.ListQueueConsumersResponse:
        runtime = RuntimeOptions()
        return self.list_queue_consumers_with_options(request, runtime)

    async def list_queue_consumers_async(
        self,
        request: main_models.ListQueueConsumersRequest,
    ) -> main_models.ListQueueConsumersResponse:
        runtime = RuntimeOptions()
        return await self.list_queue_consumers_with_options_async(request, runtime)

    def list_queue_up_stream_bindings_with_options(
        self,
        request: main_models.ListQueueUpStreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueueUpStreamBindingsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueueUpStreamBindings',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueueUpStreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queue_up_stream_bindings_with_options_async(
        self,
        request: main_models.ListQueueUpStreamBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueueUpStreamBindingsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueueUpStreamBindings',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueueUpStreamBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_queue_up_stream_bindings(
        self,
        request: main_models.ListQueueUpStreamBindingsRequest,
    ) -> main_models.ListQueueUpStreamBindingsResponse:
        runtime = RuntimeOptions()
        return self.list_queue_up_stream_bindings_with_options(request, runtime)

    async def list_queue_up_stream_bindings_async(
        self,
        request: main_models.ListQueueUpStreamBindingsRequest,
    ) -> main_models.ListQueueUpStreamBindingsResponse:
        runtime = RuntimeOptions()
        return await self.list_queue_up_stream_bindings_with_options_async(request, runtime)

    def list_queues_with_options(
        self,
        request: main_models.ListQueuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueuesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueues',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queues_with_options_async(
        self,
        request: main_models.ListQueuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueuesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueues',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_queues(
        self,
        request: main_models.ListQueuesRequest,
    ) -> main_models.ListQueuesResponse:
        runtime = RuntimeOptions()
        return self.list_queues_with_options(request, runtime)

    async def list_queues_async(
        self,
        request: main_models.ListQueuesRequest,
    ) -> main_models.ListQueuesResponse:
        runtime = RuntimeOptions()
        return await self.list_queues_with_options_async(request, runtime)

    def list_virtual_hosts_with_options(
        self,
        request: main_models.ListVirtualHostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVirtualHostsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVirtualHosts',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVirtualHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_virtual_hosts_with_options_async(
        self,
        request: main_models.ListVirtualHostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVirtualHostsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVirtualHosts',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVirtualHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_virtual_hosts(
        self,
        request: main_models.ListVirtualHostsRequest,
    ) -> main_models.ListVirtualHostsResponse:
        runtime = RuntimeOptions()
        return self.list_virtual_hosts_with_options(request, runtime)

    async def list_virtual_hosts_async(
        self,
        request: main_models.ListVirtualHostsRequest,
    ) -> main_models.ListVirtualHostsResponse:
        runtime = RuntimeOptions()
        return await self.list_virtual_hosts_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.encrypted_instance):
            query['EncryptedInstance'] = request.encrypted_instance
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.max_connections):
            query['MaxConnections'] = request.max_connections
        if not DaraCore.is_null(request.max_eip_tps):
            query['MaxEipTps'] = request.max_eip_tps
        if not DaraCore.is_null(request.max_private_tps):
            query['MaxPrivateTps'] = request.max_private_tps
        if not DaraCore.is_null(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.provisioned_capacity):
            query['ProvisionedCapacity'] = request.provisioned_capacity
        if not DaraCore.is_null(request.queue_capacity):
            query['QueueCapacity'] = request.queue_capacity
        if not DaraCore.is_null(request.serverless_charge_type):
            query['ServerlessChargeType'] = request.serverless_charge_type
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.support_eip):
            query['SupportEip'] = request.support_eip
        if not DaraCore.is_null(request.support_tracing):
            query['SupportTracing'] = request.support_tracing
        if not DaraCore.is_null(request.tracing_storage_time):
            query['TracingStorageTime'] = request.tracing_storage_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.encrypted_instance):
            query['EncryptedInstance'] = request.encrypted_instance
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.max_connections):
            query['MaxConnections'] = request.max_connections
        if not DaraCore.is_null(request.max_eip_tps):
            query['MaxEipTps'] = request.max_eip_tps
        if not DaraCore.is_null(request.max_private_tps):
            query['MaxPrivateTps'] = request.max_private_tps
        if not DaraCore.is_null(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.provisioned_capacity):
            query['ProvisionedCapacity'] = request.provisioned_capacity
        if not DaraCore.is_null(request.queue_capacity):
            query['QueueCapacity'] = request.queue_capacity
        if not DaraCore.is_null(request.serverless_charge_type):
            query['ServerlessChargeType'] = request.serverless_charge_type
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not DaraCore.is_null(request.support_eip):
            query['SupportEip'] = request.support_eip
        if not DaraCore.is_null(request.support_tracing):
            query['SupportTracing'] = request.support_tracing
        if not DaraCore.is_null(request.tracing_storage_time):
            query['TracingStorageTime'] = request.tracing_storage_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_instance_name_with_options(
        self,
        request: main_models.UpdateInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceName',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_name_with_options_async(
        self,
        request: main_models.UpdateInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceName',
            version = '2019-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_name(
        self,
        request: main_models.UpdateInstanceNameRequest,
    ) -> main_models.UpdateInstanceNameResponse:
        runtime = RuntimeOptions()
        return self.update_instance_name_with_options(request, runtime)

    async def update_instance_name_async(
        self,
        request: main_models.UpdateInstanceNameRequest,
    ) -> main_models.UpdateInstanceNameResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_name_with_options_async(request, runtime)
