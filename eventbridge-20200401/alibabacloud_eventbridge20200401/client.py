# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eventbridge20200401 import models as eventbridge_20200401_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_api_destination_with_options(
        self,
        tmp_req: eventbridge_20200401_models.CreateApiDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateApiDestinationResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateApiDestinationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.http_api_parameters):
            request.http_api_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.http_api_parameters, 'HttpApiParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.http_api_parameters_shrink):
            query['HttpApiParameters'] = request.http_api_parameters_shrink
        if not UtilClient.is_unset(request.invocation_rate_limit_per_second):
            query['InvocationRateLimitPerSecond'] = request.invocation_rate_limit_per_second
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiDestination',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateApiDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_destination_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.CreateApiDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateApiDestinationResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateApiDestinationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.http_api_parameters):
            request.http_api_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.http_api_parameters, 'HttpApiParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.http_api_parameters_shrink):
            query['HttpApiParameters'] = request.http_api_parameters_shrink
        if not UtilClient.is_unset(request.invocation_rate_limit_per_second):
            query['InvocationRateLimitPerSecond'] = request.invocation_rate_limit_per_second
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiDestination',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateApiDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_destination(
        self,
        request: eventbridge_20200401_models.CreateApiDestinationRequest,
    ) -> eventbridge_20200401_models.CreateApiDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_api_destination_with_options(request, runtime)

    async def create_api_destination_async(
        self,
        request: eventbridge_20200401_models.CreateApiDestinationRequest,
    ) -> eventbridge_20200401_models.CreateApiDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_api_destination_with_options_async(request, runtime)

    def create_connection_with_options(
        self,
        tmp_req: eventbridge_20200401_models.CreateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateConnectionResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateConnectionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auth_parameters):
            request.auth_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auth_parameters, 'AuthParameters', 'json')
        if not UtilClient.is_unset(tmp_req.network_parameters):
            request.network_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network_parameters, 'NetworkParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.auth_parameters_shrink):
            query['AuthParameters'] = request.auth_parameters_shrink
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.network_parameters_shrink):
            query['NetworkParameters'] = request.network_parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConnection',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_connection_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.CreateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateConnectionResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateConnectionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auth_parameters):
            request.auth_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auth_parameters, 'AuthParameters', 'json')
        if not UtilClient.is_unset(tmp_req.network_parameters):
            request.network_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network_parameters, 'NetworkParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.auth_parameters_shrink):
            query['AuthParameters'] = request.auth_parameters_shrink
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.network_parameters_shrink):
            query['NetworkParameters'] = request.network_parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConnection',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_connection(
        self,
        request: eventbridge_20200401_models.CreateConnectionRequest,
    ) -> eventbridge_20200401_models.CreateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_connection_with_options(request, runtime)

    async def create_connection_async(
        self,
        request: eventbridge_20200401_models.CreateConnectionRequest,
    ) -> eventbridge_20200401_models.CreateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_connection_with_options_async(request, runtime)

    def create_event_bus_with_options(
        self,
        request: eventbridge_20200401_models.CreateEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateEventBusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEventBus',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateEventBusResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_bus_with_options_async(
        self,
        request: eventbridge_20200401_models.CreateEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateEventBusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEventBus',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateEventBusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event_bus(
        self,
        request: eventbridge_20200401_models.CreateEventBusRequest,
    ) -> eventbridge_20200401_models.CreateEventBusResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_event_bus_with_options(request, runtime)

    async def create_event_bus_async(
        self,
        request: eventbridge_20200401_models.CreateEventBusRequest,
    ) -> eventbridge_20200401_models.CreateEventBusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_event_bus_with_options_async(request, runtime)

    def create_event_source_with_options(
        self,
        tmp_req: eventbridge_20200401_models.CreateEventSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateEventSourceResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateEventSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not UtilClient.is_unset(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not UtilClient.is_unset(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not UtilClient.is_unset(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not UtilClient.is_unset(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEventSource',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateEventSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_source_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.CreateEventSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateEventSourceResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateEventSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not UtilClient.is_unset(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not UtilClient.is_unset(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not UtilClient.is_unset(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not UtilClient.is_unset(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEventSource',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateEventSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event_source(
        self,
        request: eventbridge_20200401_models.CreateEventSourceRequest,
    ) -> eventbridge_20200401_models.CreateEventSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_event_source_with_options(request, runtime)

    async def create_event_source_async(
        self,
        request: eventbridge_20200401_models.CreateEventSourceRequest,
    ) -> eventbridge_20200401_models.CreateEventSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_event_source_with_options_async(request, runtime)

    def create_event_streaming_with_options(
        self,
        tmp_req: eventbridge_20200401_models.CreateEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateEventStreamingResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateEventStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.run_options):
            request.run_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not UtilClient.is_unset(tmp_req.sink):
            request.sink_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        if not UtilClient.is_unset(request.filter_pattern):
            body['FilterPattern'] = request.filter_pattern
        if not UtilClient.is_unset(request.run_options_shrink):
            body['RunOptions'] = request.run_options_shrink
        if not UtilClient.is_unset(request.sink_shrink):
            body['Sink'] = request.sink_shrink
        if not UtilClient.is_unset(request.source_shrink):
            body['Source'] = request.source_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_streaming_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.CreateEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateEventStreamingResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateEventStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.run_options):
            request.run_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not UtilClient.is_unset(tmp_req.sink):
            request.sink_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        if not UtilClient.is_unset(request.filter_pattern):
            body['FilterPattern'] = request.filter_pattern
        if not UtilClient.is_unset(request.run_options_shrink):
            body['RunOptions'] = request.run_options_shrink
        if not UtilClient.is_unset(request.sink_shrink):
            body['Sink'] = request.sink_shrink
        if not UtilClient.is_unset(request.source_shrink):
            body['Source'] = request.source_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event_streaming(
        self,
        request: eventbridge_20200401_models.CreateEventStreamingRequest,
    ) -> eventbridge_20200401_models.CreateEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_event_streaming_with_options(request, runtime)

    async def create_event_streaming_async(
        self,
        request: eventbridge_20200401_models.CreateEventStreamingRequest,
    ) -> eventbridge_20200401_models.CreateEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_event_streaming_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        tmp_req: eventbridge_20200401_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.event_targets):
            request.event_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_targets, 'EventTargets', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_targets_shrink):
            query['EventTargets'] = request.event_targets_shrink
        if not UtilClient.is_unset(request.filter_pattern):
            query['FilterPattern'] = request.filter_pattern
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.event_targets):
            request.event_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_targets, 'EventTargets', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_targets_shrink):
            query['EventTargets'] = request.event_targets_shrink
        if not UtilClient.is_unset(request.filter_pattern):
            query['FilterPattern'] = request.filter_pattern
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rule(
        self,
        request: eventbridge_20200401_models.CreateRuleRequest,
    ) -> eventbridge_20200401_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: eventbridge_20200401_models.CreateRuleRequest,
    ) -> eventbridge_20200401_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_targets_with_options(
        self,
        tmp_req: eventbridge_20200401_models.CreateTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateTargetsResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateTargetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTargets',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_targets_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.CreateTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateTargetsResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateTargetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTargets',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.CreateTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_targets(
        self,
        request: eventbridge_20200401_models.CreateTargetsRequest,
    ) -> eventbridge_20200401_models.CreateTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_targets_with_options(request, runtime)

    async def create_targets_async(
        self,
        request: eventbridge_20200401_models.CreateTargetsRequest,
    ) -> eventbridge_20200401_models.CreateTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_targets_with_options_async(request, runtime)

    def delete_api_destination_with_options(
        self,
        request: eventbridge_20200401_models.DeleteApiDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteApiDestinationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiDestination',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteApiDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_destination_with_options_async(
        self,
        request: eventbridge_20200401_models.DeleteApiDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteApiDestinationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiDestination',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteApiDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_destination(
        self,
        request: eventbridge_20200401_models.DeleteApiDestinationRequest,
    ) -> eventbridge_20200401_models.DeleteApiDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_api_destination_with_options(request, runtime)

    async def delete_api_destination_async(
        self,
        request: eventbridge_20200401_models.DeleteApiDestinationRequest,
    ) -> eventbridge_20200401_models.DeleteApiDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_destination_with_options_async(request, runtime)

    def delete_connection_with_options(
        self,
        request: eventbridge_20200401_models.DeleteConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConnection',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_connection_with_options_async(
        self,
        request: eventbridge_20200401_models.DeleteConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConnection',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_connection(
        self,
        request: eventbridge_20200401_models.DeleteConnectionRequest,
    ) -> eventbridge_20200401_models.DeleteConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_connection_with_options(request, runtime)

    async def delete_connection_async(
        self,
        request: eventbridge_20200401_models.DeleteConnectionRequest,
    ) -> eventbridge_20200401_models.DeleteConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_connection_with_options_async(request, runtime)

    def delete_event_bus_with_options(
        self,
        request: eventbridge_20200401_models.DeleteEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteEventBusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventBus',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteEventBusResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_bus_with_options_async(
        self,
        request: eventbridge_20200401_models.DeleteEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteEventBusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventBus',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteEventBusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_bus(
        self,
        request: eventbridge_20200401_models.DeleteEventBusRequest,
    ) -> eventbridge_20200401_models.DeleteEventBusResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_bus_with_options(request, runtime)

    async def delete_event_bus_async(
        self,
        request: eventbridge_20200401_models.DeleteEventBusRequest,
    ) -> eventbridge_20200401_models.DeleteEventBusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_bus_with_options_async(request, runtime)

    def delete_event_source_with_options(
        self,
        request: eventbridge_20200401_models.DeleteEventSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteEventSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEventSource',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteEventSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_source_with_options_async(
        self,
        request: eventbridge_20200401_models.DeleteEventSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteEventSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEventSource',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteEventSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_source(
        self,
        request: eventbridge_20200401_models.DeleteEventSourceRequest,
    ) -> eventbridge_20200401_models.DeleteEventSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_source_with_options(request, runtime)

    async def delete_event_source_async(
        self,
        request: eventbridge_20200401_models.DeleteEventSourceRequest,
    ) -> eventbridge_20200401_models.DeleteEventSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_source_with_options_async(request, runtime)

    def delete_event_streaming_with_options(
        self,
        request: eventbridge_20200401_models.DeleteEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteEventStreamingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_streaming_with_options_async(
        self,
        request: eventbridge_20200401_models.DeleteEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteEventStreamingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_streaming(
        self,
        request: eventbridge_20200401_models.DeleteEventStreamingRequest,
    ) -> eventbridge_20200401_models.DeleteEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_streaming_with_options(request, runtime)

    async def delete_event_streaming_async(
        self,
        request: eventbridge_20200401_models.DeleteEventStreamingRequest,
    ) -> eventbridge_20200401_models.DeleteEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_streaming_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: eventbridge_20200401_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: eventbridge_20200401_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule(
        self,
        request: eventbridge_20200401_models.DeleteRuleRequest,
    ) -> eventbridge_20200401_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: eventbridge_20200401_models.DeleteRuleRequest,
    ) -> eventbridge_20200401_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_targets_with_options(
        self,
        tmp_req: eventbridge_20200401_models.DeleteTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteTargetsResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.DeleteTargetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.target_ids):
            request.target_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_ids, 'TargetIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.target_ids_shrink):
            query['TargetIds'] = request.target_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTargets',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_targets_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.DeleteTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteTargetsResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.DeleteTargetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.target_ids):
            request.target_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_ids, 'TargetIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.target_ids_shrink):
            query['TargetIds'] = request.target_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTargets',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DeleteTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_targets(
        self,
        request: eventbridge_20200401_models.DeleteTargetsRequest,
    ) -> eventbridge_20200401_models.DeleteTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_targets_with_options(request, runtime)

    async def delete_targets_async(
        self,
        request: eventbridge_20200401_models.DeleteTargetsRequest,
    ) -> eventbridge_20200401_models.DeleteTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_targets_with_options_async(request, runtime)

    def disable_rule_with_options(
        self,
        request: eventbridge_20200401_models.DisableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DisableRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DisableRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_rule_with_options_async(
        self,
        request: eventbridge_20200401_models.DisableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DisableRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.DisableRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_rule(
        self,
        request: eventbridge_20200401_models.DisableRuleRequest,
    ) -> eventbridge_20200401_models.DisableRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_rule_with_options(request, runtime)

    async def disable_rule_async(
        self,
        request: eventbridge_20200401_models.DisableRuleRequest,
    ) -> eventbridge_20200401_models.DisableRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_rule_with_options_async(request, runtime)

    def enable_rule_with_options(
        self,
        request: eventbridge_20200401_models.EnableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.EnableRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.EnableRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_rule_with_options_async(
        self,
        request: eventbridge_20200401_models.EnableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.EnableRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.EnableRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_rule(
        self,
        request: eventbridge_20200401_models.EnableRuleRequest,
    ) -> eventbridge_20200401_models.EnableRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_rule_with_options(request, runtime)

    async def enable_rule_async(
        self,
        request: eventbridge_20200401_models.EnableRuleRequest,
    ) -> eventbridge_20200401_models.EnableRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_rule_with_options_async(request, runtime)

    def get_api_destination_with_options(
        self,
        request: eventbridge_20200401_models.GetApiDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetApiDestinationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiDestination',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetApiDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_destination_with_options_async(
        self,
        request: eventbridge_20200401_models.GetApiDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetApiDestinationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiDestination',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetApiDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_destination(
        self,
        request: eventbridge_20200401_models.GetApiDestinationRequest,
    ) -> eventbridge_20200401_models.GetApiDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_api_destination_with_options(request, runtime)

    async def get_api_destination_async(
        self,
        request: eventbridge_20200401_models.GetApiDestinationRequest,
    ) -> eventbridge_20200401_models.GetApiDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_api_destination_with_options_async(request, runtime)

    def get_connection_with_options(
        self,
        request: eventbridge_20200401_models.GetConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnection',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_connection_with_options_async(
        self,
        request: eventbridge_20200401_models.GetConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnection',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_connection(
        self,
        request: eventbridge_20200401_models.GetConnectionRequest,
    ) -> eventbridge_20200401_models.GetConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_connection_with_options(request, runtime)

    async def get_connection_async(
        self,
        request: eventbridge_20200401_models.GetConnectionRequest,
    ) -> eventbridge_20200401_models.GetConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_connection_with_options_async(request, runtime)

    def get_event_bus_with_options(
        self,
        request: eventbridge_20200401_models.GetEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetEventBusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventBus',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetEventBusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_bus_with_options_async(
        self,
        request: eventbridge_20200401_models.GetEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetEventBusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventBus',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetEventBusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_bus(
        self,
        request: eventbridge_20200401_models.GetEventBusRequest,
    ) -> eventbridge_20200401_models.GetEventBusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_bus_with_options(request, runtime)

    async def get_event_bus_async(
        self,
        request: eventbridge_20200401_models.GetEventBusRequest,
    ) -> eventbridge_20200401_models.GetEventBusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_bus_with_options_async(request, runtime)

    def get_event_streaming_with_options(
        self,
        request: eventbridge_20200401_models.GetEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetEventStreamingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_streaming_with_options_async(
        self,
        request: eventbridge_20200401_models.GetEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetEventStreamingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_streaming(
        self,
        request: eventbridge_20200401_models.GetEventStreamingRequest,
    ) -> eventbridge_20200401_models.GetEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_streaming_with_options(request, runtime)

    async def get_event_streaming_async(
        self,
        request: eventbridge_20200401_models.GetEventStreamingRequest,
    ) -> eventbridge_20200401_models.GetEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_streaming_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: eventbridge_20200401_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_with_options_async(
        self,
        request: eventbridge_20200401_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule(
        self,
        request: eventbridge_20200401_models.GetRuleRequest,
    ) -> eventbridge_20200401_models.GetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: eventbridge_20200401_models.GetRuleRequest,
    ) -> eventbridge_20200401_models.GetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def list_aliyun_official_event_sources_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAliyunOfficialEventSources',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliyun_official_event_sources_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAliyunOfficialEventSources',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliyun_official_event_sources(self) -> eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aliyun_official_event_sources_with_options(runtime)

    async def list_aliyun_official_event_sources_async(self) -> eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aliyun_official_event_sources_with_options_async(runtime)

    def list_api_destinations_with_options(
        self,
        request: eventbridge_20200401_models.ListApiDestinationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListApiDestinationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name_prefix):
            query['ApiDestinationNamePrefix'] = request.api_destination_name_prefix
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiDestinations',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListApiDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_destinations_with_options_async(
        self,
        request: eventbridge_20200401_models.ListApiDestinationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListApiDestinationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name_prefix):
            query['ApiDestinationNamePrefix'] = request.api_destination_name_prefix
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiDestinations',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListApiDestinationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_destinations(
        self,
        request: eventbridge_20200401_models.ListApiDestinationsRequest,
    ) -> eventbridge_20200401_models.ListApiDestinationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_api_destinations_with_options(request, runtime)

    async def list_api_destinations_async(
        self,
        request: eventbridge_20200401_models.ListApiDestinationsRequest,
    ) -> eventbridge_20200401_models.ListApiDestinationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_api_destinations_with_options_async(request, runtime)

    def list_connections_with_options(
        self,
        request: eventbridge_20200401_models.ListConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListConnectionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.connection_name_prefix):
            body['ConnectionNamePrefix'] = request.connection_name_prefix
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConnections',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_connections_with_options_async(
        self,
        request: eventbridge_20200401_models.ListConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListConnectionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.connection_name_prefix):
            body['ConnectionNamePrefix'] = request.connection_name_prefix
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConnections',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_connections(
        self,
        request: eventbridge_20200401_models.ListConnectionsRequest,
    ) -> eventbridge_20200401_models.ListConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_connections_with_options(request, runtime)

    async def list_connections_async(
        self,
        request: eventbridge_20200401_models.ListConnectionsRequest,
    ) -> eventbridge_20200401_models.ListConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_connections_with_options_async(request, runtime)

    def list_event_buses_with_options(
        self,
        request: eventbridge_20200401_models.ListEventBusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventBusesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventBuses',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListEventBusesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_buses_with_options_async(
        self,
        request: eventbridge_20200401_models.ListEventBusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventBusesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventBuses',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListEventBusesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_buses(
        self,
        request: eventbridge_20200401_models.ListEventBusesRequest,
    ) -> eventbridge_20200401_models.ListEventBusesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_buses_with_options(request, runtime)

    async def list_event_buses_async(
        self,
        request: eventbridge_20200401_models.ListEventBusesRequest,
    ) -> eventbridge_20200401_models.ListEventBusesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_buses_with_options_async(request, runtime)

    def list_event_streamings_with_options(
        self,
        request: eventbridge_20200401_models.ListEventStreamingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventStreamingsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            body['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEventStreamings',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListEventStreamingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_streamings_with_options_async(
        self,
        request: eventbridge_20200401_models.ListEventStreamingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventStreamingsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            body['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEventStreamings',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListEventStreamingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_streamings(
        self,
        request: eventbridge_20200401_models.ListEventStreamingsRequest,
    ) -> eventbridge_20200401_models.ListEventStreamingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_streamings_with_options(request, runtime)

    async def list_event_streamings_async(
        self,
        request: eventbridge_20200401_models.ListEventStreamingsRequest,
    ) -> eventbridge_20200401_models.ListEventStreamingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_streamings_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: eventbridge_20200401_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.rule_name_prefix):
            query['RuleNamePrefix'] = request.rule_name_prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: eventbridge_20200401_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.rule_name_prefix):
            query['RuleNamePrefix'] = request.rule_name_prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        request: eventbridge_20200401_models.ListRulesRequest,
    ) -> eventbridge_20200401_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: eventbridge_20200401_models.ListRulesRequest,
    ) -> eventbridge_20200401_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_user_defined_event_sources_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListUserDefinedEventSourcesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListUserDefinedEventSources',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListUserDefinedEventSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_defined_event_sources_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListUserDefinedEventSourcesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListUserDefinedEventSources',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListUserDefinedEventSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_defined_event_sources(self) -> eventbridge_20200401_models.ListUserDefinedEventSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_defined_event_sources_with_options(runtime)

    async def list_user_defined_event_sources_async(self) -> eventbridge_20200401_models.ListUserDefinedEventSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_defined_event_sources_with_options_async(runtime)

    def pause_event_streaming_with_options(
        self,
        request: eventbridge_20200401_models.PauseEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.PauseEventStreamingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PauseEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.PauseEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_event_streaming_with_options_async(
        self,
        request: eventbridge_20200401_models.PauseEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.PauseEventStreamingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PauseEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.PauseEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_event_streaming(
        self,
        request: eventbridge_20200401_models.PauseEventStreamingRequest,
    ) -> eventbridge_20200401_models.PauseEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return self.pause_event_streaming_with_options(request, runtime)

    async def pause_event_streaming_async(
        self,
        request: eventbridge_20200401_models.PauseEventStreamingRequest,
    ) -> eventbridge_20200401_models.PauseEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pause_event_streaming_with_options_async(request, runtime)

    def start_event_streaming_with_options(
        self,
        request: eventbridge_20200401_models.StartEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.StartEventStreamingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.StartEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_event_streaming_with_options_async(
        self,
        request: eventbridge_20200401_models.StartEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.StartEventStreamingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.StartEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_event_streaming(
        self,
        request: eventbridge_20200401_models.StartEventStreamingRequest,
    ) -> eventbridge_20200401_models.StartEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_event_streaming_with_options(request, runtime)

    async def start_event_streaming_async(
        self,
        request: eventbridge_20200401_models.StartEventStreamingRequest,
    ) -> eventbridge_20200401_models.StartEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_event_streaming_with_options_async(request, runtime)

    def update_api_destination_with_options(
        self,
        tmp_req: eventbridge_20200401_models.UpdateApiDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateApiDestinationResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateApiDestinationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.http_api_parameters):
            request.http_api_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.http_api_parameters, 'HttpApiParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.http_api_parameters_shrink):
            query['HttpApiParameters'] = request.http_api_parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApiDestination',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateApiDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_api_destination_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.UpdateApiDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateApiDestinationResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateApiDestinationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.http_api_parameters):
            request.http_api_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.http_api_parameters, 'HttpApiParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.http_api_parameters_shrink):
            query['HttpApiParameters'] = request.http_api_parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApiDestination',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateApiDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_api_destination(
        self,
        request: eventbridge_20200401_models.UpdateApiDestinationRequest,
    ) -> eventbridge_20200401_models.UpdateApiDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_api_destination_with_options(request, runtime)

    async def update_api_destination_async(
        self,
        request: eventbridge_20200401_models.UpdateApiDestinationRequest,
    ) -> eventbridge_20200401_models.UpdateApiDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_api_destination_with_options_async(request, runtime)

    def update_connection_with_options(
        self,
        tmp_req: eventbridge_20200401_models.UpdateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateConnectionResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateConnectionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auth_parameters):
            request.auth_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auth_parameters, 'AuthParameters', 'json')
        if not UtilClient.is_unset(tmp_req.network_parameters):
            request.network_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network_parameters, 'NetworkParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.auth_parameters_shrink):
            query['AuthParameters'] = request.auth_parameters_shrink
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.network_parameters_shrink):
            query['NetworkParameters'] = request.network_parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConnection',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_connection_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.UpdateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateConnectionResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateConnectionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auth_parameters):
            request.auth_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auth_parameters, 'AuthParameters', 'json')
        if not UtilClient.is_unset(tmp_req.network_parameters):
            request.network_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network_parameters, 'NetworkParameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.auth_parameters_shrink):
            query['AuthParameters'] = request.auth_parameters_shrink
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.network_parameters_shrink):
            query['NetworkParameters'] = request.network_parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConnection',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_connection(
        self,
        request: eventbridge_20200401_models.UpdateConnectionRequest,
    ) -> eventbridge_20200401_models.UpdateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_connection_with_options(request, runtime)

    async def update_connection_async(
        self,
        request: eventbridge_20200401_models.UpdateConnectionRequest,
    ) -> eventbridge_20200401_models.UpdateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_connection_with_options_async(request, runtime)

    def update_event_bus_with_options(
        self,
        request: eventbridge_20200401_models.UpdateEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateEventBusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEventBus',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateEventBusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_bus_with_options_async(
        self,
        request: eventbridge_20200401_models.UpdateEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateEventBusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEventBus',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateEventBusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_event_bus(
        self,
        request: eventbridge_20200401_models.UpdateEventBusRequest,
    ) -> eventbridge_20200401_models.UpdateEventBusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_event_bus_with_options(request, runtime)

    async def update_event_bus_async(
        self,
        request: eventbridge_20200401_models.UpdateEventBusRequest,
    ) -> eventbridge_20200401_models.UpdateEventBusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_event_bus_with_options_async(request, runtime)

    def update_event_source_with_options(
        self,
        tmp_req: eventbridge_20200401_models.UpdateEventSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateEventSourceResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateEventSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not UtilClient.is_unset(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not UtilClient.is_unset(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not UtilClient.is_unset(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not UtilClient.is_unset(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEventSource',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateEventSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_source_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.UpdateEventSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateEventSourceResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateEventSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not UtilClient.is_unset(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not UtilClient.is_unset(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not UtilClient.is_unset(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not UtilClient.is_unset(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEventSource',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateEventSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_event_source(
        self,
        request: eventbridge_20200401_models.UpdateEventSourceRequest,
    ) -> eventbridge_20200401_models.UpdateEventSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_event_source_with_options(request, runtime)

    async def update_event_source_async(
        self,
        request: eventbridge_20200401_models.UpdateEventSourceRequest,
    ) -> eventbridge_20200401_models.UpdateEventSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_event_source_with_options_async(request, runtime)

    def update_event_streaming_with_options(
        self,
        tmp_req: eventbridge_20200401_models.UpdateEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateEventStreamingResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateEventStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.run_options):
            request.run_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not UtilClient.is_unset(tmp_req.sink):
            request.sink_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        if not UtilClient.is_unset(request.filter_pattern):
            body['FilterPattern'] = request.filter_pattern
        if not UtilClient.is_unset(request.run_options_shrink):
            body['RunOptions'] = request.run_options_shrink
        if not UtilClient.is_unset(request.sink_shrink):
            body['Sink'] = request.sink_shrink
        if not UtilClient.is_unset(request.source_shrink):
            body['Source'] = request.source_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_streaming_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.UpdateEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateEventStreamingResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateEventStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.run_options):
            request.run_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not UtilClient.is_unset(tmp_req.sink):
            request.sink_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_streaming_name):
            body['EventStreamingName'] = request.event_streaming_name
        if not UtilClient.is_unset(request.filter_pattern):
            body['FilterPattern'] = request.filter_pattern
        if not UtilClient.is_unset(request.run_options_shrink):
            body['RunOptions'] = request.run_options_shrink
        if not UtilClient.is_unset(request.sink_shrink):
            body['Sink'] = request.sink_shrink
        if not UtilClient.is_unset(request.source_shrink):
            body['Source'] = request.source_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEventStreaming',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_event_streaming(
        self,
        request: eventbridge_20200401_models.UpdateEventStreamingRequest,
    ) -> eventbridge_20200401_models.UpdateEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_event_streaming_with_options(request, runtime)

    async def update_event_streaming_async(
        self,
        request: eventbridge_20200401_models.UpdateEventStreamingRequest,
    ) -> eventbridge_20200401_models.UpdateEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_event_streaming_with_options_async(request, runtime)

    def update_rule_with_options(
        self,
        request: eventbridge_20200401_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.filter_pattern):
            query['FilterPattern'] = request.filter_pattern
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_with_options_async(
        self,
        request: eventbridge_20200401_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.filter_pattern):
            query['FilterPattern'] = request.filter_pattern
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRule',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.UpdateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule(
        self,
        request: eventbridge_20200401_models.UpdateRuleRequest,
    ) -> eventbridge_20200401_models.UpdateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    async def update_rule_async(
        self,
        request: eventbridge_20200401_models.UpdateRuleRequest,
    ) -> eventbridge_20200401_models.UpdateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_with_options_async(request, runtime)
