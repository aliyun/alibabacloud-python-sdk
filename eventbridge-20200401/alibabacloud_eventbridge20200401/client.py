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
        """
        You can call this API operation to create an API destination.
        
        @param tmp_req: CreateApiDestinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApiDestinationResponse
        """
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
        """
        You can call this API operation to create an API destination.
        
        @param tmp_req: CreateApiDestinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApiDestinationResponse
        """
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
        """
        You can call this API operation to create an API destination.
        
        @param request: CreateApiDestinationRequest
        @return: CreateApiDestinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_api_destination_with_options(request, runtime)

    async def create_api_destination_async(
        self,
        request: eventbridge_20200401_models.CreateApiDestinationRequest,
    ) -> eventbridge_20200401_models.CreateApiDestinationResponse:
        """
        You can call this API operation to create an API destination.
        
        @param request: CreateApiDestinationRequest
        @return: CreateApiDestinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_api_destination_with_options_async(request, runtime)

    def create_connection_with_options(
        self,
        tmp_req: eventbridge_20200401_models.CreateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateConnectionResponse:
        """
        You can call this API operation to create a connection.
        
        @param tmp_req: CreateConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConnectionResponse
        """
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
        """
        You can call this API operation to create a connection.
        
        @param tmp_req: CreateConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConnectionResponse
        """
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
        """
        You can call this API operation to create a connection.
        
        @param request: CreateConnectionRequest
        @return: CreateConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_connection_with_options(request, runtime)

    async def create_connection_async(
        self,
        request: eventbridge_20200401_models.CreateConnectionRequest,
    ) -> eventbridge_20200401_models.CreateConnectionResponse:
        """
        You can call this API operation to create a connection.
        
        @param request: CreateConnectionRequest
        @return: CreateConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_connection_with_options_async(request, runtime)

    def create_event_bus_with_options(
        self,
        request: eventbridge_20200401_models.CreateEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateEventBusResponse:
        """
        You can call this API operation to create an event bus.
        
        @param request: CreateEventBusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventBusResponse
        """
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
        """
        You can call this API operation to create an event bus.
        
        @param request: CreateEventBusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventBusResponse
        """
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
        """
        You can call this API operation to create an event bus.
        
        @param request: CreateEventBusRequest
        @return: CreateEventBusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_event_bus_with_options(request, runtime)

    async def create_event_bus_async(
        self,
        request: eventbridge_20200401_models.CreateEventBusRequest,
    ) -> eventbridge_20200401_models.CreateEventBusResponse:
        """
        You can call this API operation to create an event bus.
        
        @param request: CreateEventBusRequest
        @return: CreateEventBusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_event_bus_with_options_async(request, runtime)

    def create_event_source_with_options(
        self,
        tmp_req: eventbridge_20200401_models.CreateEventSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateEventSourceResponse:
        """
        You can call this operation to create an event source.
        
        @param tmp_req: CreateEventSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventSourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateEventSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_kafka_parameters):
            request.source_kafka_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_kafka_parameters, 'SourceKafkaParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_scheduled_event_parameters):
            request.source_scheduled_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_scheduled_event_parameters, 'SourceScheduledEventParameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not UtilClient.is_unset(request.source_kafka_parameters_shrink):
            body['SourceKafkaParameters'] = request.source_kafka_parameters_shrink
        if not UtilClient.is_unset(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not UtilClient.is_unset(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not UtilClient.is_unset(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not UtilClient.is_unset(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        if not UtilClient.is_unset(request.source_scheduled_event_parameters_shrink):
            body['SourceScheduledEventParameters'] = request.source_scheduled_event_parameters_shrink
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
        """
        You can call this operation to create an event source.
        
        @param tmp_req: CreateEventSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventSourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateEventSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_kafka_parameters):
            request.source_kafka_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_kafka_parameters, 'SourceKafkaParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_scheduled_event_parameters):
            request.source_scheduled_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_scheduled_event_parameters, 'SourceScheduledEventParameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not UtilClient.is_unset(request.source_kafka_parameters_shrink):
            body['SourceKafkaParameters'] = request.source_kafka_parameters_shrink
        if not UtilClient.is_unset(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not UtilClient.is_unset(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not UtilClient.is_unset(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not UtilClient.is_unset(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        if not UtilClient.is_unset(request.source_scheduled_event_parameters_shrink):
            body['SourceScheduledEventParameters'] = request.source_scheduled_event_parameters_shrink
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
        """
        You can call this operation to create an event source.
        
        @param request: CreateEventSourceRequest
        @return: CreateEventSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_event_source_with_options(request, runtime)

    async def create_event_source_async(
        self,
        request: eventbridge_20200401_models.CreateEventSourceRequest,
    ) -> eventbridge_20200401_models.CreateEventSourceResponse:
        """
        You can call this operation to create an event source.
        
        @param request: CreateEventSourceRequest
        @return: CreateEventSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_event_source_with_options_async(request, runtime)

    def create_event_streaming_with_options(
        self,
        tmp_req: eventbridge_20200401_models.CreateEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateEventStreamingResponse:
        """
        You can call this API operation to create an event stream.
        
        @param tmp_req: CreateEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventStreamingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateEventStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.run_options):
            request.run_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not UtilClient.is_unset(tmp_req.sink):
            request.sink_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        if not UtilClient.is_unset(tmp_req.transforms):
            request.transforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transforms, 'Transforms', 'json')
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
        if not UtilClient.is_unset(request.transforms_shrink):
            body['Transforms'] = request.transforms_shrink
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
        """
        You can call this API operation to create an event stream.
        
        @param tmp_req: CreateEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventStreamingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.CreateEventStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.run_options):
            request.run_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not UtilClient.is_unset(tmp_req.sink):
            request.sink_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        if not UtilClient.is_unset(tmp_req.transforms):
            request.transforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transforms, 'Transforms', 'json')
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
        if not UtilClient.is_unset(request.transforms_shrink):
            body['Transforms'] = request.transforms_shrink
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
        """
        You can call this API operation to create an event stream.
        
        @param request: CreateEventStreamingRequest
        @return: CreateEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_event_streaming_with_options(request, runtime)

    async def create_event_streaming_async(
        self,
        request: eventbridge_20200401_models.CreateEventStreamingRequest,
    ) -> eventbridge_20200401_models.CreateEventStreamingResponse:
        """
        You can call this API operation to create an event stream.
        
        @param request: CreateEventStreamingRequest
        @return: CreateEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_event_streaming_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        tmp_req: eventbridge_20200401_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateRuleResponse:
        """
        You can call this API operation to create an event rule.
        
        @param tmp_req: CreateRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRuleResponse
        """
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
        """
        You can call this API operation to create an event rule.
        
        @param tmp_req: CreateRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRuleResponse
        """
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
        """
        You can call this API operation to create an event rule.
        
        @param request: CreateRuleRequest
        @return: CreateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: eventbridge_20200401_models.CreateRuleRequest,
    ) -> eventbridge_20200401_models.CreateRuleResponse:
        """
        You can call this API operation to create an event rule.
        
        @param request: CreateRuleRequest
        @return: CreateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_service_linked_role_for_product_with_options(
        self,
        request: eventbridge_20200401_models.CreateServiceLinkedRoleForProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateServiceLinkedRoleForProductResponse:
        """
        You can call this API operation to create a service-linked role for your cloud service.
        
        @param request: CreateServiceLinkedRoleForProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleForProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRoleForProduct',
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
            eventbridge_20200401_models.CreateServiceLinkedRoleForProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_for_product_with_options_async(
        self,
        request: eventbridge_20200401_models.CreateServiceLinkedRoleForProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateServiceLinkedRoleForProductResponse:
        """
        You can call this API operation to create a service-linked role for your cloud service.
        
        @param request: CreateServiceLinkedRoleForProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleForProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRoleForProduct',
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
            eventbridge_20200401_models.CreateServiceLinkedRoleForProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role_for_product(
        self,
        request: eventbridge_20200401_models.CreateServiceLinkedRoleForProductRequest,
    ) -> eventbridge_20200401_models.CreateServiceLinkedRoleForProductResponse:
        """
        You can call this API operation to create a service-linked role for your cloud service.
        
        @param request: CreateServiceLinkedRoleForProductRequest
        @return: CreateServiceLinkedRoleForProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_for_product_with_options(request, runtime)

    async def create_service_linked_role_for_product_async(
        self,
        request: eventbridge_20200401_models.CreateServiceLinkedRoleForProductRequest,
    ) -> eventbridge_20200401_models.CreateServiceLinkedRoleForProductResponse:
        """
        You can call this API operation to create a service-linked role for your cloud service.
        
        @param request: CreateServiceLinkedRoleForProductRequest
        @return: CreateServiceLinkedRoleForProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_for_product_with_options_async(request, runtime)

    def delete_api_destination_with_options(
        self,
        request: eventbridge_20200401_models.DeleteApiDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteApiDestinationResponse:
        """
        You can call this API operation to delete an API destination.
        
        @param request: DeleteApiDestinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApiDestinationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
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
        """
        You can call this API operation to delete an API destination.
        
        @param request: DeleteApiDestinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApiDestinationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
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
        """
        You can call this API operation to delete an API destination.
        
        @param request: DeleteApiDestinationRequest
        @return: DeleteApiDestinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_api_destination_with_options(request, runtime)

    async def delete_api_destination_async(
        self,
        request: eventbridge_20200401_models.DeleteApiDestinationRequest,
    ) -> eventbridge_20200401_models.DeleteApiDestinationResponse:
        """
        You can call this API operation to delete an API destination.
        
        @param request: DeleteApiDestinationRequest
        @return: DeleteApiDestinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_destination_with_options_async(request, runtime)

    def delete_connection_with_options(
        self,
        request: eventbridge_20200401_models.DeleteConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteConnectionResponse:
        """
        You can call this API operation to delete a connection.
        
        @param request: DeleteConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConnectionResponse
        """
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
        """
        You can call this API operation to delete a connection.
        
        @param request: DeleteConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConnectionResponse
        """
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
        """
        You can call this API operation to delete a connection.
        
        @param request: DeleteConnectionRequest
        @return: DeleteConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_connection_with_options(request, runtime)

    async def delete_connection_async(
        self,
        request: eventbridge_20200401_models.DeleteConnectionRequest,
    ) -> eventbridge_20200401_models.DeleteConnectionResponse:
        """
        You can call this API operation to delete a connection.
        
        @param request: DeleteConnectionRequest
        @return: DeleteConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_connection_with_options_async(request, runtime)

    def delete_event_bus_with_options(
        self,
        request: eventbridge_20200401_models.DeleteEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteEventBusResponse:
        """
        You can call this API operation to delete an event bus.
        
        @param request: DeleteEventBusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventBusResponse
        """
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
        """
        You can call this API operation to delete an event bus.
        
        @param request: DeleteEventBusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventBusResponse
        """
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
        """
        You can call this API operation to delete an event bus.
        
        @param request: DeleteEventBusRequest
        @return: DeleteEventBusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_event_bus_with_options(request, runtime)

    async def delete_event_bus_async(
        self,
        request: eventbridge_20200401_models.DeleteEventBusRequest,
    ) -> eventbridge_20200401_models.DeleteEventBusResponse:
        """
        You can call this API operation to delete an event bus.
        
        @param request: DeleteEventBusRequest
        @return: DeleteEventBusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_bus_with_options_async(request, runtime)

    def delete_event_source_with_options(
        self,
        request: eventbridge_20200401_models.DeleteEventSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteEventSourceResponse:
        """
        You can call this API operation to delete an event source.
        
        @param request: DeleteEventSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventSourceResponse
        """
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
        """
        You can call this API operation to delete an event source.
        
        @param request: DeleteEventSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventSourceResponse
        """
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
        """
        You can call this API operation to delete an event source.
        
        @param request: DeleteEventSourceRequest
        @return: DeleteEventSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_event_source_with_options(request, runtime)

    async def delete_event_source_async(
        self,
        request: eventbridge_20200401_models.DeleteEventSourceRequest,
    ) -> eventbridge_20200401_models.DeleteEventSourceResponse:
        """
        You can call this API operation to delete an event source.
        
        @param request: DeleteEventSourceRequest
        @return: DeleteEventSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_source_with_options_async(request, runtime)

    def delete_event_streaming_with_options(
        self,
        request: eventbridge_20200401_models.DeleteEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteEventStreamingResponse:
        """
        You can call this API operation to delete an event stream.
        
        @param request: DeleteEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventStreamingResponse
        """
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
        """
        You can call this API operation to delete an event stream.
        
        @param request: DeleteEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventStreamingResponse
        """
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
        """
        You can call this API operation to delete an event stream.
        
        @param request: DeleteEventStreamingRequest
        @return: DeleteEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_event_streaming_with_options(request, runtime)

    async def delete_event_streaming_async(
        self,
        request: eventbridge_20200401_models.DeleteEventStreamingRequest,
    ) -> eventbridge_20200401_models.DeleteEventStreamingResponse:
        """
        You can call this API operation to delete an event stream.
        
        @param request: DeleteEventStreamingRequest
        @return: DeleteEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_streaming_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: eventbridge_20200401_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteRuleResponse:
        """
        You can call this API operation to delete an event rule.
        
        @param request: DeleteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRuleResponse
        """
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
        """
        You can call this API operation to delete an event rule.
        
        @param request: DeleteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRuleResponse
        """
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
        """
        You can call this API operation to delete an event rule.
        
        @param request: DeleteRuleRequest
        @return: DeleteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: eventbridge_20200401_models.DeleteRuleRequest,
    ) -> eventbridge_20200401_models.DeleteRuleResponse:
        """
        You can call this API operation to delete an event rule.
        
        @param request: DeleteRuleRequest
        @return: DeleteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_targets_with_options(
        self,
        tmp_req: eventbridge_20200401_models.DeleteTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteTargetsResponse:
        """
        You can call this API operation to delete one or more event targets of an event rule.
        
        @param tmp_req: DeleteTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTargetsResponse
        """
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
        """
        You can call this API operation to delete one or more event targets of an event rule.
        
        @param tmp_req: DeleteTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTargetsResponse
        """
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
        """
        You can call this API operation to delete one or more event targets of an event rule.
        
        @param request: DeleteTargetsRequest
        @return: DeleteTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_targets_with_options(request, runtime)

    async def delete_targets_async(
        self,
        request: eventbridge_20200401_models.DeleteTargetsRequest,
    ) -> eventbridge_20200401_models.DeleteTargetsResponse:
        """
        You can call this API operation to delete one or more event targets of an event rule.
        
        @param request: DeleteTargetsRequest
        @return: DeleteTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_targets_with_options_async(request, runtime)

    def disable_rule_with_options(
        self,
        request: eventbridge_20200401_models.DisableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DisableRuleResponse:
        """
        You can call this API operation to disable an event rule.
        
        @param request: DisableRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableRuleResponse
        """
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
        """
        You can call this API operation to disable an event rule.
        
        @param request: DisableRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableRuleResponse
        """
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
        """
        You can call this API operation to disable an event rule.
        
        @param request: DisableRuleRequest
        @return: DisableRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_rule_with_options(request, runtime)

    async def disable_rule_async(
        self,
        request: eventbridge_20200401_models.DisableRuleRequest,
    ) -> eventbridge_20200401_models.DisableRuleResponse:
        """
        You can call this API operation to disable an event rule.
        
        @param request: DisableRuleRequest
        @return: DisableRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_rule_with_options_async(request, runtime)

    def enable_rule_with_options(
        self,
        request: eventbridge_20200401_models.EnableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.EnableRuleResponse:
        """
        You can call this API operation to enable an event rule.
        
        @param request: EnableRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableRuleResponse
        """
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
        """
        You can call this API operation to enable an event rule.
        
        @param request: EnableRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableRuleResponse
        """
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
        """
        You can call this API operation to enable an event rule.
        
        @param request: EnableRuleRequest
        @return: EnableRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_rule_with_options(request, runtime)

    async def enable_rule_async(
        self,
        request: eventbridge_20200401_models.EnableRuleRequest,
    ) -> eventbridge_20200401_models.EnableRuleResponse:
        """
        You can call this API operation to enable an event rule.
        
        @param request: EnableRuleRequest
        @return: EnableRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_rule_with_options_async(request, runtime)

    def get_api_destination_with_options(
        self,
        request: eventbridge_20200401_models.GetApiDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetApiDestinationResponse:
        """
        You can call this API operation to query the information about an API destination.
        
        @param request: GetApiDestinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApiDestinationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
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
        """
        You can call this API operation to query the information about an API destination.
        
        @param request: GetApiDestinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApiDestinationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name):
            query['ApiDestinationName'] = request.api_destination_name
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
        """
        You can call this API operation to query the information about an API destination.
        
        @param request: GetApiDestinationRequest
        @return: GetApiDestinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_api_destination_with_options(request, runtime)

    async def get_api_destination_async(
        self,
        request: eventbridge_20200401_models.GetApiDestinationRequest,
    ) -> eventbridge_20200401_models.GetApiDestinationResponse:
        """
        You can call this API operation to query the information about an API destination.
        
        @param request: GetApiDestinationRequest
        @return: GetApiDestinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_api_destination_with_options_async(request, runtime)

    def get_connection_with_options(
        self,
        request: eventbridge_20200401_models.GetConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetConnectionResponse:
        """
        You can call this API operation to query the configurations of a connection.
        
        @param request: GetConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionResponse
        """
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
        """
        You can call this API operation to query the configurations of a connection.
        
        @param request: GetConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionResponse
        """
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
        """
        You can call this API operation to query the configurations of a connection.
        
        @param request: GetConnectionRequest
        @return: GetConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_connection_with_options(request, runtime)

    async def get_connection_async(
        self,
        request: eventbridge_20200401_models.GetConnectionRequest,
    ) -> eventbridge_20200401_models.GetConnectionResponse:
        """
        You can call this API operation to query the configurations of a connection.
        
        @param request: GetConnectionRequest
        @return: GetConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_connection_with_options_async(request, runtime)

    def get_event_bus_with_options(
        self,
        request: eventbridge_20200401_models.GetEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetEventBusResponse:
        """
        You can call this API operation to query the detailed information about an event bus.
        
        @param request: GetEventBusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEventBusResponse
        """
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
        """
        You can call this API operation to query the detailed information about an event bus.
        
        @param request: GetEventBusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEventBusResponse
        """
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
        """
        You can call this API operation to query the detailed information about an event bus.
        
        @param request: GetEventBusRequest
        @return: GetEventBusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_event_bus_with_options(request, runtime)

    async def get_event_bus_async(
        self,
        request: eventbridge_20200401_models.GetEventBusRequest,
    ) -> eventbridge_20200401_models.GetEventBusResponse:
        """
        You can call this API operation to query the detailed information about an event bus.
        
        @param request: GetEventBusRequest
        @return: GetEventBusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_event_bus_with_options_async(request, runtime)

    def get_event_streaming_with_options(
        self,
        request: eventbridge_20200401_models.GetEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetEventStreamingResponse:
        """
        You can call this API operation to query the details of an event stream.
        
        @param request: GetEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEventStreamingResponse
        """
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
        """
        You can call this API operation to query the details of an event stream.
        
        @param request: GetEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEventStreamingResponse
        """
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
        """
        You can call this API operation to query the details of an event stream.
        
        @param request: GetEventStreamingRequest
        @return: GetEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_event_streaming_with_options(request, runtime)

    async def get_event_streaming_async(
        self,
        request: eventbridge_20200401_models.GetEventStreamingRequest,
    ) -> eventbridge_20200401_models.GetEventStreamingResponse:
        """
        You can call this API operation to query the details of an event stream.
        
        @param request: GetEventStreamingRequest
        @return: GetEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_event_streaming_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: eventbridge_20200401_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetRuleResponse:
        """
        You can call this API operation to query the details of an event rule.
        
        @param request: GetRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleResponse
        """
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
        """
        You can call this API operation to query the details of an event rule.
        
        @param request: GetRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleResponse
        """
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
        """
        You can call this API operation to query the details of an event rule.
        
        @param request: GetRuleRequest
        @return: GetRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: eventbridge_20200401_models.GetRuleRequest,
    ) -> eventbridge_20200401_models.GetRuleResponse:
        """
        You can call this API operation to query the details of an event rule.
        
        @param request: GetRuleRequest
        @return: GetRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def list_aliyun_official_event_sources_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse:
        """
        You can call this API operation to query all Alibaba Cloud service event sources.
        
        @param request: ListAliyunOfficialEventSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliyunOfficialEventSourcesResponse
        """
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
        """
        You can call this API operation to query all Alibaba Cloud service event sources.
        
        @param request: ListAliyunOfficialEventSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliyunOfficialEventSourcesResponse
        """
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
        """
        You can call this API operation to query all Alibaba Cloud service event sources.
        
        @return: ListAliyunOfficialEventSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aliyun_official_event_sources_with_options(runtime)

    async def list_aliyun_official_event_sources_async(self) -> eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse:
        """
        You can call this API operation to query all Alibaba Cloud service event sources.
        
        @return: ListAliyunOfficialEventSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_aliyun_official_event_sources_with_options_async(runtime)

    def list_api_destinations_with_options(
        self,
        request: eventbridge_20200401_models.ListApiDestinationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListApiDestinationsResponse:
        """
        You can use this API operation to query a list of API destinations.
        
        @param request: ListApiDestinationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiDestinationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name_prefix):
            query['ApiDestinationNamePrefix'] = request.api_destination_name_prefix
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
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
        """
        You can use this API operation to query a list of API destinations.
        
        @param request: ListApiDestinationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiDestinationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_destination_name_prefix):
            query['ApiDestinationNamePrefix'] = request.api_destination_name_prefix
        if not UtilClient.is_unset(request.connection_name):
            query['ConnectionName'] = request.connection_name
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
        """
        You can use this API operation to query a list of API destinations.
        
        @param request: ListApiDestinationsRequest
        @return: ListApiDestinationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_api_destinations_with_options(request, runtime)

    async def list_api_destinations_async(
        self,
        request: eventbridge_20200401_models.ListApiDestinationsRequest,
    ) -> eventbridge_20200401_models.ListApiDestinationsResponse:
        """
        You can use this API operation to query a list of API destinations.
        
        @param request: ListApiDestinationsRequest
        @return: ListApiDestinationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_api_destinations_with_options_async(request, runtime)

    def list_connections_with_options(
        self,
        request: eventbridge_20200401_models.ListConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListConnectionsResponse:
        """
        You can call this API operation to query connections.
        
        @param request: ListConnectionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConnectionsResponse
        """
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
        """
        You can call this API operation to query connections.
        
        @param request: ListConnectionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConnectionsResponse
        """
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
        """
        You can call this API operation to query connections.
        
        @param request: ListConnectionsRequest
        @return: ListConnectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_connections_with_options(request, runtime)

    async def list_connections_async(
        self,
        request: eventbridge_20200401_models.ListConnectionsRequest,
    ) -> eventbridge_20200401_models.ListConnectionsResponse:
        """
        You can call this API operation to query connections.
        
        @param request: ListConnectionsRequest
        @return: ListConnectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_connections_with_options_async(request, runtime)

    def list_event_buses_with_options(
        self,
        request: eventbridge_20200401_models.ListEventBusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventBusesResponse:
        """
        You can call this API operation to query all event buses.
        
        @param request: ListEventBusesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventBusesResponse
        """
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
        """
        You can call this API operation to query all event buses.
        
        @param request: ListEventBusesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventBusesResponse
        """
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
        """
        You can call this API operation to query all event buses.
        
        @param request: ListEventBusesRequest
        @return: ListEventBusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_event_buses_with_options(request, runtime)

    async def list_event_buses_async(
        self,
        request: eventbridge_20200401_models.ListEventBusesRequest,
    ) -> eventbridge_20200401_models.ListEventBusesResponse:
        """
        You can call this API operation to query all event buses.
        
        @param request: ListEventBusesRequest
        @return: ListEventBusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_event_buses_with_options_async(request, runtime)

    def list_event_streamings_with_options(
        self,
        request: eventbridge_20200401_models.ListEventStreamingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventStreamingsResponse:
        """
        You can call this API operation to query event streams.
        
        @param request: ListEventStreamingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventStreamingsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            body['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sink_arn):
            body['SinkArn'] = request.sink_arn
        if not UtilClient.is_unset(request.source_arn):
            body['SourceArn'] = request.source_arn
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
        """
        You can call this API operation to query event streams.
        
        @param request: ListEventStreamingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEventStreamingsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            body['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sink_arn):
            body['SinkArn'] = request.sink_arn
        if not UtilClient.is_unset(request.source_arn):
            body['SourceArn'] = request.source_arn
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
        """
        You can call this API operation to query event streams.
        
        @param request: ListEventStreamingsRequest
        @return: ListEventStreamingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_event_streamings_with_options(request, runtime)

    async def list_event_streamings_async(
        self,
        request: eventbridge_20200401_models.ListEventStreamingsRequest,
    ) -> eventbridge_20200401_models.ListEventStreamingsResponse:
        """
        You can call this API operation to query event streams.
        
        @param request: ListEventStreamingsRequest
        @return: ListEventStreamingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_event_streamings_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: eventbridge_20200401_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListRulesResponse:
        """
        You can call this API operation to query all rules of an event bus.
        
        @param request: ListRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesResponse
        """
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
        """
        You can call this API operation to query all rules of an event bus.
        
        @param request: ListRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesResponse
        """
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
        """
        You can call this API operation to query all rules of an event bus.
        
        @param request: ListRulesRequest
        @return: ListRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: eventbridge_20200401_models.ListRulesRequest,
    ) -> eventbridge_20200401_models.ListRulesResponse:
        """
        You can call this API operation to query all rules of an event bus.
        
        @param request: ListRulesRequest
        @return: ListRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_targets_with_options(
        self,
        request: eventbridge_20200401_models.ListTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arn):
            query['Arn'] = request.arn
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTargets',
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
            eventbridge_20200401_models.ListTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_targets_with_options_async(
        self,
        request: eventbridge_20200401_models.ListTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arn):
            query['Arn'] = request.arn
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTargets',
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
            eventbridge_20200401_models.ListTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_targets(
        self,
        request: eventbridge_20200401_models.ListTargetsRequest,
    ) -> eventbridge_20200401_models.ListTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_targets_with_options(request, runtime)

    async def list_targets_async(
        self,
        request: eventbridge_20200401_models.ListTargetsRequest,
    ) -> eventbridge_20200401_models.ListTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_targets_with_options_async(request, runtime)

    def list_user_defined_event_sources_with_options(
        self,
        request: eventbridge_20200401_models.ListUserDefinedEventSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListUserDefinedEventSourcesResponse:
        """
        You can call this API operation to query custom event sources.
        
        @param request: ListUserDefinedEventSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserDefinedEventSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
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
        request: eventbridge_20200401_models.ListUserDefinedEventSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListUserDefinedEventSourcesResponse:
        """
        You can call this API operation to query custom event sources.
        
        @param request: ListUserDefinedEventSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserDefinedEventSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
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

    def list_user_defined_event_sources(
        self,
        request: eventbridge_20200401_models.ListUserDefinedEventSourcesRequest,
    ) -> eventbridge_20200401_models.ListUserDefinedEventSourcesResponse:
        """
        You can call this API operation to query custom event sources.
        
        @param request: ListUserDefinedEventSourcesRequest
        @return: ListUserDefinedEventSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_defined_event_sources_with_options(request, runtime)

    async def list_user_defined_event_sources_async(
        self,
        request: eventbridge_20200401_models.ListUserDefinedEventSourcesRequest,
    ) -> eventbridge_20200401_models.ListUserDefinedEventSourcesResponse:
        """
        You can call this API operation to query custom event sources.
        
        @param request: ListUserDefinedEventSourcesRequest
        @return: ListUserDefinedEventSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_defined_event_sources_with_options_async(request, runtime)

    def pause_event_streaming_with_options(
        self,
        request: eventbridge_20200401_models.PauseEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.PauseEventStreamingResponse:
        """
        You can call this API operation to stop an event stream that is running.
        
        @param request: PauseEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseEventStreamingResponse
        """
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
        """
        You can call this API operation to stop an event stream that is running.
        
        @param request: PauseEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseEventStreamingResponse
        """
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
        """
        You can call this API operation to stop an event stream that is running.
        
        @param request: PauseEventStreamingRequest
        @return: PauseEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pause_event_streaming_with_options(request, runtime)

    async def pause_event_streaming_async(
        self,
        request: eventbridge_20200401_models.PauseEventStreamingRequest,
    ) -> eventbridge_20200401_models.PauseEventStreamingResponse:
        """
        You can call this API operation to stop an event stream that is running.
        
        @param request: PauseEventStreamingRequest
        @return: PauseEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pause_event_streaming_with_options_async(request, runtime)

    def put_targets_with_options(
        self,
        tmp_req: eventbridge_20200401_models.PutTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.PutTargetsResponse:
        """
        You can call this API operation to create or update event targets under a rule.
        
        @param tmp_req: PutTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutTargetsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.PutTargetsShrinkRequest()
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
            action='PutTargets',
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
            eventbridge_20200401_models.PutTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_targets_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.PutTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.PutTargetsResponse:
        """
        You can call this API operation to create or update event targets under a rule.
        
        @param tmp_req: PutTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutTargetsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.PutTargetsShrinkRequest()
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
            action='PutTargets',
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
            eventbridge_20200401_models.PutTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_targets(
        self,
        request: eventbridge_20200401_models.PutTargetsRequest,
    ) -> eventbridge_20200401_models.PutTargetsResponse:
        """
        You can call this API operation to create or update event targets under a rule.
        
        @param request: PutTargetsRequest
        @return: PutTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_targets_with_options(request, runtime)

    async def put_targets_async(
        self,
        request: eventbridge_20200401_models.PutTargetsRequest,
    ) -> eventbridge_20200401_models.PutTargetsResponse:
        """
        You can call this API operation to create or update event targets under a rule.
        
        @param request: PutTargetsRequest
        @return: PutTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_targets_with_options_async(request, runtime)

    def query_event_with_options(
        self,
        request: eventbridge_20200401_models.QueryEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryEventResponse:
        """
        You can call this API operation to query the content of an event.
        
        @param request: QueryEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.event_source):
            query['EventSource'] = request.event_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEvent',
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
            eventbridge_20200401_models.QueryEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_with_options_async(
        self,
        request: eventbridge_20200401_models.QueryEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryEventResponse:
        """
        You can call this API operation to query the content of an event.
        
        @param request: QueryEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.event_source):
            query['EventSource'] = request.event_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEvent',
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
            eventbridge_20200401_models.QueryEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_event(
        self,
        request: eventbridge_20200401_models.QueryEventRequest,
    ) -> eventbridge_20200401_models.QueryEventResponse:
        """
        You can call this API operation to query the content of an event.
        
        @param request: QueryEventRequest
        @return: QueryEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_event_with_options(request, runtime)

    async def query_event_async(
        self,
        request: eventbridge_20200401_models.QueryEventRequest,
    ) -> eventbridge_20200401_models.QueryEventResponse:
        """
        You can call this API operation to query the content of an event.
        
        @param request: QueryEventRequest
        @return: QueryEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_event_with_options_async(request, runtime)

    def query_event_traces_with_options(
        self,
        request: eventbridge_20200401_models.QueryEventTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryEventTracesResponse:
        """
        You can call this API operation to query event traces.
        
        @param request: QueryEventTracesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEventTracesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventTraces',
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
            eventbridge_20200401_models.QueryEventTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_traces_with_options_async(
        self,
        request: eventbridge_20200401_models.QueryEventTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryEventTracesResponse:
        """
        You can call this API operation to query event traces.
        
        @param request: QueryEventTracesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEventTracesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventTraces',
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
            eventbridge_20200401_models.QueryEventTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_event_traces(
        self,
        request: eventbridge_20200401_models.QueryEventTracesRequest,
    ) -> eventbridge_20200401_models.QueryEventTracesResponse:
        """
        You can call this API operation to query event traces.
        
        @param request: QueryEventTracesRequest
        @return: QueryEventTracesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_event_traces_with_options(request, runtime)

    async def query_event_traces_async(
        self,
        request: eventbridge_20200401_models.QueryEventTracesRequest,
    ) -> eventbridge_20200401_models.QueryEventTracesResponse:
        """
        You can call this API operation to query event traces.
        
        @param request: QueryEventTracesRequest
        @return: QueryEventTracesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_event_traces_with_options_async(request, runtime)

    def query_traced_event_by_event_id_with_options(
        self,
        request: eventbridge_20200401_models.QueryTracedEventByEventIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryTracedEventByEventIdResponse:
        """
        You can call this API operation to query event traces by event ID.
        
        @param request: QueryTracedEventByEventIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTracedEventByEventIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.event_source):
            query['EventSource'] = request.event_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTracedEventByEventId',
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
            eventbridge_20200401_models.QueryTracedEventByEventIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_traced_event_by_event_id_with_options_async(
        self,
        request: eventbridge_20200401_models.QueryTracedEventByEventIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryTracedEventByEventIdResponse:
        """
        You can call this API operation to query event traces by event ID.
        
        @param request: QueryTracedEventByEventIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTracedEventByEventIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.event_source):
            query['EventSource'] = request.event_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTracedEventByEventId',
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
            eventbridge_20200401_models.QueryTracedEventByEventIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_traced_event_by_event_id(
        self,
        request: eventbridge_20200401_models.QueryTracedEventByEventIdRequest,
    ) -> eventbridge_20200401_models.QueryTracedEventByEventIdResponse:
        """
        You can call this API operation to query event traces by event ID.
        
        @param request: QueryTracedEventByEventIdRequest
        @return: QueryTracedEventByEventIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_traced_event_by_event_id_with_options(request, runtime)

    async def query_traced_event_by_event_id_async(
        self,
        request: eventbridge_20200401_models.QueryTracedEventByEventIdRequest,
    ) -> eventbridge_20200401_models.QueryTracedEventByEventIdResponse:
        """
        You can call this API operation to query event traces by event ID.
        
        @param request: QueryTracedEventByEventIdRequest
        @return: QueryTracedEventByEventIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_traced_event_by_event_id_with_options_async(request, runtime)

    def query_traced_events_with_options(
        self,
        request: eventbridge_20200401_models.QueryTracedEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryTracedEventsResponse:
        """
        You can call this API operation to query event traces by time range.
        
        @param request: QueryTracedEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTracedEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source):
            query['EventSource'] = request.event_source
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.matched_rule):
            query['MatchedRule'] = request.matched_rule
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTracedEvents',
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
            eventbridge_20200401_models.QueryTracedEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_traced_events_with_options_async(
        self,
        request: eventbridge_20200401_models.QueryTracedEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryTracedEventsResponse:
        """
        You can call this API operation to query event traces by time range.
        
        @param request: QueryTracedEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTracedEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source):
            query['EventSource'] = request.event_source
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.matched_rule):
            query['MatchedRule'] = request.matched_rule
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTracedEvents',
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
            eventbridge_20200401_models.QueryTracedEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_traced_events(
        self,
        request: eventbridge_20200401_models.QueryTracedEventsRequest,
    ) -> eventbridge_20200401_models.QueryTracedEventsResponse:
        """
        You can call this API operation to query event traces by time range.
        
        @param request: QueryTracedEventsRequest
        @return: QueryTracedEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_traced_events_with_options(request, runtime)

    async def query_traced_events_async(
        self,
        request: eventbridge_20200401_models.QueryTracedEventsRequest,
    ) -> eventbridge_20200401_models.QueryTracedEventsResponse:
        """
        You can call this API operation to query event traces by time range.
        
        @param request: QueryTracedEventsRequest
        @return: QueryTracedEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_traced_events_with_options_async(request, runtime)

    def start_event_streaming_with_options(
        self,
        request: eventbridge_20200401_models.StartEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.StartEventStreamingResponse:
        """
        You can call this API operation to enable a created or deactivated event stream.
        
        @param request: StartEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartEventStreamingResponse
        """
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
        """
        You can call this API operation to enable a created or deactivated event stream.
        
        @param request: StartEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartEventStreamingResponse
        """
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
        """
        You can call this API operation to enable a created or deactivated event stream.
        
        @param request: StartEventStreamingRequest
        @return: StartEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_event_streaming_with_options(request, runtime)

    async def start_event_streaming_async(
        self,
        request: eventbridge_20200401_models.StartEventStreamingRequest,
    ) -> eventbridge_20200401_models.StartEventStreamingResponse:
        """
        You can call this API operation to enable a created or deactivated event stream.
        
        @param request: StartEventStreamingRequest
        @return: StartEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_event_streaming_with_options_async(request, runtime)

    def test_event_pattern_with_options(
        self,
        request: eventbridge_20200401_models.TestEventPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.TestEventPatternResponse:
        """
        You can call this API operation to check whether the event pattern matches the provided JSON format.
        
        @param request: TestEventPatternRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TestEventPatternResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event):
            body['Event'] = request.event
        if not UtilClient.is_unset(request.event_pattern):
            body['EventPattern'] = request.event_pattern
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TestEventPattern',
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
            eventbridge_20200401_models.TestEventPatternResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_event_pattern_with_options_async(
        self,
        request: eventbridge_20200401_models.TestEventPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.TestEventPatternResponse:
        """
        You can call this API operation to check whether the event pattern matches the provided JSON format.
        
        @param request: TestEventPatternRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TestEventPatternResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event):
            body['Event'] = request.event
        if not UtilClient.is_unset(request.event_pattern):
            body['EventPattern'] = request.event_pattern
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TestEventPattern',
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
            eventbridge_20200401_models.TestEventPatternResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_event_pattern(
        self,
        request: eventbridge_20200401_models.TestEventPatternRequest,
    ) -> eventbridge_20200401_models.TestEventPatternResponse:
        """
        You can call this API operation to check whether the event pattern matches the provided JSON format.
        
        @param request: TestEventPatternRequest
        @return: TestEventPatternResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.test_event_pattern_with_options(request, runtime)

    async def test_event_pattern_async(
        self,
        request: eventbridge_20200401_models.TestEventPatternRequest,
    ) -> eventbridge_20200401_models.TestEventPatternResponse:
        """
        You can call this API operation to check whether the event pattern matches the provided JSON format.
        
        @param request: TestEventPatternRequest
        @return: TestEventPatternResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.test_event_pattern_with_options_async(request, runtime)

    def update_api_destination_with_options(
        self,
        tmp_req: eventbridge_20200401_models.UpdateApiDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateApiDestinationResponse:
        """
        You can call this API operation to update an API destination.
        
        @param tmp_req: UpdateApiDestinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApiDestinationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateApiDestinationShrinkRequest()
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
        """
        You can call this API operation to update an API destination.
        
        @param tmp_req: UpdateApiDestinationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApiDestinationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateApiDestinationShrinkRequest()
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
        """
        You can call this API operation to update an API destination.
        
        @param request: UpdateApiDestinationRequest
        @return: UpdateApiDestinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_api_destination_with_options(request, runtime)

    async def update_api_destination_async(
        self,
        request: eventbridge_20200401_models.UpdateApiDestinationRequest,
    ) -> eventbridge_20200401_models.UpdateApiDestinationResponse:
        """
        You can call this API operation to update an API destination.
        
        @param request: UpdateApiDestinationRequest
        @return: UpdateApiDestinationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_api_destination_with_options_async(request, runtime)

    def update_connection_with_options(
        self,
        tmp_req: eventbridge_20200401_models.UpdateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateConnectionResponse:
        """
        You can call this API operation to update a connection.
        
        @param tmp_req: UpdateConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConnectionResponse
        """
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
        """
        You can call this API operation to update a connection.
        
        @param tmp_req: UpdateConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConnectionResponse
        """
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
        """
        You can call this API operation to update a connection.
        
        @param request: UpdateConnectionRequest
        @return: UpdateConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_connection_with_options(request, runtime)

    async def update_connection_async(
        self,
        request: eventbridge_20200401_models.UpdateConnectionRequest,
    ) -> eventbridge_20200401_models.UpdateConnectionResponse:
        """
        You can call this API operation to update a connection.
        
        @param request: UpdateConnectionRequest
        @return: UpdateConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_connection_with_options_async(request, runtime)

    def update_event_bus_with_options(
        self,
        request: eventbridge_20200401_models.UpdateEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateEventBusResponse:
        """
        You can call this API operation to modify an event bus.
        
        @param request: UpdateEventBusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEventBusResponse
        """
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
        """
        You can call this API operation to modify an event bus.
        
        @param request: UpdateEventBusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEventBusResponse
        """
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
        """
        You can call this API operation to modify an event bus.
        
        @param request: UpdateEventBusRequest
        @return: UpdateEventBusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_event_bus_with_options(request, runtime)

    async def update_event_bus_async(
        self,
        request: eventbridge_20200401_models.UpdateEventBusRequest,
    ) -> eventbridge_20200401_models.UpdateEventBusResponse:
        """
        You can call this API operation to modify an event bus.
        
        @param request: UpdateEventBusRequest
        @return: UpdateEventBusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_event_bus_with_options_async(request, runtime)

    def update_event_source_with_options(
        self,
        tmp_req: eventbridge_20200401_models.UpdateEventSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateEventSourceResponse:
        """
        You can call this API operation to update an event source.
        
        @param tmp_req: UpdateEventSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEventSourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateEventSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_kafka_parameters):
            request.source_kafka_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_kafka_parameters, 'SourceKafkaParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_scheduled_event_parameters):
            request.source_scheduled_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_scheduled_event_parameters, 'SourceScheduledEventParameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not UtilClient.is_unset(request.source_kafka_parameters_shrink):
            body['SourceKafkaParameters'] = request.source_kafka_parameters_shrink
        if not UtilClient.is_unset(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not UtilClient.is_unset(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not UtilClient.is_unset(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not UtilClient.is_unset(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        if not UtilClient.is_unset(request.source_scheduled_event_parameters_shrink):
            body['SourceScheduledEventParameters'] = request.source_scheduled_event_parameters_shrink
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
        """
        You can call this API operation to update an event source.
        
        @param tmp_req: UpdateEventSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEventSourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateEventSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_http_event_parameters):
            request.source_http_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_http_event_parameters, 'SourceHttpEventParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_kafka_parameters):
            request.source_kafka_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_kafka_parameters, 'SourceKafkaParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_mnsparameters):
            request.source_mnsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_mnsparameters, 'SourceMNSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rabbit_mqparameters):
            request.source_rabbit_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rabbit_mqparameters, 'SourceRabbitMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_rocket_mqparameters):
            request.source_rocket_mqparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_rocket_mqparameters, 'SourceRocketMQParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_slsparameters):
            request.source_slsparameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_slsparameters, 'SourceSLSParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_scheduled_event_parameters):
            request.source_scheduled_event_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_scheduled_event_parameters, 'SourceScheduledEventParameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.source_http_event_parameters_shrink):
            body['SourceHttpEventParameters'] = request.source_http_event_parameters_shrink
        if not UtilClient.is_unset(request.source_kafka_parameters_shrink):
            body['SourceKafkaParameters'] = request.source_kafka_parameters_shrink
        if not UtilClient.is_unset(request.source_mnsparameters_shrink):
            body['SourceMNSParameters'] = request.source_mnsparameters_shrink
        if not UtilClient.is_unset(request.source_rabbit_mqparameters_shrink):
            body['SourceRabbitMQParameters'] = request.source_rabbit_mqparameters_shrink
        if not UtilClient.is_unset(request.source_rocket_mqparameters_shrink):
            body['SourceRocketMQParameters'] = request.source_rocket_mqparameters_shrink
        if not UtilClient.is_unset(request.source_slsparameters_shrink):
            body['SourceSLSParameters'] = request.source_slsparameters_shrink
        if not UtilClient.is_unset(request.source_scheduled_event_parameters_shrink):
            body['SourceScheduledEventParameters'] = request.source_scheduled_event_parameters_shrink
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
        """
        You can call this API operation to update an event source.
        
        @param request: UpdateEventSourceRequest
        @return: UpdateEventSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_event_source_with_options(request, runtime)

    async def update_event_source_async(
        self,
        request: eventbridge_20200401_models.UpdateEventSourceRequest,
    ) -> eventbridge_20200401_models.UpdateEventSourceResponse:
        """
        You can call this API operation to update an event source.
        
        @param request: UpdateEventSourceRequest
        @return: UpdateEventSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_event_source_with_options_async(request, runtime)

    def update_event_streaming_with_options(
        self,
        tmp_req: eventbridge_20200401_models.UpdateEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateEventStreamingResponse:
        """
        You can call this API operation to modify the information about an event stream, such as the basic information and the information about the event source, event filtering rule, and event target.
        
        @param tmp_req: UpdateEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEventStreamingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateEventStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.run_options):
            request.run_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not UtilClient.is_unset(tmp_req.sink):
            request.sink_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        if not UtilClient.is_unset(tmp_req.transforms):
            request.transforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transforms, 'Transforms', 'json')
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
        if not UtilClient.is_unset(request.transforms_shrink):
            body['Transforms'] = request.transforms_shrink
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
        """
        You can call this API operation to modify the information about an event stream, such as the basic information and the information about the event source, event filtering rule, and event target.
        
        @param tmp_req: UpdateEventStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEventStreamingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateEventStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.run_options):
            request.run_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.run_options, 'RunOptions', 'json')
        if not UtilClient.is_unset(tmp_req.sink):
            request.sink_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sink, 'Sink', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        if not UtilClient.is_unset(tmp_req.transforms):
            request.transforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transforms, 'Transforms', 'json')
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
        if not UtilClient.is_unset(request.transforms_shrink):
            body['Transforms'] = request.transforms_shrink
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
        """
        You can call this API operation to modify the information about an event stream, such as the basic information and the information about the event source, event filtering rule, and event target.
        
        @param request: UpdateEventStreamingRequest
        @return: UpdateEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_event_streaming_with_options(request, runtime)

    async def update_event_streaming_async(
        self,
        request: eventbridge_20200401_models.UpdateEventStreamingRequest,
    ) -> eventbridge_20200401_models.UpdateEventStreamingResponse:
        """
        You can call this API operation to modify the information about an event stream, such as the basic information and the information about the event source, event filtering rule, and event target.
        
        @param request: UpdateEventStreamingRequest
        @return: UpdateEventStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_event_streaming_with_options_async(request, runtime)

    def update_rule_with_options(
        self,
        request: eventbridge_20200401_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateRuleResponse:
        """
        You can call this API operation to update the configurations of an event rule.
        
        @param request: UpdateRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleResponse
        """
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
        """
        You can call this API operation to update the configurations of an event rule.
        
        @param request: UpdateRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleResponse
        """
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
        """
        You can call this API operation to update the configurations of an event rule.
        
        @param request: UpdateRuleRequest
        @return: UpdateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    async def update_rule_async(
        self,
        request: eventbridge_20200401_models.UpdateRuleRequest,
    ) -> eventbridge_20200401_models.UpdateRuleResponse:
        """
        You can call this API operation to update the configurations of an event rule.
        
        @param request: UpdateRuleRequest
        @return: UpdateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_with_options_async(request, runtime)
