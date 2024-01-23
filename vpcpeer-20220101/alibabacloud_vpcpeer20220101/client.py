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
        """
        For a cross-account VPC peering connection, the connection is activated only after the accepter VPC accepts the connection request.
        *   **AcceptVpcPeerConnection** is an asynchronous operation. After a request is sent, the system returns a **request ID** and runs the operation in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of the task.
        *   If a VPC peering connection is in the **Updating** state, the VPC peering connection is being activated.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is activated.
        *   You cannot repeatedly call the **AcceptVpcPeerConnection** operation within a specific period of time.
        
        @param request: AcceptVpcPeerConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptVpcPeerConnectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
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
        """
        For a cross-account VPC peering connection, the connection is activated only after the accepter VPC accepts the connection request.
        *   **AcceptVpcPeerConnection** is an asynchronous operation. After a request is sent, the system returns a **request ID** and runs the operation in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of the task.
        *   If a VPC peering connection is in the **Updating** state, the VPC peering connection is being activated.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is activated.
        *   You cannot repeatedly call the **AcceptVpcPeerConnection** operation within a specific period of time.
        
        @param request: AcceptVpcPeerConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptVpcPeerConnectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
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
        """
        For a cross-account VPC peering connection, the connection is activated only after the accepter VPC accepts the connection request.
        *   **AcceptVpcPeerConnection** is an asynchronous operation. After a request is sent, the system returns a **request ID** and runs the operation in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of the task.
        *   If a VPC peering connection is in the **Updating** state, the VPC peering connection is being activated.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is activated.
        *   You cannot repeatedly call the **AcceptVpcPeerConnection** operation within a specific period of time.
        
        @param request: AcceptVpcPeerConnectionRequest
        @return: AcceptVpcPeerConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.accept_vpc_peer_connection_with_options(request, runtime)

    async def accept_vpc_peer_connection_async(
        self,
        request: vpc_peer_20220101_models.AcceptVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.AcceptVpcPeerConnectionResponse:
        """
        For a cross-account VPC peering connection, the connection is activated only after the accepter VPC accepts the connection request.
        *   **AcceptVpcPeerConnection** is an asynchronous operation. After a request is sent, the system returns a **request ID** and runs the operation in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of the task.
        *   If a VPC peering connection is in the **Updating** state, the VPC peering connection is being activated.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is activated.
        *   You cannot repeatedly call the **AcceptVpcPeerConnection** operation within a specific period of time.
        
        @param request: AcceptVpcPeerConnectionRequest
        @return: AcceptVpcPeerConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.accept_vpc_peer_connection_with_options_async(request, runtime)

    def create_vpc_peer_connection_with_options(
        self,
        request: vpc_peer_20220101_models.CreateVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.CreateVpcPeerConnectionResponse:
        """
        Before you create a VPC peering connection, make sure that the following requirements are met:
        *   Cloud Data Transfer (CDT) is activated to manage the billing of intra-border data transfers. To activate CDT, call the [OpenCdtService](~~337842~~) operation.
        *   **CreateVpcPeerConnection** is an asynchronous operation. After a request is sent, the system returns a request ID and an **instance ID** and runs the task in the background. You can call the [GetVpcPeerConnectionAttribute](~~426095~~) operation to query the status of the task.
        *   If a VPC peering connection is in the **Creating** state, the VPC peering connection is being created.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is created.
        *   If a VPC peering connection is in the **Accepting** state, the VPC peering connection is created across accounts and the accepter is accepting the VPC peering connection.
        *   You cannot repeatedly call the **CreateVpcPeerConnection** operation within a specific period of time.
        
        @param request: CreateVpcPeerConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpcPeerConnectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accepting_ali_uid):
            body['AcceptingAliUid'] = request.accepting_ali_uid
        if not UtilClient.is_unset(request.accepting_region_id):
            body['AcceptingRegionId'] = request.accepting_region_id
        if not UtilClient.is_unset(request.accepting_vpc_id):
            body['AcceptingVpcId'] = request.accepting_vpc_id
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
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
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
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
        """
        Before you create a VPC peering connection, make sure that the following requirements are met:
        *   Cloud Data Transfer (CDT) is activated to manage the billing of intra-border data transfers. To activate CDT, call the [OpenCdtService](~~337842~~) operation.
        *   **CreateVpcPeerConnection** is an asynchronous operation. After a request is sent, the system returns a request ID and an **instance ID** and runs the task in the background. You can call the [GetVpcPeerConnectionAttribute](~~426095~~) operation to query the status of the task.
        *   If a VPC peering connection is in the **Creating** state, the VPC peering connection is being created.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is created.
        *   If a VPC peering connection is in the **Accepting** state, the VPC peering connection is created across accounts and the accepter is accepting the VPC peering connection.
        *   You cannot repeatedly call the **CreateVpcPeerConnection** operation within a specific period of time.
        
        @param request: CreateVpcPeerConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpcPeerConnectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accepting_ali_uid):
            body['AcceptingAliUid'] = request.accepting_ali_uid
        if not UtilClient.is_unset(request.accepting_region_id):
            body['AcceptingRegionId'] = request.accepting_region_id
        if not UtilClient.is_unset(request.accepting_vpc_id):
            body['AcceptingVpcId'] = request.accepting_vpc_id
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
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
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
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
        """
        Before you create a VPC peering connection, make sure that the following requirements are met:
        *   Cloud Data Transfer (CDT) is activated to manage the billing of intra-border data transfers. To activate CDT, call the [OpenCdtService](~~337842~~) operation.
        *   **CreateVpcPeerConnection** is an asynchronous operation. After a request is sent, the system returns a request ID and an **instance ID** and runs the task in the background. You can call the [GetVpcPeerConnectionAttribute](~~426095~~) operation to query the status of the task.
        *   If a VPC peering connection is in the **Creating** state, the VPC peering connection is being created.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is created.
        *   If a VPC peering connection is in the **Accepting** state, the VPC peering connection is created across accounts and the accepter is accepting the VPC peering connection.
        *   You cannot repeatedly call the **CreateVpcPeerConnection** operation within a specific period of time.
        
        @param request: CreateVpcPeerConnectionRequest
        @return: CreateVpcPeerConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_peer_connection_with_options(request, runtime)

    async def create_vpc_peer_connection_async(
        self,
        request: vpc_peer_20220101_models.CreateVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.CreateVpcPeerConnectionResponse:
        """
        Before you create a VPC peering connection, make sure that the following requirements are met:
        *   Cloud Data Transfer (CDT) is activated to manage the billing of intra-border data transfers. To activate CDT, call the [OpenCdtService](~~337842~~) operation.
        *   **CreateVpcPeerConnection** is an asynchronous operation. After a request is sent, the system returns a request ID and an **instance ID** and runs the task in the background. You can call the [GetVpcPeerConnectionAttribute](~~426095~~) operation to query the status of the task.
        *   If a VPC peering connection is in the **Creating** state, the VPC peering connection is being created.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is created.
        *   If a VPC peering connection is in the **Accepting** state, the VPC peering connection is created across accounts and the accepter is accepting the VPC peering connection.
        *   You cannot repeatedly call the **CreateVpcPeerConnection** operation within a specific period of time.
        
        @param request: CreateVpcPeerConnectionRequest
        @return: CreateVpcPeerConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_peer_connection_with_options_async(request, runtime)

    def delete_vpc_peer_connection_with_options(
        self,
        request: vpc_peer_20220101_models.DeleteVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.DeleteVpcPeerConnectionResponse:
        """
        You can delete VPC peering connections. After you delete a VPC peering connection, your service is affected. Proceed with caution.
        *   If you forcefully delete a VPC peering connection, the system deletes the routes that point to the VPC peering connection from the VPC route table.
        *   If you do not forcefully delete a VPC peering connection, the system does not delete these routes. You must manually delete them.
        *   The **DeleteVpcPeerConnection** operation is asynchronous. After you send a request, the system returns **RequestId**, but the operation is still being performed in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of a VPC peering connection.
        *   If a VPC peering connection is in the **Deleting** state, it is being deleted.
        *   If a VPC peering connection is in the **Deleted** state, it is deleted.
        *   You cannot repeatedly call the **DeleteVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: DeleteVpcPeerConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpcPeerConnectionResponse
        """
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
        """
        You can delete VPC peering connections. After you delete a VPC peering connection, your service is affected. Proceed with caution.
        *   If you forcefully delete a VPC peering connection, the system deletes the routes that point to the VPC peering connection from the VPC route table.
        *   If you do not forcefully delete a VPC peering connection, the system does not delete these routes. You must manually delete them.
        *   The **DeleteVpcPeerConnection** operation is asynchronous. After you send a request, the system returns **RequestId**, but the operation is still being performed in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of a VPC peering connection.
        *   If a VPC peering connection is in the **Deleting** state, it is being deleted.
        *   If a VPC peering connection is in the **Deleted** state, it is deleted.
        *   You cannot repeatedly call the **DeleteVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: DeleteVpcPeerConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpcPeerConnectionResponse
        """
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
        """
        You can delete VPC peering connections. After you delete a VPC peering connection, your service is affected. Proceed with caution.
        *   If you forcefully delete a VPC peering connection, the system deletes the routes that point to the VPC peering connection from the VPC route table.
        *   If you do not forcefully delete a VPC peering connection, the system does not delete these routes. You must manually delete them.
        *   The **DeleteVpcPeerConnection** operation is asynchronous. After you send a request, the system returns **RequestId**, but the operation is still being performed in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of a VPC peering connection.
        *   If a VPC peering connection is in the **Deleting** state, it is being deleted.
        *   If a VPC peering connection is in the **Deleted** state, it is deleted.
        *   You cannot repeatedly call the **DeleteVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: DeleteVpcPeerConnectionRequest
        @return: DeleteVpcPeerConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_peer_connection_with_options(request, runtime)

    async def delete_vpc_peer_connection_async(
        self,
        request: vpc_peer_20220101_models.DeleteVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.DeleteVpcPeerConnectionResponse:
        """
        You can delete VPC peering connections. After you delete a VPC peering connection, your service is affected. Proceed with caution.
        *   If you forcefully delete a VPC peering connection, the system deletes the routes that point to the VPC peering connection from the VPC route table.
        *   If you do not forcefully delete a VPC peering connection, the system does not delete these routes. You must manually delete them.
        *   The **DeleteVpcPeerConnection** operation is asynchronous. After you send a request, the system returns **RequestId**, but the operation is still being performed in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of a VPC peering connection.
        *   If a VPC peering connection is in the **Deleting** state, it is being deleted.
        *   If a VPC peering connection is in the **Deleted** state, it is deleted.
        *   You cannot repeatedly call the **DeleteVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: DeleteVpcPeerConnectionRequest
        @return: DeleteVpcPeerConnectionResponse
        """
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

    def list_tag_resources_with_options(
        self,
        request: vpc_peer_20220101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.ListTagResourcesResponse:
        """
        Set **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value** in the request to specify the object to be queried.
        *   **Tag.N** is a resource tag that consists of a key-value pair. If you set only **Tag.N.Key**, all tag values that are associated with the specified key are returned. If you set only **Tag.N.Value**, an error message is returned.
        *   If you set **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        *   If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
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
            vpc_peer_20220101_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: vpc_peer_20220101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.ListTagResourcesResponse:
        """
        Set **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value** in the request to specify the object to be queried.
        *   **Tag.N** is a resource tag that consists of a key-value pair. If you set only **Tag.N.Key**, all tag values that are associated with the specified key are returned. If you set only **Tag.N.Value**, an error message is returned.
        *   If you set **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        *   If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
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
            vpc_peer_20220101_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: vpc_peer_20220101_models.ListTagResourcesRequest,
    ) -> vpc_peer_20220101_models.ListTagResourcesResponse:
        """
        Set **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value** in the request to specify the object to be queried.
        *   **Tag.N** is a resource tag that consists of a key-value pair. If you set only **Tag.N.Key**, all tag values that are associated with the specified key are returned. If you set only **Tag.N.Value**, an error message is returned.
        *   If you set **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        *   If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: vpc_peer_20220101_models.ListTagResourcesRequest,
    ) -> vpc_peer_20220101_models.ListTagResourcesResponse:
        """
        Set **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value** in the request to specify the object to be queried.
        *   **Tag.N** is a resource tag that consists of a key-value pair. If you set only **Tag.N.Key**, all tag values that are associated with the specified key are returned. If you set only **Tag.N.Value**, an error message is returned.
        *   If you set **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        *   If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
            query=OpenApiUtilClient.query(query),
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
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
            query=OpenApiUtilClient.query(query),
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
        """
        The **ModifyVpcPeerConnection** operation is asynchronous. After you send a request, the system returns **RequestId**, but the operation is still being performed in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of a VPC peering connection.
        *   If a VPC peering connection is in the **Updating** state, the VPC peering connection is being modified.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is modified.
        *   You cannot repeatedly call the **ModifyVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: ModifyVpcPeerConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcPeerConnectionResponse
        """
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
        """
        The **ModifyVpcPeerConnection** operation is asynchronous. After you send a request, the system returns **RequestId**, but the operation is still being performed in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of a VPC peering connection.
        *   If a VPC peering connection is in the **Updating** state, the VPC peering connection is being modified.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is modified.
        *   You cannot repeatedly call the **ModifyVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: ModifyVpcPeerConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcPeerConnectionResponse
        """
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
        """
        The **ModifyVpcPeerConnection** operation is asynchronous. After you send a request, the system returns **RequestId**, but the operation is still being performed in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of a VPC peering connection.
        *   If a VPC peering connection is in the **Updating** state, the VPC peering connection is being modified.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is modified.
        *   You cannot repeatedly call the **ModifyVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: ModifyVpcPeerConnectionRequest
        @return: ModifyVpcPeerConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_peer_connection_with_options(request, runtime)

    async def modify_vpc_peer_connection_async(
        self,
        request: vpc_peer_20220101_models.ModifyVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.ModifyVpcPeerConnectionResponse:
        """
        The **ModifyVpcPeerConnection** operation is asynchronous. After you send a request, the system returns **RequestId**, but the operation is still being performed in the background. You can call the [GetVpcPeerConnectionAttribute](~~426100~~) operation to query the status of a VPC peering connection.
        *   If a VPC peering connection is in the **Updating** state, the VPC peering connection is being modified.
        *   If a VPC peering connection is in the **Activated** state, the VPC peering connection is modified.
        *   You cannot repeatedly call the **ModifyVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: ModifyVpcPeerConnectionRequest
        @return: ModifyVpcPeerConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_peer_connection_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: vpc_peer_20220101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
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
            vpc_peer_20220101_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: vpc_peer_20220101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
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
            vpc_peer_20220101_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: vpc_peer_20220101_models.MoveResourceGroupRequest,
    ) -> vpc_peer_20220101_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: vpc_peer_20220101_models.MoveResourceGroupRequest,
    ) -> vpc_peer_20220101_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def reject_vpc_peer_connection_with_options(
        self,
        request: vpc_peer_20220101_models.RejectVpcPeerConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.RejectVpcPeerConnectionResponse:
        """
        An acceptor VPC can reject a connection request from the requester VPC of a cross-account VPC peering connection. After the connection request is rejected, the VPC peering connection enters the **Rejected** state.
        *   You cannot repeatedly call the **RejectVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: RejectVpcPeerConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectVpcPeerConnectionResponse
        """
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
        """
        An acceptor VPC can reject a connection request from the requester VPC of a cross-account VPC peering connection. After the connection request is rejected, the VPC peering connection enters the **Rejected** state.
        *   You cannot repeatedly call the **RejectVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: RejectVpcPeerConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectVpcPeerConnectionResponse
        """
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
        """
        An acceptor VPC can reject a connection request from the requester VPC of a cross-account VPC peering connection. After the connection request is rejected, the VPC peering connection enters the **Rejected** state.
        *   You cannot repeatedly call the **RejectVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: RejectVpcPeerConnectionRequest
        @return: RejectVpcPeerConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reject_vpc_peer_connection_with_options(request, runtime)

    async def reject_vpc_peer_connection_async(
        self,
        request: vpc_peer_20220101_models.RejectVpcPeerConnectionRequest,
    ) -> vpc_peer_20220101_models.RejectVpcPeerConnectionResponse:
        """
        An acceptor VPC can reject a connection request from the requester VPC of a cross-account VPC peering connection. After the connection request is rejected, the VPC peering connection enters the **Rejected** state.
        *   You cannot repeatedly call the **RejectVpcPeerConnection** operation for the same VPC peering connection within the specified period of time.
        
        @param request: RejectVpcPeerConnectionRequest
        @return: RejectVpcPeerConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reject_vpc_peer_connection_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: vpc_peer_20220101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.TagResourcesResponse:
        """
        Tags are used to classify instances. Each tag consists of a key-value pair. Before you use tags, take note of the following limits:
        *   The keys of tags that are added to the same instance must be unique.
        *   You cannot create tags without adding them to instances. All tags must be added to instances.
        *   Tag information is not shared across regions.
        For example, you cannot view the tags that are created in the China (Hangzhou) region from the China (Shanghai) region.
        *   For the same account and region, tags added to different VPC peering connections are shared.
        For example, if a tag is added to a VPC peering connection, the tag can also be added to other VPC peering connections within the same account and region. You can modify the key and the value of a tag or remove a tag from an instance. After you delete an instance, all tags that are added to the instance are deleted.
        *   You can add up to 20 tags to each instance. Before you add a tag to an instance, the system automatically checks the number of existing tags. An error message is returned if the maximum number of tags is reached.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
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
            vpc_peer_20220101_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: vpc_peer_20220101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.TagResourcesResponse:
        """
        Tags are used to classify instances. Each tag consists of a key-value pair. Before you use tags, take note of the following limits:
        *   The keys of tags that are added to the same instance must be unique.
        *   You cannot create tags without adding them to instances. All tags must be added to instances.
        *   Tag information is not shared across regions.
        For example, you cannot view the tags that are created in the China (Hangzhou) region from the China (Shanghai) region.
        *   For the same account and region, tags added to different VPC peering connections are shared.
        For example, if a tag is added to a VPC peering connection, the tag can also be added to other VPC peering connections within the same account and region. You can modify the key and the value of a tag or remove a tag from an instance. After you delete an instance, all tags that are added to the instance are deleted.
        *   You can add up to 20 tags to each instance. Before you add a tag to an instance, the system automatically checks the number of existing tags. An error message is returned if the maximum number of tags is reached.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
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
            vpc_peer_20220101_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: vpc_peer_20220101_models.TagResourcesRequest,
    ) -> vpc_peer_20220101_models.TagResourcesResponse:
        """
        Tags are used to classify instances. Each tag consists of a key-value pair. Before you use tags, take note of the following limits:
        *   The keys of tags that are added to the same instance must be unique.
        *   You cannot create tags without adding them to instances. All tags must be added to instances.
        *   Tag information is not shared across regions.
        For example, you cannot view the tags that are created in the China (Hangzhou) region from the China (Shanghai) region.
        *   For the same account and region, tags added to different VPC peering connections are shared.
        For example, if a tag is added to a VPC peering connection, the tag can also be added to other VPC peering connections within the same account and region. You can modify the key and the value of a tag or remove a tag from an instance. After you delete an instance, all tags that are added to the instance are deleted.
        *   You can add up to 20 tags to each instance. Before you add a tag to an instance, the system automatically checks the number of existing tags. An error message is returned if the maximum number of tags is reached.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: vpc_peer_20220101_models.TagResourcesRequest,
    ) -> vpc_peer_20220101_models.TagResourcesResponse:
        """
        Tags are used to classify instances. Each tag consists of a key-value pair. Before you use tags, take note of the following limits:
        *   The keys of tags that are added to the same instance must be unique.
        *   You cannot create tags without adding them to instances. All tags must be added to instances.
        *   Tag information is not shared across regions.
        For example, you cannot view the tags that are created in the China (Hangzhou) region from the China (Shanghai) region.
        *   For the same account and region, tags added to different VPC peering connections are shared.
        For example, if a tag is added to a VPC peering connection, the tag can also be added to other VPC peering connections within the same account and region. You can modify the key and the value of a tag or remove a tag from an instance. After you delete an instance, all tags that are added to the instance are deleted.
        *   You can add up to 20 tags to each instance. Before you add a tag to an instance, the system automatically checks the number of existing tags. An error message is returned if the maximum number of tags is reached.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: vpc_peer_20220101_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
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
            vpc_peer_20220101_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: vpc_peer_20220101_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_peer_20220101_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
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
            vpc_peer_20220101_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: vpc_peer_20220101_models.UnTagResourcesRequest,
    ) -> vpc_peer_20220101_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: vpc_peer_20220101_models.UnTagResourcesRequest,
    ) -> vpc_peer_20220101_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)
