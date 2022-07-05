# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vpcpeer20220101 import models as vpc_peer_20220101_models
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
        self._endpoint = self.get_endpoint('vpcpeer', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def accept_vpc_peer_connection_with_options(
        self,
        request: vpc_peer_20220101_models.AcceptVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.AcceptVpcPeerConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AcceptVpcPeerConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.AcceptVpcPeerConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_vpc_peer_connection_with_options_async(
        self,
        request: vpc_peer_20220101_models.AcceptVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.AcceptVpcPeerConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AcceptVpcPeerConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.AcceptVpcPeerConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_vpc_peer_connection(
        self,
        request: vpc_peer_20220101_models.AcceptVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.AcceptVpcPeerConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_vpc_peer_connection_with_options(request, runtime)

    async def accept_vpc_peer_connection_async(
        self,
        request: vpc_peer_20220101_models.AcceptVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.AcceptVpcPeerConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_vpc_peer_connection_with_options_async(request, runtime)

    def create_vpc_peer_connection_with_options(
        self,
        request: vpc_peer_20220101_models.CreateVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.CreateVpcPeerConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accepting_ali_uid):
            body['AcceptingAliUid'] = request.accepting_ali_uid
        if not UtilClient.is_unset(request.accepting_region_id):
            body['AcceptingRegionId'] = request.accepting_region_id
        if not UtilClient.is_unset(request.accepting_vpc_id):
            body['AcceptingVpcId'] = request.accepting_vpc_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpcPeerConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.CreateVpcPeerConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_peer_connection_with_options_async(
        self,
        request: vpc_peer_20220101_models.CreateVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.CreateVpcPeerConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accepting_ali_uid):
            body['AcceptingAliUid'] = request.accepting_ali_uid
        if not UtilClient.is_unset(request.accepting_region_id):
            body['AcceptingRegionId'] = request.accepting_region_id
        if not UtilClient.is_unset(request.accepting_vpc_id):
            body['AcceptingVpcId'] = request.accepting_vpc_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpcPeerConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.CreateVpcPeerConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_peer_connection(
        self,
        request: vpc_peer_20220101_models.CreateVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.CreateVpcPeerConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_peer_connection_with_options(request, runtime)

    async def create_vpc_peer_connection_async(
        self,
        request: vpc_peer_20220101_models.CreateVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.CreateVpcPeerConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_peer_connection_with_options_async(request, runtime)

    def delete_vpc_peer_connection_with_options(
        self,
        request: vpc_peer_20220101_models.DeleteVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.DeleteVpcPeerConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpcPeerConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.DeleteVpcPeerConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_peer_connection_with_options_async(
        self,
        request: vpc_peer_20220101_models.DeleteVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.DeleteVpcPeerConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpcPeerConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.DeleteVpcPeerConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_peer_connection(
        self,
        request: vpc_peer_20220101_models.DeleteVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.DeleteVpcPeerConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_peer_connection_with_options(request, runtime)

    async def delete_vpc_peer_connection_async(
        self,
        request: vpc_peer_20220101_models.DeleteVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.DeleteVpcPeerConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_peer_connection_with_options_async(request, runtime)

    def get_vpc_peer_connection_attribute_with_options(
        self,
        request: vpc_peer_20220101_models.GetVpcPeerConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.GetVpcPeerConnectionAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpcPeerConnectionAttribute',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.GetVpcPeerConnectionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpc_peer_connection_attribute_with_options_async(
        self,
        request: vpc_peer_20220101_models.GetVpcPeerConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.GetVpcPeerConnectionAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpcPeerConnectionAttribute',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.GetVpcPeerConnectionAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpc_peer_connection_attribute(
        self,
        request: vpc_peer_20220101_models.GetVpcPeerConnectionAttributeRequest,
    ) -> vpc_peer_20220101_models.GetVpcPeerConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vpc_peer_connection_attribute_with_options(request, runtime)

    async def get_vpc_peer_connection_attribute_async(
        self,
        request: vpc_peer_20220101_models.GetVpcPeerConnectionAttributeRequest,
    ) -> vpc_peer_20220101_models.GetVpcPeerConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vpc_peer_connection_attribute_with_options_async(request, runtime)

    def list_vpc_peer_connections_with_options(
        self,
        tmp_req: vpc_peer_20220101_models.ListVpcPeerConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.ListVpcPeerConnectionsResponse:
        UtilClient.validate_model(tmp_req)
        request = vpc_peer_20220101_models.ListVpcPeerConnectionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vpc_id):
            request.vpc_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vpc_id, 'VpcId', 'simple')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id_shrink):
            body['VpcId'] = request.vpc_id_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpcPeerConnections',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.ListVpcPeerConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_peer_connections_with_options_async(
        self,
        tmp_req: vpc_peer_20220101_models.ListVpcPeerConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.ListVpcPeerConnectionsResponse:
        UtilClient.validate_model(tmp_req)
        request = vpc_peer_20220101_models.ListVpcPeerConnectionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vpc_id):
            request.vpc_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vpc_id, 'VpcId', 'simple')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id_shrink):
            body['VpcId'] = request.vpc_id_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpcPeerConnections',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.ListVpcPeerConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_peer_connections(
        self,
        request: vpc_peer_20220101_models.ListVpcPeerConnectionsRequest,
    ) -> vpc_peer_20220101_models.ListVpcPeerConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_peer_connections_with_options(request, runtime)

    async def list_vpc_peer_connections_async(
        self,
        request: vpc_peer_20220101_models.ListVpcPeerConnectionsRequest,
    ) -> vpc_peer_20220101_models.ListVpcPeerConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_peer_connections_with_options_async(request, runtime)

    def modify_vpc_peer_connection_with_options(
        self,
        request: vpc_peer_20220101_models.ModifyVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.ModifyVpcPeerConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyVpcPeerConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.ModifyVpcPeerConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_peer_connection_with_options_async(
        self,
        request: vpc_peer_20220101_models.ModifyVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.ModifyVpcPeerConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyVpcPeerConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.ModifyVpcPeerConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_peer_connection(
        self,
        request: vpc_peer_20220101_models.ModifyVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.ModifyVpcPeerConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_peer_connection_with_options(request, runtime)

    async def modify_vpc_peer_connection_async(
        self,
        request: vpc_peer_20220101_models.ModifyVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.ModifyVpcPeerConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_peer_connection_with_options_async(request, runtime)

    def reject_vpc_peer_connection_with_options(
        self,
        request: vpc_peer_20220101_models.RejectVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.RejectVpcPeerConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RejectVpcPeerConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.RejectVpcPeerConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_vpc_peer_connection_with_options_async(
        self,
        request: vpc_peer_20220101_models.RejectVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.RejectVpcPeerConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RejectVpcPeerConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_peer_20220101_models.RejectVpcPeerConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_vpc_peer_connection(
        self,
        request: vpc_peer_20220101_models.RejectVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.RejectVpcPeerConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.reject_vpc_peer_connection_with_options(request, runtime)

    async def reject_vpc_peer_connection_async(
        self,
        request: vpc_peer_20220101_models.RejectVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.RejectVpcPeerConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reject_vpc_peer_connection_with_options_async(request, runtime)
