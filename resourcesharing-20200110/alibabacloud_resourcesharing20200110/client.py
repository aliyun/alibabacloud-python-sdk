# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_resourcesharing20200110 import models as resource_sharing_20200110_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_resource_share_invitation_with_options(
        self,
        request: resource_sharing_20200110_models.AcceptResourceShareInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AcceptResourceShareInvitationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptResourceShareInvitation',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AcceptResourceShareInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_resource_share_invitation_with_options_async(
        self,
        request: resource_sharing_20200110_models.AcceptResourceShareInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AcceptResourceShareInvitationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptResourceShareInvitation',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AcceptResourceShareInvitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_resource_share_invitation(
        self,
        request: resource_sharing_20200110_models.AcceptResourceShareInvitationRequest,
    ) -> resource_sharing_20200110_models.AcceptResourceShareInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_resource_share_invitation_with_options(request, runtime)

    async def accept_resource_share_invitation_async(
        self,
        request: resource_sharing_20200110_models.AcceptResourceShareInvitationRequest,
    ) -> resource_sharing_20200110_models.AcceptResourceShareInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_resource_share_invitation_with_options_async(request, runtime)

    def associate_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AssociateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AssociateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_resource_share(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_resource_share_with_options(request, runtime)

    async def associate_resource_share_async(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_resource_share_with_options_async(request, runtime)

    def create_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.CreateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.CreateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_share(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_share_with_options(request, runtime)

    async def create_resource_share_async(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_share_with_options_async(request, runtime)

    def delete_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DeleteResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DeleteResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_share(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_share_with_options(request, runtime)

    async def delete_resource_share_async(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_share_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def disassociate_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DisassociateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DisassociateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_resource_share(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.disassociate_resource_share_with_options(request, runtime)

    async def disassociate_resource_share_async(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_resource_share_with_options_async(request, runtime)

    def enable_sharing_with_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableSharingWithResourceDirectory',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sharing_with_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableSharingWithResourceDirectory',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_sharing_with_resource_directory(self) -> resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_sharing_with_resource_directory_with_options(runtime)

    async def enable_sharing_with_resource_directory_async(self) -> resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_sharing_with_resource_directory_with_options_async(runtime)

    def list_resource_share_associations_with_options(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.association_status):
            query['AssociationStatus'] = request.association_status
        if not UtilClient.is_unset(request.association_type):
            query['AssociationType'] = request.association_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShareAssociations',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceShareAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_share_associations_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.association_status):
            query['AssociationStatus'] = request.association_status
        if not UtilClient.is_unset(request.association_type):
            query['AssociationType'] = request.association_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShareAssociations',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceShareAssociationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_share_associations(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_share_associations_with_options(request, runtime)

    async def list_resource_share_associations_async(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_share_associations_with_options_async(request, runtime)

    def list_resource_share_invitations_with_options(
        self,
        request: resource_sharing_20200110_models.ListResourceShareInvitationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceShareInvitationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_share_invitation_ids):
            query['ResourceShareInvitationIds'] = request.resource_share_invitation_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShareInvitations',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceShareInvitationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_share_invitations_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListResourceShareInvitationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceShareInvitationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_share_invitation_ids):
            query['ResourceShareInvitationIds'] = request.resource_share_invitation_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShareInvitations',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceShareInvitationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_share_invitations(
        self,
        request: resource_sharing_20200110_models.ListResourceShareInvitationsRequest,
    ) -> resource_sharing_20200110_models.ListResourceShareInvitationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_share_invitations_with_options(request, runtime)

    async def list_resource_share_invitations_async(
        self,
        request: resource_sharing_20200110_models.ListResourceShareInvitationsRequest,
    ) -> resource_sharing_20200110_models.ListResourceShareInvitationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_share_invitations_with_options_async(request, runtime)

    def list_resource_shares_with_options(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not UtilClient.is_unset(request.resource_share_status):
            query['ResourceShareStatus'] = request.resource_share_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShares',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceSharesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_shares_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not UtilClient.is_unset(request.resource_share_status):
            query['ResourceShareStatus'] = request.resource_share_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShares',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceSharesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_shares(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_shares_with_options(request, runtime)

    async def list_resource_shares_async(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_shares_with_options_async(request, runtime)

    def list_shared_resources_with_options(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedResources',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListSharedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_shared_resources_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedResources',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListSharedResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_shared_resources(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_shared_resources_with_options(request, runtime)

    async def list_shared_resources_async(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_shared_resources_with_options_async(request, runtime)

    def list_shared_targets_with_options(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedTargets',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListSharedTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_shared_targets_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedTargets',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListSharedTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_shared_targets(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_shared_targets_with_options(request, runtime)

    async def list_shared_targets_async(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_shared_targets_with_options_async(request, runtime)

    def reject_resource_share_invitation_with_options(
        self,
        request: resource_sharing_20200110_models.RejectResourceShareInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.RejectResourceShareInvitationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectResourceShareInvitation',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.RejectResourceShareInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_resource_share_invitation_with_options_async(
        self,
        request: resource_sharing_20200110_models.RejectResourceShareInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.RejectResourceShareInvitationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectResourceShareInvitation',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.RejectResourceShareInvitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_resource_share_invitation(
        self,
        request: resource_sharing_20200110_models.RejectResourceShareInvitationRequest,
    ) -> resource_sharing_20200110_models.RejectResourceShareInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return self.reject_resource_share_invitation_with_options(request, runtime)

    async def reject_resource_share_invitation_async(
        self,
        request: resource_sharing_20200110_models.RejectResourceShareInvitationRequest,
    ) -> resource_sharing_20200110_models.RejectResourceShareInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reject_resource_share_invitation_with_options_async(request, runtime)

    def update_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.UpdateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.UpdateResourceShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_share(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_share_with_options(request, runtime)

    async def update_resource_share_async(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_share_with_options_async(request, runtime)
