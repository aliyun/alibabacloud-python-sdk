# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hologram20220601 import models as hologram_20220601_models
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
        self._endpoint = self.get_endpoint('hologram', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_instance_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
        request: hologram_20220601_models.GetInstanceRequest,
    ) -> hologram_20220601_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, request, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.GetInstanceRequest,
    ) -> hologram_20220601_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        request: hologram_20220601_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: hologram_20220601_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: hologram_20220601_models.ListInstancesRequest,
    ) -> hologram_20220601_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: hologram_20220601_models.ListInstancesRequest,
    ) -> hologram_20220601_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def restart_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RestartInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/restart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.RestartInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/restart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_instance_with_options(instance_id, headers, runtime)

    async def restart_instance_async(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_instance_with_options_async(instance_id, headers, runtime)

    def resume_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ResumeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ResumeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.ResumeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ResumeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_instance(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.ResumeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_instance_with_options(instance_id, headers, runtime)

    async def resume_instance_async(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.ResumeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_instance_with_options_async(instance_id, headers, runtime)

    def stop_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.StopInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.StopInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_instance_with_options(instance_id, headers, runtime)

    async def stop_instance_async(
        self,
        instance_id: str,
    ) -> hologram_20220601_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_instance_with_options_async(instance_id, headers, runtime)

    def update_instance_name_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.UpdateInstanceNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/instanceName',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.UpdateInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_name_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.UpdateInstanceNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/instanceName',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.UpdateInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_name(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNameRequest,
    ) -> hologram_20220601_models.UpdateInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_name_with_options(instance_id, request, headers, runtime)

    async def update_instance_name_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNameRequest,
    ) -> hologram_20220601_models.UpdateInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_name_with_options_async(instance_id, request, headers, runtime)

    def update_instance_network_type_with_options(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNetworkTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.UpdateInstanceNetworkTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.any_tunnel_to_single_tunnel):
            body['anyTunnelToSingleTunnel'] = request.any_tunnel_to_single_tunnel
        if not UtilClient.is_unset(request.network_types):
            body['networkTypes'] = request.network_types
        if not UtilClient.is_unset(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_owner_id):
            body['vpcOwnerId'] = request.vpc_owner_id
        if not UtilClient.is_unset(request.vpc_region_id):
            body['vpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceNetworkType',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/network',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.UpdateInstanceNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_network_type_with_options_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNetworkTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hologram_20220601_models.UpdateInstanceNetworkTypeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.any_tunnel_to_single_tunnel):
            body['anyTunnelToSingleTunnel'] = request.any_tunnel_to_single_tunnel
        if not UtilClient.is_unset(request.network_types):
            body['networkTypes'] = request.network_types
        if not UtilClient.is_unset(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_owner_id):
            body['vpcOwnerId'] = request.vpc_owner_id
        if not UtilClient.is_unset(request.vpc_region_id):
            body['vpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceNetworkType',
            version='2022-06-01',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/network',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.UpdateInstanceNetworkTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_network_type(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNetworkTypeRequest,
    ) -> hologram_20220601_models.UpdateInstanceNetworkTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_network_type_with_options(instance_id, request, headers, runtime)

    async def update_instance_network_type_async(
        self,
        instance_id: str,
        request: hologram_20220601_models.UpdateInstanceNetworkTypeRequest,
    ) -> hologram_20220601_models.UpdateInstanceNetworkTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_network_type_with_options_async(instance_id, request, headers, runtime)
