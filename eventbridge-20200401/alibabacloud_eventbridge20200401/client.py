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

    def attach_ebevent_bus_with_options(
        self,
        request: eventbridge_20200401_models.AttachEBEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.AttachEBEventBusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_full_name):
            body['EventSourceFullName'] = request.event_source_full_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachEBEventBus',
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
            eventbridge_20200401_models.AttachEBEventBusResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_ebevent_bus_with_options_async(
        self,
        request: eventbridge_20200401_models.AttachEBEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.AttachEBEventBusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_full_name):
            body['EventSourceFullName'] = request.event_source_full_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachEBEventBus',
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
            eventbridge_20200401_models.AttachEBEventBusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_ebevent_bus(
        self,
        request: eventbridge_20200401_models.AttachEBEventBusRequest,
    ) -> eventbridge_20200401_models.AttachEBEventBusResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_ebevent_bus_with_options(request, runtime)

    async def attach_ebevent_bus_async(
        self,
        request: eventbridge_20200401_models.AttachEBEventBusRequest,
    ) -> eventbridge_20200401_models.AttachEBEventBusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_ebevent_bus_with_options_async(request, runtime)

    def check_role_for_product_with_options(
        self,
        request: eventbridge_20200401_models.CheckRoleForProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CheckRoleForProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckRoleForProduct',
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
            eventbridge_20200401_models.CheckRoleForProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_role_for_product_with_options_async(
        self,
        request: eventbridge_20200401_models.CheckRoleForProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CheckRoleForProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckRoleForProduct',
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
            eventbridge_20200401_models.CheckRoleForProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_role_for_product(
        self,
        request: eventbridge_20200401_models.CheckRoleForProductRequest,
    ) -> eventbridge_20200401_models.CheckRoleForProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_role_for_product_with_options(request, runtime)

    async def check_role_for_product_async(
        self,
        request: eventbridge_20200401_models.CheckRoleForProductRequest,
    ) -> eventbridge_20200401_models.CheckRoleForProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_role_for_product_with_options_async(request, runtime)

    def check_role_for_target_with_options(
        self,
        request: eventbridge_20200401_models.CheckRoleForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CheckRoleForTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckRoleForTarget',
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
            eventbridge_20200401_models.CheckRoleForTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_role_for_target_with_options_async(
        self,
        request: eventbridge_20200401_models.CheckRoleForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CheckRoleForTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckRoleForTarget',
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
            eventbridge_20200401_models.CheckRoleForTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_role_for_target(
        self,
        request: eventbridge_20200401_models.CheckRoleForTargetRequest,
    ) -> eventbridge_20200401_models.CheckRoleForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_role_for_target_with_options(request, runtime)

    async def check_role_for_target_async(
        self,
        request: eventbridge_20200401_models.CheckRoleForTargetRequest,
    ) -> eventbridge_20200401_models.CheckRoleForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_role_for_target_with_options_async(request, runtime)

    def check_service_linked_role_for_delete_with_options(
        self,
        request: eventbridge_20200401_models.CheckServiceLinkedRoleForDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CheckServiceLinkedRoleForDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRoleForDelete',
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
            eventbridge_20200401_models.CheckServiceLinkedRoleForDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_for_delete_with_options_async(
        self,
        request: eventbridge_20200401_models.CheckServiceLinkedRoleForDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CheckServiceLinkedRoleForDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRoleForDelete',
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
            eventbridge_20200401_models.CheckServiceLinkedRoleForDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role_for_delete(
        self,
        request: eventbridge_20200401_models.CheckServiceLinkedRoleForDeleteRequest,
    ) -> eventbridge_20200401_models.CheckServiceLinkedRoleForDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_for_delete_with_options(request, runtime)

    async def check_service_linked_role_for_delete_async(
        self,
        request: eventbridge_20200401_models.CheckServiceLinkedRoleForDeleteRequest,
    ) -> eventbridge_20200401_models.CheckServiceLinkedRoleForDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_for_delete_with_options_async(request, runtime)

    def complete_commodity_with_options(
        self,
        request: eventbridge_20200401_models.CompleteCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CompleteCommodityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteCommodity',
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
            eventbridge_20200401_models.CompleteCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_commodity_with_options_async(
        self,
        request: eventbridge_20200401_models.CompleteCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CompleteCommodityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteCommodity',
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
            eventbridge_20200401_models.CompleteCommodityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_commodity(
        self,
        request: eventbridge_20200401_models.CompleteCommodityRequest,
    ) -> eventbridge_20200401_models.CompleteCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return self.complete_commodity_with_options(request, runtime)

    async def complete_commodity_async(
        self,
        request: eventbridge_20200401_models.CompleteCommodityRequest,
    ) -> eventbridge_20200401_models.CompleteCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.complete_commodity_with_options_async(request, runtime)

    def complete_order_param_with_options(
        self,
        request: eventbridge_20200401_models.CompleteOrderParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CompleteOrderParamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteOrderParam',
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
            eventbridge_20200401_models.CompleteOrderParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_order_param_with_options_async(
        self,
        request: eventbridge_20200401_models.CompleteOrderParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CompleteOrderParamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteOrderParam',
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
            eventbridge_20200401_models.CompleteOrderParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_order_param(
        self,
        request: eventbridge_20200401_models.CompleteOrderParamRequest,
    ) -> eventbridge_20200401_models.CompleteOrderParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.complete_order_param_with_options(request, runtime)

    async def complete_order_param_async(
        self,
        request: eventbridge_20200401_models.CompleteOrderParamRequest,
    ) -> eventbridge_20200401_models.CompleteOrderParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.complete_order_param_with_options_async(request, runtime)

    def create_event_bus_with_options(
        self,
        request: eventbridge_20200401_models.CreateEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateEventBusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(tmp_req.external_source_config):
            request.external_source_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_source_config, 'ExternalSourceConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.external_source_config_shrink):
            body['ExternalSourceConfig'] = request.external_source_config_shrink
        if not UtilClient.is_unset(request.external_source_type):
            body['ExternalSourceType'] = request.external_source_type
        if not UtilClient.is_unset(request.linked_external_source):
            body['LinkedExternalSource'] = request.linked_external_source
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
        if not UtilClient.is_unset(tmp_req.external_source_config):
            request.external_source_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_source_config, 'ExternalSourceConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.external_source_config_shrink):
            body['ExternalSourceConfig'] = request.external_source_config_shrink
        if not UtilClient.is_unset(request.external_source_type):
            body['ExternalSourceType'] = request.external_source_type
        if not UtilClient.is_unset(request.linked_external_source):
            body['LinkedExternalSource'] = request.linked_external_source
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
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
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
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
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
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
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
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
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

    def create_schema_with_options(
        self,
        request: eventbridge_20200401_models.CreateSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compatible_type):
            query['CompatibleType'] = request.compatible_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchema',
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
            eventbridge_20200401_models.CreateSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schema_with_options_async(
        self,
        request: eventbridge_20200401_models.CreateSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compatible_type):
            query['CompatibleType'] = request.compatible_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchema',
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
            eventbridge_20200401_models.CreateSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schema(
        self,
        request: eventbridge_20200401_models.CreateSchemaRequest,
    ) -> eventbridge_20200401_models.CreateSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_schema_with_options(request, runtime)

    async def create_schema_async(
        self,
        request: eventbridge_20200401_models.CreateSchemaRequest,
    ) -> eventbridge_20200401_models.CreateSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_schema_with_options_async(request, runtime)

    def create_schema_group_with_options(
        self,
        request: eventbridge_20200401_models.CreateSchemaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateSchemaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_format):
            query['SchemaFormat'] = request.schema_format
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchemaGroup',
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
            eventbridge_20200401_models.CreateSchemaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schema_group_with_options_async(
        self,
        request: eventbridge_20200401_models.CreateSchemaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateSchemaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_format):
            query['SchemaFormat'] = request.schema_format
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchemaGroup',
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
            eventbridge_20200401_models.CreateSchemaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schema_group(
        self,
        request: eventbridge_20200401_models.CreateSchemaGroupRequest,
    ) -> eventbridge_20200401_models.CreateSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_schema_group_with_options(request, runtime)

    async def create_schema_group_async(
        self,
        request: eventbridge_20200401_models.CreateSchemaGroupRequest,
    ) -> eventbridge_20200401_models.CreateSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_schema_group_with_options_async(request, runtime)

    def create_schema_version_with_options(
        self,
        request: eventbridge_20200401_models.CreateSchemaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateSchemaVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchemaVersion',
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
            eventbridge_20200401_models.CreateSchemaVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schema_version_with_options_async(
        self,
        request: eventbridge_20200401_models.CreateSchemaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateSchemaVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchemaVersion',
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
            eventbridge_20200401_models.CreateSchemaVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schema_version(
        self,
        request: eventbridge_20200401_models.CreateSchemaVersionRequest,
    ) -> eventbridge_20200401_models.CreateSchemaVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_schema_version_with_options(request, runtime)

    async def create_schema_version_async(
        self,
        request: eventbridge_20200401_models.CreateSchemaVersionRequest,
    ) -> eventbridge_20200401_models.CreateSchemaVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_schema_version_with_options_async(request, runtime)

    def create_service_linked_role_for_product_with_options(
        self,
        request: eventbridge_20200401_models.CreateServiceLinkedRoleForProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateServiceLinkedRoleForProductResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_for_product_with_options(request, runtime)

    async def create_service_linked_role_for_product_async(
        self,
        request: eventbridge_20200401_models.CreateServiceLinkedRoleForProductRequest,
    ) -> eventbridge_20200401_models.CreateServiceLinkedRoleForProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_for_product_with_options_async(request, runtime)

    def create_service_linked_role_for_target_with_options(
        self,
        request: eventbridge_20200401_models.CreateServiceLinkedRoleForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateServiceLinkedRoleForTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRoleForTarget',
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
            eventbridge_20200401_models.CreateServiceLinkedRoleForTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_for_target_with_options_async(
        self,
        request: eventbridge_20200401_models.CreateServiceLinkedRoleForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.CreateServiceLinkedRoleForTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRoleForTarget',
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
            eventbridge_20200401_models.CreateServiceLinkedRoleForTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role_for_target(
        self,
        request: eventbridge_20200401_models.CreateServiceLinkedRoleForTargetRequest,
    ) -> eventbridge_20200401_models.CreateServiceLinkedRoleForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_for_target_with_options(request, runtime)

    async def create_service_linked_role_for_target_async(
        self,
        request: eventbridge_20200401_models.CreateServiceLinkedRoleForTargetRequest,
    ) -> eventbridge_20200401_models.CreateServiceLinkedRoleForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_for_target_with_options_async(request, runtime)

    def delete_event_bus_with_options(
        self,
        request: eventbridge_20200401_models.DeleteEventBusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteEventBusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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

    def delete_schema_with_options(
        self,
        request: eventbridge_20200401_models.DeleteSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchema',
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
            eventbridge_20200401_models.DeleteSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schema_with_options_async(
        self,
        request: eventbridge_20200401_models.DeleteSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchema',
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
            eventbridge_20200401_models.DeleteSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schema(
        self,
        request: eventbridge_20200401_models.DeleteSchemaRequest,
    ) -> eventbridge_20200401_models.DeleteSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_schema_with_options(request, runtime)

    async def delete_schema_async(
        self,
        request: eventbridge_20200401_models.DeleteSchemaRequest,
    ) -> eventbridge_20200401_models.DeleteSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_schema_with_options_async(request, runtime)

    def delete_schema_group_with_options(
        self,
        request: eventbridge_20200401_models.DeleteSchemaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteSchemaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchemaGroup',
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
            eventbridge_20200401_models.DeleteSchemaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schema_group_with_options_async(
        self,
        request: eventbridge_20200401_models.DeleteSchemaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteSchemaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchemaGroup',
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
            eventbridge_20200401_models.DeleteSchemaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schema_group(
        self,
        request: eventbridge_20200401_models.DeleteSchemaGroupRequest,
    ) -> eventbridge_20200401_models.DeleteSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_schema_group_with_options(request, runtime)

    async def delete_schema_group_async(
        self,
        request: eventbridge_20200401_models.DeleteSchemaGroupRequest,
    ) -> eventbridge_20200401_models.DeleteSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_schema_group_with_options_async(request, runtime)

    def delete_schema_version_with_options(
        self,
        request: eventbridge_20200401_models.DeleteSchemaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteSchemaVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.version_number):
            query['VersionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchemaVersion',
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
            eventbridge_20200401_models.DeleteSchemaVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schema_version_with_options_async(
        self,
        request: eventbridge_20200401_models.DeleteSchemaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteSchemaVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.version_number):
            query['VersionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchemaVersion',
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
            eventbridge_20200401_models.DeleteSchemaVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schema_version(
        self,
        request: eventbridge_20200401_models.DeleteSchemaVersionRequest,
    ) -> eventbridge_20200401_models.DeleteSchemaVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_schema_version_with_options(request, runtime)

    async def delete_schema_version_async(
        self,
        request: eventbridge_20200401_models.DeleteSchemaVersionRequest,
    ) -> eventbridge_20200401_models.DeleteSchemaVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_schema_version_with_options_async(request, runtime)

    def delete_source_task_with_options(
        self,
        request: eventbridge_20200401_models.DeleteSourceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteSourceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSourceTask',
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
            eventbridge_20200401_models.DeleteSourceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_source_task_with_options_async(
        self,
        request: eventbridge_20200401_models.DeleteSourceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DeleteSourceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSourceTask',
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
            eventbridge_20200401_models.DeleteSourceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_source_task(
        self,
        request: eventbridge_20200401_models.DeleteSourceTaskRequest,
    ) -> eventbridge_20200401_models.DeleteSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_source_task_with_options(request, runtime)

    async def delete_source_task_async(
        self,
        request: eventbridge_20200401_models.DeleteSourceTaskRequest,
    ) -> eventbridge_20200401_models.DeleteSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_source_task_with_options_async(request, runtime)

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

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
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
            eventbridge_20200401_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
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
            eventbridge_20200401_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> eventbridge_20200401_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> eventbridge_20200401_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

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

    def fetch_product_resource_values_with_options(
        self,
        request: eventbridge_20200401_models.FetchProductResourceValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.FetchProductResourceValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extra_params):
            query['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.resource_key):
            query['ResourceKey'] = request.resource_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchProductResourceValues',
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
            eventbridge_20200401_models.FetchProductResourceValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_product_resource_values_with_options_async(
        self,
        request: eventbridge_20200401_models.FetchProductResourceValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.FetchProductResourceValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extra_params):
            query['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.resource_key):
            query['ResourceKey'] = request.resource_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchProductResourceValues',
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
            eventbridge_20200401_models.FetchProductResourceValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_product_resource_values(
        self,
        request: eventbridge_20200401_models.FetchProductResourceValuesRequest,
    ) -> eventbridge_20200401_models.FetchProductResourceValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.fetch_product_resource_values_with_options(request, runtime)

    async def fetch_product_resource_values_async(
        self,
        request: eventbridge_20200401_models.FetchProductResourceValuesRequest,
    ) -> eventbridge_20200401_models.FetchProductResourceValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fetch_product_resource_values_with_options_async(request, runtime)

    def fetch_target_resource_values_with_options(
        self,
        request: eventbridge_20200401_models.FetchTargetResourceValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.FetchTargetResourceValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extra_params):
            query['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.resource_key):
            query['ResourceKey'] = request.resource_key
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchTargetResourceValues',
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
            eventbridge_20200401_models.FetchTargetResourceValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_target_resource_values_with_options_async(
        self,
        request: eventbridge_20200401_models.FetchTargetResourceValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.FetchTargetResourceValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extra_params):
            query['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.resource_key):
            query['ResourceKey'] = request.resource_key
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchTargetResourceValues',
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
            eventbridge_20200401_models.FetchTargetResourceValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_target_resource_values(
        self,
        request: eventbridge_20200401_models.FetchTargetResourceValuesRequest,
    ) -> eventbridge_20200401_models.FetchTargetResourceValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.fetch_target_resource_values_with_options(request, runtime)

    async def fetch_target_resource_values_async(
        self,
        request: eventbridge_20200401_models.FetchTargetResourceValuesRequest,
    ) -> eventbridge_20200401_models.FetchTargetResourceValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fetch_target_resource_values_with_options_async(request, runtime)

    def get_acsevents_schema_with_options(
        self,
        request: eventbridge_20200401_models.GetACSEventsSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetACSEventsSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetACSEventsSchema',
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
            eventbridge_20200401_models.GetACSEventsSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_acsevents_schema_with_options_async(
        self,
        request: eventbridge_20200401_models.GetACSEventsSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetACSEventsSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetACSEventsSchema',
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
            eventbridge_20200401_models.GetACSEventsSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_acsevents_schema(
        self,
        request: eventbridge_20200401_models.GetACSEventsSchemaRequest,
    ) -> eventbridge_20200401_models.GetACSEventsSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_acsevents_schema_with_options(request, runtime)

    async def get_acsevents_schema_async(
        self,
        request: eventbridge_20200401_models.GetACSEventsSchemaRequest,
    ) -> eventbridge_20200401_models.GetACSEventsSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_acsevents_schema_with_options_async(request, runtime)

    def get_acsevents_schema_group_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetACSEventsSchemaGroupResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetACSEventsSchemaGroup',
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
            eventbridge_20200401_models.GetACSEventsSchemaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_acsevents_schema_group_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetACSEventsSchemaGroupResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetACSEventsSchemaGroup',
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
            eventbridge_20200401_models.GetACSEventsSchemaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_acsevents_schema_group(self) -> eventbridge_20200401_models.GetACSEventsSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_acsevents_schema_group_with_options(runtime)

    async def get_acsevents_schema_group_async(self) -> eventbridge_20200401_models.GetACSEventsSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_acsevents_schema_group_with_options_async(runtime)

    def get_acsevents_schema_version_with_options(
        self,
        request: eventbridge_20200401_models.GetACSEventsSchemaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetACSEventsSchemaVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.version_number):
            query['VersionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetACSEventsSchemaVersion',
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
            eventbridge_20200401_models.GetACSEventsSchemaVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_acsevents_schema_version_with_options_async(
        self,
        request: eventbridge_20200401_models.GetACSEventsSchemaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetACSEventsSchemaVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.version_number):
            query['VersionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetACSEventsSchemaVersion',
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
            eventbridge_20200401_models.GetACSEventsSchemaVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_acsevents_schema_version(
        self,
        request: eventbridge_20200401_models.GetACSEventsSchemaVersionRequest,
    ) -> eventbridge_20200401_models.GetACSEventsSchemaVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_acsevents_schema_version_with_options(request, runtime)

    async def get_acsevents_schema_version_async(
        self,
        request: eventbridge_20200401_models.GetACSEventsSchemaVersionRequest,
    ) -> eventbridge_20200401_models.GetACSEventsSchemaVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_acsevents_schema_version_with_options_async(request, runtime)

    def get_default_schema_group_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetDefaultSchemaGroupResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDefaultSchemaGroup',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetDefaultSchemaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_default_schema_group_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetDefaultSchemaGroupResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDefaultSchemaGroup',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetDefaultSchemaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_default_schema_group(self) -> eventbridge_20200401_models.GetDefaultSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_default_schema_group_with_options(runtime)

    async def get_default_schema_group_async(self) -> eventbridge_20200401_models.GetDefaultSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_default_schema_group_with_options_async(runtime)

    def get_endpoints_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetEndpointsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetEndpoints',
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
            eventbridge_20200401_models.GetEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_endpoints_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetEndpointsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetEndpoints',
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
            eventbridge_20200401_models.GetEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_endpoints(self) -> eventbridge_20200401_models.GetEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_endpoints_with_options(runtime)

    async def get_endpoints_async(self) -> eventbridge_20200401_models.GetEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_endpoints_with_options_async(runtime)

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

    def get_schema_with_options(
        self,
        request: eventbridge_20200401_models.GetSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSchema',
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
            eventbridge_20200401_models.GetSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_schema_with_options_async(
        self,
        request: eventbridge_20200401_models.GetSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSchema',
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
            eventbridge_20200401_models.GetSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_schema(
        self,
        request: eventbridge_20200401_models.GetSchemaRequest,
    ) -> eventbridge_20200401_models.GetSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_schema_with_options(request, runtime)

    async def get_schema_async(
        self,
        request: eventbridge_20200401_models.GetSchemaRequest,
    ) -> eventbridge_20200401_models.GetSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_schema_with_options_async(request, runtime)

    def get_schema_group_with_options(
        self,
        request: eventbridge_20200401_models.GetSchemaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetSchemaGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSchemaGroup',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetSchemaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_schema_group_with_options_async(
        self,
        request: eventbridge_20200401_models.GetSchemaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetSchemaGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSchemaGroup',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.GetSchemaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_schema_group(
        self,
        request: eventbridge_20200401_models.GetSchemaGroupRequest,
    ) -> eventbridge_20200401_models.GetSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_schema_group_with_options(request, runtime)

    async def get_schema_group_async(
        self,
        request: eventbridge_20200401_models.GetSchemaGroupRequest,
    ) -> eventbridge_20200401_models.GetSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_schema_group_with_options_async(request, runtime)

    def get_schema_version_with_options(
        self,
        request: eventbridge_20200401_models.GetSchemaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetSchemaVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.version_number):
            query['VersionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSchemaVersion',
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
            eventbridge_20200401_models.GetSchemaVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_schema_version_with_options_async(
        self,
        request: eventbridge_20200401_models.GetSchemaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetSchemaVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.version_number):
            query['VersionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSchemaVersion',
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
            eventbridge_20200401_models.GetSchemaVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_schema_version(
        self,
        request: eventbridge_20200401_models.GetSchemaVersionRequest,
    ) -> eventbridge_20200401_models.GetSchemaVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_schema_version_with_options(request, runtime)

    async def get_schema_version_async(
        self,
        request: eventbridge_20200401_models.GetSchemaVersionRequest,
    ) -> eventbridge_20200401_models.GetSchemaVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_schema_version_with_options_async(request, runtime)

    def get_source_task_with_options(
        self,
        request: eventbridge_20200401_models.GetSourceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetSourceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSourceTask',
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
            eventbridge_20200401_models.GetSourceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_source_task_with_options_async(
        self,
        request: eventbridge_20200401_models.GetSourceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.GetSourceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSourceTask',
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
            eventbridge_20200401_models.GetSourceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_source_task(
        self,
        request: eventbridge_20200401_models.GetSourceTaskRequest,
    ) -> eventbridge_20200401_models.GetSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_source_task_with_options(request, runtime)

    async def get_source_task_async(
        self,
        request: eventbridge_20200401_models.GetSourceTaskRequest,
    ) -> eventbridge_20200401_models.GetSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_source_task_with_options_async(request, runtime)

    def list_acsevents_schema_versions_with_options(
        self,
        request: eventbridge_20200401_models.ListACSEventsSchemaVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListACSEventsSchemaVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListACSEventsSchemaVersions',
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
            eventbridge_20200401_models.ListACSEventsSchemaVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acsevents_schema_versions_with_options_async(
        self,
        request: eventbridge_20200401_models.ListACSEventsSchemaVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListACSEventsSchemaVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListACSEventsSchemaVersions',
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
            eventbridge_20200401_models.ListACSEventsSchemaVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acsevents_schema_versions(
        self,
        request: eventbridge_20200401_models.ListACSEventsSchemaVersionsRequest,
    ) -> eventbridge_20200401_models.ListACSEventsSchemaVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_acsevents_schema_versions_with_options(request, runtime)

    async def list_acsevents_schema_versions_async(
        self,
        request: eventbridge_20200401_models.ListACSEventsSchemaVersionsRequest,
    ) -> eventbridge_20200401_models.ListACSEventsSchemaVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_acsevents_schema_versions_with_options_async(request, runtime)

    def list_acsevents_schemas_with_options(
        self,
        request: eventbridge_20200401_models.ListACSEventsSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListACSEventsSchemasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListACSEventsSchemas',
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
            eventbridge_20200401_models.ListACSEventsSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acsevents_schemas_with_options_async(
        self,
        request: eventbridge_20200401_models.ListACSEventsSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListACSEventsSchemasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListACSEventsSchemas',
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
            eventbridge_20200401_models.ListACSEventsSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acsevents_schemas(
        self,
        request: eventbridge_20200401_models.ListACSEventsSchemasRequest,
    ) -> eventbridge_20200401_models.ListACSEventsSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_acsevents_schemas_with_options(request, runtime)

    async def list_acsevents_schemas_async(
        self,
        request: eventbridge_20200401_models.ListACSEventsSchemasRequest,
    ) -> eventbridge_20200401_models.ListACSEventsSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_acsevents_schemas_with_options_async(request, runtime)

    def list_aliyun_official_event_sources_with_options(
        self,
        request: eventbridge_20200401_models.ListAliyunOfficialEventSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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
        request: eventbridge_20200401_models.ListAliyunOfficialEventSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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

    def list_aliyun_official_event_sources(
        self,
        request: eventbridge_20200401_models.ListAliyunOfficialEventSourcesRequest,
    ) -> eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aliyun_official_event_sources_with_options(request, runtime)

    async def list_aliyun_official_event_sources_async(
        self,
        request: eventbridge_20200401_models.ListAliyunOfficialEventSourcesRequest,
    ) -> eventbridge_20200401_models.ListAliyunOfficialEventSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aliyun_official_event_sources_with_options_async(request, runtime)

    def list_event_buses_with_options(
        self,
        request: eventbridge_20200401_models.ListEventBusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventBusesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_type):
            query['EventBusType'] = request.event_bus_type
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
        if not UtilClient.is_unset(request.event_bus_type):
            query['EventBusType'] = request.event_bus_type
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

    def list_event_sources_with_options(
        self,
        request: eventbridge_20200401_models.ListEventSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventSources',
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
            eventbridge_20200401_models.ListEventSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_sources_with_options_async(
        self,
        request: eventbridge_20200401_models.ListEventSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventSources',
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
            eventbridge_20200401_models.ListEventSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_sources(
        self,
        request: eventbridge_20200401_models.ListEventSourcesRequest,
    ) -> eventbridge_20200401_models.ListEventSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_sources_with_options(request, runtime)

    async def list_event_sources_async(
        self,
        request: eventbridge_20200401_models.ListEventSourcesRequest,
    ) -> eventbridge_20200401_models.ListEventSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_sources_with_options_async(request, runtime)

    def list_event_streaming_with_options(
        self,
        request: eventbridge_20200401_models.ListEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventStreamingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            body['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sink_type):
            body['SinkType'] = request.sink_type
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEventStreaming',
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
            eventbridge_20200401_models.ListEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_streaming_with_options_async(
        self,
        request: eventbridge_20200401_models.ListEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventStreamingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            body['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sink_type):
            body['SinkType'] = request.sink_type
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEventStreaming',
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
            eventbridge_20200401_models.ListEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_streaming(
        self,
        request: eventbridge_20200401_models.ListEventStreamingRequest,
    ) -> eventbridge_20200401_models.ListEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_streaming_with_options(request, runtime)

    async def list_event_streaming_async(
        self,
        request: eventbridge_20200401_models.ListEventStreamingRequest,
    ) -> eventbridge_20200401_models.ListEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_streaming_with_options_async(request, runtime)

    def list_event_streaming_metrics_with_options(
        self,
        request: eventbridge_20200401_models.ListEventStreamingMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventStreamingMetricsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventStreamingMetrics',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListEventStreamingMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_streaming_metrics_with_options_async(
        self,
        request: eventbridge_20200401_models.ListEventStreamingMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListEventStreamingMetricsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventStreamingMetrics',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListEventStreamingMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_streaming_metrics(
        self,
        request: eventbridge_20200401_models.ListEventStreamingMetricsRequest,
    ) -> eventbridge_20200401_models.ListEventStreamingMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_streaming_metrics_with_options(request, runtime)

    async def list_event_streaming_metrics_async(
        self,
        request: eventbridge_20200401_models.ListEventStreamingMetricsRequest,
    ) -> eventbridge_20200401_models.ListEventStreamingMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_streaming_metrics_with_options_async(request, runtime)

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

    def list_schema_groups_with_options(
        self,
        request: eventbridge_20200401_models.ListSchemaGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListSchemaGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchemaGroups',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListSchemaGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schema_groups_with_options_async(
        self,
        request: eventbridge_20200401_models.ListSchemaGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListSchemaGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchemaGroups',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListSchemaGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schema_groups(
        self,
        request: eventbridge_20200401_models.ListSchemaGroupsRequest,
    ) -> eventbridge_20200401_models.ListSchemaGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_schema_groups_with_options(request, runtime)

    async def list_schema_groups_async(
        self,
        request: eventbridge_20200401_models.ListSchemaGroupsRequest,
    ) -> eventbridge_20200401_models.ListSchemaGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_schema_groups_with_options_async(request, runtime)

    def list_schema_versions_with_options(
        self,
        request: eventbridge_20200401_models.ListSchemaVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListSchemaVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchemaVersions',
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
            eventbridge_20200401_models.ListSchemaVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schema_versions_with_options_async(
        self,
        request: eventbridge_20200401_models.ListSchemaVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListSchemaVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchemaVersions',
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
            eventbridge_20200401_models.ListSchemaVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schema_versions(
        self,
        request: eventbridge_20200401_models.ListSchemaVersionsRequest,
    ) -> eventbridge_20200401_models.ListSchemaVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_schema_versions_with_options(request, runtime)

    async def list_schema_versions_async(
        self,
        request: eventbridge_20200401_models.ListSchemaVersionsRequest,
    ) -> eventbridge_20200401_models.ListSchemaVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_schema_versions_with_options_async(request, runtime)

    def list_schemas_with_options(
        self,
        request: eventbridge_20200401_models.ListSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListSchemasResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchemas',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schemas_with_options_async(
        self,
        request: eventbridge_20200401_models.ListSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListSchemasResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchemas',
            version='2020-04-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eventbridge_20200401_models.ListSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schemas(
        self,
        request: eventbridge_20200401_models.ListSchemasRequest,
    ) -> eventbridge_20200401_models.ListSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_schemas_with_options(request, runtime)

    async def list_schemas_async(
        self,
        request: eventbridge_20200401_models.ListSchemasRequest,
    ) -> eventbridge_20200401_models.ListSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_schemas_with_options_async(request, runtime)

    def list_source_task_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListSourceTaskResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSourceTask',
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
            eventbridge_20200401_models.ListSourceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_source_task_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListSourceTaskResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSourceTask',
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
            eventbridge_20200401_models.ListSourceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_source_task(self) -> eventbridge_20200401_models.ListSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_source_task_with_options(runtime)

    async def list_source_task_async(self) -> eventbridge_20200401_models.ListSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_source_task_with_options_async(runtime)

    def list_target_types_with_options(
        self,
        request: eventbridge_20200401_models.ListTargetTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListTargetTypesResponse:
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
            action='ListTargetTypes',
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
            eventbridge_20200401_models.ListTargetTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_target_types_with_options_async(
        self,
        request: eventbridge_20200401_models.ListTargetTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListTargetTypesResponse:
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
            action='ListTargetTypes',
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
            eventbridge_20200401_models.ListTargetTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_target_types(
        self,
        request: eventbridge_20200401_models.ListTargetTypesRequest,
    ) -> eventbridge_20200401_models.ListTargetTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_target_types_with_options(request, runtime)

    async def list_target_types_async(
        self,
        request: eventbridge_20200401_models.ListTargetTypesRequest,
    ) -> eventbridge_20200401_models.ListTargetTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_target_types_with_options_async(request, runtime)

    def list_targets_with_options(
        self,
        request: eventbridge_20200401_models.ListTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.ListTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
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
        if not UtilClient.is_unset(request.event_bus_name):
            query['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
        runtime = util_models.RuntimeOptions()
        return self.list_user_defined_event_sources_with_options(request, runtime)

    async def list_user_defined_event_sources_async(
        self,
        request: eventbridge_20200401_models.ListUserDefinedEventSourcesRequest,
    ) -> eventbridge_20200401_models.ListUserDefinedEventSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_defined_event_sources_with_options_async(request, runtime)

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

    def pay_order_callback_with_options(
        self,
        request: eventbridge_20200401_models.PayOrderCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.PayOrderCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PayOrderCallback',
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
            eventbridge_20200401_models.PayOrderCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def pay_order_callback_with_options_async(
        self,
        request: eventbridge_20200401_models.PayOrderCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.PayOrderCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PayOrderCallback',
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
            eventbridge_20200401_models.PayOrderCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pay_order_callback(
        self,
        request: eventbridge_20200401_models.PayOrderCallbackRequest,
    ) -> eventbridge_20200401_models.PayOrderCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.pay_order_callback_with_options(request, runtime)

    async def pay_order_callback_async(
        self,
        request: eventbridge_20200401_models.PayOrderCallbackRequest,
    ) -> eventbridge_20200401_models.PayOrderCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pay_order_callback_with_options_async(request, runtime)

    def put_events_with_options(
        self,
        request: eventbridge_20200401_models.PutEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.PutEventsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_string):
            body['EventString'] = request.event_string
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutEvents',
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
            eventbridge_20200401_models.PutEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_events_with_options_async(
        self,
        request: eventbridge_20200401_models.PutEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.PutEventsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_string):
            body['EventString'] = request.event_string
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutEvents',
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
            eventbridge_20200401_models.PutEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_events(
        self,
        request: eventbridge_20200401_models.PutEventsRequest,
    ) -> eventbridge_20200401_models.PutEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_events_with_options(request, runtime)

    async def put_events_async(
        self,
        request: eventbridge_20200401_models.PutEventsRequest,
    ) -> eventbridge_20200401_models.PutEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_events_with_options_async(request, runtime)

    def query_event_with_options(
        self,
        request: eventbridge_20200401_models.QueryEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryEventResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_event_with_options(request, runtime)

    async def query_event_async(
        self,
        request: eventbridge_20200401_models.QueryEventRequest,
    ) -> eventbridge_20200401_models.QueryEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_event_with_options_async(request, runtime)

    def query_event_traces_with_options(
        self,
        request: eventbridge_20200401_models.QueryEventTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryEventTracesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_event_traces_with_options(request, runtime)

    async def query_event_traces_async(
        self,
        request: eventbridge_20200401_models.QueryEventTracesRequest,
    ) -> eventbridge_20200401_models.QueryEventTracesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_event_traces_with_options_async(request, runtime)

    def query_traced_event_by_event_id_with_options(
        self,
        request: eventbridge_20200401_models.QueryTracedEventByEventIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryTracedEventByEventIdResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_traced_event_by_event_id_with_options(request, runtime)

    async def query_traced_event_by_event_id_async(
        self,
        request: eventbridge_20200401_models.QueryTracedEventByEventIdRequest,
    ) -> eventbridge_20200401_models.QueryTracedEventByEventIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_traced_event_by_event_id_with_options_async(request, runtime)

    def query_traced_events_with_options(
        self,
        request: eventbridge_20200401_models.QueryTracedEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.QueryTracedEventsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_traced_events_with_options(request, runtime)

    async def query_traced_events_async(
        self,
        request: eventbridge_20200401_models.QueryTracedEventsRequest,
    ) -> eventbridge_20200401_models.QueryTracedEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_traced_events_with_options_async(request, runtime)

    def refund_with_options(
        self,
        request: eventbridge_20200401_models.RefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.RefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Refund',
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
            eventbridge_20200401_models.RefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_with_options_async(
        self,
        request: eventbridge_20200401_models.RefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.RefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Refund',
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
            eventbridge_20200401_models.RefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund(
        self,
        request: eventbridge_20200401_models.RefundRequest,
    ) -> eventbridge_20200401_models.RefundResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_with_options(request, runtime)

    async def refund_async(
        self,
        request: eventbridge_20200401_models.RefundRequest,
    ) -> eventbridge_20200401_models.RefundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_with_options_async(request, runtime)

    def save_and_publish_source_task_with_options(
        self,
        tmp_req: eventbridge_20200401_models.SaveAndPublishSourceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.SaveAndPublishSourceTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.SaveAndPublishSourceTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_config):
            request.source_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_config, 'SourceConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.bus_name):
            body['BusName'] = request.bus_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source_config_shrink):
            body['SourceConfig'] = request.source_config_shrink
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAndPublishSourceTask',
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
            eventbridge_20200401_models.SaveAndPublishSourceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_and_publish_source_task_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.SaveAndPublishSourceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.SaveAndPublishSourceTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.SaveAndPublishSourceTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_config):
            request.source_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_config, 'SourceConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.bus_name):
            body['BusName'] = request.bus_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source_config_shrink):
            body['SourceConfig'] = request.source_config_shrink
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAndPublishSourceTask',
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
            eventbridge_20200401_models.SaveAndPublishSourceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_and_publish_source_task(
        self,
        request: eventbridge_20200401_models.SaveAndPublishSourceTaskRequest,
    ) -> eventbridge_20200401_models.SaveAndPublishSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_and_publish_source_task_with_options(request, runtime)

    async def save_and_publish_source_task_async(
        self,
        request: eventbridge_20200401_models.SaveAndPublishSourceTaskRequest,
    ) -> eventbridge_20200401_models.SaveAndPublishSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_and_publish_source_task_with_options_async(request, runtime)

    def save_and_start_event_streaming_with_options(
        self,
        tmp_req: eventbridge_20200401_models.SaveAndStartEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.SaveAndStartEventStreamingResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.SaveAndStartEventStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ebevent_source_entry):
            request.ebevent_source_entry_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ebevent_source_entry, 'EBEventSourceEntry', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.ebevent_source_entry_shrink):
            body['EBEventSourceEntry'] = request.ebevent_source_entry_shrink
        if not UtilClient.is_unset(request.filter_pattern):
            body['FilterPattern'] = request.filter_pattern
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        body_flat = {}
        if not UtilClient.is_unset(request.targets):
            body_flat['Targets'] = request.targets
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAndStartEventStreaming',
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
            eventbridge_20200401_models.SaveAndStartEventStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_and_start_event_streaming_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.SaveAndStartEventStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.SaveAndStartEventStreamingResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.SaveAndStartEventStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ebevent_source_entry):
            request.ebevent_source_entry_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ebevent_source_entry, 'EBEventSourceEntry', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.ebevent_source_entry_shrink):
            body['EBEventSourceEntry'] = request.ebevent_source_entry_shrink
        if not UtilClient.is_unset(request.filter_pattern):
            body['FilterPattern'] = request.filter_pattern
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        body_flat = {}
        if not UtilClient.is_unset(request.targets):
            body_flat['Targets'] = request.targets
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAndStartEventStreaming',
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
            eventbridge_20200401_models.SaveAndStartEventStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_and_start_event_streaming(
        self,
        request: eventbridge_20200401_models.SaveAndStartEventStreamingRequest,
    ) -> eventbridge_20200401_models.SaveAndStartEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_and_start_event_streaming_with_options(request, runtime)

    async def save_and_start_event_streaming_async(
        self,
        request: eventbridge_20200401_models.SaveAndStartEventStreamingRequest,
    ) -> eventbridge_20200401_models.SaveAndStartEventStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_and_start_event_streaming_with_options_async(request, runtime)

    def save_and_start_source_task_with_options(
        self,
        tmp_req: eventbridge_20200401_models.SaveAndStartSourceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.SaveAndStartSourceTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.SaveAndStartSourceTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_config):
            request.source_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_config, 'SourceConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.bus_name):
            body['BusName'] = request.bus_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source_config_shrink):
            body['SourceConfig'] = request.source_config_shrink
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAndStartSourceTask',
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
            eventbridge_20200401_models.SaveAndStartSourceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_and_start_source_task_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.SaveAndStartSourceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.SaveAndStartSourceTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.SaveAndStartSourceTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_config):
            request.source_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_config, 'SourceConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.bus_name):
            body['BusName'] = request.bus_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source_config_shrink):
            body['SourceConfig'] = request.source_config_shrink
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAndStartSourceTask',
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
            eventbridge_20200401_models.SaveAndStartSourceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_and_start_source_task(
        self,
        request: eventbridge_20200401_models.SaveAndStartSourceTaskRequest,
    ) -> eventbridge_20200401_models.SaveAndStartSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_and_start_source_task_with_options(request, runtime)

    async def save_and_start_source_task_async(
        self,
        request: eventbridge_20200401_models.SaveAndStartSourceTaskRequest,
    ) -> eventbridge_20200401_models.SaveAndStartSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_and_start_source_task_with_options_async(request, runtime)

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

    def start_source_task_with_options(
        self,
        request: eventbridge_20200401_models.StartSourceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.StartSourceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSourceTask',
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
            eventbridge_20200401_models.StartSourceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_source_task_with_options_async(
        self,
        request: eventbridge_20200401_models.StartSourceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.StartSourceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSourceTask',
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
            eventbridge_20200401_models.StartSourceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_source_task(
        self,
        request: eventbridge_20200401_models.StartSourceTaskRequest,
    ) -> eventbridge_20200401_models.StartSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_source_task_with_options(request, runtime)

    async def start_source_task_async(
        self,
        request: eventbridge_20200401_models.StartSourceTaskRequest,
    ) -> eventbridge_20200401_models.StartSourceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_source_task_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(tmp_req.external_source_config):
            request.external_source_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_source_config, 'ExternalSourceConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.external_source_config_shrink):
            body['ExternalSourceConfig'] = request.external_source_config_shrink
        if not UtilClient.is_unset(request.external_source_type):
            body['ExternalSourceType'] = request.external_source_type
        if not UtilClient.is_unset(request.linked_external_source):
            body['LinkedExternalSource'] = request.linked_external_source
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
        if not UtilClient.is_unset(tmp_req.external_source_config):
            request.external_source_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_source_config, 'ExternalSourceConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_source_name):
            body['EventSourceName'] = request.event_source_name
        if not UtilClient.is_unset(request.external_source_config_shrink):
            body['ExternalSourceConfig'] = request.external_source_config_shrink
        if not UtilClient.is_unset(request.external_source_type):
            body['ExternalSourceType'] = request.external_source_type
        if not UtilClient.is_unset(request.linked_external_source):
            body['LinkedExternalSource'] = request.linked_external_source
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
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
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
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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

    def update_schema_with_options(
        self,
        request: eventbridge_20200401_models.UpdateSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compatible_type):
            query['CompatibleType'] = request.compatible_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSchema',
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
            eventbridge_20200401_models.UpdateSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_schema_with_options_async(
        self,
        request: eventbridge_20200401_models.UpdateSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateSchemaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compatible_type):
            query['CompatibleType'] = request.compatible_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSchema',
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
            eventbridge_20200401_models.UpdateSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_schema(
        self,
        request: eventbridge_20200401_models.UpdateSchemaRequest,
    ) -> eventbridge_20200401_models.UpdateSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_schema_with_options(request, runtime)

    async def update_schema_async(
        self,
        request: eventbridge_20200401_models.UpdateSchemaRequest,
    ) -> eventbridge_20200401_models.UpdateSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_schema_with_options_async(request, runtime)

    def update_schema_group_with_options(
        self,
        request: eventbridge_20200401_models.UpdateSchemaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateSchemaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSchemaGroup',
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
            eventbridge_20200401_models.UpdateSchemaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_schema_group_with_options_async(
        self,
        request: eventbridge_20200401_models.UpdateSchemaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateSchemaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSchemaGroup',
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
            eventbridge_20200401_models.UpdateSchemaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_schema_group(
        self,
        request: eventbridge_20200401_models.UpdateSchemaGroupRequest,
    ) -> eventbridge_20200401_models.UpdateSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_schema_group_with_options(request, runtime)

    async def update_schema_group_async(
        self,
        request: eventbridge_20200401_models.UpdateSchemaGroupRequest,
    ) -> eventbridge_20200401_models.UpdateSchemaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_schema_group_with_options_async(request, runtime)

    def update_schema_version_with_options(
        self,
        request: eventbridge_20200401_models.UpdateSchemaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateSchemaVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.version_number):
            query['VersionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSchemaVersion',
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
            eventbridge_20200401_models.UpdateSchemaVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_schema_version_with_options_async(
        self,
        request: eventbridge_20200401_models.UpdateSchemaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateSchemaVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.version_number):
            query['VersionNumber'] = request.version_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSchemaVersion',
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
            eventbridge_20200401_models.UpdateSchemaVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_schema_version(
        self,
        request: eventbridge_20200401_models.UpdateSchemaVersionRequest,
    ) -> eventbridge_20200401_models.UpdateSchemaVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_schema_version_with_options(request, runtime)

    async def update_schema_version_async(
        self,
        request: eventbridge_20200401_models.UpdateSchemaVersionRequest,
    ) -> eventbridge_20200401_models.UpdateSchemaVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_schema_version_with_options_async(request, runtime)

    def update_targets_with_options(
        self,
        tmp_req: eventbridge_20200401_models.UpdateTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateTargetsResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateTargetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='UpdateTargets',
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
            eventbridge_20200401_models.UpdateTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_targets_with_options_async(
        self,
        tmp_req: eventbridge_20200401_models.UpdateTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.UpdateTargetsResponse:
        UtilClient.validate_model(tmp_req)
        request = eventbridge_20200401_models.UpdateTargetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='UpdateTargets',
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
            eventbridge_20200401_models.UpdateTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_targets(
        self,
        request: eventbridge_20200401_models.UpdateTargetsRequest,
    ) -> eventbridge_20200401_models.UpdateTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_targets_with_options(request, runtime)

    async def update_targets_async(
        self,
        request: eventbridge_20200401_models.UpdateTargetsRequest,
    ) -> eventbridge_20200401_models.UpdateTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_targets_with_options_async(request, runtime)

    def verify_with_options(
        self,
        request: eventbridge_20200401_models.VerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.VerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Verify',
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
            eventbridge_20200401_models.VerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_with_options_async(
        self,
        request: eventbridge_20200401_models.VerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eventbridge_20200401_models.VerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Verify',
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
            eventbridge_20200401_models.VerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify(
        self,
        request: eventbridge_20200401_models.VerifyRequest,
    ) -> eventbridge_20200401_models.VerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_with_options(request, runtime)

    async def verify_async(
        self,
        request: eventbridge_20200401_models.VerifyRequest,
    ) -> eventbridge_20200401_models.VerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_with_options_async(request, runtime)
