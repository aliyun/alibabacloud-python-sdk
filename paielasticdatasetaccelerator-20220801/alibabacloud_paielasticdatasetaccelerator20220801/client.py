# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paielasticdatasetaccelerator20220801 import models as paielastic_dataset_accelerator_20220801_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_endpoint(
        self,
        endpoint_id: str,
        slot_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.BindEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_endpoint_with_options(endpoint_id, slot_id, headers, runtime)

    async def bind_endpoint_async(
        self,
        endpoint_id: str,
        slot_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.BindEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.bind_endpoint_with_options_async(endpoint_id, slot_id, headers, runtime)

    def bind_endpoint_with_options(
        self,
        endpoint_id: str,
        slot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.BindEndpointResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='BindEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/endpoints/{OpenApiUtilClient.get_encode_param(endpoint_id)}/slots/{OpenApiUtilClient.get_encode_param(slot_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.BindEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_endpoint_with_options_async(
        self,
        endpoint_id: str,
        slot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.BindEndpointResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='BindEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/endpoints/{OpenApiUtilClient.get_encode_param(endpoint_id)}/slots/{OpenApiUtilClient.get_encode_param(slot_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.BindEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_endpoint(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateEndpointRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_endpoint_with_options(request, headers, runtime)

    async def create_endpoint_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateEndpointRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_endpoint_with_options_async(request, headers, runtime)

    def create_endpoint_with_options(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateEndpointResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/endpoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_endpoint_with_options_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateEndpointResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/endpoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateInstanceRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateInstanceRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_instance_with_options(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.capacity):
            body['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.max_slot):
            body['MaxSlot'] = request.max_slot
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.capacity):
            body['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.max_slot):
            body['MaxSlot'] = request.max_slot
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_slot(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateSlotRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateSlotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_slot_with_options(request, headers, runtime)

    async def create_slot_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateSlotRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateSlotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_slot_with_options_async(request, headers, runtime)

    def create_slot_with_options(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateSlotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateSlotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.capacity):
            body['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint_ids):
            body['EndpointIds'] = request.endpoint_ids
        if not UtilClient.is_unset(request.endpoints):
            body['Endpoints'] = request.endpoints
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.life_cycle):
            body['LifeCycle'] = request.life_cycle
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.storage_type):
            body['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.storage_uri):
            body['StorageUri'] = request.storage_uri
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_slot_with_options_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateSlotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateSlotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.capacity):
            body['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint_ids):
            body['EndpointIds'] = request.endpoint_ids
        if not UtilClient.is_unset(request.endpoints):
            body['Endpoints'] = request.endpoints
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.life_cycle):
            body['LifeCycle'] = request.life_cycle
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.storage_type):
            body['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.storage_uri):
            body['StorageUri'] = request.storage_uri
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateSlotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateTagRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tag_with_options(request, headers, runtime)

    async def create_tag_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateTagRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_tag_with_options_async(request, headers, runtime)

    def create_tag_with_options(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.CreateTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.CreateTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_slot(
        self,
        slot_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteSlotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_slot_with_options(slot_id, headers, runtime)

    async def delete_slot_async(
        self,
        slot_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteSlotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_slot_with_options_async(slot_id, headers, runtime)

    def delete_slot_with_options(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteSlotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots/{OpenApiUtilClient.get_encode_param(slot_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DeleteSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_slot_with_options_async(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteSlotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots/{OpenApiUtilClient.get_encode_param(slot_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DeleteSlotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag(
        self,
        request: paielastic_dataset_accelerator_20220801_models.DeleteTagRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_tag_with_options(request, headers, runtime)

    async def delete_tag_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.DeleteTagRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_tag_with_options_async(request, headers, runtime)

    def delete_tag_with_options(
        self,
        request: paielastic_dataset_accelerator_20220801_models.DeleteTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.DeleteTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DeleteTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component(
        self,
        component_id: str,
        request: paielastic_dataset_accelerator_20220801_models.DescribeComponentRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_component_with_options(component_id, request, headers, runtime)

    async def describe_component_async(
        self,
        component_id: str,
        request: paielastic_dataset_accelerator_20220801_models.DescribeComponentRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeComponentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_component_with_options_async(component_id, request, headers, runtime)

    def describe_component_with_options(
        self,
        component_id: str,
        tmp_req: paielastic_dataset_accelerator_20220801_models.DescribeComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeComponentResponse:
        UtilClient.validate_model(tmp_req)
        request = paielastic_dataset_accelerator_20220801_models.DescribeComponentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.values):
            request.values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        if not UtilClient.is_unset(request.render_template):
            query['RenderTemplate'] = request.render_template
        if not UtilClient.is_unset(request.values_shrink):
            query['Values'] = request.values_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponent',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/components/{OpenApiUtilClient.get_encode_param(component_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_with_options_async(
        self,
        component_id: str,
        tmp_req: paielastic_dataset_accelerator_20220801_models.DescribeComponentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeComponentResponse:
        UtilClient.validate_model(tmp_req)
        request = paielastic_dataset_accelerator_20220801_models.DescribeComponentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.values):
            request.values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        if not UtilClient.is_unset(request.render_template):
            query['RenderTemplate'] = request.render_template
        if not UtilClient.is_unset(request.values_shrink):
            query['Values'] = request.values_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponent',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/components/{OpenApiUtilClient.get_encode_param(component_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_endpoint(
        self,
        endpoint_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_endpoint_with_options(endpoint_id, headers, runtime)

    async def describe_endpoint_async(
        self,
        endpoint_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_endpoint_with_options_async(endpoint_id, headers, runtime)

    def describe_endpoint_with_options(
        self,
        endpoint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeEndpointResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/endpoints/{OpenApiUtilClient.get_encode_param(endpoint_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_endpoint_with_options_async(
        self,
        endpoint_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeEndpointResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/endpoints/{OpenApiUtilClient.get_encode_param(endpoint_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        instance_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_with_options(instance_id, headers, runtime)

    async def describe_instance_async(
        self,
        instance_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instance_with_options_async(instance_id, headers, runtime)

    def describe_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slot(
        self,
        slot_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeSlotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_slot_with_options(slot_id, headers, runtime)

    async def describe_slot_async(
        self,
        slot_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeSlotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_slot_with_options_async(slot_id, headers, runtime)

    def describe_slot_with_options(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeSlotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots/{OpenApiUtilClient.get_encode_param(slot_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slot_with_options_async(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.DescribeSlotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots/{OpenApiUtilClient.get_encode_param(slot_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeSlotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListComponentsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_components_with_options(request, headers, runtime)

    async def list_components_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListComponentsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_components_with_options_async(request, headers, runtime)

    def list_components_with_options(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.ListComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.ListComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_endpoints(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListEndpointsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.ListEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_endpoints_with_options(request, headers, runtime)

    async def list_endpoints_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListEndpointsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.ListEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_endpoints_with_options_async(request, headers, runtime)

    def list_endpoints_with_options(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListEndpointsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.ListEndpointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_ids):
            query['EndpointIds'] = request.endpoint_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.slot_ids):
            query['SlotIds'] = request.slot_ids
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEndpoints',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/endpoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_endpoints_with_options_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListEndpointsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.ListEndpointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_ids):
            query['EndpointIds'] = request.endpoint_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.slot_ids):
            query['SlotIds'] = request.slot_ids
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEndpoints',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/endpoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListInstancesRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListInstancesRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_slots(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListSlotsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.ListSlotsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_slots_with_options(request, headers, runtime)

    async def list_slots_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListSlotsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.ListSlotsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_slots_with_options_async(request, headers, runtime)

    def list_slots_with_options(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListSlotsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.ListSlotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.slot_ids):
            query['SlotIds'] = request.slot_ids
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSlots',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListSlotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_slots_with_options_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListSlotsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.ListSlotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.slot_ids):
            query['SlotIds'] = request.slot_ids
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSlots',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListSlotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListTagsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tags_with_options(request, headers, runtime)

    async def list_tags_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListTagsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tags_with_options_async(request, headers, runtime)

    def list_tags_with_options(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.ListTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.ListTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_metrics(
        self,
        instance_id: str,
        request: paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_instance_metrics_with_options(instance_id, request, headers, runtime)

    async def query_instance_metrics_async(
        self,
        instance_id: str,
        request: paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_instance_metrics_with_options_async(instance_id, request, headers, runtime)

    def query_instance_metrics_with_options(
        self,
        instance_id: str,
        tmp_req: paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dimensions):
            request.dimensions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not UtilClient.is_unset(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceMetrics',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/metrics/action/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_metrics_with_options_async(
        self,
        instance_id: str,
        tmp_req: paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dimensions):
            request.dimensions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not UtilClient.is_unset(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceMetrics',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/metrics/action/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_slot_metrics(
        self,
        slot_id: str,
        request: paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_slot_metrics_with_options(slot_id, request, headers, runtime)

    async def query_slot_metrics_async(
        self,
        slot_id: str,
        request: paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_slot_metrics_with_options_async(slot_id, request, headers, runtime)

    def query_slot_metrics_with_options(
        self,
        slot_id: str,
        tmp_req: paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dimensions):
            request.dimensions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not UtilClient.is_unset(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySlotMetrics',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots/{OpenApiUtilClient.get_encode_param(slot_id)}/metrics/action/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_slot_metrics_with_options_async(
        self,
        slot_id: str,
        tmp_req: paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dimensions):
            request.dimensions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not UtilClient.is_unset(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySlotMetrics',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots/{OpenApiUtilClient.get_encode_param(slot_id)}/metrics/action/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_statistic(
        self,
        request: paielastic_dataset_accelerator_20220801_models.QueryStatisticRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.QueryStatisticResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_statistic_with_options(request, headers, runtime)

    async def query_statistic_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.QueryStatisticRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.QueryStatisticResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_statistic_with_options_async(request, headers, runtime)

    def query_statistic_with_options(
        self,
        request: paielastic_dataset_accelerator_20220801_models.QueryStatisticRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.QueryStatisticResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStatistic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/action/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.QueryStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_statistic_with_options_async(
        self,
        request: paielastic_dataset_accelerator_20220801_models.QueryStatisticRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.QueryStatisticResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStatistic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/action/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.QueryStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_slot(
        self,
        slot_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.StopSlotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_slot_with_options(slot_id, headers, runtime)

    async def stop_slot_async(
        self,
        slot_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.StopSlotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_slot_with_options_async(slot_id, headers, runtime)

    def stop_slot_with_options(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.StopSlotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots/{OpenApiUtilClient.get_encode_param(slot_id)}/action/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.StopSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_slot_with_options_async(
        self,
        slot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.StopSlotResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots/{OpenApiUtilClient.get_encode_param(slot_id)}/action/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.StopSlotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_endpoint(
        self,
        endpoint_id: str,
        slot_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.UnbindEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_endpoint_with_options(endpoint_id, slot_id, headers, runtime)

    async def unbind_endpoint_async(
        self,
        endpoint_id: str,
        slot_id: str,
    ) -> paielastic_dataset_accelerator_20220801_models.UnbindEndpointResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.unbind_endpoint_with_options_async(endpoint_id, slot_id, headers, runtime)

    def unbind_endpoint_with_options(
        self,
        endpoint_id: str,
        slot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.UnbindEndpointResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnbindEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/endpoints/{OpenApiUtilClient.get_encode_param(endpoint_id)}/slots/{OpenApiUtilClient.get_encode_param(slot_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.UnbindEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_endpoint_with_options_async(
        self,
        endpoint_id: str,
        slot_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.UnbindEndpointResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnbindEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/endpoints/{OpenApiUtilClient.get_encode_param(endpoint_id)}/slots/{OpenApiUtilClient.get_encode_param(slot_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.UnbindEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        instance_id: str,
        request: paielastic_dataset_accelerator_20220801_models.UpdateInstanceRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    async def update_instance_async(
        self,
        instance_id: str,
        request: paielastic_dataset_accelerator_20220801_models.UpdateInstanceRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)

    def update_instance_with_options(
        self,
        instance_id: str,
        request: paielastic_dataset_accelerator_20220801_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.max_slot):
            body['MaxSlot'] = request.max_slot
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        instance_id: str,
        request: paielastic_dataset_accelerator_20220801_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.max_slot):
            body['MaxSlot'] = request.max_slot
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_slot(
        self,
        slot_id: str,
        request: paielastic_dataset_accelerator_20220801_models.UpdateSlotRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.UpdateSlotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_slot_with_options(slot_id, request, headers, runtime)

    async def update_slot_async(
        self,
        slot_id: str,
        request: paielastic_dataset_accelerator_20220801_models.UpdateSlotRequest,
    ) -> paielastic_dataset_accelerator_20220801_models.UpdateSlotResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_slot_with_options_async(slot_id, request, headers, runtime)

    def update_slot_with_options(
        self,
        slot_id: str,
        request: paielastic_dataset_accelerator_20220801_models.UpdateSlotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.UpdateSlotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.capacity):
            body['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.life_cycle):
            body['LifeCycle'] = request.life_cycle
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.storage_type):
            body['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.storage_uri):
            body['StorageUri'] = request.storage_uri
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots/{OpenApiUtilClient.get_encode_param(slot_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.UpdateSlotResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_slot_with_options_async(
        self,
        slot_id: str,
        request: paielastic_dataset_accelerator_20220801_models.UpdateSlotRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paielastic_dataset_accelerator_20220801_models.UpdateSlotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.capacity):
            body['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.life_cycle):
            body['LifeCycle'] = request.life_cycle
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.storage_type):
            body['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.storage_uri):
            body['StorageUri'] = request.storage_uri
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname=f'/api/v1/slots/{OpenApiUtilClient.get_encode_param(slot_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.UpdateSlotResponse(),
            await self.call_api_async(params, req, runtime)
        )
