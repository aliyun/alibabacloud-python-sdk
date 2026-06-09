# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_eventbridge20200401 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('eventbridge', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def ask_luma_with_options(
        self,
        request: main_models.AskLumaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AskLumaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.max_rows):
            body['MaxRows'] = request.max_rows
        if not DaraCore.is_null(request.question):
            body['Question'] = request.question
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AskLuma',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AskLumaResponse(),
            self.call_api(params, req, runtime)
        )

    async def ask_luma_with_options_async(
        self,
        request: main_models.AskLumaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AskLumaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.conversation_id):
            body['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.max_rows):
            body['MaxRows'] = request.max_rows
        if not DaraCore.is_null(request.question):
            body['Question'] = request.question
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AskLuma',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AskLumaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ask_luma(
        self,
        request: main_models.AskLumaRequest,
    ) -> main_models.AskLumaResponse:
        runtime = RuntimeOptions()
        return self.ask_luma_with_options(request, runtime)

    async def ask_luma_async(
        self,
        request: main_models.AskLumaRequest,
    ) -> main_models.AskLumaResponse:
        runtime = RuntimeOptions()
        return await self.ask_luma_with_options_async(request, runtime)

    def check_service_linked_role_for_product_with_options(
        self,
        request: main_models.CheckServiceLinkedRoleForProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceLinkedRoleForProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRoleForProduct',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceLinkedRoleForProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_for_product_with_options_async(
        self,
        request: main_models.CheckServiceLinkedRoleForProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceLinkedRoleForProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRoleForProduct',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceLinkedRoleForProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role_for_product(
        self,
        request: main_models.CheckServiceLinkedRoleForProductRequest,
    ) -> main_models.CheckServiceLinkedRoleForProductResponse:
        runtime = RuntimeOptions()
        return self.check_service_linked_role_for_product_with_options(request, runtime)

    async def check_service_linked_role_for_product_async(
        self,
        request: main_models.CheckServiceLinkedRoleForProductRequest,
    ) -> main_models.CheckServiceLinkedRoleForProductResponse:
        runtime = RuntimeOptions()
        return await self.check_service_linked_role_for_product_with_options_async(request, runtime)

    def create_agent_with_options(
        self,
        tmp_req: main_models.CreateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResponse:
        tmp_req.validate()
        request = main_models.CreateAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metadata):
            request.metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.metadata_shrink):
            body['Metadata'] = request.metadata_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgent',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_with_options_async(
        self,
        tmp_req: main_models.CreateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResponse:
        tmp_req.validate()
        request = main_models.CreateAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metadata):
            request.metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.metadata_shrink):
            body['Metadata'] = request.metadata_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgent',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent(
        self,
        request: main_models.CreateAgentRequest,
    ) -> main_models.CreateAgentResponse:
        runtime = RuntimeOptions()
        return self.create_agent_with_options(request, runtime)

    async def create_agent_async(
        self,
        request: main_models.CreateAgentRequest,
    ) -> main_models.CreateAgentResponse:
        runtime = RuntimeOptions()
        return await self.create_agent_with_options_async(request, runtime)

    def create_api_destination_with_options(
        self,
        tmp_req: main_models.CreateApiDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiDestinationResponse:
        tmp_req.validate()
        request = main_models.CreateApiDestinationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.http_api_parameters):
            request.http_api_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.http_api_parameters, 'HttpApiParameters', 'json')
        query = {}
        if not DaraCore.is_null(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.http_api_parameters_shrink):
            query['HttpApiParameters'] = request.http_api_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiDestination',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_destination_with_options_async(
        self,
        tmp_req: main_models.CreateApiDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiDestinationResponse:
        tmp_req.validate()
        request = main_models.CreateApiDestinationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.http_api_parameters):
            request.http_api_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.http_api_parameters, 'HttpApiParameters', 'json')
        query = {}
        if not DaraCore.is_null(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.http_api_parameters_shrink):
            query['HttpApiParameters'] = request.http_api_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiDestination',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_destination(
        self,
        request: main_models.CreateApiDestinationRequest,
    ) -> main_models.CreateApiDestinationResponse:
        runtime = RuntimeOptions()
        return self.create_api_destination_with_options(request, runtime)

    async def create_api_destination_async(
        self,
        request: main_models.CreateApiDestinationRequest,
    ) -> main_models.CreateApiDestinationResponse:
        runtime = RuntimeOptions()
        return await self.create_api_destination_with_options_async(request, runtime)

    def create_connection_with_options(
        self,
        tmp_req: main_models.CreateConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConnectionResponse:
        tmp_req.validate()
        request = main_models.CreateConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_parameters):
            request.auth_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_parameters, 'AuthParameters', 'json')
        if not DaraCore.is_null(tmp_req.network_parameters):
            request.network_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_parameters, 'NetworkParameters', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_parameters_shrink):
            query['AuthParameters'] = request.auth_parameters_shrink
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.network_parameters_shrink):
            query['NetworkParameters'] = request.network_parameters_shrink
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConnection',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_connection_with_options_async(
        self,
        tmp_req: main_models.CreateConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConnectionResponse:
        tmp_req.validate()
        request = main_models.CreateConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_parameters):
            request.auth_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_parameters, 'AuthParameters', 'json')
        if not DaraCore.is_null(tmp_req.network_parameters):
            request.network_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_parameters, 'NetworkParameters', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_parameters_shrink):
            query['AuthParameters'] = request.auth_parameters_shrink
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.network_parameters_shrink):
            query['NetworkParameters'] = request.network_parameters_shrink
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConnection',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_connection(
        self,
        request: main_models.CreateConnectionRequest,
    ) -> main_models.CreateConnectionResponse:
        runtime = RuntimeOptions()
        return self.create_connection_with_options(request, runtime)

    async def create_connection_async(
        self,
        request: main_models.CreateConnectionRequest,
    ) -> main_models.CreateConnectionResponse:
        runtime = RuntimeOptions()
        return await self.create_connection_with_options_async(request, runtime)

    def create_event_bus_with_options(
        self,
        request: main_models.CreateEventBusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventBusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventBus',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventBusResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_bus_with_options_async(
        self,
        request: main_models.CreateEventBusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventBusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventBus',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventBusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event_bus(
        self,
        request: main_models.CreateEventBusRequest,
    ) -> main_models.CreateEventBusResponse:
        runtime = RuntimeOptions()
        return self.create_event_bus_with_options(request, runtime)

    async def create_event_bus_async(
        self,
        request: main_models.CreateEventBusRequest,
    ) -> main_models.CreateEventBusResponse:
        runtime = RuntimeOptions()
        return await self.create_event_bus_with_options_async(request, runtime)

    def create_event_source_with_options(
        self,
        tmp_req: main_models.CreateEventSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventSourceResponse:
        tmp_req.validate()
        request = main_models.CreateEventSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.external_source_config):
            request.external_source_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.external_source_config, 'ExternalSourceConfig', 'json')
        if not DaraCore.is_null(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_kafka_parameters):
            request.source_kafka_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_kafka_parameters, 'SourceKafkaParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_ossevent_parameters):
            request.source_ossevent_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_ossevent_parameters, 'SourceOSSEventParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_scheduled_event_parameters):
            request.source_scheduled_event_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_scheduled_event_parameters, 'SourceScheduledEventParameters', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not DaraCore.is_null(request.external_source_config_shrink):
            body['ExternalSourceConfig'] = request.external_source_config_shrink
        if not DaraCore.is_null(request.external_source_type):
            body['ExternalSourceType'] = request.external_source_type
        if not DaraCore.is_null(request.linked_external_source):
            body['LinkedExternalSource'] = request.linked_external_source
        if not DaraCore.is_null(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not DaraCore.is_null(request.source_kafka_parameters_shrink):
            body['SourceKafkaParameters'] = request.source_kafka_parameters_shrink
        if not DaraCore.is_null(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not DaraCore.is_null(request.source_ossevent_parameters_shrink):
            body['SourceOSSEventParameters'] = request.source_ossevent_parameters_shrink
        if not DaraCore.is_null(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not DaraCore.is_null(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not DaraCore.is_null(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        if not DaraCore.is_null(request.source_scheduled_event_parameters_shrink):
            body['SourceScheduledEventParameters'] = request.source_scheduled_event_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventSource',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_source_with_options_async(
        self,
        tmp_req: main_models.CreateEventSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventSourceResponse:
        tmp_req.validate()
        request = main_models.CreateEventSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.external_source_config):
            request.external_source_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.external_source_config, 'ExternalSourceConfig', 'json')
        if not DaraCore.is_null(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_kafka_parameters):
            request.source_kafka_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_kafka_parameters, 'SourceKafkaParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_ossevent_parameters):
            request.source_ossevent_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_ossevent_parameters, 'SourceOSSEventParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_scheduled_event_parameters):
            request.source_scheduled_event_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_scheduled_event_parameters, 'SourceScheduledEventParameters', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not DaraCore.is_null(request.external_source_config_shrink):
            body['ExternalSourceConfig'] = request.external_source_config_shrink
        if not DaraCore.is_null(request.external_source_type):
            body['ExternalSourceType'] = request.external_source_type
        if not DaraCore.is_null(request.linked_external_source):
            body['LinkedExternalSource'] = request.linked_external_source
        if not DaraCore.is_null(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not DaraCore.is_null(request.source_kafka_parameters_shrink):
            body['SourceKafkaParameters'] = request.source_kafka_parameters_shrink
        if not DaraCore.is_null(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not DaraCore.is_null(request.source_ossevent_parameters_shrink):
            body['SourceOSSEventParameters'] = request.source_ossevent_parameters_shrink
        if not DaraCore.is_null(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not DaraCore.is_null(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not DaraCore.is_null(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        if not DaraCore.is_null(request.source_scheduled_event_parameters_shrink):
            body['SourceScheduledEventParameters'] = request.source_scheduled_event_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventSource',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event_source(
        self,
        request: main_models.CreateEventSourceRequest,
    ) -> main_models.CreateEventSourceResponse:
        runtime = RuntimeOptions()
        return self.create_event_source_with_options(request, runtime)

    async def create_event_source_async(
        self,
        request: main_models.CreateEventSourceRequest,
    ) -> main_models.CreateEventSourceResponse:
        runtime = RuntimeOptions()
        return await self.create_event_source_with_options_async(request, runtime)

    def create_event_streaming_with_options(
        self,
        tmp_req: main_models.CreateEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventStreamingResponse:
        tmp_req.validate()
        request = main_models.CreateEventStreamingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.run_options):
            request.run_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not DaraCore.is_null(tmp_req.sink):
            request.sink_shrink = Utils.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not DaraCore.is_null(tmp_req.source):
            request.source_shrink = Utils.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        if not DaraCore.is_null(tmp_req.transforms):
            request.transforms_shrink = Utils.array_to_string_with_specified_style(tmp_req.transforms, 'Transforms', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        if not DaraCore.is_null(request.filter_pattern):
            body['FilterPattern'] = request.filter_pattern
        if not DaraCore.is_null(request.run_options_shrink):
            body['RunOptions'] = request.run_options_shrink
        if not DaraCore.is_null(request.sink_shrink):
            body['Sink'] = request.sink_shrink
        if not DaraCore.is_null(request.source_shrink):
            body['Source'] = request.source_shrink
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.transforms_shrink):
            body['Transforms'] = request.transforms_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_streaming_with_options_async(
        self,
        tmp_req: main_models.CreateEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventStreamingResponse:
        tmp_req.validate()
        request = main_models.CreateEventStreamingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.run_options):
            request.run_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not DaraCore.is_null(tmp_req.sink):
            request.sink_shrink = Utils.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not DaraCore.is_null(tmp_req.source):
            request.source_shrink = Utils.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        if not DaraCore.is_null(tmp_req.transforms):
            request.transforms_shrink = Utils.array_to_string_with_specified_style(tmp_req.transforms, 'Transforms', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        if not DaraCore.is_null(request.filter_pattern):
            body['FilterPattern'] = request.filter_pattern
        if not DaraCore.is_null(request.run_options_shrink):
            body['RunOptions'] = request.run_options_shrink
        if not DaraCore.is_null(request.sink_shrink):
            body['Sink'] = request.sink_shrink
        if not DaraCore.is_null(request.source_shrink):
            body['Source'] = request.source_shrink
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.transforms_shrink):
            body['Transforms'] = request.transforms_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event_streaming(
        self,
        request: main_models.CreateEventStreamingRequest,
    ) -> main_models.CreateEventStreamingResponse:
        runtime = RuntimeOptions()
        return self.create_event_streaming_with_options(request, runtime)

    async def create_event_streaming_async(
        self,
        request: main_models.CreateEventStreamingRequest,
    ) -> main_models.CreateEventStreamingResponse:
        runtime = RuntimeOptions()
        return await self.create_event_streaming_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        request: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        tmp_req: main_models.CreateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRuleResponse:
        tmp_req.validate()
        request = main_models.CreateRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.event_targets):
            request.event_targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_targets, 'EventTargets', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_targets_shrink):
            query['EventTargets'] = request.event_targets_shrink
        if not DaraCore.is_null(request.filter_pattern):
            query['FilterPattern'] = request.filter_pattern
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        tmp_req: main_models.CreateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRuleResponse:
        tmp_req.validate()
        request = main_models.CreateRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.event_targets):
            request.event_targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_targets, 'EventTargets', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_targets_shrink):
            query['EventTargets'] = request.event_targets_shrink
        if not DaraCore.is_null(request.filter_pattern):
            query['FilterPattern'] = request.filter_pattern
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rule(
        self,
        request: main_models.CreateRuleRequest,
    ) -> main_models.CreateRuleResponse:
        runtime = RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: main_models.CreateRuleRequest,
    ) -> main_models.CreateRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_service_linked_role_for_product_with_options(
        self,
        request: main_models.CreateServiceLinkedRoleForProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleForProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRoleForProduct',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleForProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_for_product_with_options_async(
        self,
        request: main_models.CreateServiceLinkedRoleForProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleForProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRoleForProduct',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleForProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role_for_product(
        self,
        request: main_models.CreateServiceLinkedRoleForProductRequest,
    ) -> main_models.CreateServiceLinkedRoleForProductResponse:
        runtime = RuntimeOptions()
        return self.create_service_linked_role_for_product_with_options(request, runtime)

    async def create_service_linked_role_for_product_async(
        self,
        request: main_models.CreateServiceLinkedRoleForProductRequest,
    ) -> main_models.CreateServiceLinkedRoleForProductResponse:
        runtime = RuntimeOptions()
        return await self.create_service_linked_role_for_product_with_options_async(request, runtime)

    def create_table_with_options(
        self,
        tmp_req: main_models.CreateTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTableResponse:
        tmp_req.validate()
        request = main_models.CreateTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.columns):
            request.columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        if not DaraCore.is_null(tmp_req.retention_policy):
            request.retention_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.retention_policy, 'RetentionPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.columns_shrink):
            query['Columns'] = request.columns_shrink
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.retention_policy_shrink):
            query['RetentionPolicy'] = request.retention_policy_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTable',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_table_with_options_async(
        self,
        tmp_req: main_models.CreateTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTableResponse:
        tmp_req.validate()
        request = main_models.CreateTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.columns):
            request.columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        if not DaraCore.is_null(tmp_req.retention_policy):
            request.retention_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.retention_policy, 'RetentionPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.columns_shrink):
            query['Columns'] = request.columns_shrink
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.retention_policy_shrink):
            query['RetentionPolicy'] = request.retention_policy_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTable',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_table(
        self,
        request: main_models.CreateTableRequest,
    ) -> main_models.CreateTableResponse:
        runtime = RuntimeOptions()
        return self.create_table_with_options(request, runtime)

    async def create_table_async(
        self,
        request: main_models.CreateTableRequest,
    ) -> main_models.CreateTableResponse:
        runtime = RuntimeOptions()
        return await self.create_table_with_options_async(request, runtime)

    def delete_agent_with_options(
        self,
        request: main_models.DeleteAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_with_options_async(
        self,
        request: main_models.DeleteAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent(
        self,
        request: main_models.DeleteAgentRequest,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        return self.delete_agent_with_options(request, runtime)

    async def delete_agent_async(
        self,
        request: main_models.DeleteAgentRequest,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        return await self.delete_agent_with_options_async(request, runtime)

    def delete_api_destination_with_options(
        self,
        request: main_models.DeleteApiDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiDestination',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_destination_with_options_async(
        self,
        request: main_models.DeleteApiDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiDestination',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_destination(
        self,
        request: main_models.DeleteApiDestinationRequest,
    ) -> main_models.DeleteApiDestinationResponse:
        runtime = RuntimeOptions()
        return self.delete_api_destination_with_options(request, runtime)

    async def delete_api_destination_async(
        self,
        request: main_models.DeleteApiDestinationRequest,
    ) -> main_models.DeleteApiDestinationResponse:
        runtime = RuntimeOptions()
        return await self.delete_api_destination_with_options_async(request, runtime)

    def delete_connection_with_options(
        self,
        request: main_models.DeleteConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConnection',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_connection_with_options_async(
        self,
        request: main_models.DeleteConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConnection',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_connection(
        self,
        request: main_models.DeleteConnectionRequest,
    ) -> main_models.DeleteConnectionResponse:
        runtime = RuntimeOptions()
        return self.delete_connection_with_options(request, runtime)

    async def delete_connection_async(
        self,
        request: main_models.DeleteConnectionRequest,
    ) -> main_models.DeleteConnectionResponse:
        runtime = RuntimeOptions()
        return await self.delete_connection_with_options_async(request, runtime)

    def delete_event_bus_with_options(
        self,
        request: main_models.DeleteEventBusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventBusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventBus',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventBusResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_bus_with_options_async(
        self,
        request: main_models.DeleteEventBusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventBusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventBus',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventBusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_bus(
        self,
        request: main_models.DeleteEventBusRequest,
    ) -> main_models.DeleteEventBusResponse:
        runtime = RuntimeOptions()
        return self.delete_event_bus_with_options(request, runtime)

    async def delete_event_bus_async(
        self,
        request: main_models.DeleteEventBusRequest,
    ) -> main_models.DeleteEventBusResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_bus_with_options_async(request, runtime)

    def delete_event_source_with_options(
        self,
        request: main_models.DeleteEventSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventSource',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_source_with_options_async(
        self,
        request: main_models.DeleteEventSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventSource',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_source(
        self,
        request: main_models.DeleteEventSourceRequest,
    ) -> main_models.DeleteEventSourceResponse:
        runtime = RuntimeOptions()
        return self.delete_event_source_with_options(request, runtime)

    async def delete_event_source_async(
        self,
        request: main_models.DeleteEventSourceRequest,
    ) -> main_models.DeleteEventSourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_source_with_options_async(request, runtime)

    def delete_event_streaming_with_options(
        self,
        request: main_models.DeleteEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventStreamingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_streaming_with_options_async(
        self,
        request: main_models.DeleteEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventStreamingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_streaming(
        self,
        request: main_models.DeleteEventStreamingRequest,
    ) -> main_models.DeleteEventStreamingResponse:
        runtime = RuntimeOptions()
        return self.delete_event_streaming_with_options(request, runtime)

    async def delete_event_streaming_async(
        self,
        request: main_models.DeleteEventStreamingRequest,
    ) -> main_models.DeleteEventStreamingResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_streaming_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: main_models.DeleteRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: main_models.DeleteRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule(
        self,
        request: main_models.DeleteRuleRequest,
    ) -> main_models.DeleteRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: main_models.DeleteRuleRequest,
    ) -> main_models.DeleteRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_table_with_options(
        self,
        request: main_models.DeleteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTable',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_table_with_options_async(
        self,
        request: main_models.DeleteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTable',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_table(
        self,
        request: main_models.DeleteTableRequest,
    ) -> main_models.DeleteTableResponse:
        runtime = RuntimeOptions()
        return self.delete_table_with_options(request, runtime)

    async def delete_table_async(
        self,
        request: main_models.DeleteTableRequest,
    ) -> main_models.DeleteTableResponse:
        runtime = RuntimeOptions()
        return await self.delete_table_with_options_async(request, runtime)

    def delete_targets_with_options(
        self,
        tmp_req: main_models.DeleteTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTargetsResponse:
        tmp_req.validate()
        request = main_models.DeleteTargetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.target_ids):
            request.target_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.target_ids, 'TargetIds', 'json')
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.target_ids_shrink):
            query['TargetIds'] = request.target_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTargets',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_targets_with_options_async(
        self,
        tmp_req: main_models.DeleteTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTargetsResponse:
        tmp_req.validate()
        request = main_models.DeleteTargetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.target_ids):
            request.target_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.target_ids, 'TargetIds', 'json')
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.target_ids_shrink):
            query['TargetIds'] = request.target_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTargets',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_targets(
        self,
        request: main_models.DeleteTargetsRequest,
    ) -> main_models.DeleteTargetsResponse:
        runtime = RuntimeOptions()
        return self.delete_targets_with_options(request, runtime)

    async def delete_targets_async(
        self,
        request: main_models.DeleteTargetsRequest,
    ) -> main_models.DeleteTargetsResponse:
        runtime = RuntimeOptions()
        return await self.delete_targets_with_options_async(request, runtime)

    def disable_rule_with_options(
        self,
        request: main_models.DisableRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_rule_with_options_async(
        self,
        request: main_models.DisableRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_rule(
        self,
        request: main_models.DisableRuleRequest,
    ) -> main_models.DisableRuleResponse:
        runtime = RuntimeOptions()
        return self.disable_rule_with_options(request, runtime)

    async def disable_rule_async(
        self,
        request: main_models.DisableRuleRequest,
    ) -> main_models.DisableRuleResponse:
        runtime = RuntimeOptions()
        return await self.disable_rule_with_options_async(request, runtime)

    def discover_event_source_with_options(
        self,
        tmp_req: main_models.DiscoverEventSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DiscoverEventSourceResponse:
        tmp_req.validate()
        request = main_models.DiscoverEventSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_my_sqlparameters):
            request.source_my_sqlparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_my_sqlparameters, 'SourceMySQLParameters', 'json')
        body = {}
        if not DaraCore.is_null(request.source_my_sqlparameters_shrink):
            body['SourceMySQLParameters'] = request.source_my_sqlparameters_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DiscoverEventSource',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DiscoverEventSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def discover_event_source_with_options_async(
        self,
        tmp_req: main_models.DiscoverEventSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DiscoverEventSourceResponse:
        tmp_req.validate()
        request = main_models.DiscoverEventSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_my_sqlparameters):
            request.source_my_sqlparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_my_sqlparameters, 'SourceMySQLParameters', 'json')
        body = {}
        if not DaraCore.is_null(request.source_my_sqlparameters_shrink):
            body['SourceMySQLParameters'] = request.source_my_sqlparameters_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DiscoverEventSource',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DiscoverEventSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def discover_event_source(
        self,
        request: main_models.DiscoverEventSourceRequest,
    ) -> main_models.DiscoverEventSourceResponse:
        runtime = RuntimeOptions()
        return self.discover_event_source_with_options(request, runtime)

    async def discover_event_source_async(
        self,
        request: main_models.DiscoverEventSourceRequest,
    ) -> main_models.DiscoverEventSourceResponse:
        runtime = RuntimeOptions()
        return await self.discover_event_source_with_options_async(request, runtime)

    def enable_rule_with_options(
        self,
        request: main_models.EnableRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_rule_with_options_async(
        self,
        request: main_models.EnableRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_rule(
        self,
        request: main_models.EnableRuleRequest,
    ) -> main_models.EnableRuleResponse:
        runtime = RuntimeOptions()
        return self.enable_rule_with_options(request, runtime)

    async def enable_rule_async(
        self,
        request: main_models.EnableRuleRequest,
    ) -> main_models.EnableRuleResponse:
        runtime = RuntimeOptions()
        return await self.enable_rule_with_options_async(request, runtime)

    def event_center_query_events_with_options(
        self,
        tmp_req: main_models.EventCenterQueryEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EventCenterQueryEventsResponse:
        tmp_req.validate()
        request = main_models.EventCenterQueryEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        query = {}
        if not DaraCore.is_null(request.bus_name):
            query['BusName'] = request.bus_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['Body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EventCenterQueryEvents',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EventCenterQueryEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def event_center_query_events_with_options_async(
        self,
        tmp_req: main_models.EventCenterQueryEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EventCenterQueryEventsResponse:
        tmp_req.validate()
        request = main_models.EventCenterQueryEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.body):
            request.body_shrink = Utils.array_to_string_with_specified_style(tmp_req.body, 'Body', 'json')
        query = {}
        if not DaraCore.is_null(request.bus_name):
            query['BusName'] = request.bus_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.body_shrink):
            body['Body'] = request.body_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EventCenterQueryEvents',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EventCenterQueryEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def event_center_query_events(
        self,
        request: main_models.EventCenterQueryEventsRequest,
    ) -> main_models.EventCenterQueryEventsResponse:
        runtime = RuntimeOptions()
        return self.event_center_query_events_with_options(request, runtime)

    async def event_center_query_events_async(
        self,
        request: main_models.EventCenterQueryEventsRequest,
    ) -> main_models.EventCenterQueryEventsResponse:
        runtime = RuntimeOptions()
        return await self.event_center_query_events_with_options_async(request, runtime)

    def get_agent_with_options(
        self,
        request: main_models.GetAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_with_options_async(
        self,
        request: main_models.GetAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent(
        self,
        request: main_models.GetAgentRequest,
    ) -> main_models.GetAgentResponse:
        runtime = RuntimeOptions()
        return self.get_agent_with_options(request, runtime)

    async def get_agent_async(
        self,
        request: main_models.GetAgentRequest,
    ) -> main_models.GetAgentResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_with_options_async(request, runtime)

    def get_api_destination_with_options(
        self,
        request: main_models.GetApiDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApiDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApiDestination',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_destination_with_options_async(
        self,
        request: main_models.GetApiDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApiDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApiDestination',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_destination(
        self,
        request: main_models.GetApiDestinationRequest,
    ) -> main_models.GetApiDestinationResponse:
        runtime = RuntimeOptions()
        return self.get_api_destination_with_options(request, runtime)

    async def get_api_destination_async(
        self,
        request: main_models.GetApiDestinationRequest,
    ) -> main_models.GetApiDestinationResponse:
        runtime = RuntimeOptions()
        return await self.get_api_destination_with_options_async(request, runtime)

    def get_catalog_with_options(
        self,
        request: main_models.GetCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCatalog',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_with_options_async(
        self,
        request: main_models.GetCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCatalog',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog(
        self,
        request: main_models.GetCatalogRequest,
    ) -> main_models.GetCatalogResponse:
        runtime = RuntimeOptions()
        return self.get_catalog_with_options(request, runtime)

    async def get_catalog_async(
        self,
        request: main_models.GetCatalogRequest,
    ) -> main_models.GetCatalogResponse:
        runtime = RuntimeOptions()
        return await self.get_catalog_with_options_async(request, runtime)

    def get_connection_with_options(
        self,
        request: main_models.GetConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConnection',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_connection_with_options_async(
        self,
        request: main_models.GetConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConnection',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_connection(
        self,
        request: main_models.GetConnectionRequest,
    ) -> main_models.GetConnectionResponse:
        runtime = RuntimeOptions()
        return self.get_connection_with_options(request, runtime)

    async def get_connection_async(
        self,
        request: main_models.GetConnectionRequest,
    ) -> main_models.GetConnectionResponse:
        runtime = RuntimeOptions()
        return await self.get_connection_with_options_async(request, runtime)

    def get_event_bus_with_options(
        self,
        request: main_models.GetEventBusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEventBusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEventBus',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEventBusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_bus_with_options_async(
        self,
        request: main_models.GetEventBusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEventBusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEventBus',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEventBusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_bus(
        self,
        request: main_models.GetEventBusRequest,
    ) -> main_models.GetEventBusResponse:
        runtime = RuntimeOptions()
        return self.get_event_bus_with_options(request, runtime)

    async def get_event_bus_async(
        self,
        request: main_models.GetEventBusRequest,
    ) -> main_models.GetEventBusResponse:
        runtime = RuntimeOptions()
        return await self.get_event_bus_with_options_async(request, runtime)

    def get_event_streaming_with_options(
        self,
        request: main_models.GetEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEventStreamingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_streaming_with_options_async(
        self,
        request: main_models.GetEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEventStreamingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_streaming(
        self,
        request: main_models.GetEventStreamingRequest,
    ) -> main_models.GetEventStreamingResponse:
        runtime = RuntimeOptions()
        return self.get_event_streaming_with_options(request, runtime)

    async def get_event_streaming_async(
        self,
        request: main_models.GetEventStreamingRequest,
    ) -> main_models.GetEventStreamingResponse:
        runtime = RuntimeOptions()
        return await self.get_event_streaming_with_options_async(request, runtime)

    def get_namespace_with_options(
        self,
        request: main_models.GetNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNamespace',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_namespace_with_options_async(
        self,
        request: main_models.GetNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNamespace',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_namespace(
        self,
        request: main_models.GetNamespaceRequest,
    ) -> main_models.GetNamespaceResponse:
        runtime = RuntimeOptions()
        return self.get_namespace_with_options(request, runtime)

    async def get_namespace_async(
        self,
        request: main_models.GetNamespaceRequest,
    ) -> main_models.GetNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.get_namespace_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: main_models.GetRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_with_options_async(
        self,
        request: main_models.GetRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule(
        self,
        request: main_models.GetRuleRequest,
    ) -> main_models.GetRuleResponse:
        runtime = RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: main_models.GetRuleRequest,
    ) -> main_models.GetRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def get_table_with_options(
        self,
        request: main_models.GetTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTable',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_with_options_async(
        self,
        request: main_models.GetTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTable',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table(
        self,
        request: main_models.GetTableRequest,
    ) -> main_models.GetTableResponse:
        runtime = RuntimeOptions()
        return self.get_table_with_options(request, runtime)

    async def get_table_async(
        self,
        request: main_models.GetTableRequest,
    ) -> main_models.GetTableResponse:
        runtime = RuntimeOptions()
        return await self.get_table_with_options_async(request, runtime)

    def list_agents_with_options(
        self,
        request: main_models.ListAgentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.after):
            body['After'] = request.after
        if not DaraCore.is_null(request.limit):
            body['Limit'] = request.limit
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAgents',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agents_with_options_async(
        self,
        request: main_models.ListAgentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.after):
            body['After'] = request.after
        if not DaraCore.is_null(request.limit):
            body['Limit'] = request.limit
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAgents',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agents(
        self,
        request: main_models.ListAgentsRequest,
    ) -> main_models.ListAgentsResponse:
        runtime = RuntimeOptions()
        return self.list_agents_with_options(request, runtime)

    async def list_agents_async(
        self,
        request: main_models.ListAgentsRequest,
    ) -> main_models.ListAgentsResponse:
        runtime = RuntimeOptions()
        return await self.list_agents_with_options_async(request, runtime)

    def list_aliyun_official_event_sources_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListAliyunOfficialEventSourcesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListAliyunOfficialEventSources',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAliyunOfficialEventSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliyun_official_event_sources_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListAliyunOfficialEventSourcesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListAliyunOfficialEventSources',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAliyunOfficialEventSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliyun_official_event_sources(self) -> main_models.ListAliyunOfficialEventSourcesResponse:
        runtime = RuntimeOptions()
        return self.list_aliyun_official_event_sources_with_options(runtime)

    async def list_aliyun_official_event_sources_async(self) -> main_models.ListAliyunOfficialEventSourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_aliyun_official_event_sources_with_options_async(runtime)

    def list_api_destinations_with_options(
        self,
        request: main_models.ListApiDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_destination_name_prefix):
            query['ApiDestinationNamePrefix'] = request.api_destination_name_prefix
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiDestinations',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_destinations_with_options_async(
        self,
        request: main_models.ListApiDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_destination_name_prefix):
            query['ApiDestinationNamePrefix'] = request.api_destination_name_prefix
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiDestinations',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiDestinationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_destinations(
        self,
        request: main_models.ListApiDestinationsRequest,
    ) -> main_models.ListApiDestinationsResponse:
        runtime = RuntimeOptions()
        return self.list_api_destinations_with_options(request, runtime)

    async def list_api_destinations_async(
        self,
        request: main_models.ListApiDestinationsRequest,
    ) -> main_models.ListApiDestinationsResponse:
        runtime = RuntimeOptions()
        return await self.list_api_destinations_with_options_async(request, runtime)

    def list_catalogs_with_options(
        self,
        request: main_models.ListCatalogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCatalogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCatalogs',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_catalogs_with_options_async(
        self,
        request: main_models.ListCatalogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCatalogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCatalogs',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCatalogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_catalogs(
        self,
        request: main_models.ListCatalogsRequest,
    ) -> main_models.ListCatalogsResponse:
        runtime = RuntimeOptions()
        return self.list_catalogs_with_options(request, runtime)

    async def list_catalogs_async(
        self,
        request: main_models.ListCatalogsRequest,
    ) -> main_models.ListCatalogsResponse:
        runtime = RuntimeOptions()
        return await self.list_catalogs_with_options_async(request, runtime)

    def list_connections_with_options(
        self,
        request: main_models.ListConnectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConnectionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.connection_name_prefix):
            body['ConnectionNamePrefix'] = request.connection_name_prefix
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListConnections',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_connections_with_options_async(
        self,
        request: main_models.ListConnectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConnectionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.connection_name_prefix):
            body['ConnectionNamePrefix'] = request.connection_name_prefix
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListConnections',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_connections(
        self,
        request: main_models.ListConnectionsRequest,
    ) -> main_models.ListConnectionsResponse:
        runtime = RuntimeOptions()
        return self.list_connections_with_options(request, runtime)

    async def list_connections_async(
        self,
        request: main_models.ListConnectionsRequest,
    ) -> main_models.ListConnectionsResponse:
        runtime = RuntimeOptions()
        return await self.list_connections_with_options_async(request, runtime)

    def list_event_buses_with_options(
        self,
        request: main_models.ListEventBusesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventBusesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEventBuses',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventBusesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_buses_with_options_async(
        self,
        request: main_models.ListEventBusesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventBusesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEventBuses',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventBusesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_buses(
        self,
        request: main_models.ListEventBusesRequest,
    ) -> main_models.ListEventBusesResponse:
        runtime = RuntimeOptions()
        return self.list_event_buses_with_options(request, runtime)

    async def list_event_buses_async(
        self,
        request: main_models.ListEventBusesRequest,
    ) -> main_models.ListEventBusesResponse:
        runtime = RuntimeOptions()
        return await self.list_event_buses_with_options_async(request, runtime)

    def list_event_streamings_with_options(
        self,
        request: main_models.ListEventStreamingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventStreamingsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['Limit'] = request.limit
        if not DaraCore.is_null(request.name_prefix):
            body['NamePrefix'] = request.name_prefix
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sink_arn):
            body['SinkArn'] = request.sink_arn
        if not DaraCore.is_null(request.source_arn):
            body['SourceArn'] = request.source_arn
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEventStreamings',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventStreamingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_streamings_with_options_async(
        self,
        request: main_models.ListEventStreamingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventStreamingsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['Limit'] = request.limit
        if not DaraCore.is_null(request.name_prefix):
            body['NamePrefix'] = request.name_prefix
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sink_arn):
            body['SinkArn'] = request.sink_arn
        if not DaraCore.is_null(request.source_arn):
            body['SourceArn'] = request.source_arn
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListEventStreamings',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventStreamingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_streamings(
        self,
        request: main_models.ListEventStreamingsRequest,
    ) -> main_models.ListEventStreamingsResponse:
        runtime = RuntimeOptions()
        return self.list_event_streamings_with_options(request, runtime)

    async def list_event_streamings_async(
        self,
        request: main_models.ListEventStreamingsRequest,
    ) -> main_models.ListEventStreamingsResponse:
        runtime = RuntimeOptions()
        return await self.list_event_streamings_with_options_async(request, runtime)

    def list_namespaces_with_options(
        self,
        request: main_models.ListNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaces',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespaces_with_options_async(
        self,
        request: main_models.ListNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaces',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespaces(
        self,
        request: main_models.ListNamespacesRequest,
    ) -> main_models.ListNamespacesResponse:
        runtime = RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    async def list_namespaces_async(
        self,
        request: main_models.ListNamespacesRequest,
    ) -> main_models.ListNamespacesResponse:
        runtime = RuntimeOptions()
        return await self.list_namespaces_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: main_models.ListRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.rule_name_prefix):
            query['RuleNamePrefix'] = request.rule_name_prefix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRules',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: main_models.ListRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.rule_name_prefix):
            query['RuleNamePrefix'] = request.rule_name_prefix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRules',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        request: main_models.ListRulesRequest,
    ) -> main_models.ListRulesResponse:
        runtime = RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: main_models.ListRulesRequest,
    ) -> main_models.ListRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_tables_with_options(
        self,
        request: main_models.ListTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        request: main_models.ListTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tables(
        self,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        return self.list_tables_with_options(request, runtime)

    async def list_tables_async(
        self,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        return await self.list_tables_with_options_async(request, runtime)

    def list_targets_with_options(
        self,
        request: main_models.ListTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arn):
            query['Arn'] = request.arn
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTargets',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_targets_with_options_async(
        self,
        request: main_models.ListTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arn):
            query['Arn'] = request.arn
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTargets',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_targets(
        self,
        request: main_models.ListTargetsRequest,
    ) -> main_models.ListTargetsResponse:
        runtime = RuntimeOptions()
        return self.list_targets_with_options(request, runtime)

    async def list_targets_async(
        self,
        request: main_models.ListTargetsRequest,
    ) -> main_models.ListTargetsResponse:
        runtime = RuntimeOptions()
        return await self.list_targets_with_options_async(request, runtime)

    def list_user_defined_event_sources_with_options(
        self,
        request: main_models.ListUserDefinedEventSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserDefinedEventSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserDefinedEventSources',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserDefinedEventSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_defined_event_sources_with_options_async(
        self,
        request: main_models.ListUserDefinedEventSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserDefinedEventSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserDefinedEventSources',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserDefinedEventSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_defined_event_sources(
        self,
        request: main_models.ListUserDefinedEventSourcesRequest,
    ) -> main_models.ListUserDefinedEventSourcesResponse:
        runtime = RuntimeOptions()
        return self.list_user_defined_event_sources_with_options(request, runtime)

    async def list_user_defined_event_sources_async(
        self,
        request: main_models.ListUserDefinedEventSourcesRequest,
    ) -> main_models.ListUserDefinedEventSourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_user_defined_event_sources_with_options_async(request, runtime)

    def pause_event_streaming_with_options(
        self,
        request: main_models.PauseEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseEventStreamingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PauseEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_event_streaming_with_options_async(
        self,
        request: main_models.PauseEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseEventStreamingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PauseEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_event_streaming(
        self,
        request: main_models.PauseEventStreamingRequest,
    ) -> main_models.PauseEventStreamingResponse:
        runtime = RuntimeOptions()
        return self.pause_event_streaming_with_options(request, runtime)

    async def pause_event_streaming_async(
        self,
        request: main_models.PauseEventStreamingRequest,
    ) -> main_models.PauseEventStreamingResponse:
        runtime = RuntimeOptions()
        return await self.pause_event_streaming_with_options_async(request, runtime)

    def poll_ask_result_with_options(
        self,
        request: main_models.PollAskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PollAskResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.message_id):
            body['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PollAskResult',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PollAskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def poll_ask_result_with_options_async(
        self,
        request: main_models.PollAskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PollAskResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.message_id):
            body['MessageId'] = request.message_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PollAskResult',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PollAskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def poll_ask_result(
        self,
        request: main_models.PollAskResultRequest,
    ) -> main_models.PollAskResultResponse:
        runtime = RuntimeOptions()
        return self.poll_ask_result_with_options(request, runtime)

    async def poll_ask_result_async(
        self,
        request: main_models.PollAskResultRequest,
    ) -> main_models.PollAskResultResponse:
        runtime = RuntimeOptions()
        return await self.poll_ask_result_with_options_async(request, runtime)

    def put_targets_with_options(
        self,
        tmp_req: main_models.PutTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutTargetsResponse:
        tmp_req.validate()
        request = main_models.PutTargetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.targets):
            request.targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutTargets',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_targets_with_options_async(
        self,
        tmp_req: main_models.PutTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutTargetsResponse:
        tmp_req.validate()
        request = main_models.PutTargetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.targets):
            request.targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutTargets',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_targets(
        self,
        request: main_models.PutTargetsRequest,
    ) -> main_models.PutTargetsResponse:
        runtime = RuntimeOptions()
        return self.put_targets_with_options(request, runtime)

    async def put_targets_async(
        self,
        request: main_models.PutTargetsRequest,
    ) -> main_models.PutTargetsResponse:
        runtime = RuntimeOptions()
        return await self.put_targets_with_options_async(request, runtime)

    def query_ask_luma_log_with_options(
        self,
        request: main_models.QueryAskLumaLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAskLumaLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.after):
            body['After'] = request.after
        if not DaraCore.is_null(request.agent_name):
            body['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.limit):
            body['Limit'] = request.limit
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAskLumaLog',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAskLumaLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ask_luma_log_with_options_async(
        self,
        request: main_models.QueryAskLumaLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAskLumaLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.after):
            body['After'] = request.after
        if not DaraCore.is_null(request.agent_name):
            body['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.limit):
            body['Limit'] = request.limit
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAskLumaLog',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAskLumaLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ask_luma_log(
        self,
        request: main_models.QueryAskLumaLogRequest,
    ) -> main_models.QueryAskLumaLogResponse:
        runtime = RuntimeOptions()
        return self.query_ask_luma_log_with_options(request, runtime)

    async def query_ask_luma_log_async(
        self,
        request: main_models.QueryAskLumaLogRequest,
    ) -> main_models.QueryAskLumaLogResponse:
        runtime = RuntimeOptions()
        return await self.query_ask_luma_log_with_options_async(request, runtime)

    def query_event_with_options(
        self,
        request: main_models.QueryEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_source):
            query['EventSource'] = request.event_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEvent',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_with_options_async(
        self,
        request: main_models.QueryEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_source):
            query['EventSource'] = request.event_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEvent',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_event(
        self,
        request: main_models.QueryEventRequest,
    ) -> main_models.QueryEventResponse:
        runtime = RuntimeOptions()
        return self.query_event_with_options(request, runtime)

    async def query_event_async(
        self,
        request: main_models.QueryEventRequest,
    ) -> main_models.QueryEventResponse:
        runtime = RuntimeOptions()
        return await self.query_event_with_options_async(request, runtime)

    def query_event_house_with_options(
        self,
        request: main_models.QueryEventHouseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventHouseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventHouse',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventHouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_house_with_options_async(
        self,
        request: main_models.QueryEventHouseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventHouseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventHouse',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventHouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_event_house(
        self,
        request: main_models.QueryEventHouseRequest,
    ) -> main_models.QueryEventHouseResponse:
        runtime = RuntimeOptions()
        return self.query_event_house_with_options(request, runtime)

    async def query_event_house_async(
        self,
        request: main_models.QueryEventHouseRequest,
    ) -> main_models.QueryEventHouseResponse:
        runtime = RuntimeOptions()
        return await self.query_event_house_with_options_async(request, runtime)

    def query_event_traces_with_options(
        self,
        request: main_models.QueryEventTracesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventTracesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventTraces',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_traces_with_options_async(
        self,
        request: main_models.QueryEventTracesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventTracesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventTraces',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_event_traces(
        self,
        request: main_models.QueryEventTracesRequest,
    ) -> main_models.QueryEventTracesResponse:
        runtime = RuntimeOptions()
        return self.query_event_traces_with_options(request, runtime)

    async def query_event_traces_async(
        self,
        request: main_models.QueryEventTracesRequest,
    ) -> main_models.QueryEventTracesResponse:
        runtime = RuntimeOptions()
        return await self.query_event_traces_with_options_async(request, runtime)

    def query_traced_event_by_event_id_with_options(
        self,
        request: main_models.QueryTracedEventByEventIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTracedEventByEventIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_source):
            query['EventSource'] = request.event_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTracedEventByEventId',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTracedEventByEventIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_traced_event_by_event_id_with_options_async(
        self,
        request: main_models.QueryTracedEventByEventIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTracedEventByEventIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_source):
            query['EventSource'] = request.event_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTracedEventByEventId',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTracedEventByEventIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_traced_event_by_event_id(
        self,
        request: main_models.QueryTracedEventByEventIdRequest,
    ) -> main_models.QueryTracedEventByEventIdResponse:
        runtime = RuntimeOptions()
        return self.query_traced_event_by_event_id_with_options(request, runtime)

    async def query_traced_event_by_event_id_async(
        self,
        request: main_models.QueryTracedEventByEventIdRequest,
    ) -> main_models.QueryTracedEventByEventIdResponse:
        runtime = RuntimeOptions()
        return await self.query_traced_event_by_event_id_with_options_async(request, runtime)

    def query_traced_events_with_options(
        self,
        request: main_models.QueryTracedEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTracedEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_source):
            query['EventSource'] = request.event_source
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.matched_rule):
            query['MatchedRule'] = request.matched_rule
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTracedEvents',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTracedEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_traced_events_with_options_async(
        self,
        request: main_models.QueryTracedEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTracedEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_source):
            query['EventSource'] = request.event_source
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.matched_rule):
            query['MatchedRule'] = request.matched_rule
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTracedEvents',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTracedEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_traced_events(
        self,
        request: main_models.QueryTracedEventsRequest,
    ) -> main_models.QueryTracedEventsResponse:
        runtime = RuntimeOptions()
        return self.query_traced_events_with_options(request, runtime)

    async def query_traced_events_async(
        self,
        request: main_models.QueryTracedEventsRequest,
    ) -> main_models.QueryTracedEventsResponse:
        runtime = RuntimeOptions()
        return await self.query_traced_events_with_options_async(request, runtime)

    def start_event_streaming_with_options(
        self,
        request: main_models.StartEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartEventStreamingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_event_streaming_with_options_async(
        self,
        request: main_models.StartEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartEventStreamingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_event_streaming(
        self,
        request: main_models.StartEventStreamingRequest,
    ) -> main_models.StartEventStreamingResponse:
        runtime = RuntimeOptions()
        return self.start_event_streaming_with_options(request, runtime)

    async def start_event_streaming_async(
        self,
        request: main_models.StartEventStreamingRequest,
    ) -> main_models.StartEventStreamingResponse:
        runtime = RuntimeOptions()
        return await self.start_event_streaming_with_options_async(request, runtime)

    def test_event_pattern_with_options(
        self,
        request: main_models.TestEventPatternRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestEventPatternResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event):
            body['Event'] = request.event
        if not DaraCore.is_null(request.event_pattern):
            body['EventPattern'] = request.event_pattern
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TestEventPattern',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestEventPatternResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_event_pattern_with_options_async(
        self,
        request: main_models.TestEventPatternRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestEventPatternResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.event):
            body['Event'] = request.event
        if not DaraCore.is_null(request.event_pattern):
            body['EventPattern'] = request.event_pattern
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TestEventPattern',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestEventPatternResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_event_pattern(
        self,
        request: main_models.TestEventPatternRequest,
    ) -> main_models.TestEventPatternResponse:
        runtime = RuntimeOptions()
        return self.test_event_pattern_with_options(request, runtime)

    async def test_event_pattern_async(
        self,
        request: main_models.TestEventPatternRequest,
    ) -> main_models.TestEventPatternResponse:
        runtime = RuntimeOptions()
        return await self.test_event_pattern_with_options_async(request, runtime)

    def test_event_source_config_with_options(
        self,
        tmp_req: main_models.TestEventSourceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestEventSourceConfigResponse:
        tmp_req.validate()
        request = main_models.TestEventSourceConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_my_sqlparameters):
            request.source_my_sqlparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_my_sqlparameters, 'SourceMySQLParameters', 'json')
        body = {}
        if not DaraCore.is_null(request.source_my_sqlparameters_shrink):
            body['SourceMySQLParameters'] = request.source_my_sqlparameters_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TestEventSourceConfig',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestEventSourceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_event_source_config_with_options_async(
        self,
        tmp_req: main_models.TestEventSourceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TestEventSourceConfigResponse:
        tmp_req.validate()
        request = main_models.TestEventSourceConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_my_sqlparameters):
            request.source_my_sqlparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_my_sqlparameters, 'SourceMySQLParameters', 'json')
        body = {}
        if not DaraCore.is_null(request.source_my_sqlparameters_shrink):
            body['SourceMySQLParameters'] = request.source_my_sqlparameters_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TestEventSourceConfig',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestEventSourceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_event_source_config(
        self,
        request: main_models.TestEventSourceConfigRequest,
    ) -> main_models.TestEventSourceConfigResponse:
        runtime = RuntimeOptions()
        return self.test_event_source_config_with_options(request, runtime)

    async def test_event_source_config_async(
        self,
        request: main_models.TestEventSourceConfigRequest,
    ) -> main_models.TestEventSourceConfigResponse:
        runtime = RuntimeOptions()
        return await self.test_event_source_config_with_options_async(request, runtime)

    def update_agent_with_options(
        self,
        tmp_req: main_models.UpdateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metadata):
            request.metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.metadata_shrink):
            body['Metadata'] = request.metadata_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgent',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_with_options_async(
        self,
        tmp_req: main_models.UpdateAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metadata):
            request.metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.metadata_shrink):
            body['Metadata'] = request.metadata_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgent',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent(
        self,
        request: main_models.UpdateAgentRequest,
    ) -> main_models.UpdateAgentResponse:
        runtime = RuntimeOptions()
        return self.update_agent_with_options(request, runtime)

    async def update_agent_async(
        self,
        request: main_models.UpdateAgentRequest,
    ) -> main_models.UpdateAgentResponse:
        runtime = RuntimeOptions()
        return await self.update_agent_with_options_async(request, runtime)

    def update_api_destination_with_options(
        self,
        tmp_req: main_models.UpdateApiDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiDestinationResponse:
        tmp_req.validate()
        request = main_models.UpdateApiDestinationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.http_api_parameters):
            request.http_api_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.http_api_parameters, 'HttpApiParameters', 'json')
        query = {}
        if not DaraCore.is_null(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.http_api_parameters_shrink):
            query['HttpApiParameters'] = request.http_api_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiDestination',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_api_destination_with_options_async(
        self,
        tmp_req: main_models.UpdateApiDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiDestinationResponse:
        tmp_req.validate()
        request = main_models.UpdateApiDestinationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.http_api_parameters):
            request.http_api_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.http_api_parameters, 'HttpApiParameters', 'json')
        query = {}
        if not DaraCore.is_null(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.http_api_parameters_shrink):
            query['HttpApiParameters'] = request.http_api_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiDestination',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_api_destination(
        self,
        request: main_models.UpdateApiDestinationRequest,
    ) -> main_models.UpdateApiDestinationResponse:
        runtime = RuntimeOptions()
        return self.update_api_destination_with_options(request, runtime)

    async def update_api_destination_async(
        self,
        request: main_models.UpdateApiDestinationRequest,
    ) -> main_models.UpdateApiDestinationResponse:
        runtime = RuntimeOptions()
        return await self.update_api_destination_with_options_async(request, runtime)

    def update_connection_with_options(
        self,
        tmp_req: main_models.UpdateConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConnectionResponse:
        tmp_req.validate()
        request = main_models.UpdateConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_parameters):
            request.auth_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_parameters, 'AuthParameters', 'json')
        if not DaraCore.is_null(tmp_req.network_parameters):
            request.network_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_parameters, 'NetworkParameters', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_parameters_shrink):
            query['AuthParameters'] = request.auth_parameters_shrink
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.network_parameters_shrink):
            query['NetworkParameters'] = request.network_parameters_shrink
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConnection',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_connection_with_options_async(
        self,
        tmp_req: main_models.UpdateConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConnectionResponse:
        tmp_req.validate()
        request = main_models.UpdateConnectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auth_parameters):
            request.auth_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.auth_parameters, 'AuthParameters', 'json')
        if not DaraCore.is_null(tmp_req.network_parameters):
            request.network_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_parameters, 'NetworkParameters', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_parameters_shrink):
            query['AuthParameters'] = request.auth_parameters_shrink
        if not DaraCore.is_null(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.network_parameters_shrink):
            query['NetworkParameters'] = request.network_parameters_shrink
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConnection',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_connection(
        self,
        request: main_models.UpdateConnectionRequest,
    ) -> main_models.UpdateConnectionResponse:
        runtime = RuntimeOptions()
        return self.update_connection_with_options(request, runtime)

    async def update_connection_async(
        self,
        request: main_models.UpdateConnectionRequest,
    ) -> main_models.UpdateConnectionResponse:
        runtime = RuntimeOptions()
        return await self.update_connection_with_options_async(request, runtime)

    def update_event_bus_with_options(
        self,
        request: main_models.UpdateEventBusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventBusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventBus',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventBusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_bus_with_options_async(
        self,
        request: main_models.UpdateEventBusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventBusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventBus',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventBusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_event_bus(
        self,
        request: main_models.UpdateEventBusRequest,
    ) -> main_models.UpdateEventBusResponse:
        runtime = RuntimeOptions()
        return self.update_event_bus_with_options(request, runtime)

    async def update_event_bus_async(
        self,
        request: main_models.UpdateEventBusRequest,
    ) -> main_models.UpdateEventBusResponse:
        runtime = RuntimeOptions()
        return await self.update_event_bus_with_options_async(request, runtime)

    def update_event_source_with_options(
        self,
        tmp_req: main_models.UpdateEventSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventSourceResponse:
        tmp_req.validate()
        request = main_models.UpdateEventSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.external_source_config):
            request.external_source_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.external_source_config, 'ExternalSourceConfig', 'json')
        if not DaraCore.is_null(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_kafka_parameters):
            request.source_kafka_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_kafka_parameters, 'SourceKafkaParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_ossevent_parameters):
            request.source_ossevent_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_ossevent_parameters, 'SourceOSSEventParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_scheduled_event_parameters):
            request.source_scheduled_event_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_scheduled_event_parameters, 'SourceScheduledEventParameters', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not DaraCore.is_null(request.external_source_config_shrink):
            body['ExternalSourceConfig'] = request.external_source_config_shrink
        if not DaraCore.is_null(request.external_source_type):
            body['ExternalSourceType'] = request.external_source_type
        if not DaraCore.is_null(request.linked_external_source):
            body['LinkedExternalSource'] = request.linked_external_source
        if not DaraCore.is_null(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not DaraCore.is_null(request.source_kafka_parameters_shrink):
            body['SourceKafkaParameters'] = request.source_kafka_parameters_shrink
        if not DaraCore.is_null(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not DaraCore.is_null(request.source_ossevent_parameters_shrink):
            body['SourceOSSEventParameters'] = request.source_ossevent_parameters_shrink
        if not DaraCore.is_null(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not DaraCore.is_null(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not DaraCore.is_null(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        if not DaraCore.is_null(request.source_scheduled_event_parameters_shrink):
            body['SourceScheduledEventParameters'] = request.source_scheduled_event_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventSource',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_source_with_options_async(
        self,
        tmp_req: main_models.UpdateEventSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventSourceResponse:
        tmp_req.validate()
        request = main_models.UpdateEventSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.external_source_config):
            request.external_source_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.external_source_config, 'ExternalSourceConfig', 'json')
        if not DaraCore.is_null(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_kafka_parameters):
            request.source_kafka_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_kafka_parameters, 'SourceKafkaParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_ossevent_parameters):
            request.source_ossevent_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_ossevent_parameters, 'SourceOSSEventParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_scheduled_event_parameters):
            request.source_scheduled_event_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_scheduled_event_parameters, 'SourceScheduledEventParameters', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not DaraCore.is_null(request.external_source_config_shrink):
            body['ExternalSourceConfig'] = request.external_source_config_shrink
        if not DaraCore.is_null(request.external_source_type):
            body['ExternalSourceType'] = request.external_source_type
        if not DaraCore.is_null(request.linked_external_source):
            body['LinkedExternalSource'] = request.linked_external_source
        if not DaraCore.is_null(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not DaraCore.is_null(request.source_kafka_parameters_shrink):
            body['SourceKafkaParameters'] = request.source_kafka_parameters_shrink
        if not DaraCore.is_null(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not DaraCore.is_null(request.source_ossevent_parameters_shrink):
            body['SourceOSSEventParameters'] = request.source_ossevent_parameters_shrink
        if not DaraCore.is_null(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not DaraCore.is_null(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not DaraCore.is_null(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        if not DaraCore.is_null(request.source_scheduled_event_parameters_shrink):
            body['SourceScheduledEventParameters'] = request.source_scheduled_event_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventSource',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_event_source(
        self,
        request: main_models.UpdateEventSourceRequest,
    ) -> main_models.UpdateEventSourceResponse:
        runtime = RuntimeOptions()
        return self.update_event_source_with_options(request, runtime)

    async def update_event_source_async(
        self,
        request: main_models.UpdateEventSourceRequest,
    ) -> main_models.UpdateEventSourceResponse:
        runtime = RuntimeOptions()
        return await self.update_event_source_with_options_async(request, runtime)

    def update_event_streaming_with_options(
        self,
        tmp_req: main_models.UpdateEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventStreamingResponse:
        tmp_req.validate()
        request = main_models.UpdateEventStreamingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.run_options):
            request.run_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not DaraCore.is_null(tmp_req.sink):
            request.sink_shrink = Utils.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not DaraCore.is_null(tmp_req.source):
            request.source_shrink = Utils.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        if not DaraCore.is_null(tmp_req.transforms):
            request.transforms_shrink = Utils.array_to_string_with_specified_style(tmp_req.transforms, 'Transforms', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        if not DaraCore.is_null(request.filter_pattern):
            body['FilterPattern'] = request.filter_pattern
        if not DaraCore.is_null(request.run_options_shrink):
            body['RunOptions'] = request.run_options_shrink
        if not DaraCore.is_null(request.sink_shrink):
            body['Sink'] = request.sink_shrink
        if not DaraCore.is_null(request.source_shrink):
            body['Source'] = request.source_shrink
        if not DaraCore.is_null(request.transforms_shrink):
            body['Transforms'] = request.transforms_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_streaming_with_options_async(
        self,
        tmp_req: main_models.UpdateEventStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventStreamingResponse:
        tmp_req.validate()
        request = main_models.UpdateEventStreamingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.run_options):
            request.run_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not DaraCore.is_null(tmp_req.sink):
            request.sink_shrink = Utils.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not DaraCore.is_null(tmp_req.source):
            request.source_shrink = Utils.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        if not DaraCore.is_null(tmp_req.transforms):
            request.transforms_shrink = Utils.array_to_string_with_specified_style(tmp_req.transforms, 'Transforms', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        if not DaraCore.is_null(request.filter_pattern):
            body['FilterPattern'] = request.filter_pattern
        if not DaraCore.is_null(request.run_options_shrink):
            body['RunOptions'] = request.run_options_shrink
        if not DaraCore.is_null(request.sink_shrink):
            body['Sink'] = request.sink_shrink
        if not DaraCore.is_null(request.source_shrink):
            body['Source'] = request.source_shrink
        if not DaraCore.is_null(request.transforms_shrink):
            body['Transforms'] = request.transforms_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventStreaming',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_event_streaming(
        self,
        request: main_models.UpdateEventStreamingRequest,
    ) -> main_models.UpdateEventStreamingResponse:
        runtime = RuntimeOptions()
        return self.update_event_streaming_with_options(request, runtime)

    async def update_event_streaming_async(
        self,
        request: main_models.UpdateEventStreamingRequest,
    ) -> main_models.UpdateEventStreamingResponse:
        runtime = RuntimeOptions()
        return await self.update_event_streaming_with_options_async(request, runtime)

    def update_event_streaming_business_option_with_options(
        self,
        request: main_models.UpdateEventStreamingBusinessOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventStreamingBusinessOptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_mode):
            body['BusinessMode'] = request.business_mode
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        if not DaraCore.is_null(request.max_capacity_unit_count):
            body['MaxCapacityUnitCount'] = request.max_capacity_unit_count
        if not DaraCore.is_null(request.min_capacity_unit_count):
            body['MinCapacityUnitCount'] = request.min_capacity_unit_count
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventStreamingBusinessOption',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventStreamingBusinessOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_streaming_business_option_with_options_async(
        self,
        request: main_models.UpdateEventStreamingBusinessOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventStreamingBusinessOptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_mode):
            body['BusinessMode'] = request.business_mode
        if not DaraCore.is_null(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        if not DaraCore.is_null(request.max_capacity_unit_count):
            body['MaxCapacityUnitCount'] = request.max_capacity_unit_count
        if not DaraCore.is_null(request.min_capacity_unit_count):
            body['MinCapacityUnitCount'] = request.min_capacity_unit_count
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventStreamingBusinessOption',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventStreamingBusinessOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_event_streaming_business_option(
        self,
        request: main_models.UpdateEventStreamingBusinessOptionRequest,
    ) -> main_models.UpdateEventStreamingBusinessOptionResponse:
        runtime = RuntimeOptions()
        return self.update_event_streaming_business_option_with_options(request, runtime)

    async def update_event_streaming_business_option_async(
        self,
        request: main_models.UpdateEventStreamingBusinessOptionRequest,
    ) -> main_models.UpdateEventStreamingBusinessOptionResponse:
        runtime = RuntimeOptions()
        return await self.update_event_streaming_business_option_with_options_async(request, runtime)

    def update_namespace_with_options(
        self,
        request: main_models.UpdateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespace',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        request: main_models.UpdateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespace',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace(
        self,
        request: main_models.UpdateNamespaceRequest,
    ) -> main_models.UpdateNamespaceResponse:
        runtime = RuntimeOptions()
        return self.update_namespace_with_options(request, runtime)

    async def update_namespace_async(
        self,
        request: main_models.UpdateNamespaceRequest,
    ) -> main_models.UpdateNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.update_namespace_with_options_async(request, runtime)

    def update_rule_with_options(
        self,
        request: main_models.UpdateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.filter_pattern):
            query['FilterPattern'] = request.filter_pattern
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_with_options_async(
        self,
        request: main_models.UpdateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.filter_pattern):
            query['FilterPattern'] = request.filter_pattern
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRule',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule(
        self,
        request: main_models.UpdateRuleRequest,
    ) -> main_models.UpdateRuleResponse:
        runtime = RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    async def update_rule_async(
        self,
        request: main_models.UpdateRuleRequest,
    ) -> main_models.UpdateRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_rule_with_options_async(request, runtime)

    def update_table_with_options(
        self,
        tmp_req: main_models.UpdateTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTableResponse:
        tmp_req.validate()
        request = main_models.UpdateTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_column):
            request.add_column_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_column, 'AddColumn', 'json')
        if not DaraCore.is_null(tmp_req.delete_column):
            request.delete_column_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_column, 'DeleteColumn', 'json')
        if not DaraCore.is_null(tmp_req.rename_column):
            request.rename_column_shrink = Utils.array_to_string_with_specified_style(tmp_req.rename_column, 'RenameColumn', 'json')
        if not DaraCore.is_null(tmp_req.update_column_comment):
            request.update_column_comment_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_column_comment, 'UpdateColumnComment', 'json')
        if not DaraCore.is_null(tmp_req.update_column_type):
            request.update_column_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_column_type, 'UpdateColumnType', 'json')
        if not DaraCore.is_null(tmp_req.update_retention_policy):
            request.update_retention_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_retention_policy, 'UpdateRetentionPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.add_column_shrink):
            query['AddColumn'] = request.add_column_shrink
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_column_shrink):
            query['DeleteColumn'] = request.delete_column_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.rename_column_shrink):
            query['RenameColumn'] = request.rename_column_shrink
        if not DaraCore.is_null(request.update_column_comment_shrink):
            query['UpdateColumnComment'] = request.update_column_comment_shrink
        if not DaraCore.is_null(request.update_column_type_shrink):
            query['UpdateColumnType'] = request.update_column_type_shrink
        if not DaraCore.is_null(request.update_comment):
            query['UpdateComment'] = request.update_comment
        if not DaraCore.is_null(request.update_retention_policy_shrink):
            query['UpdateRetentionPolicy'] = request.update_retention_policy_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTable',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_table_with_options_async(
        self,
        tmp_req: main_models.UpdateTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTableResponse:
        tmp_req.validate()
        request = main_models.UpdateTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_column):
            request.add_column_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_column, 'AddColumn', 'json')
        if not DaraCore.is_null(tmp_req.delete_column):
            request.delete_column_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_column, 'DeleteColumn', 'json')
        if not DaraCore.is_null(tmp_req.rename_column):
            request.rename_column_shrink = Utils.array_to_string_with_specified_style(tmp_req.rename_column, 'RenameColumn', 'json')
        if not DaraCore.is_null(tmp_req.update_column_comment):
            request.update_column_comment_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_column_comment, 'UpdateColumnComment', 'json')
        if not DaraCore.is_null(tmp_req.update_column_type):
            request.update_column_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_column_type, 'UpdateColumnType', 'json')
        if not DaraCore.is_null(tmp_req.update_retention_policy):
            request.update_retention_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_retention_policy, 'UpdateRetentionPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.add_column_shrink):
            query['AddColumn'] = request.add_column_shrink
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_column_shrink):
            query['DeleteColumn'] = request.delete_column_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.rename_column_shrink):
            query['RenameColumn'] = request.rename_column_shrink
        if not DaraCore.is_null(request.update_column_comment_shrink):
            query['UpdateColumnComment'] = request.update_column_comment_shrink
        if not DaraCore.is_null(request.update_column_type_shrink):
            query['UpdateColumnType'] = request.update_column_type_shrink
        if not DaraCore.is_null(request.update_comment):
            query['UpdateComment'] = request.update_comment
        if not DaraCore.is_null(request.update_retention_policy_shrink):
            query['UpdateRetentionPolicy'] = request.update_retention_policy_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTable',
            version = '2020-04-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_table(
        self,
        request: main_models.UpdateTableRequest,
    ) -> main_models.UpdateTableResponse:
        runtime = RuntimeOptions()
        return self.update_table_with_options(request, runtime)

    async def update_table_async(
        self,
        request: main_models.UpdateTableRequest,
    ) -> main_models.UpdateTableResponse:
        runtime = RuntimeOptions()
        return await self.update_table_with_options_async(request, runtime)
