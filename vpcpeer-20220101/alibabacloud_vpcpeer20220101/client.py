# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_vpcpeer20220101 import models as main_models
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
        self._endpoint_rule = 'central'
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_vpc_peer_connection_with_options(
        self,
        request: main_models.AcceptVpcPeerConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptVpcPeerConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AcceptVpcPeerConnection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptVpcPeerConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_vpc_peer_connection_with_options_async(
        self,
        request: main_models.AcceptVpcPeerConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptVpcPeerConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AcceptVpcPeerConnection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptVpcPeerConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_vpc_peer_connection(
        self,
        request: main_models.AcceptVpcPeerConnectionRequest,
    ) -> main_models.AcceptVpcPeerConnectionResponse:
        runtime = RuntimeOptions()
        return self.accept_vpc_peer_connection_with_options(request, runtime)

    async def accept_vpc_peer_connection_async(
        self,
        request: main_models.AcceptVpcPeerConnectionRequest,
    ) -> main_models.AcceptVpcPeerConnectionResponse:
        runtime = RuntimeOptions()
        return await self.accept_vpc_peer_connection_with_options_async(request, runtime)

    def create_vpc_peer_connection_with_options(
        self,
        request: main_models.CreateVpcPeerConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcPeerConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.link_type):
            query['LinkType'] = request.link_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.accepting_ali_uid):
            body['AcceptingAliUid'] = request.accepting_ali_uid
        if not DaraCore.is_null(request.accepting_region_id):
            body['AcceptingRegionId'] = request.accepting_region_id
        if not DaraCore.is_null(request.accepting_vpc_id):
            body['AcceptingVpcId'] = request.accepting_vpc_id
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_jumbo_frame):
            body['EnableJumboFrame'] = request.enable_jumbo_frame
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcPeerConnection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcPeerConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_peer_connection_with_options_async(
        self,
        request: main_models.CreateVpcPeerConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcPeerConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.link_type):
            query['LinkType'] = request.link_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.accepting_ali_uid):
            body['AcceptingAliUid'] = request.accepting_ali_uid
        if not DaraCore.is_null(request.accepting_region_id):
            body['AcceptingRegionId'] = request.accepting_region_id
        if not DaraCore.is_null(request.accepting_vpc_id):
            body['AcceptingVpcId'] = request.accepting_vpc_id
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_jumbo_frame):
            body['EnableJumboFrame'] = request.enable_jumbo_frame
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcPeerConnection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcPeerConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_peer_connection(
        self,
        request: main_models.CreateVpcPeerConnectionRequest,
    ) -> main_models.CreateVpcPeerConnectionResponse:
        runtime = RuntimeOptions()
        return self.create_vpc_peer_connection_with_options(request, runtime)

    async def create_vpc_peer_connection_async(
        self,
        request: main_models.CreateVpcPeerConnectionRequest,
    ) -> main_models.CreateVpcPeerConnectionResponse:
        runtime = RuntimeOptions()
        return await self.create_vpc_peer_connection_with_options_async(request, runtime)

    def delete_vpc_peer_connection_with_options(
        self,
        request: main_models.DeleteVpcPeerConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcPeerConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            body['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcPeerConnection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcPeerConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_peer_connection_with_options_async(
        self,
        request: main_models.DeleteVpcPeerConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcPeerConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            body['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcPeerConnection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcPeerConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_peer_connection(
        self,
        request: main_models.DeleteVpcPeerConnectionRequest,
    ) -> main_models.DeleteVpcPeerConnectionResponse:
        runtime = RuntimeOptions()
        return self.delete_vpc_peer_connection_with_options(request, runtime)

    async def delete_vpc_peer_connection_async(
        self,
        request: main_models.DeleteVpcPeerConnectionRequest,
    ) -> main_models.DeleteVpcPeerConnectionResponse:
        runtime = RuntimeOptions()
        return await self.delete_vpc_peer_connection_with_options_async(request, runtime)

    def get_vpc_peer_connection_attribute_with_options(
        self,
        request: main_models.GetVpcPeerConnectionAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpcPeerConnectionAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVpcPeerConnectionAttribute',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpcPeerConnectionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpc_peer_connection_attribute_with_options_async(
        self,
        request: main_models.GetVpcPeerConnectionAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpcPeerConnectionAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVpcPeerConnectionAttribute',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpcPeerConnectionAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpc_peer_connection_attribute(
        self,
        request: main_models.GetVpcPeerConnectionAttributeRequest,
    ) -> main_models.GetVpcPeerConnectionAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_vpc_peer_connection_attribute_with_options(request, runtime)

    async def get_vpc_peer_connection_attribute_async(
        self,
        request: main_models.GetVpcPeerConnectionAttributeRequest,
    ) -> main_models.GetVpcPeerConnectionAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_vpc_peer_connection_attribute_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_vpc_peer_connections_with_options(
        self,
        tmp_req: main_models.ListVpcPeerConnectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcPeerConnectionsResponse:
        tmp_req.validate()
        request = main_models.ListVpcPeerConnectionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vpc_id):
            request.vpc_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.vpc_id, 'VpcId', 'simple')
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpc_id_shrink):
            body['VpcId'] = request.vpc_id_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcPeerConnections',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcPeerConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_peer_connections_with_options_async(
        self,
        tmp_req: main_models.ListVpcPeerConnectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcPeerConnectionsResponse:
        tmp_req.validate()
        request = main_models.ListVpcPeerConnectionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vpc_id):
            request.vpc_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.vpc_id, 'VpcId', 'simple')
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpc_id_shrink):
            body['VpcId'] = request.vpc_id_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcPeerConnections',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcPeerConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_peer_connections(
        self,
        request: main_models.ListVpcPeerConnectionsRequest,
    ) -> main_models.ListVpcPeerConnectionsResponse:
        runtime = RuntimeOptions()
        return self.list_vpc_peer_connections_with_options(request, runtime)

    async def list_vpc_peer_connections_async(
        self,
        request: main_models.ListVpcPeerConnectionsRequest,
    ) -> main_models.ListVpcPeerConnectionsResponse:
        runtime = RuntimeOptions()
        return await self.list_vpc_peer_connections_with_options_async(request, runtime)

    def modify_vpc_peer_connection_with_options(
        self,
        request: main_models.ModifyVpcPeerConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcPeerConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.link_type):
            query['LinkType'] = request.link_type
        body = {}
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_jumbo_frame):
            body['EnableJumboFrame'] = request.enable_jumbo_frame
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcPeerConnection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcPeerConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_peer_connection_with_options_async(
        self,
        request: main_models.ModifyVpcPeerConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcPeerConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.link_type):
            query['LinkType'] = request.link_type
        body = {}
        if not DaraCore.is_null(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_jumbo_frame):
            body['EnableJumboFrame'] = request.enable_jumbo_frame
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcPeerConnection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcPeerConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_peer_connection(
        self,
        request: main_models.ModifyVpcPeerConnectionRequest,
    ) -> main_models.ModifyVpcPeerConnectionResponse:
        runtime = RuntimeOptions()
        return self.modify_vpc_peer_connection_with_options(request, runtime)

    async def modify_vpc_peer_connection_async(
        self,
        request: main_models.ModifyVpcPeerConnectionRequest,
    ) -> main_models.ModifyVpcPeerConnectionResponse:
        runtime = RuntimeOptions()
        return await self.modify_vpc_peer_connection_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def reject_vpc_peer_connection_with_options(
        self,
        request: main_models.RejectVpcPeerConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectVpcPeerConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RejectVpcPeerConnection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectVpcPeerConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_vpc_peer_connection_with_options_async(
        self,
        request: main_models.RejectVpcPeerConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectVpcPeerConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RejectVpcPeerConnection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectVpcPeerConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_vpc_peer_connection(
        self,
        request: main_models.RejectVpcPeerConnectionRequest,
    ) -> main_models.RejectVpcPeerConnectionResponse:
        runtime = RuntimeOptions()
        return self.reject_vpc_peer_connection_with_options(request, runtime)

    async def reject_vpc_peer_connection_async(
        self,
        request: main_models.RejectVpcPeerConnectionRequest,
    ) -> main_models.RejectVpcPeerConnectionResponse:
        runtime = RuntimeOptions()
        return await self.reject_vpc_peer_connection_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: main_models.UnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: main_models.UnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)
