# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_resourcesharing20200110 import models as main_models
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
        self._endpoint = self.get_endpoint('resourcesharing', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def accept_resource_share_invitation_with_options(
        self,
        request: main_models.AcceptResourceShareInvitationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptResourceShareInvitationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptResourceShareInvitation',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptResourceShareInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_resource_share_invitation_with_options_async(
        self,
        request: main_models.AcceptResourceShareInvitationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptResourceShareInvitationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptResourceShareInvitation',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptResourceShareInvitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_resource_share_invitation(
        self,
        request: main_models.AcceptResourceShareInvitationRequest,
    ) -> main_models.AcceptResourceShareInvitationResponse:
        runtime = RuntimeOptions()
        return self.accept_resource_share_invitation_with_options(request, runtime)

    async def accept_resource_share_invitation_async(
        self,
        request: main_models.AcceptResourceShareInvitationRequest,
    ) -> main_models.AcceptResourceShareInvitationResponse:
        runtime = RuntimeOptions()
        return await self.accept_resource_share_invitation_with_options_async(request, runtime)

    def associate_resource_share_with_options(
        self,
        request: main_models.AssociateResourceShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateResourceShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.permission_names):
            query['PermissionNames'] = request.permission_names
        if not DaraCore.is_null(request.resource_arns):
            query['ResourceArns'] = request.resource_arns
        if not DaraCore.is_null(request.resource_properties):
            query['ResourceProperties'] = request.resource_properties
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.target_properties):
            query['TargetProperties'] = request.target_properties
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateResourceShare',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_resource_share_with_options_async(
        self,
        request: main_models.AssociateResourceShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateResourceShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.permission_names):
            query['PermissionNames'] = request.permission_names
        if not DaraCore.is_null(request.resource_arns):
            query['ResourceArns'] = request.resource_arns
        if not DaraCore.is_null(request.resource_properties):
            query['ResourceProperties'] = request.resource_properties
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.target_properties):
            query['TargetProperties'] = request.target_properties
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateResourceShare',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_resource_share(
        self,
        request: main_models.AssociateResourceShareRequest,
    ) -> main_models.AssociateResourceShareResponse:
        runtime = RuntimeOptions()
        return self.associate_resource_share_with_options(request, runtime)

    async def associate_resource_share_async(
        self,
        request: main_models.AssociateResourceShareRequest,
    ) -> main_models.AssociateResourceShareResponse:
        runtime = RuntimeOptions()
        return await self.associate_resource_share_with_options_async(request, runtime)

    def associate_resource_share_permission_with_options(
        self,
        request: main_models.AssociateResourceSharePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateResourceSharePermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not DaraCore.is_null(request.replace):
            query['Replace'] = request.replace
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateResourceSharePermission',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateResourceSharePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_resource_share_permission_with_options_async(
        self,
        request: main_models.AssociateResourceSharePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateResourceSharePermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not DaraCore.is_null(request.replace):
            query['Replace'] = request.replace
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateResourceSharePermission',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateResourceSharePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_resource_share_permission(
        self,
        request: main_models.AssociateResourceSharePermissionRequest,
    ) -> main_models.AssociateResourceSharePermissionResponse:
        runtime = RuntimeOptions()
        return self.associate_resource_share_permission_with_options(request, runtime)

    async def associate_resource_share_permission_async(
        self,
        request: main_models.AssociateResourceSharePermissionRequest,
    ) -> main_models.AssociateResourceSharePermissionResponse:
        runtime = RuntimeOptions()
        return await self.associate_resource_share_permission_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_sharing_with_resource_directory_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CheckSharingWithResourceDirectoryStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CheckSharingWithResourceDirectoryStatus',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSharingWithResourceDirectoryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_sharing_with_resource_directory_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CheckSharingWithResourceDirectoryStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CheckSharingWithResourceDirectoryStatus',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSharingWithResourceDirectoryStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_sharing_with_resource_directory_status(self) -> main_models.CheckSharingWithResourceDirectoryStatusResponse:
        runtime = RuntimeOptions()
        return self.check_sharing_with_resource_directory_status_with_options(runtime)

    async def check_sharing_with_resource_directory_status_async(self) -> main_models.CheckSharingWithResourceDirectoryStatusResponse:
        runtime = RuntimeOptions()
        return await self.check_sharing_with_resource_directory_status_with_options_async(runtime)

    def create_resource_share_with_options(
        self,
        request: main_models.CreateResourceShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not DaraCore.is_null(request.permission_names):
            query['PermissionNames'] = request.permission_names
        if not DaraCore.is_null(request.resource_arns):
            query['ResourceArns'] = request.resource_arns
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_properties):
            query['ResourceProperties'] = request.resource_properties
        if not DaraCore.is_null(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_properties):
            query['TargetProperties'] = request.target_properties
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceShare',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_share_with_options_async(
        self,
        request: main_models.CreateResourceShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not DaraCore.is_null(request.permission_names):
            query['PermissionNames'] = request.permission_names
        if not DaraCore.is_null(request.resource_arns):
            query['ResourceArns'] = request.resource_arns
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_properties):
            query['ResourceProperties'] = request.resource_properties
        if not DaraCore.is_null(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_properties):
            query['TargetProperties'] = request.target_properties
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceShare',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_share(
        self,
        request: main_models.CreateResourceShareRequest,
    ) -> main_models.CreateResourceShareResponse:
        runtime = RuntimeOptions()
        return self.create_resource_share_with_options(request, runtime)

    async def create_resource_share_async(
        self,
        request: main_models.CreateResourceShareRequest,
    ) -> main_models.CreateResourceShareResponse:
        runtime = RuntimeOptions()
        return await self.create_resource_share_with_options_async(request, runtime)

    def delete_resource_share_with_options(
        self,
        request: main_models.DeleteResourceShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceShare',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_share_with_options_async(
        self,
        request: main_models.DeleteResourceShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceShare',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_share(
        self,
        request: main_models.DeleteResourceShareRequest,
    ) -> main_models.DeleteResourceShareResponse:
        runtime = RuntimeOptions()
        return self.delete_resource_share_with_options(request, runtime)

    async def delete_resource_share_async(
        self,
        request: main_models.DeleteResourceShareRequest,
    ) -> main_models.DeleteResourceShareResponse:
        runtime = RuntimeOptions()
        return await self.delete_resource_share_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def disassociate_resource_share_with_options(
        self,
        request: main_models.DisassociateResourceShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateResourceShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_arns):
            query['ResourceArns'] = request.resource_arns
        if not DaraCore.is_null(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateResourceShare',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_resource_share_with_options_async(
        self,
        request: main_models.DisassociateResourceShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateResourceShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_arns):
            query['ResourceArns'] = request.resource_arns
        if not DaraCore.is_null(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateResourceShare',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_resource_share(
        self,
        request: main_models.DisassociateResourceShareRequest,
    ) -> main_models.DisassociateResourceShareResponse:
        runtime = RuntimeOptions()
        return self.disassociate_resource_share_with_options(request, runtime)

    async def disassociate_resource_share_async(
        self,
        request: main_models.DisassociateResourceShareRequest,
    ) -> main_models.DisassociateResourceShareResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_resource_share_with_options_async(request, runtime)

    def disassociate_resource_share_permission_with_options(
        self,
        request: main_models.DisassociateResourceSharePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateResourceSharePermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateResourceSharePermission',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateResourceSharePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_resource_share_permission_with_options_async(
        self,
        request: main_models.DisassociateResourceSharePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateResourceSharePermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateResourceSharePermission',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateResourceSharePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_resource_share_permission(
        self,
        request: main_models.DisassociateResourceSharePermissionRequest,
    ) -> main_models.DisassociateResourceSharePermissionResponse:
        runtime = RuntimeOptions()
        return self.disassociate_resource_share_permission_with_options(request, runtime)

    async def disassociate_resource_share_permission_async(
        self,
        request: main_models.DisassociateResourceSharePermissionRequest,
    ) -> main_models.DisassociateResourceSharePermissionResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_resource_share_permission_with_options_async(request, runtime)

    def enable_sharing_with_resource_directory_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSharingWithResourceDirectoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableSharingWithResourceDirectory',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSharingWithResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sharing_with_resource_directory_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSharingWithResourceDirectoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableSharingWithResourceDirectory',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSharingWithResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_sharing_with_resource_directory(self) -> main_models.EnableSharingWithResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return self.enable_sharing_with_resource_directory_with_options(runtime)

    async def enable_sharing_with_resource_directory_async(self) -> main_models.EnableSharingWithResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.enable_sharing_with_resource_directory_with_options_async(runtime)

    def get_permission_with_options(
        self,
        request: main_models.GetPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not DaraCore.is_null(request.permission_version):
            query['PermissionVersion'] = request.permission_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPermission',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_permission_with_options_async(
        self,
        request: main_models.GetPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not DaraCore.is_null(request.permission_version):
            query['PermissionVersion'] = request.permission_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPermission',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_permission(
        self,
        request: main_models.GetPermissionRequest,
    ) -> main_models.GetPermissionResponse:
        runtime = RuntimeOptions()
        return self.get_permission_with_options(request, runtime)

    async def get_permission_async(
        self,
        request: main_models.GetPermissionRequest,
    ) -> main_models.GetPermissionResponse:
        runtime = RuntimeOptions()
        return await self.get_permission_with_options_async(request, runtime)

    def list_permission_versions_with_options(
        self,
        request: main_models.ListPermissionVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.permission_name):
            query['PermissionName'] = request.permission_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissionVersions',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permission_versions_with_options_async(
        self,
        request: main_models.ListPermissionVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.permission_name):
            query['PermissionName'] = request.permission_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissionVersions',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permission_versions(
        self,
        request: main_models.ListPermissionVersionsRequest,
    ) -> main_models.ListPermissionVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_permission_versions_with_options(request, runtime)

    async def list_permission_versions_async(
        self,
        request: main_models.ListPermissionVersionsRequest,
    ) -> main_models.ListPermissionVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_permission_versions_with_options_async(request, runtime)

    def list_permissions_with_options(
        self,
        request: main_models.ListPermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissions',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permissions_with_options_async(
        self,
        request: main_models.ListPermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissions',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permissions(
        self,
        request: main_models.ListPermissionsRequest,
    ) -> main_models.ListPermissionsResponse:
        runtime = RuntimeOptions()
        return self.list_permissions_with_options(request, runtime)

    async def list_permissions_async(
        self,
        request: main_models.ListPermissionsRequest,
    ) -> main_models.ListPermissionsResponse:
        runtime = RuntimeOptions()
        return await self.list_permissions_with_options_async(request, runtime)

    def list_resource_share_associations_with_options(
        self,
        request: main_models.ListResourceShareAssociationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceShareAssociationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.association_status):
            query['AssociationStatus'] = request.association_status
        if not DaraCore.is_null(request.association_type):
            query['AssociationType'] = request.association_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceArn'] = request.resource_arn
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceShareAssociations',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceShareAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_share_associations_with_options_async(
        self,
        request: main_models.ListResourceShareAssociationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceShareAssociationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.association_status):
            query['AssociationStatus'] = request.association_status
        if not DaraCore.is_null(request.association_type):
            query['AssociationType'] = request.association_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceArn'] = request.resource_arn
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceShareAssociations',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceShareAssociationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_share_associations(
        self,
        request: main_models.ListResourceShareAssociationsRequest,
    ) -> main_models.ListResourceShareAssociationsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_share_associations_with_options(request, runtime)

    async def list_resource_share_associations_async(
        self,
        request: main_models.ListResourceShareAssociationsRequest,
    ) -> main_models.ListResourceShareAssociationsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_share_associations_with_options_async(request, runtime)

    def list_resource_share_invitations_with_options(
        self,
        request: main_models.ListResourceShareInvitationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceShareInvitationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not DaraCore.is_null(request.resource_share_invitation_ids):
            query['ResourceShareInvitationIds'] = request.resource_share_invitation_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceShareInvitations',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceShareInvitationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_share_invitations_with_options_async(
        self,
        request: main_models.ListResourceShareInvitationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceShareInvitationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not DaraCore.is_null(request.resource_share_invitation_ids):
            query['ResourceShareInvitationIds'] = request.resource_share_invitation_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceShareInvitations',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceShareInvitationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_share_invitations(
        self,
        request: main_models.ListResourceShareInvitationsRequest,
    ) -> main_models.ListResourceShareInvitationsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_share_invitations_with_options(request, runtime)

    async def list_resource_share_invitations_async(
        self,
        request: main_models.ListResourceShareInvitationsRequest,
    ) -> main_models.ListResourceShareInvitationsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_share_invitations_with_options_async(request, runtime)

    def list_resource_share_permissions_with_options(
        self,
        request: main_models.ListResourceSharePermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceSharePermissionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceSharePermissions',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceSharePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_share_permissions_with_options_async(
        self,
        request: main_models.ListResourceSharePermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceSharePermissionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceSharePermissions',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceSharePermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_share_permissions(
        self,
        request: main_models.ListResourceSharePermissionsRequest,
    ) -> main_models.ListResourceSharePermissionsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_share_permissions_with_options(request, runtime)

    async def list_resource_share_permissions_async(
        self,
        request: main_models.ListResourceSharePermissionsRequest,
    ) -> main_models.ListResourceSharePermissionsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_share_permissions_with_options_async(request, runtime)

    def list_resource_shares_with_options(
        self,
        request: main_models.ListResourceSharesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceSharesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not DaraCore.is_null(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not DaraCore.is_null(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not DaraCore.is_null(request.resource_share_status):
            query['ResourceShareStatus'] = request.resource_share_status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceShares',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceSharesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_shares_with_options_async(
        self,
        request: main_models.ListResourceSharesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceSharesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not DaraCore.is_null(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not DaraCore.is_null(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not DaraCore.is_null(request.resource_share_status):
            query['ResourceShareStatus'] = request.resource_share_status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceShares',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceSharesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_shares(
        self,
        request: main_models.ListResourceSharesRequest,
    ) -> main_models.ListResourceSharesResponse:
        runtime = RuntimeOptions()
        return self.list_resource_shares_with_options(request, runtime)

    async def list_resource_shares_async(
        self,
        request: main_models.ListResourceSharesRequest,
    ) -> main_models.ListResourceSharesResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_shares_with_options_async(request, runtime)

    def list_shared_resources_with_options(
        self,
        request: main_models.ListSharedResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSharedResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_arns):
            query['ResourceArns'] = request.resource_arns
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not DaraCore.is_null(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSharedResources',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSharedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_shared_resources_with_options_async(
        self,
        request: main_models.ListSharedResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSharedResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_arns):
            query['ResourceArns'] = request.resource_arns
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not DaraCore.is_null(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSharedResources',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSharedResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_shared_resources(
        self,
        request: main_models.ListSharedResourcesRequest,
    ) -> main_models.ListSharedResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_shared_resources_with_options(request, runtime)

    async def list_shared_resources_async(
        self,
        request: main_models.ListSharedResourcesRequest,
    ) -> main_models.ListSharedResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_shared_resources_with_options_async(request, runtime)

    def list_shared_targets_with_options(
        self,
        request: main_models.ListSharedTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSharedTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceArn'] = request.resource_arn
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not DaraCore.is_null(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSharedTargets',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSharedTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_shared_targets_with_options_async(
        self,
        request: main_models.ListSharedTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSharedTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_arn):
            query['ResourceArn'] = request.resource_arn
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not DaraCore.is_null(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSharedTargets',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSharedTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_shared_targets(
        self,
        request: main_models.ListSharedTargetsRequest,
    ) -> main_models.ListSharedTargetsResponse:
        runtime = RuntimeOptions()
        return self.list_shared_targets_with_options(request, runtime)

    async def list_shared_targets_async(
        self,
        request: main_models.ListSharedTargetsRequest,
    ) -> main_models.ListSharedTargetsResponse:
        runtime = RuntimeOptions()
        return await self.list_shared_targets_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
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
            version = '2020-01-10',
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
            version = '2020-01-10',
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

    def reject_resource_share_invitation_with_options(
        self,
        request: main_models.RejectResourceShareInvitationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectResourceShareInvitationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectResourceShareInvitation',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectResourceShareInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_resource_share_invitation_with_options_async(
        self,
        request: main_models.RejectResourceShareInvitationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectResourceShareInvitationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectResourceShareInvitation',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectResourceShareInvitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_resource_share_invitation(
        self,
        request: main_models.RejectResourceShareInvitationRequest,
    ) -> main_models.RejectResourceShareInvitationResponse:
        runtime = RuntimeOptions()
        return self.reject_resource_share_invitation_with_options(request, runtime)

    async def reject_resource_share_invitation_async(
        self,
        request: main_models.RejectResourceShareInvitationRequest,
    ) -> main_models.RejectResourceShareInvitationResponse:
        runtime = RuntimeOptions()
        return await self.reject_resource_share_invitation_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
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
            version = '2020-01-10',
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
            version = '2020-01-10',
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

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
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
            action = 'UntagResources',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
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
            action = 'UntagResources',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_resource_share_with_options(
        self,
        request: main_models.UpdateResourceShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not DaraCore.is_null(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceShare',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_share_with_options_async(
        self,
        request: main_models.UpdateResourceShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not DaraCore.is_null(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not DaraCore.is_null(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceShare',
            version = '2020-01-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_share(
        self,
        request: main_models.UpdateResourceShareRequest,
    ) -> main_models.UpdateResourceShareResponse:
        runtime = RuntimeOptions()
        return self.update_resource_share_with_options(request, runtime)

    async def update_resource_share_async(
        self,
        request: main_models.UpdateResourceShareRequest,
    ) -> main_models.UpdateResourceShareResponse:
        runtime = RuntimeOptions()
        return await self.update_resource_share_with_options_async(request, runtime)
