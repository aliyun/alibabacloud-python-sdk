# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_paielasticdatasetaccelerator20220801 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        self._endpoint = self.get_endpoint('paielasticdatasetaccelerator', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bind_endpoint_with_options(
        self,
        endpoint_id: str,
        slot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'BindEndpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints/{DaraURL.percent_encode(endpoint_id)}/slots/{DaraURL.percent_encode(slot_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_endpoint_with_options_async(
        self,
        endpoint_id: str,
        slot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'BindEndpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints/{DaraURL.percent_encode(endpoint_id)}/slots/{DaraURL.percent_encode(slot_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_endpoint(
        self,
        endpoint_id: str,
        slot_id: str,
    ) -> main_models.BindEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.bind_endpoint_with_options(endpoint_id, slot_id, headers, runtime)

    async def bind_endpoint_async(
        self,
        endpoint_id: str,
        slot_id: str,
    ) -> main_models.BindEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.bind_endpoint_with_options_async(endpoint_id, slot_id, headers, runtime)

    def create_endpoint_with_options(
        self,
        request: main_models.CreateEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEndpointResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEndpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_endpoint_with_options_async(
        self,
        request: main_models.CreateEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEndpointResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEndpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_endpoint(
        self,
        request: main_models.CreateEndpointRequest,
    ) -> main_models.CreateEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_endpoint_with_options(request, headers, runtime)

    async def create_endpoint_async(
        self,
        request: main_models.CreateEndpointRequest,
    ) -> main_models.CreateEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_endpoint_with_options_async(request, headers, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.capacity):
            body['Capacity'] = request.capacity
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.max_endpoint):
            body['MaxEndpoint'] = request.max_endpoint
        if not DaraCore.is_null(request.max_slot):
            body['MaxSlot'] = request.max_slot
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.provider_type):
            body['ProviderType'] = request.provider_type
        if not DaraCore.is_null(request.storage_type):
            body['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.capacity):
            body['Capacity'] = request.capacity
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.max_endpoint):
            body['MaxEndpoint'] = request.max_endpoint
        if not DaraCore.is_null(request.max_slot):
            body['MaxSlot'] = request.max_slot
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.provider_type):
            body['ProviderType'] = request.provider_type
        if not DaraCore.is_null(request.storage_type):
            body['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_slot_with_options(
        self,
        request: main_models.CreateSlotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSlotResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.capacity):
            body['Capacity'] = request.capacity
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_ids):
            body['EndpointIds'] = request.endpoint_ids
        if not DaraCore.is_null(request.endpoints):
            body['Endpoints'] = request.endpoints
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.io_type):
            body['IoType'] = request.io_type
        if not DaraCore.is_null(request.life_cycle):
            body['LifeCycle'] = request.life_cycle
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.storage_type):
            body['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.storage_uri):
            body['StorageUri'] = request.storage_uri
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_slot_with_options_async(
        self,
        request: main_models.CreateSlotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSlotResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.capacity):
            body['Capacity'] = request.capacity
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_ids):
            body['EndpointIds'] = request.endpoint_ids
        if not DaraCore.is_null(request.endpoints):
            body['Endpoints'] = request.endpoints
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.io_type):
            body['IoType'] = request.io_type
        if not DaraCore.is_null(request.life_cycle):
            body['LifeCycle'] = request.life_cycle
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.storage_type):
            body['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.storage_uri):
            body['StorageUri'] = request.storage_uri
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSlotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_slot(
        self,
        request: main_models.CreateSlotRequest,
    ) -> main_models.CreateSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_slot_with_options(request, headers, runtime)

    async def create_slot_async(
        self,
        request: main_models.CreateSlotRequest,
    ) -> main_models.CreateSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_slot_with_options_async(request, headers, runtime)

    def create_slots_with_options(
        self,
        request: main_models.CreateSlotsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSlotsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.slots):
            body['Slots'] = request.slots
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSlots',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/batch/slots/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSlotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_slots_with_options_async(
        self,
        request: main_models.CreateSlotsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSlotsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.slots):
            body['Slots'] = request.slots
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSlots',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/batch/slots/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSlotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_slots(
        self,
        request: main_models.CreateSlotsRequest,
    ) -> main_models.CreateSlotsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_slots_with_options(request, headers, runtime)

    async def create_slots_async(
        self,
        request: main_models.CreateSlotsRequest,
    ) -> main_models.CreateSlotsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_slots_with_options_async(request, headers, runtime)

    def create_tag_with_options(
        self,
        request: main_models.CreateTagRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.key):
            body['Key'] = request.key
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTag',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: main_models.CreateTagRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.key):
            body['Key'] = request.key
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTag',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag(
        self,
        request: main_models.CreateTagRequest,
    ) -> main_models.CreateTagResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_tag_with_options(request, headers, runtime)

    async def create_tag_async(
        self,
        request: main_models.CreateTagRequest,
    ) -> main_models.CreateTagResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_tag_with_options_async(request, headers, runtime)

    def delete_endpoint_with_options(
        self,
        endpoint_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEndpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints/{DaraURL.percent_encode(endpoint_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_endpoint_with_options_async(
        self,
        endpoint_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEndpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints/{DaraURL.percent_encode(endpoint_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_endpoint(
        self,
        endpoint_id: str,
    ) -> main_models.DeleteEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_endpoint_with_options(endpoint_id, headers, runtime)

    async def delete_endpoint_async(
        self,
        endpoint_id: str,
    ) -> main_models.DeleteEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_endpoint_with_options_async(endpoint_id, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, headers, runtime)

    def delete_slot_with_options(
        self,
        slot_id: str,
        request: main_models.DeleteSlotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSlotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_slot_with_options_async(
        self,
        slot_id: str,
        request: main_models.DeleteSlotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSlotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSlotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_slot(
        self,
        slot_id: str,
        request: main_models.DeleteSlotRequest,
    ) -> main_models.DeleteSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_slot_with_options(slot_id, request, headers, runtime)

    async def delete_slot_async(
        self,
        slot_id: str,
        request: main_models.DeleteSlotRequest,
    ) -> main_models.DeleteSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_slot_with_options_async(slot_id, request, headers, runtime)

    def delete_tag_with_options(
        self,
        request: main_models.DeleteTagRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTag',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: main_models.DeleteTagRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTag',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag(
        self,
        request: main_models.DeleteTagRequest,
    ) -> main_models.DeleteTagResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_tag_with_options(request, headers, runtime)

    async def delete_tag_async(
        self,
        request: main_models.DeleteTagRequest,
    ) -> main_models.DeleteTagResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_tag_with_options_async(request, headers, runtime)

    def describe_component_with_options(
        self,
        component_id: str,
        tmp_req: main_models.DescribeComponentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentResponse:
        tmp_req.validate()
        request = main_models.DescribeComponentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.values):
            request.values_shrink = Utils.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        if not DaraCore.is_null(request.render_template):
            query['RenderTemplate'] = request.render_template
        if not DaraCore.is_null(request.values_shrink):
            query['Values'] = request.values_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponent',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/components/{DaraURL.percent_encode(component_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_with_options_async(
        self,
        component_id: str,
        tmp_req: main_models.DescribeComponentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentResponse:
        tmp_req.validate()
        request = main_models.DescribeComponentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.values):
            request.values_shrink = Utils.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        if not DaraCore.is_null(request.render_template):
            query['RenderTemplate'] = request.render_template
        if not DaraCore.is_null(request.values_shrink):
            query['Values'] = request.values_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponent',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/components/{DaraURL.percent_encode(component_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component(
        self,
        component_id: str,
        request: main_models.DescribeComponentRequest,
    ) -> main_models.DescribeComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_component_with_options(component_id, request, headers, runtime)

    async def describe_component_async(
        self,
        component_id: str,
        request: main_models.DescribeComponentRequest,
    ) -> main_models.DescribeComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_component_with_options_async(component_id, request, headers, runtime)

    def describe_endpoint_with_options(
        self,
        endpoint_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints/{DaraURL.percent_encode(endpoint_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_endpoint_with_options_async(
        self,
        endpoint_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints/{DaraURL.percent_encode(endpoint_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_endpoint(
        self,
        endpoint_id: str,
    ) -> main_models.DescribeEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_endpoint_with_options(endpoint_id, headers, runtime)

    async def describe_endpoint_async(
        self,
        endpoint_id: str,
    ) -> main_models.DescribeEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_endpoint_with_options_async(endpoint_id, headers, runtime)

    def describe_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        instance_id: str,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_instance_with_options(instance_id, headers, runtime)

    async def describe_instance_async(
        self,
        instance_id: str,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_instance_with_options_async(instance_id, headers, runtime)

    def describe_slot_with_options(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slot_with_options_async(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slot(
        self,
        slot_id: str,
    ) -> main_models.DescribeSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_slot_with_options(slot_id, headers, runtime)

    async def describe_slot_async(
        self,
        slot_id: str,
    ) -> main_models.DescribeSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_slot_with_options_async(slot_id, headers, runtime)

    def list_components_with_options(
        self,
        request: main_models.ListComponentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponents',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/components',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: main_models.ListComponentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponents',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/components',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(
        self,
        request: main_models.ListComponentsRequest,
    ) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_components_with_options(request, headers, runtime)

    async def list_components_async(
        self,
        request: main_models.ListComponentsRequest,
    ) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_components_with_options_async(request, headers, runtime)

    def list_endpoints_with_options(
        self,
        request: main_models.ListEndpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_ids):
            query['EndpointIds'] = request.endpoint_ids
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.slot_ids):
            query['SlotIds'] = request.slot_ids
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEndpoints',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_endpoints_with_options_async(
        self,
        request: main_models.ListEndpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_ids):
            query['EndpointIds'] = request.endpoint_ids
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.slot_ids):
            query['SlotIds'] = request.slot_ids
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEndpoints',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_endpoints(
        self,
        request: main_models.ListEndpointsRequest,
    ) -> main_models.ListEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_endpoints_with_options(request, headers, runtime)

    async def list_endpoints_async(
        self,
        request: main_models.ListEndpointsRequest,
    ) -> main_models.ListEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_endpoints_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.phase):
            query['Phase'] = request.phase
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.phase):
            query['Phase'] = request.phase
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_slots_with_options(
        self,
        request: main_models.ListSlotsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSlotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_ids):
            query['EndpointIds'] = request.endpoint_ids
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phase):
            query['Phase'] = request.phase
        if not DaraCore.is_null(request.slot_ids):
            query['SlotIds'] = request.slot_ids
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.storage_uri):
            query['StorageUri'] = request.storage_uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSlots',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSlotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_slots_with_options_async(
        self,
        request: main_models.ListSlotsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSlotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_ids):
            query['EndpointIds'] = request.endpoint_ids
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phase):
            query['Phase'] = request.phase
        if not DaraCore.is_null(request.slot_ids):
            query['SlotIds'] = request.slot_ids
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.storage_uri):
            query['StorageUri'] = request.storage_uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSlots',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSlotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_slots(
        self,
        request: main_models.ListSlotsRequest,
    ) -> main_models.ListSlotsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_slots_with_options(request, headers, runtime)

    async def list_slots_async(
        self,
        request: main_models.ListSlotsRequest,
    ) -> main_models.ListSlotsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_slots_with_options_async(request, headers, runtime)

    def list_tags_with_options(
        self,
        request: main_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: main_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tags_with_options(request, headers, runtime)

    async def list_tags_async(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tags_with_options_async(request, headers, runtime)

    def query_instance_metrics_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.QueryInstanceMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceMetricsResponse:
        tmp_req.validate()
        request = main_models.QueryInstanceMetricsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dimensions):
            request.dimensions_shrink = Utils.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not DaraCore.is_null(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstanceMetrics',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/metrics/action/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_metrics_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.QueryInstanceMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceMetricsResponse:
        tmp_req.validate()
        request = main_models.QueryInstanceMetricsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dimensions):
            request.dimensions_shrink = Utils.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not DaraCore.is_null(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstanceMetrics',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/metrics/action/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_metrics(
        self,
        instance_id: str,
        request: main_models.QueryInstanceMetricsRequest,
    ) -> main_models.QueryInstanceMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_instance_metrics_with_options(instance_id, request, headers, runtime)

    async def query_instance_metrics_async(
        self,
        instance_id: str,
        request: main_models.QueryInstanceMetricsRequest,
    ) -> main_models.QueryInstanceMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_instance_metrics_with_options_async(instance_id, request, headers, runtime)

    def query_slot_metrics_with_options(
        self,
        slot_id: str,
        tmp_req: main_models.QuerySlotMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySlotMetricsResponse:
        tmp_req.validate()
        request = main_models.QuerySlotMetricsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dimensions):
            request.dimensions_shrink = Utils.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not DaraCore.is_null(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySlotMetrics',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}/metrics/action/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySlotMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_slot_metrics_with_options_async(
        self,
        slot_id: str,
        tmp_req: main_models.QuerySlotMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySlotMetricsResponse:
        tmp_req.validate()
        request = main_models.QuerySlotMetricsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dimensions):
            request.dimensions_shrink = Utils.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not DaraCore.is_null(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySlotMetrics',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}/metrics/action/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySlotMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_slot_metrics(
        self,
        slot_id: str,
        request: main_models.QuerySlotMetricsRequest,
    ) -> main_models.QuerySlotMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_slot_metrics_with_options(slot_id, request, headers, runtime)

    async def query_slot_metrics_async(
        self,
        slot_id: str,
        request: main_models.QuerySlotMetricsRequest,
    ) -> main_models.QuerySlotMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_slot_metrics_with_options_async(slot_id, request, headers, runtime)

    def query_statistic_with_options(
        self,
        request: main_models.QueryStatisticRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryStatistic',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/statistics/action/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_statistic_with_options_async(
        self,
        request: main_models.QueryStatisticRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryStatistic',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/statistics/action/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_statistic(
        self,
        request: main_models.QueryStatisticRequest,
    ) -> main_models.QueryStatisticResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_statistic_with_options(request, headers, runtime)

    async def query_statistic_async(
        self,
        request: main_models.QueryStatisticRequest,
    ) -> main_models.QueryStatisticResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_statistic_with_options_async(request, headers, runtime)

    def reload_slot_with_options(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReloadSlotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ReloadSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}/action/reload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReloadSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def reload_slot_with_options_async(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReloadSlotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ReloadSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}/action/reload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReloadSlotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reload_slot(
        self,
        slot_id: str,
    ) -> main_models.ReloadSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reload_slot_with_options(slot_id, headers, runtime)

    async def reload_slot_async(
        self,
        slot_id: str,
    ) -> main_models.ReloadSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reload_slot_with_options_async(slot_id, headers, runtime)

    def stop_slot_with_options(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopSlotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_slot_with_options_async(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopSlotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSlotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_slot(
        self,
        slot_id: str,
    ) -> main_models.StopSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_slot_with_options(slot_id, headers, runtime)

    async def stop_slot_async(
        self,
        slot_id: str,
    ) -> main_models.StopSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_slot_with_options_async(slot_id, headers, runtime)

    def unbind_endpoint_with_options(
        self,
        endpoint_id: str,
        slot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UnbindEndpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints/{DaraURL.percent_encode(endpoint_id)}/slots/{DaraURL.percent_encode(slot_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_endpoint_with_options_async(
        self,
        endpoint_id: str,
        slot_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindEndpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UnbindEndpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/endpoints/{DaraURL.percent_encode(endpoint_id)}/slots/{DaraURL.percent_encode(slot_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_endpoint(
        self,
        endpoint_id: str,
        slot_id: str,
    ) -> main_models.UnbindEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.unbind_endpoint_with_options(endpoint_id, slot_id, headers, runtime)

    async def unbind_endpoint_async(
        self,
        endpoint_id: str,
        slot_id: str,
    ) -> main_models.UnbindEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.unbind_endpoint_with_options_async(endpoint_id, slot_id, headers, runtime)

    def update_instance_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.max_slot):
            body['MaxSlot'] = request.max_slot
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.max_slot):
            body['MaxSlot'] = request.max_slot
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    async def update_instance_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)

    def update_slot_with_options(
        self,
        slot_id: str,
        request: main_models.UpdateSlotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSlotResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.capacity):
            body['Capacity'] = request.capacity
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.life_cycle):
            body['LifeCycle'] = request.life_cycle
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.storage_type):
            body['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.storage_uri):
            body['StorageUri'] = request.storage_uri
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_slot_with_options_async(
        self,
        slot_id: str,
        request: main_models.UpdateSlotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSlotResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.capacity):
            body['Capacity'] = request.capacity
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.life_cycle):
            body['LifeCycle'] = request.life_cycle
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.storage_type):
            body['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.storage_uri):
            body['StorageUri'] = request.storage_uri
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSlot',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/slots/{DaraURL.percent_encode(slot_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSlotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_slot(
        self,
        slot_id: str,
        request: main_models.UpdateSlotRequest,
    ) -> main_models.UpdateSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_slot_with_options(slot_id, request, headers, runtime)

    async def update_slot_async(
        self,
        slot_id: str,
        request: main_models.UpdateSlotRequest,
    ) -> main_models.UpdateSlotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_slot_with_options_async(slot_id, request, headers, runtime)
