# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_baas20180731 import models as baas_20180731_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'baas.aliyuncs.com',
            'cn-beijing': 'baas.aliyuncs.com',
            'cn-zhangjiakou': 'baas.aliyuncs.com',
            'cn-huhehaote': 'baas.aliyuncs.com',
            'cn-shanghai': 'baas.aliyuncs.com',
            'cn-shenzhen': 'baas.aliyuncs.com',
            'cn-hongkong': 'baas.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'baas.ap-southeast-1.aliyuncs.com',
            'ap-northeast-1': 'baas.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'baas.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'baas.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'baas.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'baas.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'baas.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('baas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def accept_ethereum_invitation_with_options(
        self,
        request: baas_20180731_models.AcceptEthereumInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AcceptEthereumInvitationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AcceptEthereumInvitation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AcceptEthereumInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_ethereum_invitation_with_options_async(
        self,
        request: baas_20180731_models.AcceptEthereumInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AcceptEthereumInvitationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AcceptEthereumInvitation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AcceptEthereumInvitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_ethereum_invitation(
        self,
        request: baas_20180731_models.AcceptEthereumInvitationRequest,
    ) -> baas_20180731_models.AcceptEthereumInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_ethereum_invitation_with_options(request, runtime)

    async def accept_ethereum_invitation_async(
        self,
        request: baas_20180731_models.AcceptEthereumInvitationRequest,
    ) -> baas_20180731_models.AcceptEthereumInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_ethereum_invitation_with_options_async(request, runtime)

    def accept_invitation_with_options(
        self,
        request: baas_20180731_models.AcceptInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AcceptInvitationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.is_accepted):
            body['IsAccepted'] = request.is_accepted
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AcceptInvitation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AcceptInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_invitation_with_options_async(
        self,
        request: baas_20180731_models.AcceptInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AcceptInvitationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.is_accepted):
            body['IsAccepted'] = request.is_accepted
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AcceptInvitation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AcceptInvitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_invitation(
        self,
        request: baas_20180731_models.AcceptInvitationRequest,
    ) -> baas_20180731_models.AcceptInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_invitation_with_options(request, runtime)

    async def accept_invitation_async(
        self,
        request: baas_20180731_models.AcceptInvitationRequest,
    ) -> baas_20180731_models.AcceptInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_invitation_with_options_async(request, runtime)

    def add_ant_chain_subnet_member_check_with_options(
        self,
        request: baas_20180731_models.AddAntChainSubnetMemberCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AddAntChainSubnetMemberCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAntChainSubnetMemberCheck',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AddAntChainSubnetMemberCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ant_chain_subnet_member_check_with_options_async(
        self,
        request: baas_20180731_models.AddAntChainSubnetMemberCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AddAntChainSubnetMemberCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAntChainSubnetMemberCheck',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AddAntChainSubnetMemberCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ant_chain_subnet_member_check(
        self,
        request: baas_20180731_models.AddAntChainSubnetMemberCheckRequest,
    ) -> baas_20180731_models.AddAntChainSubnetMemberCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ant_chain_subnet_member_check_with_options(request, runtime)

    async def add_ant_chain_subnet_member_check_async(
        self,
        request: baas_20180731_models.AddAntChainSubnetMemberCheckRequest,
    ) -> baas_20180731_models.AddAntChainSubnetMemberCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ant_chain_subnet_member_check_with_options_async(request, runtime)

    def add_ant_chain_subnet_node_check_with_options(
        self,
        request: baas_20180731_models.AddAntChainSubnetNodeCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AddAntChainSubnetNodeCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAntChainSubnetNodeCheck',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AddAntChainSubnetNodeCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ant_chain_subnet_node_check_with_options_async(
        self,
        request: baas_20180731_models.AddAntChainSubnetNodeCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AddAntChainSubnetNodeCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAntChainSubnetNodeCheck',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AddAntChainSubnetNodeCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ant_chain_subnet_node_check(
        self,
        request: baas_20180731_models.AddAntChainSubnetNodeCheckRequest,
    ) -> baas_20180731_models.AddAntChainSubnetNodeCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ant_chain_subnet_node_check_with_options(request, runtime)

    async def add_ant_chain_subnet_node_check_async(
        self,
        request: baas_20180731_models.AddAntChainSubnetNodeCheckRequest,
    ) -> baas_20180731_models.AddAntChainSubnetNodeCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ant_chain_subnet_node_check_with_options_async(request, runtime)

    def add_ethereum_node_with_options(
        self,
        request: baas_20180731_models.AddEthereumNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AddEthereumNodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        if not UtilClient.is_unset(request.external_node):
            body['ExternalNode'] = request.external_node
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEthereumNode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AddEthereumNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ethereum_node_with_options_async(
        self,
        request: baas_20180731_models.AddEthereumNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AddEthereumNodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        if not UtilClient.is_unset(request.external_node):
            body['ExternalNode'] = request.external_node
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEthereumNode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AddEthereumNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ethereum_node(
        self,
        request: baas_20180731_models.AddEthereumNodeRequest,
    ) -> baas_20180731_models.AddEthereumNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ethereum_node_with_options(request, runtime)

    async def add_ethereum_node_async(
        self,
        request: baas_20180731_models.AddEthereumNodeRequest,
    ) -> baas_20180731_models.AddEthereumNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ethereum_node_with_options_async(request, runtime)

    def add_fabric_external_organization_to_channel_with_options(
        self,
        request: baas_20180731_models.AddFabricExternalOrganizationToChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AddFabricExternalOrganizationToChannelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.join_request):
            body['JoinRequest'] = request.join_request
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFabricExternalOrganizationToChannel',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AddFabricExternalOrganizationToChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_fabric_external_organization_to_channel_with_options_async(
        self,
        request: baas_20180731_models.AddFabricExternalOrganizationToChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AddFabricExternalOrganizationToChannelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.join_request):
            body['JoinRequest'] = request.join_request
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFabricExternalOrganizationToChannel',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AddFabricExternalOrganizationToChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_fabric_external_organization_to_channel(
        self,
        request: baas_20180731_models.AddFabricExternalOrganizationToChannelRequest,
    ) -> baas_20180731_models.AddFabricExternalOrganizationToChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_fabric_external_organization_to_channel_with_options(request, runtime)

    async def add_fabric_external_organization_to_channel_async(
        self,
        request: baas_20180731_models.AddFabricExternalOrganizationToChannelRequest,
    ) -> baas_20180731_models.AddFabricExternalOrganizationToChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_fabric_external_organization_to_channel_with_options_async(request, runtime)

    def add_fabric_organization_to_external_channel_with_options(
        self,
        request: baas_20180731_models.AddFabricOrganizationToExternalChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AddFabricOrganizationToExternalChannelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.join_response):
            body['JoinResponse'] = request.join_response
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFabricOrganizationToExternalChannel',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AddFabricOrganizationToExternalChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_fabric_organization_to_external_channel_with_options_async(
        self,
        request: baas_20180731_models.AddFabricOrganizationToExternalChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.AddFabricOrganizationToExternalChannelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.join_response):
            body['JoinResponse'] = request.join_response
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFabricOrganizationToExternalChannel',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.AddFabricOrganizationToExternalChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_fabric_organization_to_external_channel(
        self,
        request: baas_20180731_models.AddFabricOrganizationToExternalChannelRequest,
    ) -> baas_20180731_models.AddFabricOrganizationToExternalChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_fabric_organization_to_external_channel_with_options(request, runtime)

    async def add_fabric_organization_to_external_channel_async(
        self,
        request: baas_20180731_models.AddFabricOrganizationToExternalChannelRequest,
    ) -> baas_20180731_models.AddFabricOrganizationToExternalChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_fabric_organization_to_external_channel_with_options_async(request, runtime)

    def apply_ant_chain_with_options(
        self,
        request: baas_20180731_models.ApplyAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyAntChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.upload_req):
            body['UploadReq'] = request.upload_req
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyAntChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyAntChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ant_chain_with_options_async(
        self,
        request: baas_20180731_models.ApplyAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyAntChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.upload_req):
            body['UploadReq'] = request.upload_req
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyAntChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyAntChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_ant_chain(
        self,
        request: baas_20180731_models.ApplyAntChainRequest,
    ) -> baas_20180731_models.ApplyAntChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_ant_chain_with_options(request, runtime)

    async def apply_ant_chain_async(
        self,
        request: baas_20180731_models.ApplyAntChainRequest,
    ) -> baas_20180731_models.ApplyAntChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_ant_chain_with_options_async(request, runtime)

    def apply_ant_chain_certificate_with_options(
        self,
        request: baas_20180731_models.ApplyAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyAntChainCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.upload_req):
            body['UploadReq'] = request.upload_req
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyAntChainCertificate',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyAntChainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ant_chain_certificate_with_options_async(
        self,
        request: baas_20180731_models.ApplyAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyAntChainCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.upload_req):
            body['UploadReq'] = request.upload_req
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyAntChainCertificate',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyAntChainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_ant_chain_certificate(
        self,
        request: baas_20180731_models.ApplyAntChainCertificateRequest,
    ) -> baas_20180731_models.ApplyAntChainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_ant_chain_certificate_with_options(request, runtime)

    async def apply_ant_chain_certificate_async(
        self,
        request: baas_20180731_models.ApplyAntChainCertificateRequest,
    ) -> baas_20180731_models.ApplyAntChainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_ant_chain_certificate_with_options_async(request, runtime)

    def apply_ant_chain_certificate_with_key_auto_creation_with_options(
        self,
        request: baas_20180731_models.ApplyAntChainCertificateWithKeyAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyAntChainCertificateWithKeyAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.common_name):
            body['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.country_name):
            body['CountryName'] = request.country_name
        if not UtilClient.is_unset(request.locality_name):
            body['LocalityName'] = request.locality_name
        if not UtilClient.is_unset(request.organization_name):
            body['OrganizationName'] = request.organization_name
        if not UtilClient.is_unset(request.organization_unit_name):
            body['OrganizationUnitName'] = request.organization_unit_name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.state_or_province_name):
            body['StateOrProvinceName'] = request.state_or_province_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyAntChainCertificateWithKeyAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyAntChainCertificateWithKeyAutoCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ant_chain_certificate_with_key_auto_creation_with_options_async(
        self,
        request: baas_20180731_models.ApplyAntChainCertificateWithKeyAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyAntChainCertificateWithKeyAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.common_name):
            body['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.country_name):
            body['CountryName'] = request.country_name
        if not UtilClient.is_unset(request.locality_name):
            body['LocalityName'] = request.locality_name
        if not UtilClient.is_unset(request.organization_name):
            body['OrganizationName'] = request.organization_name
        if not UtilClient.is_unset(request.organization_unit_name):
            body['OrganizationUnitName'] = request.organization_unit_name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.state_or_province_name):
            body['StateOrProvinceName'] = request.state_or_province_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyAntChainCertificateWithKeyAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyAntChainCertificateWithKeyAutoCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_ant_chain_certificate_with_key_auto_creation(
        self,
        request: baas_20180731_models.ApplyAntChainCertificateWithKeyAutoCreationRequest,
    ) -> baas_20180731_models.ApplyAntChainCertificateWithKeyAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_ant_chain_certificate_with_key_auto_creation_with_options(request, runtime)

    async def apply_ant_chain_certificate_with_key_auto_creation_async(
        self,
        request: baas_20180731_models.ApplyAntChainCertificateWithKeyAutoCreationRequest,
    ) -> baas_20180731_models.ApplyAntChainCertificateWithKeyAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_ant_chain_certificate_with_key_auto_creation_with_options_async(request, runtime)

    def apply_ant_chain_with_key_auto_creation_with_options(
        self,
        request: baas_20180731_models.ApplyAntChainWithKeyAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyAntChainWithKeyAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.common_name):
            body['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.country_name):
            body['CountryName'] = request.country_name
        if not UtilClient.is_unset(request.locality_name):
            body['LocalityName'] = request.locality_name
        if not UtilClient.is_unset(request.organization_name):
            body['OrganizationName'] = request.organization_name
        if not UtilClient.is_unset(request.organization_unit_name):
            body['OrganizationUnitName'] = request.organization_unit_name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.state_or_province_name):
            body['StateOrProvinceName'] = request.state_or_province_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyAntChainWithKeyAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyAntChainWithKeyAutoCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ant_chain_with_key_auto_creation_with_options_async(
        self,
        request: baas_20180731_models.ApplyAntChainWithKeyAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyAntChainWithKeyAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.common_name):
            body['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.country_name):
            body['CountryName'] = request.country_name
        if not UtilClient.is_unset(request.locality_name):
            body['LocalityName'] = request.locality_name
        if not UtilClient.is_unset(request.organization_name):
            body['OrganizationName'] = request.organization_name
        if not UtilClient.is_unset(request.organization_unit_name):
            body['OrganizationUnitName'] = request.organization_unit_name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.state_or_province_name):
            body['StateOrProvinceName'] = request.state_or_province_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyAntChainWithKeyAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyAntChainWithKeyAutoCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_ant_chain_with_key_auto_creation(
        self,
        request: baas_20180731_models.ApplyAntChainWithKeyAutoCreationRequest,
    ) -> baas_20180731_models.ApplyAntChainWithKeyAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_ant_chain_with_key_auto_creation_with_options(request, runtime)

    async def apply_ant_chain_with_key_auto_creation_async(
        self,
        request: baas_20180731_models.ApplyAntChainWithKeyAutoCreationRequest,
    ) -> baas_20180731_models.ApplyAntChainWithKeyAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_ant_chain_with_key_auto_creation_with_options_async(request, runtime)

    def apply_blockchain_with_options(
        self,
        request: baas_20180731_models.ApplyBlockchainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyBlockchainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.account_pub_key):
            body['AccountPubKey'] = request.account_pub_key
        if not UtilClient.is_unset(request.account_recover_pub_key):
            body['AccountRecoverPubKey'] = request.account_recover_pub_key
        if not UtilClient.is_unset(request.blockchain):
            body['Blockchain'] = request.blockchain
        if not UtilClient.is_unset(request.upload_req):
            body['UploadReq'] = request.upload_req
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyBlockchain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyBlockchainResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_blockchain_with_options_async(
        self,
        request: baas_20180731_models.ApplyBlockchainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyBlockchainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.account_pub_key):
            body['AccountPubKey'] = request.account_pub_key
        if not UtilClient.is_unset(request.account_recover_pub_key):
            body['AccountRecoverPubKey'] = request.account_recover_pub_key
        if not UtilClient.is_unset(request.blockchain):
            body['Blockchain'] = request.blockchain
        if not UtilClient.is_unset(request.upload_req):
            body['UploadReq'] = request.upload_req
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyBlockchain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyBlockchainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_blockchain(
        self,
        request: baas_20180731_models.ApplyBlockchainRequest,
    ) -> baas_20180731_models.ApplyBlockchainResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_blockchain_with_options(request, runtime)

    async def apply_blockchain_async(
        self,
        request: baas_20180731_models.ApplyBlockchainRequest,
    ) -> baas_20180731_models.ApplyBlockchainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_blockchain_with_options_async(request, runtime)

    def apply_blockchain_with_key_auto_creation_with_options(
        self,
        request: baas_20180731_models.ApplyBlockchainWithKeyAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyBlockchainWithKeyAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.common_name):
            body['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country_name):
            body['CountryName'] = request.country_name
        if not UtilClient.is_unset(request.locality_name):
            body['LocalityName'] = request.locality_name
        if not UtilClient.is_unset(request.organization_name):
            body['OrganizationName'] = request.organization_name
        if not UtilClient.is_unset(request.organization_unit_name):
            body['OrganizationUnitName'] = request.organization_unit_name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.state_or_province_name):
            body['StateOrProvinceName'] = request.state_or_province_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyBlockchainWithKeyAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyBlockchainWithKeyAutoCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_blockchain_with_key_auto_creation_with_options_async(
        self,
        request: baas_20180731_models.ApplyBlockchainWithKeyAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyBlockchainWithKeyAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.common_name):
            body['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country_name):
            body['CountryName'] = request.country_name
        if not UtilClient.is_unset(request.locality_name):
            body['LocalityName'] = request.locality_name
        if not UtilClient.is_unset(request.organization_name):
            body['OrganizationName'] = request.organization_name
        if not UtilClient.is_unset(request.organization_unit_name):
            body['OrganizationUnitName'] = request.organization_unit_name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.state_or_province_name):
            body['StateOrProvinceName'] = request.state_or_province_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyBlockchainWithKeyAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyBlockchainWithKeyAutoCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_blockchain_with_key_auto_creation(
        self,
        request: baas_20180731_models.ApplyBlockchainWithKeyAutoCreationRequest,
    ) -> baas_20180731_models.ApplyBlockchainWithKeyAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_blockchain_with_key_auto_creation_with_options(request, runtime)

    async def apply_blockchain_with_key_auto_creation_async(
        self,
        request: baas_20180731_models.ApplyBlockchainWithKeyAutoCreationRequest,
    ) -> baas_20180731_models.ApplyBlockchainWithKeyAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_blockchain_with_key_auto_creation_with_options_async(request, runtime)

    def apply_public_ant_chain_with_options(
        self,
        request: baas_20180731_models.ApplyPublicAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyPublicAntChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.upload_req):
            body['UploadReq'] = request.upload_req
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyPublicAntChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyPublicAntChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_public_ant_chain_with_options_async(
        self,
        request: baas_20180731_models.ApplyPublicAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyPublicAntChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.upload_req):
            body['UploadReq'] = request.upload_req
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyPublicAntChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyPublicAntChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_public_ant_chain(
        self,
        request: baas_20180731_models.ApplyPublicAntChainRequest,
    ) -> baas_20180731_models.ApplyPublicAntChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_public_ant_chain_with_options(request, runtime)

    async def apply_public_ant_chain_async(
        self,
        request: baas_20180731_models.ApplyPublicAntChainRequest,
    ) -> baas_20180731_models.ApplyPublicAntChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_public_ant_chain_with_options_async(request, runtime)

    def apply_public_ant_chain_with_key_auto_creation_with_options(
        self,
        request: baas_20180731_models.ApplyPublicAntChainWithKeyAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyPublicAntChainWithKeyAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.common_name):
            body['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country_name):
            body['CountryName'] = request.country_name
        if not UtilClient.is_unset(request.locality_name):
            body['LocalityName'] = request.locality_name
        if not UtilClient.is_unset(request.organization_name):
            body['OrganizationName'] = request.organization_name
        if not UtilClient.is_unset(request.organization_unit_name):
            body['OrganizationUnitName'] = request.organization_unit_name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.state_or_province_name):
            body['StateOrProvinceName'] = request.state_or_province_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyPublicAntChainWithKeyAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyPublicAntChainWithKeyAutoCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_public_ant_chain_with_key_auto_creation_with_options_async(
        self,
        request: baas_20180731_models.ApplyPublicAntChainWithKeyAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApplyPublicAntChainWithKeyAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.common_name):
            body['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country_name):
            body['CountryName'] = request.country_name
        if not UtilClient.is_unset(request.locality_name):
            body['LocalityName'] = request.locality_name
        if not UtilClient.is_unset(request.organization_name):
            body['OrganizationName'] = request.organization_name
        if not UtilClient.is_unset(request.organization_unit_name):
            body['OrganizationUnitName'] = request.organization_unit_name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.state_or_province_name):
            body['StateOrProvinceName'] = request.state_or_province_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyPublicAntChainWithKeyAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApplyPublicAntChainWithKeyAutoCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_public_ant_chain_with_key_auto_creation(
        self,
        request: baas_20180731_models.ApplyPublicAntChainWithKeyAutoCreationRequest,
    ) -> baas_20180731_models.ApplyPublicAntChainWithKeyAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_public_ant_chain_with_key_auto_creation_with_options(request, runtime)

    async def apply_public_ant_chain_with_key_auto_creation_async(
        self,
        request: baas_20180731_models.ApplyPublicAntChainWithKeyAutoCreationRequest,
    ) -> baas_20180731_models.ApplyPublicAntChainWithKeyAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_public_ant_chain_with_key_auto_creation_with_options_async(request, runtime)

    def approve_ethereum_invitee_with_options(
        self,
        request: baas_20180731_models.ApproveEthereumInviteeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApproveEthereumInviteeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.invitee):
            body['Invitee'] = request.invitee
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApproveEthereumInvitee',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApproveEthereumInviteeResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_ethereum_invitee_with_options_async(
        self,
        request: baas_20180731_models.ApproveEthereumInviteeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApproveEthereumInviteeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.invitee):
            body['Invitee'] = request.invitee
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApproveEthereumInvitee',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApproveEthereumInviteeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_ethereum_invitee(
        self,
        request: baas_20180731_models.ApproveEthereumInviteeRequest,
    ) -> baas_20180731_models.ApproveEthereumInviteeResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_ethereum_invitee_with_options(request, runtime)

    async def approve_ethereum_invitee_async(
        self,
        request: baas_20180731_models.ApproveEthereumInviteeRequest,
    ) -> baas_20180731_models.ApproveEthereumInviteeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_ethereum_invitee_with_options_async(request, runtime)

    def approve_fabric_chaincode_definition_with_options(
        self,
        request: baas_20180731_models.ApproveFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApproveFabricChaincodeDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.chaincode_package_id):
            body['ChaincodePackageId'] = request.chaincode_package_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApproveFabricChaincodeDefinition',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApproveFabricChaincodeDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_fabric_chaincode_definition_with_options_async(
        self,
        request: baas_20180731_models.ApproveFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ApproveFabricChaincodeDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.chaincode_package_id):
            body['ChaincodePackageId'] = request.chaincode_package_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApproveFabricChaincodeDefinition',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ApproveFabricChaincodeDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_fabric_chaincode_definition(
        self,
        request: baas_20180731_models.ApproveFabricChaincodeDefinitionRequest,
    ) -> baas_20180731_models.ApproveFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_fabric_chaincode_definition_with_options(request, runtime)

    async def approve_fabric_chaincode_definition_async(
        self,
        request: baas_20180731_models.ApproveFabricChaincodeDefinitionRequest,
    ) -> baas_20180731_models.ApproveFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_fabric_chaincode_definition_with_options_async(request, runtime)

    def batch_add_ant_chain_mini_app_qrcode_authorized_users_with_options(
        self,
        tmp_req: baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_list):
            request.phone_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_list, 'PhoneList', 'json')
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.phone_list_shrink):
            body['PhoneList'] = request.phone_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddAntChainMiniAppQRCodeAuthorizedUsers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_ant_chain_mini_app_qrcode_authorized_users_with_options_async(
        self,
        tmp_req: baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_list):
            request.phone_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_list, 'PhoneList', 'json')
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.phone_list_shrink):
            body['PhoneList'] = request.phone_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddAntChainMiniAppQRCodeAuthorizedUsers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_ant_chain_mini_app_qrcode_authorized_users(
        self,
        request: baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersRequest,
    ) -> baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_add_ant_chain_mini_app_qrcode_authorized_users_with_options(request, runtime)

    async def batch_add_ant_chain_mini_app_qrcode_authorized_users_async(
        self,
        request: baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersRequest,
    ) -> baas_20180731_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_ant_chain_mini_app_qrcode_authorized_users_with_options_async(request, runtime)

    def bind_fabric_management_chaincode_with_options(
        self,
        request: baas_20180731_models.BindFabricManagementChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.BindFabricManagementChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindFabricManagementChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.BindFabricManagementChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_fabric_management_chaincode_with_options_async(
        self,
        request: baas_20180731_models.BindFabricManagementChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.BindFabricManagementChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindFabricManagementChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.BindFabricManagementChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_fabric_management_chaincode(
        self,
        request: baas_20180731_models.BindFabricManagementChaincodeRequest,
    ) -> baas_20180731_models.BindFabricManagementChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_fabric_management_chaincode_with_options(request, runtime)

    async def bind_fabric_management_chaincode_async(
        self,
        request: baas_20180731_models.BindFabricManagementChaincodeRequest,
    ) -> baas_20180731_models.BindFabricManagementChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_fabric_management_chaincode_with_options_async(request, runtime)

    def check_consortium_domain_with_options(
        self,
        request: baas_20180731_models.CheckConsortiumDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CheckConsortiumDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_code):
            body['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckConsortiumDomain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CheckConsortiumDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_consortium_domain_with_options_async(
        self,
        request: baas_20180731_models.CheckConsortiumDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CheckConsortiumDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_code):
            body['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckConsortiumDomain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CheckConsortiumDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_consortium_domain(
        self,
        request: baas_20180731_models.CheckConsortiumDomainRequest,
    ) -> baas_20180731_models.CheckConsortiumDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_consortium_domain_with_options(request, runtime)

    async def check_consortium_domain_async(
        self,
        request: baas_20180731_models.CheckConsortiumDomainRequest,
    ) -> baas_20180731_models.CheckConsortiumDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_consortium_domain_with_options_async(request, runtime)

    def check_organization_domain_with_options(
        self,
        request: baas_20180731_models.CheckOrganizationDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CheckOrganizationDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_code):
            body['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckOrganizationDomain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CheckOrganizationDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_organization_domain_with_options_async(
        self,
        request: baas_20180731_models.CheckOrganizationDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CheckOrganizationDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_code):
            body['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckOrganizationDomain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CheckOrganizationDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_organization_domain(
        self,
        request: baas_20180731_models.CheckOrganizationDomainRequest,
    ) -> baas_20180731_models.CheckOrganizationDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_organization_domain_with_options(request, runtime)

    async def check_organization_domain_async(
        self,
        request: baas_20180731_models.CheckOrganizationDomainRequest,
    ) -> baas_20180731_models.CheckOrganizationDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_organization_domain_with_options_async(request, runtime)

    def confirm_consortium_member_with_options(
        self,
        request: baas_20180731_models.ConfirmConsortiumMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ConfirmConsortiumMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmConsortiumMember',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ConfirmConsortiumMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_consortium_member_with_options_async(
        self,
        request: baas_20180731_models.ConfirmConsortiumMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ConfirmConsortiumMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmConsortiumMember',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ConfirmConsortiumMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_consortium_member(
        self,
        request: baas_20180731_models.ConfirmConsortiumMemberRequest,
    ) -> baas_20180731_models.ConfirmConsortiumMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_consortium_member_with_options(request, runtime)

    async def confirm_consortium_member_async(
        self,
        request: baas_20180731_models.ConfirmConsortiumMemberRequest,
    ) -> baas_20180731_models.ConfirmConsortiumMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_consortium_member_with_options_async(request, runtime)

    def copy_ant_chain_contract_project_with_options(
        self,
        request: baas_20180731_models.CopyAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CopyAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_description):
            body['ProjectDescription'] = request.project_description
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_version):
            body['ProjectVersion'] = request.project_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyAntChainContractProject',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CopyAntChainContractProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20180731_models.CopyAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CopyAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_description):
            body['ProjectDescription'] = request.project_description
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_version):
            body['ProjectVersion'] = request.project_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyAntChainContractProject',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CopyAntChainContractProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_ant_chain_contract_project(
        self,
        request: baas_20180731_models.CopyAntChainContractProjectRequest,
    ) -> baas_20180731_models.CopyAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_ant_chain_contract_project_with_options(request, runtime)

    async def copy_ant_chain_contract_project_async(
        self,
        request: baas_20180731_models.CopyAntChainContractProjectRequest,
    ) -> baas_20180731_models.CopyAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_ant_chain_contract_project_with_options_async(request, runtime)

    def create_access_token_with_options(
        self,
        request: baas_20180731_models.CreateAccessTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAccessTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_token_lifetime):
            body['AccessTokenLifetime'] = request.access_token_lifetime
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.refresh_token_lifetime):
            body['RefreshTokenLifetime'] = request.refresh_token_lifetime
        if not UtilClient.is_unset(request.scope):
            body['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAccessToken',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_token_with_options_async(
        self,
        request: baas_20180731_models.CreateAccessTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAccessTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_token_lifetime):
            body['AccessTokenLifetime'] = request.access_token_lifetime
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.refresh_token_lifetime):
            body['RefreshTokenLifetime'] = request.refresh_token_lifetime
        if not UtilClient.is_unset(request.scope):
            body['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAccessToken',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_token(
        self,
        request: baas_20180731_models.CreateAccessTokenRequest,
    ) -> baas_20180731_models.CreateAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_token_with_options(request, runtime)

    async def create_access_token_async(
        self,
        request: baas_20180731_models.CreateAccessTokenRequest,
    ) -> baas_20180731_models.CreateAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_token_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: baas_20180731_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.account_pub_key):
            body['AccountPubKey'] = request.account_pub_key
        if not UtilClient.is_unset(request.account_recover_pub_key):
            body['AccountRecoverPubKey'] = request.account_recover_pub_key
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: baas_20180731_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.account_pub_key):
            body['AccountPubKey'] = request.account_pub_key
        if not UtilClient.is_unset(request.account_recover_pub_key):
            body['AccountRecoverPubKey'] = request.account_recover_pub_key
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: baas_20180731_models.CreateAccountRequest,
    ) -> baas_20180731_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: baas_20180731_models.CreateAccountRequest,
    ) -> baas_20180731_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_account_with_key_pair_auto_creation_with_options(
        self,
        request: baas_20180731_models.CreateAccountWithKeyPairAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAccountWithKeyPairAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAccountWithKeyPairAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAccountWithKeyPairAutoCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_key_pair_auto_creation_with_options_async(
        self,
        request: baas_20180731_models.CreateAccountWithKeyPairAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAccountWithKeyPairAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAccountWithKeyPairAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAccountWithKeyPairAutoCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account_with_key_pair_auto_creation(
        self,
        request: baas_20180731_models.CreateAccountWithKeyPairAutoCreationRequest,
    ) -> baas_20180731_models.CreateAccountWithKeyPairAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_key_pair_auto_creation_with_options(request, runtime)

    async def create_account_with_key_pair_auto_creation_async(
        self,
        request: baas_20180731_models.CreateAccountWithKeyPairAutoCreationRequest,
    ) -> baas_20180731_models.CreateAccountWithKeyPairAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_key_pair_auto_creation_with_options_async(request, runtime)

    def create_ant_chain_with_options(
        self,
        request: baas_20180731_models.CreateAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_name):
            body['AntChainName'] = request.ant_chain_name
        if not UtilClient.is_unset(request.blockchain_region_id):
            body['BlockchainRegionId'] = request.blockchain_region_id
        if not UtilClient.is_unset(request.cipher_suit):
            body['CipherSuit'] = request.cipher_suit
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.live_time):
            body['LiveTime'] = request.live_time
        if not UtilClient.is_unset(request.merkle_tree_suit):
            body['MerkleTreeSuit'] = request.merkle_tree_suit
        if not UtilClient.is_unset(request.node_num):
            body['NodeNum'] = request.node_num
        if not UtilClient.is_unset(request.resource_size):
            body['ResourceSize'] = request.resource_size
        if not UtilClient.is_unset(request.tls_algo):
            body['TlsAlgo'] = request.tls_algo
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_chain_with_options_async(
        self,
        request: baas_20180731_models.CreateAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_name):
            body['AntChainName'] = request.ant_chain_name
        if not UtilClient.is_unset(request.blockchain_region_id):
            body['BlockchainRegionId'] = request.blockchain_region_id
        if not UtilClient.is_unset(request.cipher_suit):
            body['CipherSuit'] = request.cipher_suit
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.live_time):
            body['LiveTime'] = request.live_time
        if not UtilClient.is_unset(request.merkle_tree_suit):
            body['MerkleTreeSuit'] = request.merkle_tree_suit
        if not UtilClient.is_unset(request.node_num):
            body['NodeNum'] = request.node_num
        if not UtilClient.is_unset(request.resource_size):
            body['ResourceSize'] = request.resource_size
        if not UtilClient.is_unset(request.tls_algo):
            body['TlsAlgo'] = request.tls_algo
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ant_chain(
        self,
        request: baas_20180731_models.CreateAntChainRequest,
    ) -> baas_20180731_models.CreateAntChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ant_chain_with_options(request, runtime)

    async def create_ant_chain_async(
        self,
        request: baas_20180731_models.CreateAntChainRequest,
    ) -> baas_20180731_models.CreateAntChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ant_chain_with_options_async(request, runtime)

    def create_ant_chain_account_with_options(
        self,
        request: baas_20180731_models.CreateAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.account_pub_key):
            body['AccountPubKey'] = request.account_pub_key
        if not UtilClient.is_unset(request.account_recover_pub_key):
            body['AccountRecoverPubKey'] = request.account_recover_pub_key
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChainAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_chain_account_with_options_async(
        self,
        request: baas_20180731_models.CreateAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.account_pub_key):
            body['AccountPubKey'] = request.account_pub_key
        if not UtilClient.is_unset(request.account_recover_pub_key):
            body['AccountRecoverPubKey'] = request.account_recover_pub_key
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChainAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ant_chain_account(
        self,
        request: baas_20180731_models.CreateAntChainAccountRequest,
    ) -> baas_20180731_models.CreateAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ant_chain_account_with_options(request, runtime)

    async def create_ant_chain_account_async(
        self,
        request: baas_20180731_models.CreateAntChainAccountRequest,
    ) -> baas_20180731_models.CreateAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ant_chain_account_with_options_async(request, runtime)

    def create_ant_chain_account_with_key_pair_auto_creation_with_options(
        self,
        request: baas_20180731_models.CreateAntChainAccountWithKeyPairAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainAccountWithKeyPairAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.recover_password):
            body['RecoverPassword'] = request.recover_password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChainAccountWithKeyPairAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainAccountWithKeyPairAutoCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_chain_account_with_key_pair_auto_creation_with_options_async(
        self,
        request: baas_20180731_models.CreateAntChainAccountWithKeyPairAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainAccountWithKeyPairAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.recover_password):
            body['RecoverPassword'] = request.recover_password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChainAccountWithKeyPairAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainAccountWithKeyPairAutoCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ant_chain_account_with_key_pair_auto_creation(
        self,
        request: baas_20180731_models.CreateAntChainAccountWithKeyPairAutoCreationRequest,
    ) -> baas_20180731_models.CreateAntChainAccountWithKeyPairAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ant_chain_account_with_key_pair_auto_creation_with_options(request, runtime)

    async def create_ant_chain_account_with_key_pair_auto_creation_async(
        self,
        request: baas_20180731_models.CreateAntChainAccountWithKeyPairAutoCreationRequest,
    ) -> baas_20180731_models.CreateAntChainAccountWithKeyPairAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ant_chain_account_with_key_pair_auto_creation_with_options_async(request, runtime)

    def create_ant_chain_consortium_with_options(
        self,
        request: baas_20180731_models.CreateAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_description):
            body['ConsortiumDescription'] = request.consortium_description
        if not UtilClient.is_unset(request.consortium_name):
            body['ConsortiumName'] = request.consortium_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChainConsortium',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainConsortiumResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_chain_consortium_with_options_async(
        self,
        request: baas_20180731_models.CreateAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_description):
            body['ConsortiumDescription'] = request.consortium_description
        if not UtilClient.is_unset(request.consortium_name):
            body['ConsortiumName'] = request.consortium_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChainConsortium',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainConsortiumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ant_chain_consortium(
        self,
        request: baas_20180731_models.CreateAntChainConsortiumRequest,
    ) -> baas_20180731_models.CreateAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ant_chain_consortium_with_options(request, runtime)

    async def create_ant_chain_consortium_async(
        self,
        request: baas_20180731_models.CreateAntChainConsortiumRequest,
    ) -> baas_20180731_models.CreateAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ant_chain_consortium_with_options_async(request, runtime)

    def create_ant_chain_contract_content_with_options(
        self,
        request: baas_20180731_models.CreateAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainContractContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_name):
            body['ContentName'] = request.content_name
        if not UtilClient.is_unset(request.is_directory):
            body['IsDirectory'] = request.is_directory
        if not UtilClient.is_unset(request.parent_content_id):
            body['ParentContentId'] = request.parent_content_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChainContractContent',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainContractContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_chain_contract_content_with_options_async(
        self,
        request: baas_20180731_models.CreateAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainContractContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_name):
            body['ContentName'] = request.content_name
        if not UtilClient.is_unset(request.is_directory):
            body['IsDirectory'] = request.is_directory
        if not UtilClient.is_unset(request.parent_content_id):
            body['ParentContentId'] = request.parent_content_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChainContractContent',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainContractContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ant_chain_contract_content(
        self,
        request: baas_20180731_models.CreateAntChainContractContentRequest,
    ) -> baas_20180731_models.CreateAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ant_chain_contract_content_with_options(request, runtime)

    async def create_ant_chain_contract_content_async(
        self,
        request: baas_20180731_models.CreateAntChainContractContentRequest,
    ) -> baas_20180731_models.CreateAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ant_chain_contract_content_with_options_async(request, runtime)

    def create_ant_chain_contract_project_with_options(
        self,
        request: baas_20180731_models.CreateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.project_description):
            body['ProjectDescription'] = request.project_description
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_version):
            body['ProjectVersion'] = request.project_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChainContractProject',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainContractProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20180731_models.CreateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.project_description):
            body['ProjectDescription'] = request.project_description
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_version):
            body['ProjectVersion'] = request.project_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAntChainContractProject',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateAntChainContractProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ant_chain_contract_project(
        self,
        request: baas_20180731_models.CreateAntChainContractProjectRequest,
    ) -> baas_20180731_models.CreateAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ant_chain_contract_project_with_options(request, runtime)

    async def create_ant_chain_contract_project_async(
        self,
        request: baas_20180731_models.CreateAntChainContractProjectRequest,
    ) -> baas_20180731_models.CreateAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ant_chain_contract_project_with_options_async(request, runtime)

    def create_blockchain_with_options(
        self,
        request: baas_20180731_models.CreateBlockchainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateBlockchainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.blockchain_region_id):
            body['BlockchainRegionId'] = request.blockchain_region_id
        if not UtilClient.is_unset(request.blockchain_type):
            body['BlockchainType'] = request.blockchain_type
        if not UtilClient.is_unset(request.cipher_suit):
            body['CipherSuit'] = request.cipher_suit
        if not UtilClient.is_unset(request.live_time):
            body['LiveTime'] = request.live_time
        if not UtilClient.is_unset(request.machine_num):
            body['MachineNum'] = request.machine_num
        if not UtilClient.is_unset(request.merkle_tree_suit):
            body['MerkleTreeSuit'] = request.merkle_tree_suit
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tls_algo):
            body['TlsAlgo'] = request.tls_algo
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBlockchain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateBlockchainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_blockchain_with_options_async(
        self,
        request: baas_20180731_models.CreateBlockchainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateBlockchainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.blockchain_region_id):
            body['BlockchainRegionId'] = request.blockchain_region_id
        if not UtilClient.is_unset(request.blockchain_type):
            body['BlockchainType'] = request.blockchain_type
        if not UtilClient.is_unset(request.cipher_suit):
            body['CipherSuit'] = request.cipher_suit
        if not UtilClient.is_unset(request.live_time):
            body['LiveTime'] = request.live_time
        if not UtilClient.is_unset(request.machine_num):
            body['MachineNum'] = request.machine_num
        if not UtilClient.is_unset(request.merkle_tree_suit):
            body['MerkleTreeSuit'] = request.merkle_tree_suit
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tls_algo):
            body['TlsAlgo'] = request.tls_algo
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBlockchain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateBlockchainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_blockchain(
        self,
        request: baas_20180731_models.CreateBlockchainRequest,
    ) -> baas_20180731_models.CreateBlockchainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_blockchain_with_options(request, runtime)

    async def create_blockchain_async(
        self,
        request: baas_20180731_models.CreateBlockchainRequest,
    ) -> baas_20180731_models.CreateBlockchainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_blockchain_with_options_async(request, runtime)

    def create_blockchain_application_with_options(
        self,
        request: baas_20180731_models.CreateBlockchainApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateBlockchainApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.blockchain_region_id):
            body['BlockchainRegionId'] = request.blockchain_region_id
        if not UtilClient.is_unset(request.blockchain_type):
            body['BlockchainType'] = request.blockchain_type
        if not UtilClient.is_unset(request.cipher_suit):
            body['CipherSuit'] = request.cipher_suit
        if not UtilClient.is_unset(request.live_time):
            body['LiveTime'] = request.live_time
        if not UtilClient.is_unset(request.machine_num):
            body['MachineNum'] = request.machine_num
        if not UtilClient.is_unset(request.merkle_tree_suit):
            body['MerkleTreeSuit'] = request.merkle_tree_suit
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tls_algo):
            body['TlsAlgo'] = request.tls_algo
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBlockchainApplication',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateBlockchainApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_blockchain_application_with_options_async(
        self,
        request: baas_20180731_models.CreateBlockchainApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateBlockchainApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.blockchain_region_id):
            body['BlockchainRegionId'] = request.blockchain_region_id
        if not UtilClient.is_unset(request.blockchain_type):
            body['BlockchainType'] = request.blockchain_type
        if not UtilClient.is_unset(request.cipher_suit):
            body['CipherSuit'] = request.cipher_suit
        if not UtilClient.is_unset(request.live_time):
            body['LiveTime'] = request.live_time
        if not UtilClient.is_unset(request.machine_num):
            body['MachineNum'] = request.machine_num
        if not UtilClient.is_unset(request.merkle_tree_suit):
            body['MerkleTreeSuit'] = request.merkle_tree_suit
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tls_algo):
            body['TlsAlgo'] = request.tls_algo
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBlockchainApplication',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateBlockchainApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_blockchain_application(
        self,
        request: baas_20180731_models.CreateBlockchainApplicationRequest,
    ) -> baas_20180731_models.CreateBlockchainApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_blockchain_application_with_options(request, runtime)

    async def create_blockchain_application_async(
        self,
        request: baas_20180731_models.CreateBlockchainApplicationRequest,
    ) -> baas_20180731_models.CreateBlockchainApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_blockchain_application_with_options_async(request, runtime)

    def create_blockchain_apply_with_options(
        self,
        request: baas_20180731_models.CreateBlockchainApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateBlockchainApplyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.live_time):
            body['LiveTime'] = request.live_time
        if not UtilClient.is_unset(request.machine_num):
            body['MachineNum'] = request.machine_num
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBlockchainApply',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateBlockchainApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_blockchain_apply_with_options_async(
        self,
        request: baas_20180731_models.CreateBlockchainApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateBlockchainApplyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.live_time):
            body['LiveTime'] = request.live_time
        if not UtilClient.is_unset(request.machine_num):
            body['MachineNum'] = request.machine_num
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBlockchainApply',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateBlockchainApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_blockchain_apply(
        self,
        request: baas_20180731_models.CreateBlockchainApplyRequest,
    ) -> baas_20180731_models.CreateBlockchainApplyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_blockchain_apply_with_options(request, runtime)

    async def create_blockchain_apply_async(
        self,
        request: baas_20180731_models.CreateBlockchainApplyRequest,
    ) -> baas_20180731_models.CreateBlockchainApplyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_blockchain_apply_with_options_async(request, runtime)

    def create_chaincode_with_options(
        self,
        request: baas_20180731_models.CreateChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.endorse_policy):
            body['EndorsePolicy'] = request.endorse_policy
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.oss_bucket):
            body['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_url):
            body['OssUrl'] = request.oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chaincode_with_options_async(
        self,
        request: baas_20180731_models.CreateChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.endorse_policy):
            body['EndorsePolicy'] = request.endorse_policy
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.oss_bucket):
            body['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_url):
            body['OssUrl'] = request.oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chaincode(
        self,
        request: baas_20180731_models.CreateChaincodeRequest,
    ) -> baas_20180731_models.CreateChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_chaincode_with_options(request, runtime)

    async def create_chaincode_async(
        self,
        request: baas_20180731_models.CreateChaincodeRequest,
    ) -> baas_20180731_models.CreateChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_chaincode_with_options_async(request, runtime)

    def create_channel_with_options(
        self,
        request: baas_20180731_models.CreateChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_name):
            query['ChannelName'] = request.channel_name
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        body = {}
        if not UtilClient.is_unset(request.batch_timeout):
            body['BatchTimeout'] = request.batch_timeout
        if not UtilClient.is_unset(request.max_message_count):
            body['MaxMessageCount'] = request.max_message_count
        if not UtilClient.is_unset(request.preferred_max_bytes):
            body['PreferredMaxBytes'] = request.preferred_max_bytes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateChannel',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_channel_with_options_async(
        self,
        request: baas_20180731_models.CreateChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_name):
            query['ChannelName'] = request.channel_name
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        body = {}
        if not UtilClient.is_unset(request.batch_timeout):
            body['BatchTimeout'] = request.batch_timeout
        if not UtilClient.is_unset(request.max_message_count):
            body['MaxMessageCount'] = request.max_message_count
        if not UtilClient.is_unset(request.preferred_max_bytes):
            body['PreferredMaxBytes'] = request.preferred_max_bytes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateChannel',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_channel(
        self,
        request: baas_20180731_models.CreateChannelRequest,
    ) -> baas_20180731_models.CreateChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_channel_with_options(request, runtime)

    async def create_channel_async(
        self,
        request: baas_20180731_models.CreateChannelRequest,
    ) -> baas_20180731_models.CreateChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_channel_with_options_async(request, runtime)

    def create_channel_member_with_options(
        self,
        request: baas_20180731_models.CreateChannelMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateChannelMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChannelMember',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateChannelMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_channel_member_with_options_async(
        self,
        request: baas_20180731_models.CreateChannelMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateChannelMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChannelMember',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateChannelMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_channel_member(
        self,
        request: baas_20180731_models.CreateChannelMemberRequest,
    ) -> baas_20180731_models.CreateChannelMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_channel_member_with_options(request, runtime)

    async def create_channel_member_async(
        self,
        request: baas_20180731_models.CreateChannelMemberRequest,
    ) -> baas_20180731_models.CreateChannelMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_channel_member_with_options_async(request, runtime)

    def create_cloud_integration_service_token_with_options(
        self,
        request: baas_20180731_models.CreateCloudIntegrationServiceTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateCloudIntegrationServiceTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudIntegrationServiceToken',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateCloudIntegrationServiceTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_integration_service_token_with_options_async(
        self,
        request: baas_20180731_models.CreateCloudIntegrationServiceTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateCloudIntegrationServiceTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudIntegrationServiceToken',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateCloudIntegrationServiceTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_integration_service_token(
        self,
        request: baas_20180731_models.CreateCloudIntegrationServiceTokenRequest,
    ) -> baas_20180731_models.CreateCloudIntegrationServiceTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_integration_service_token_with_options(request, runtime)

    async def create_cloud_integration_service_token_async(
        self,
        request: baas_20180731_models.CreateCloudIntegrationServiceTokenRequest,
    ) -> baas_20180731_models.CreateCloudIntegrationServiceTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_integration_service_token_with_options_async(request, runtime)

    def create_cloud_service_integration_with_options(
        self,
        request: baas_20180731_models.CreateCloudServiceIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateCloudServiceIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudServiceIntegration',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateCloudServiceIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_service_integration_with_options_async(
        self,
        request: baas_20180731_models.CreateCloudServiceIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateCloudServiceIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudServiceIntegration',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateCloudServiceIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_service_integration(
        self,
        request: baas_20180731_models.CreateCloudServiceIntegrationRequest,
    ) -> baas_20180731_models.CreateCloudServiceIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_service_integration_with_options(request, runtime)

    async def create_cloud_service_integration_async(
        self,
        request: baas_20180731_models.CreateCloudServiceIntegrationRequest,
    ) -> baas_20180731_models.CreateCloudServiceIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_service_integration_with_options_async(request, runtime)

    def create_cloud_service_session_with_options(
        self,
        request: baas_20180731_models.CreateCloudServiceSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateCloudServiceSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudServiceSession',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateCloudServiceSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_service_session_with_options_async(
        self,
        request: baas_20180731_models.CreateCloudServiceSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateCloudServiceSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudServiceSession',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateCloudServiceSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_service_session(
        self,
        request: baas_20180731_models.CreateCloudServiceSessionRequest,
    ) -> baas_20180731_models.CreateCloudServiceSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_service_session_with_options(request, runtime)

    async def create_cloud_service_session_async(
        self,
        request: baas_20180731_models.CreateCloudServiceSessionRequest,
    ) -> baas_20180731_models.CreateCloudServiceSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_service_session_with_options_async(request, runtime)

    def create_consortium_with_options(
        self,
        request: baas_20180731_models.CreateConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_policy):
            body['ChannelPolicy'] = request.channel_policy
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.major_version):
            body['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.orderer_type):
            body['OrdererType'] = request.orderer_type
        if not UtilClient.is_unset(request.orderers_count):
            body['OrderersCount'] = request.orderers_count
        if not UtilClient.is_unset(request.organization):
            body['Organization'] = request.organization
        if not UtilClient.is_unset(request.peers_count):
            body['PeersCount'] = request.peers_count
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.spec_name):
            body['SpecName'] = request.spec_name
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsortium',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateConsortiumResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consortium_with_options_async(
        self,
        request: baas_20180731_models.CreateConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_policy):
            body['ChannelPolicy'] = request.channel_policy
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.major_version):
            body['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.orderer_type):
            body['OrdererType'] = request.orderer_type
        if not UtilClient.is_unset(request.orderers_count):
            body['OrderersCount'] = request.orderers_count
        if not UtilClient.is_unset(request.organization):
            body['Organization'] = request.organization
        if not UtilClient.is_unset(request.peers_count):
            body['PeersCount'] = request.peers_count
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.spec_name):
            body['SpecName'] = request.spec_name
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsortium',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateConsortiumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consortium(
        self,
        request: baas_20180731_models.CreateConsortiumRequest,
    ) -> baas_20180731_models.CreateConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_consortium_with_options(request, runtime)

    async def create_consortium_async(
        self,
        request: baas_20180731_models.CreateConsortiumRequest,
    ) -> baas_20180731_models.CreateConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_consortium_with_options_async(request, runtime)

    def create_consortium_member_with_options(
        self,
        request: baas_20180731_models.CreateConsortiumMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateConsortiumMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsortiumMember',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateConsortiumMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consortium_member_with_options_async(
        self,
        request: baas_20180731_models.CreateConsortiumMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateConsortiumMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsortiumMember',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateConsortiumMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consortium_member(
        self,
        request: baas_20180731_models.CreateConsortiumMemberRequest,
    ) -> baas_20180731_models.CreateConsortiumMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_consortium_member_with_options(request, runtime)

    async def create_consortium_member_async(
        self,
        request: baas_20180731_models.CreateConsortiumMemberRequest,
    ) -> baas_20180731_models.CreateConsortiumMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_consortium_member_with_options_async(request, runtime)

    def create_ecosphere_with_options(
        self,
        request: baas_20180731_models.CreateEcosphereRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateEcosphereResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_policy):
            body['ChannelPolicy'] = request.channel_policy
        if not UtilClient.is_unset(request.consortium_name):
            body['ConsortiumName'] = request.consortium_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.major_version):
            body['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.orderer_domain):
            body['OrdererDomain'] = request.orderer_domain
        if not UtilClient.is_unset(request.orderer_type):
            body['OrdererType'] = request.orderer_type
        if not UtilClient.is_unset(request.orderers_count):
            body['OrderersCount'] = request.orderers_count
        if not UtilClient.is_unset(request.organization):
            body['Organization'] = request.organization
        if not UtilClient.is_unset(request.peers_count):
            body['PeersCount'] = request.peers_count
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.spec_name):
            body['SpecName'] = request.spec_name
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEcosphere',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateEcosphereResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ecosphere_with_options_async(
        self,
        request: baas_20180731_models.CreateEcosphereRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateEcosphereResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_policy):
            body['ChannelPolicy'] = request.channel_policy
        if not UtilClient.is_unset(request.consortium_name):
            body['ConsortiumName'] = request.consortium_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.major_version):
            body['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.orderer_domain):
            body['OrdererDomain'] = request.orderer_domain
        if not UtilClient.is_unset(request.orderer_type):
            body['OrdererType'] = request.orderer_type
        if not UtilClient.is_unset(request.orderers_count):
            body['OrderersCount'] = request.orderers_count
        if not UtilClient.is_unset(request.organization):
            body['Organization'] = request.organization
        if not UtilClient.is_unset(request.peers_count):
            body['PeersCount'] = request.peers_count
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.spec_name):
            body['SpecName'] = request.spec_name
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEcosphere',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateEcosphereResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ecosphere(
        self,
        request: baas_20180731_models.CreateEcosphereRequest,
    ) -> baas_20180731_models.CreateEcosphereResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ecosphere_with_options(request, runtime)

    async def create_ecosphere_async(
        self,
        request: baas_20180731_models.CreateEcosphereRequest,
    ) -> baas_20180731_models.CreateEcosphereResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ecosphere_with_options_async(request, runtime)

    def create_ethereum_with_options(
        self,
        request: baas_20180731_models.CreateEthereumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateEthereumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consensus):
            body['Consensus'] = request.consensus
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.difficulty):
            body['Difficulty'] = request.difficulty
        if not UtilClient.is_unset(request.gas):
            body['Gas'] = request.gas
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.network_id):
            body['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.node):
            body['Node'] = request.node
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEthereum',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateEthereumResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ethereum_with_options_async(
        self,
        request: baas_20180731_models.CreateEthereumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateEthereumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consensus):
            body['Consensus'] = request.consensus
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.difficulty):
            body['Difficulty'] = request.difficulty
        if not UtilClient.is_unset(request.gas):
            body['Gas'] = request.gas
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.network_id):
            body['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.node):
            body['Node'] = request.node
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEthereum',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateEthereumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ethereum(
        self,
        request: baas_20180731_models.CreateEthereumRequest,
    ) -> baas_20180731_models.CreateEthereumResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ethereum_with_options(request, runtime)

    async def create_ethereum_async(
        self,
        request: baas_20180731_models.CreateEthereumRequest,
    ) -> baas_20180731_models.CreateEthereumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ethereum_with_options_async(request, runtime)

    def create_ethereum_invitation_with_options(
        self,
        request: baas_20180731_models.CreateEthereumInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateEthereumInvitationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEthereumInvitation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateEthereumInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ethereum_invitation_with_options_async(
        self,
        request: baas_20180731_models.CreateEthereumInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateEthereumInvitationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEthereumInvitation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateEthereumInvitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ethereum_invitation(
        self,
        request: baas_20180731_models.CreateEthereumInvitationRequest,
    ) -> baas_20180731_models.CreateEthereumInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ethereum_invitation_with_options(request, runtime)

    async def create_ethereum_invitation_async(
        self,
        request: baas_20180731_models.CreateEthereumInvitationRequest,
    ) -> baas_20180731_models.CreateEthereumInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ethereum_invitation_with_options_async(request, runtime)

    def create_fabric_chaincode_package_with_options(
        self,
        request: baas_20180731_models.CreateFabricChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateFabricChaincodePackageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.oss_bucket):
            body['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_url):
            body['OssUrl'] = request.oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFabricChaincodePackage',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateFabricChaincodePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fabric_chaincode_package_with_options_async(
        self,
        request: baas_20180731_models.CreateFabricChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateFabricChaincodePackageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.oss_bucket):
            body['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_url):
            body['OssUrl'] = request.oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFabricChaincodePackage',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateFabricChaincodePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fabric_chaincode_package(
        self,
        request: baas_20180731_models.CreateFabricChaincodePackageRequest,
    ) -> baas_20180731_models.CreateFabricChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fabric_chaincode_package_with_options(request, runtime)

    async def create_fabric_chaincode_package_async(
        self,
        request: baas_20180731_models.CreateFabricChaincodePackageRequest,
    ) -> baas_20180731_models.CreateFabricChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fabric_chaincode_package_with_options_async(request, runtime)

    def create_organization_with_options(
        self,
        request: baas_20180731_models.CreateOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.peers_count):
            query['PeersCount'] = request.peers_count
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.spec_name):
            query['SpecName'] = request.spec_name
        body = {}
        if not UtilClient.is_unset(request.major_version):
            body['MajorVersion'] = request.major_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrganization',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_organization_with_options_async(
        self,
        request: baas_20180731_models.CreateOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.peers_count):
            query['PeersCount'] = request.peers_count
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.spec_name):
            query['SpecName'] = request.spec_name
        body = {}
        if not UtilClient.is_unset(request.major_version):
            body['MajorVersion'] = request.major_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrganization',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_organization(
        self,
        request: baas_20180731_models.CreateOrganizationRequest,
    ) -> baas_20180731_models.CreateOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_organization_with_options(request, runtime)

    async def create_organization_async(
        self,
        request: baas_20180731_models.CreateOrganizationRequest,
    ) -> baas_20180731_models.CreateOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_organization_with_options_async(request, runtime)

    def create_organization_user_with_options(
        self,
        request: baas_20180731_models.CreateOrganizationUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateOrganizationUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attrs):
            body['Attrs'] = request.attrs
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrganizationUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateOrganizationUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_organization_user_with_options_async(
        self,
        request: baas_20180731_models.CreateOrganizationUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateOrganizationUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attrs):
            body['Attrs'] = request.attrs
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrganizationUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateOrganizationUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_organization_user(
        self,
        request: baas_20180731_models.CreateOrganizationUserRequest,
    ) -> baas_20180731_models.CreateOrganizationUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_organization_user_with_options(request, runtime)

    async def create_organization_user_async(
        self,
        request: baas_20180731_models.CreateOrganizationUserRequest,
    ) -> baas_20180731_models.CreateOrganizationUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_organization_user_with_options_async(request, runtime)

    def create_own_account_with_options(
        self,
        request: baas_20180731_models.CreateOwnAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateOwnAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        if not UtilClient.is_unset(request.public_key):
            body['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.recovery_key):
            body['RecoveryKey'] = request.recovery_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOwnAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateOwnAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_own_account_with_options_async(
        self,
        request: baas_20180731_models.CreateOwnAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateOwnAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        if not UtilClient.is_unset(request.public_key):
            body['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.recovery_key):
            body['RecoveryKey'] = request.recovery_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOwnAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateOwnAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_own_account(
        self,
        request: baas_20180731_models.CreateOwnAccountRequest,
    ) -> baas_20180731_models.CreateOwnAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_own_account_with_options(request, runtime)

    async def create_own_account_async(
        self,
        request: baas_20180731_models.CreateOwnAccountRequest,
    ) -> baas_20180731_models.CreateOwnAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_own_account_with_options_async(request, runtime)

    def create_public_account_with_key_pair_auto_creation_with_options(
        self,
        request: baas_20180731_models.CreatePublicAccountWithKeyPairAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreatePublicAccountWithKeyPairAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.recover_password):
            body['RecoverPassword'] = request.recover_password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePublicAccountWithKeyPairAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreatePublicAccountWithKeyPairAutoCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_public_account_with_key_pair_auto_creation_with_options_async(
        self,
        request: baas_20180731_models.CreatePublicAccountWithKeyPairAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreatePublicAccountWithKeyPairAutoCreationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.recover_password):
            body['RecoverPassword'] = request.recover_password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePublicAccountWithKeyPairAutoCreation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreatePublicAccountWithKeyPairAutoCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_public_account_with_key_pair_auto_creation(
        self,
        request: baas_20180731_models.CreatePublicAccountWithKeyPairAutoCreationRequest,
    ) -> baas_20180731_models.CreatePublicAccountWithKeyPairAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_public_account_with_key_pair_auto_creation_with_options(request, runtime)

    async def create_public_account_with_key_pair_auto_creation_async(
        self,
        request: baas_20180731_models.CreatePublicAccountWithKeyPairAutoCreationRequest,
    ) -> baas_20180731_models.CreatePublicAccountWithKeyPairAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_public_account_with_key_pair_auto_creation_with_options_async(request, runtime)

    def create_public_ant_chain_account_with_options(
        self,
        request: baas_20180731_models.CreatePublicAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreatePublicAntChainAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.account_pub_key):
            body['AccountPubKey'] = request.account_pub_key
        if not UtilClient.is_unset(request.account_recover_pub_key):
            body['AccountRecoverPubKey'] = request.account_recover_pub_key
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePublicAntChainAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreatePublicAntChainAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_public_ant_chain_account_with_options_async(
        self,
        request: baas_20180731_models.CreatePublicAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreatePublicAntChainAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.account_pub_key):
            body['AccountPubKey'] = request.account_pub_key
        if not UtilClient.is_unset(request.account_recover_pub_key):
            body['AccountRecoverPubKey'] = request.account_recover_pub_key
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePublicAntChainAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreatePublicAntChainAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_public_ant_chain_account(
        self,
        request: baas_20180731_models.CreatePublicAntChainAccountRequest,
    ) -> baas_20180731_models.CreatePublicAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_public_ant_chain_account_with_options(request, runtime)

    async def create_public_ant_chain_account_async(
        self,
        request: baas_20180731_models.CreatePublicAntChainAccountRequest,
    ) -> baas_20180731_models.CreatePublicAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_public_ant_chain_account_with_options_async(request, runtime)

    def create_smart_contract_job_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateSmartContractJobResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CreateSmartContractJob',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateSmartContractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_smart_contract_job_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateSmartContractJobResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CreateSmartContractJob',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateSmartContractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_smart_contract_job(self) -> baas_20180731_models.CreateSmartContractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_smart_contract_job_with_options(runtime)

    async def create_smart_contract_job_async(self) -> baas_20180731_models.CreateSmartContractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_smart_contract_job_with_options_async(runtime)

    def create_trigger_with_options(
        self,
        request: baas_20180731_models.CreateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trigger_with_options_async(
        self,
        request: baas_20180731_models.CreateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.CreateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.CreateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trigger(
        self,
        request: baas_20180731_models.CreateTriggerRequest,
    ) -> baas_20180731_models.CreateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_trigger_with_options(request, runtime)

    async def create_trigger_async(
        self,
        request: baas_20180731_models.CreateTriggerRequest,
    ) -> baas_20180731_models.CreateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_trigger_with_options_async(request, runtime)

    def delete_ant_chain_consortium_with_options(
        self,
        request: baas_20180731_models.DeleteAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainConsortium',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteAntChainConsortiumResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ant_chain_consortium_with_options_async(
        self,
        request: baas_20180731_models.DeleteAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainConsortium',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteAntChainConsortiumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ant_chain_consortium(
        self,
        request: baas_20180731_models.DeleteAntChainConsortiumRequest,
    ) -> baas_20180731_models.DeleteAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ant_chain_consortium_with_options(request, runtime)

    async def delete_ant_chain_consortium_async(
        self,
        request: baas_20180731_models.DeleteAntChainConsortiumRequest,
    ) -> baas_20180731_models.DeleteAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ant_chain_consortium_with_options_async(request, runtime)

    def delete_ant_chain_contract_content_with_options(
        self,
        request: baas_20180731_models.DeleteAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteAntChainContractContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content_id):
            body['ContentId'] = request.content_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainContractContent',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteAntChainContractContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ant_chain_contract_content_with_options_async(
        self,
        request: baas_20180731_models.DeleteAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteAntChainContractContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content_id):
            body['ContentId'] = request.content_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainContractContent',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteAntChainContractContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ant_chain_contract_content(
        self,
        request: baas_20180731_models.DeleteAntChainContractContentRequest,
    ) -> baas_20180731_models.DeleteAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ant_chain_contract_content_with_options(request, runtime)

    async def delete_ant_chain_contract_content_async(
        self,
        request: baas_20180731_models.DeleteAntChainContractContentRequest,
    ) -> baas_20180731_models.DeleteAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ant_chain_contract_content_with_options_async(request, runtime)

    def delete_ant_chain_contract_project_with_options(
        self,
        request: baas_20180731_models.DeleteAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainContractProject',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteAntChainContractProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20180731_models.DeleteAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainContractProject',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteAntChainContractProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ant_chain_contract_project(
        self,
        request: baas_20180731_models.DeleteAntChainContractProjectRequest,
    ) -> baas_20180731_models.DeleteAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ant_chain_contract_project_with_options(request, runtime)

    async def delete_ant_chain_contract_project_async(
        self,
        request: baas_20180731_models.DeleteAntChainContractProjectRequest,
    ) -> baas_20180731_models.DeleteAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ant_chain_contract_project_with_options_async(request, runtime)

    def delete_ant_chain_mini_app_qrcode_authorized_user_with_options(
        self,
        request: baas_20180731_models.DeleteAntChainMiniAppQRCodeAuthorizedUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainMiniAppQRCodeAuthorizedUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ant_chain_mini_app_qrcode_authorized_user_with_options_async(
        self,
        request: baas_20180731_models.DeleteAntChainMiniAppQRCodeAuthorizedUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainMiniAppQRCodeAuthorizedUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ant_chain_mini_app_qrcode_authorized_user(
        self,
        request: baas_20180731_models.DeleteAntChainMiniAppQRCodeAuthorizedUserRequest,
    ) -> baas_20180731_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ant_chain_mini_app_qrcode_authorized_user_with_options(request, runtime)

    async def delete_ant_chain_mini_app_qrcode_authorized_user_async(
        self,
        request: baas_20180731_models.DeleteAntChainMiniAppQRCodeAuthorizedUserRequest,
    ) -> baas_20180731_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ant_chain_mini_app_qrcode_authorized_user_with_options_async(request, runtime)

    def delete_chaincode_with_options(
        self,
        request: baas_20180731_models.DeleteChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chaincode_with_options_async(
        self,
        request: baas_20180731_models.DeleteChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chaincode(
        self,
        request: baas_20180731_models.DeleteChaincodeRequest,
    ) -> baas_20180731_models.DeleteChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_chaincode_with_options(request, runtime)

    async def delete_chaincode_async(
        self,
        request: baas_20180731_models.DeleteChaincodeRequest,
    ) -> baas_20180731_models.DeleteChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_chaincode_with_options_async(request, runtime)

    def delete_governance_task_with_options(
        self,
        request: baas_20180731_models.DeleteGovernanceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteGovernanceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGovernanceTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteGovernanceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_governance_task_with_options_async(
        self,
        request: baas_20180731_models.DeleteGovernanceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteGovernanceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGovernanceTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteGovernanceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_governance_task(
        self,
        request: baas_20180731_models.DeleteGovernanceTaskRequest,
    ) -> baas_20180731_models.DeleteGovernanceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_governance_task_with_options(request, runtime)

    async def delete_governance_task_async(
        self,
        request: baas_20180731_models.DeleteGovernanceTaskRequest,
    ) -> baas_20180731_models.DeleteGovernanceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_governance_task_with_options_async(request, runtime)

    def delete_trigger_with_options(
        self,
        request: baas_20180731_models.DeleteTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trigger_with_options_async(
        self,
        request: baas_20180731_models.DeleteTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DeleteTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DeleteTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trigger(
        self,
        request: baas_20180731_models.DeleteTriggerRequest,
    ) -> baas_20180731_models.DeleteTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_trigger_with_options(request, runtime)

    async def delete_trigger_async(
        self,
        request: baas_20180731_models.DeleteTriggerRequest,
    ) -> baas_20180731_models.DeleteTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_trigger_with_options_async(request, runtime)

    def describe_ant_chain_accounts_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainAccountsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainAccounts',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_accounts_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainAccountsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainAccounts',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_accounts(
        self,
        request: baas_20180731_models.DescribeAntChainAccountsRequest,
    ) -> baas_20180731_models.DescribeAntChainAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_accounts_with_options(request, runtime)

    async def describe_ant_chain_accounts_async(
        self,
        request: baas_20180731_models.DescribeAntChainAccountsRequest,
    ) -> baas_20180731_models.DescribeAntChainAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_accounts_with_options_async(request, runtime)

    def describe_ant_chain_accounts_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainAccountsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainAccountsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainAccountsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainAccountsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_accounts_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainAccountsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainAccountsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainAccountsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainAccountsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_accounts_new(
        self,
        request: baas_20180731_models.DescribeAntChainAccountsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainAccountsNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_accounts_new_with_options(request, runtime)

    async def describe_ant_chain_accounts_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainAccountsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainAccountsNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_accounts_new_with_options_async(request, runtime)

    def describe_ant_chain_applications_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainApplicationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainApplications',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_applications_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainApplicationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainApplications',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_applications(
        self,
        request: baas_20180731_models.DescribeAntChainApplicationsRequest,
    ) -> baas_20180731_models.DescribeAntChainApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_applications_with_options(request, runtime)

    async def describe_ant_chain_applications_async(
        self,
        request: baas_20180731_models.DescribeAntChainApplicationsRequest,
    ) -> baas_20180731_models.DescribeAntChainApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_applications_with_options_async(request, runtime)

    def describe_ant_chain_block_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainBlockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainBlock',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_block_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainBlockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainBlock',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_block(
        self,
        request: baas_20180731_models.DescribeAntChainBlockRequest,
    ) -> baas_20180731_models.DescribeAntChainBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_block_with_options(request, runtime)

    async def describe_ant_chain_block_async(
        self,
        request: baas_20180731_models.DescribeAntChainBlockRequest,
    ) -> baas_20180731_models.DescribeAntChainBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_block_with_options_async(request, runtime)

    def describe_ant_chain_block_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainBlockNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainBlockNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainBlockNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainBlockNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_block_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainBlockNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainBlockNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainBlockNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainBlockNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_block_new(
        self,
        request: baas_20180731_models.DescribeAntChainBlockNewRequest,
    ) -> baas_20180731_models.DescribeAntChainBlockNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_block_new_with_options(request, runtime)

    async def describe_ant_chain_block_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainBlockNewRequest,
    ) -> baas_20180731_models.DescribeAntChainBlockNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_block_new_with_options_async(request, runtime)

    def describe_ant_chain_certificate_applications_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainCertificateApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainCertificateApplicationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainCertificateApplications',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainCertificateApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_certificate_applications_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainCertificateApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainCertificateApplicationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainCertificateApplications',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainCertificateApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_certificate_applications(
        self,
        request: baas_20180731_models.DescribeAntChainCertificateApplicationsRequest,
    ) -> baas_20180731_models.DescribeAntChainCertificateApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_certificate_applications_with_options(request, runtime)

    async def describe_ant_chain_certificate_applications_async(
        self,
        request: baas_20180731_models.DescribeAntChainCertificateApplicationsRequest,
    ) -> baas_20180731_models.DescribeAntChainCertificateApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_certificate_applications_with_options_async(request, runtime)

    def describe_ant_chain_certificate_applications_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainCertificateApplicationsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainCertificateApplicationsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainCertificateApplicationsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainCertificateApplicationsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_certificate_applications_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainCertificateApplicationsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainCertificateApplicationsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainCertificateApplicationsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainCertificateApplicationsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_certificate_applications_new(
        self,
        request: baas_20180731_models.DescribeAntChainCertificateApplicationsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainCertificateApplicationsNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_certificate_applications_new_with_options(request, runtime)

    async def describe_ant_chain_certificate_applications_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainCertificateApplicationsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainCertificateApplicationsNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_certificate_applications_new_with_options_async(request, runtime)

    def describe_ant_chain_config_options_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainConfigOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainConfigOptionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAntChainConfigOptions',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainConfigOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_config_options_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainConfigOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainConfigOptionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAntChainConfigOptions',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainConfigOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_config_options(
        self,
        request: baas_20180731_models.DescribeAntChainConfigOptionsRequest,
    ) -> baas_20180731_models.DescribeAntChainConfigOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_config_options_with_options(request, runtime)

    async def describe_ant_chain_config_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainConfigOptionsRequest,
    ) -> baas_20180731_models.DescribeAntChainConfigOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_config_options_with_options_async(request, runtime)

    def describe_ant_chain_consortiums_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainConsortiumsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainConsortiums',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainConsortiumsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_consortiums_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainConsortiumsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainConsortiums',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainConsortiumsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_consortiums(
        self,
        request: baas_20180731_models.DescribeAntChainConsortiumsRequest,
    ) -> baas_20180731_models.DescribeAntChainConsortiumsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_consortiums_with_options(request, runtime)

    async def describe_ant_chain_consortiums_async(
        self,
        request: baas_20180731_models.DescribeAntChainConsortiumsRequest,
    ) -> baas_20180731_models.DescribeAntChainConsortiumsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_consortiums_with_options_async(request, runtime)

    def describe_ant_chain_consortiums_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainConsortiumsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainConsortiumsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainConsortiumsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainConsortiumsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_consortiums_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainConsortiumsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainConsortiumsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainConsortiumsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainConsortiumsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_consortiums_new(
        self,
        request: baas_20180731_models.DescribeAntChainConsortiumsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainConsortiumsNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_consortiums_new_with_options(request, runtime)

    async def describe_ant_chain_consortiums_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainConsortiumsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainConsortiumsNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_consortiums_new_with_options_async(request, runtime)

    def describe_ant_chain_contract_project_content_tree_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectContentTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainContractProjectContentTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainContractProjectContentTree',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainContractProjectContentTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_contract_project_content_tree_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectContentTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainContractProjectContentTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainContractProjectContentTree',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainContractProjectContentTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_contract_project_content_tree(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectContentTreeRequest,
    ) -> baas_20180731_models.DescribeAntChainContractProjectContentTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_contract_project_content_tree_with_options(request, runtime)

    async def describe_ant_chain_contract_project_content_tree_async(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectContentTreeRequest,
    ) -> baas_20180731_models.DescribeAntChainContractProjectContentTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_contract_project_content_tree_with_options_async(request, runtime)

    def describe_ant_chain_contract_project_content_tree_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectContentTreeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainContractProjectContentTreeNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainContractProjectContentTreeNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainContractProjectContentTreeNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_contract_project_content_tree_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectContentTreeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainContractProjectContentTreeNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainContractProjectContentTreeNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainContractProjectContentTreeNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_contract_project_content_tree_new(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectContentTreeNewRequest,
    ) -> baas_20180731_models.DescribeAntChainContractProjectContentTreeNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_contract_project_content_tree_new_with_options(request, runtime)

    async def describe_ant_chain_contract_project_content_tree_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectContentTreeNewRequest,
    ) -> baas_20180731_models.DescribeAntChainContractProjectContentTreeNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_contract_project_content_tree_new_with_options_async(request, runtime)

    def describe_ant_chain_contract_projects_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainContractProjectsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainContractProjects',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainContractProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_contract_projects_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainContractProjectsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainContractProjects',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainContractProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_contract_projects(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectsRequest,
    ) -> baas_20180731_models.DescribeAntChainContractProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_contract_projects_with_options(request, runtime)

    async def describe_ant_chain_contract_projects_async(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectsRequest,
    ) -> baas_20180731_models.DescribeAntChainContractProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_contract_projects_with_options_async(request, runtime)

    def describe_ant_chain_contract_projects_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainContractProjectsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainContractProjectsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainContractProjectsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_contract_projects_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainContractProjectsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainContractProjectsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainContractProjectsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_contract_projects_new(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainContractProjectsNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_contract_projects_new_with_options(request, runtime)

    async def describe_ant_chain_contract_projects_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainContractProjectsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainContractProjectsNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_contract_projects_new_with_options_async(request, runtime)

    def describe_ant_chain_download_paths_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainDownloadPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainDownloadPathsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainDownloadPaths',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainDownloadPathsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_download_paths_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainDownloadPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainDownloadPathsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainDownloadPaths',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainDownloadPathsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_download_paths(
        self,
        request: baas_20180731_models.DescribeAntChainDownloadPathsRequest,
    ) -> baas_20180731_models.DescribeAntChainDownloadPathsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_download_paths_with_options(request, runtime)

    async def describe_ant_chain_download_paths_async(
        self,
        request: baas_20180731_models.DescribeAntChainDownloadPathsRequest,
    ) -> baas_20180731_models.DescribeAntChainDownloadPathsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_download_paths_with_options_async(request, runtime)

    def describe_ant_chain_download_paths_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainDownloadPathsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainDownloadPathsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainDownloadPathsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainDownloadPathsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_download_paths_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainDownloadPathsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainDownloadPathsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainDownloadPathsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainDownloadPathsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_download_paths_new(
        self,
        request: baas_20180731_models.DescribeAntChainDownloadPathsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainDownloadPathsNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_download_paths_new_with_options(request, runtime)

    async def describe_ant_chain_download_paths_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainDownloadPathsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainDownloadPathsNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_download_paths_new_with_options_async(request, runtime)

    def describe_ant_chain_information_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainInformationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainInformation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_information_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainInformationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainInformation',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_information(
        self,
        request: baas_20180731_models.DescribeAntChainInformationRequest,
    ) -> baas_20180731_models.DescribeAntChainInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_information_with_options(request, runtime)

    async def describe_ant_chain_information_async(
        self,
        request: baas_20180731_models.DescribeAntChainInformationRequest,
    ) -> baas_20180731_models.DescribeAntChainInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_information_with_options_async(request, runtime)

    def describe_ant_chain_information_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainInformationNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainInformationNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainInformationNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainInformationNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_information_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainInformationNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainInformationNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainInformationNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainInformationNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_information_new(
        self,
        request: baas_20180731_models.DescribeAntChainInformationNewRequest,
    ) -> baas_20180731_models.DescribeAntChainInformationNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_information_new_with_options(request, runtime)

    async def describe_ant_chain_information_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainInformationNewRequest,
    ) -> baas_20180731_models.DescribeAntChainInformationNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_information_new_with_options_async(request, runtime)

    def describe_ant_chain_latest_blocks_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainLatestBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainLatestBlocksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestBlocks',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainLatestBlocksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_latest_blocks_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainLatestBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainLatestBlocksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestBlocks',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainLatestBlocksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_latest_blocks(
        self,
        request: baas_20180731_models.DescribeAntChainLatestBlocksRequest,
    ) -> baas_20180731_models.DescribeAntChainLatestBlocksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_latest_blocks_with_options(request, runtime)

    async def describe_ant_chain_latest_blocks_async(
        self,
        request: baas_20180731_models.DescribeAntChainLatestBlocksRequest,
    ) -> baas_20180731_models.DescribeAntChainLatestBlocksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_latest_blocks_with_options_async(request, runtime)

    def describe_ant_chain_latest_blocks_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainLatestBlocksNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainLatestBlocksNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestBlocksNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainLatestBlocksNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_latest_blocks_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainLatestBlocksNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainLatestBlocksNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestBlocksNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainLatestBlocksNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_latest_blocks_new(
        self,
        request: baas_20180731_models.DescribeAntChainLatestBlocksNewRequest,
    ) -> baas_20180731_models.DescribeAntChainLatestBlocksNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_latest_blocks_new_with_options(request, runtime)

    async def describe_ant_chain_latest_blocks_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainLatestBlocksNewRequest,
    ) -> baas_20180731_models.DescribeAntChainLatestBlocksNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_latest_blocks_new_with_options_async(request, runtime)

    def describe_ant_chain_latest_transaction_digests_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainLatestTransactionDigestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainLatestTransactionDigestsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestTransactionDigests',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainLatestTransactionDigestsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_latest_transaction_digests_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainLatestTransactionDigestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainLatestTransactionDigestsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestTransactionDigests',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainLatestTransactionDigestsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_latest_transaction_digests(
        self,
        request: baas_20180731_models.DescribeAntChainLatestTransactionDigestsRequest,
    ) -> baas_20180731_models.DescribeAntChainLatestTransactionDigestsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_latest_transaction_digests_with_options(request, runtime)

    async def describe_ant_chain_latest_transaction_digests_async(
        self,
        request: baas_20180731_models.DescribeAntChainLatestTransactionDigestsRequest,
    ) -> baas_20180731_models.DescribeAntChainLatestTransactionDigestsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_latest_transaction_digests_with_options_async(request, runtime)

    def describe_ant_chain_latest_transaction_digests_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainLatestTransactionDigestsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainLatestTransactionDigestsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestTransactionDigestsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainLatestTransactionDigestsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_latest_transaction_digests_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainLatestTransactionDigestsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainLatestTransactionDigestsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestTransactionDigestsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainLatestTransactionDigestsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_latest_transaction_digests_new(
        self,
        request: baas_20180731_models.DescribeAntChainLatestTransactionDigestsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainLatestTransactionDigestsNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_latest_transaction_digests_new_with_options(request, runtime)

    async def describe_ant_chain_latest_transaction_digests_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainLatestTransactionDigestsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainLatestTransactionDigestsNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_latest_transaction_digests_new_with_options_async(request, runtime)

    def describe_ant_chain_members_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMembers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_members_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMembers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_members(
        self,
        request: baas_20180731_models.DescribeAntChainMembersRequest,
    ) -> baas_20180731_models.DescribeAntChainMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_members_with_options(request, runtime)

    async def describe_ant_chain_members_async(
        self,
        request: baas_20180731_models.DescribeAntChainMembersRequest,
    ) -> baas_20180731_models.DescribeAntChainMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_members_with_options_async(request, runtime)

    def describe_ant_chain_members_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainMembersNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMembersNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMembersNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMembersNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_members_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainMembersNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMembersNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMembersNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMembersNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_members_new(
        self,
        request: baas_20180731_models.DescribeAntChainMembersNewRequest,
    ) -> baas_20180731_models.DescribeAntChainMembersNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_members_new_with_options(request, runtime)

    async def describe_ant_chain_members_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainMembersNewRequest,
    ) -> baas_20180731_models.DescribeAntChainMembersNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_members_new_with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_qrcode_access_log_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserQRCodeAccessLog',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_qrcode_access_log_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserQRCodeAccessLog',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_mini_app_browser_qrcode_access_log(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_qrcode_access_log_with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_qrcode_access_log_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_qrcode_access_log_with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_qrcode_access_log_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserQRCodeAccessLogNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_qrcode_access_log_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserQRCodeAccessLogNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_mini_app_browser_qrcode_access_log_new(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogNewRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_qrcode_access_log_new_with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_qrcode_access_log_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogNewRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_qrcode_access_log_new_with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_qrcode_authorized_users_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_qrcode_authorized_users_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_mini_app_browser_qrcode_authorized_users(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_qrcode_authorized_users_with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_qrcode_authorized_users_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_qrcode_authorized_users_with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_qrcode_authorized_users_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_qrcode_authorized_users_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_mini_app_browser_qrcode_authorized_users_new(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNewRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_qrcode_authorized_users_new_with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_qrcode_authorized_users_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNewRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_qrcode_authorized_users_new_with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_transaction_qrcode_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.transaction_hash):
            body['TransactionHash'] = request.transaction_hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserTransactionQRCode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_transaction_qrcode_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.transaction_hash):
            body['TransactionHash'] = request.transaction_hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserTransactionQRCode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_mini_app_browser_transaction_qrcode(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_transaction_qrcode_with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_transaction_qrcode_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_transaction_qrcode_with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_transaction_qrcode_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.contract_id):
            body['ContractId'] = request.contract_id
        if not UtilClient.is_unset(request.transaction_hash):
            body['TransactionHash'] = request.transaction_hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserTransactionQRCodeNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_transaction_qrcode_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.contract_id):
            body['ContractId'] = request.contract_id
        if not UtilClient.is_unset(request.transaction_hash):
            body['TransactionHash'] = request.transaction_hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainMiniAppBrowserTransactionQRCodeNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_mini_app_browser_transaction_qrcode_new(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_transaction_qrcode_new_with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_transaction_qrcode_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewRequest,
    ) -> baas_20180731_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_transaction_qrcode_new_with_options_async(request, runtime)

    def describe_ant_chain_nodes_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainNodesNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainNodesNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainNodesNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainNodesNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_nodes_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainNodesNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainNodesNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainNodesNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainNodesNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_nodes_new(
        self,
        request: baas_20180731_models.DescribeAntChainNodesNewRequest,
    ) -> baas_20180731_models.DescribeAntChainNodesNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_nodes_new_with_options(request, runtime)

    async def describe_ant_chain_nodes_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainNodesNewRequest,
    ) -> baas_20180731_models.DescribeAntChainNodesNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_nodes_new_with_options_async(request, runtime)

    def describe_ant_chain_qrcode_authorization_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainQRCodeAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainQRCodeAuthorizationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainQRCodeAuthorization',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainQRCodeAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_qrcode_authorization_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainQRCodeAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainQRCodeAuthorizationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainQRCodeAuthorization',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainQRCodeAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_qrcode_authorization(
        self,
        request: baas_20180731_models.DescribeAntChainQRCodeAuthorizationRequest,
    ) -> baas_20180731_models.DescribeAntChainQRCodeAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_qrcode_authorization_with_options(request, runtime)

    async def describe_ant_chain_qrcode_authorization_async(
        self,
        request: baas_20180731_models.DescribeAntChainQRCodeAuthorizationRequest,
    ) -> baas_20180731_models.DescribeAntChainQRCodeAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_qrcode_authorization_with_options_async(request, runtime)

    def describe_ant_chain_qrcode_authorization_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainQRCodeAuthorizationNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainQRCodeAuthorizationNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainQRCodeAuthorizationNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainQRCodeAuthorizationNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_qrcode_authorization_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainQRCodeAuthorizationNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainQRCodeAuthorizationNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainQRCodeAuthorizationNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainQRCodeAuthorizationNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_qrcode_authorization_new(
        self,
        request: baas_20180731_models.DescribeAntChainQRCodeAuthorizationNewRequest,
    ) -> baas_20180731_models.DescribeAntChainQRCodeAuthorizationNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_qrcode_authorization_new_with_options(request, runtime)

    async def describe_ant_chain_qrcode_authorization_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainQRCodeAuthorizationNewRequest,
    ) -> baas_20180731_models.DescribeAntChainQRCodeAuthorizationNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_qrcode_authorization_new_with_options_async(request, runtime)

    def describe_ant_chain_region_names_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainRegionNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainRegionNamesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.locale):
            body['Locale'] = request.locale
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainRegionNames',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainRegionNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_region_names_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainRegionNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainRegionNamesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.locale):
            body['Locale'] = request.locale
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainRegionNames',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainRegionNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_region_names(
        self,
        request: baas_20180731_models.DescribeAntChainRegionNamesRequest,
    ) -> baas_20180731_models.DescribeAntChainRegionNamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_region_names_with_options(request, runtime)

    async def describe_ant_chain_region_names_async(
        self,
        request: baas_20180731_models.DescribeAntChainRegionNamesRequest,
    ) -> baas_20180731_models.DescribeAntChainRegionNamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_region_names_with_options_async(request, runtime)

    def describe_ant_chain_regions_for_sale_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainRegionsForSaleResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAntChainRegionsForSale',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainRegionsForSaleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_regions_for_sale_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainRegionsForSaleResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAntChainRegionsForSale',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainRegionsForSaleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_regions_for_sale(self) -> baas_20180731_models.DescribeAntChainRegionsForSaleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_regions_for_sale_with_options(runtime)

    async def describe_ant_chain_regions_for_sale_async(self) -> baas_20180731_models.DescribeAntChainRegionsForSaleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_regions_for_sale_with_options_async(runtime)

    def describe_ant_chain_resource_types_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAntChainResourceTypes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_resource_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAntChainResourceTypes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_resource_types(self) -> baas_20180731_models.DescribeAntChainResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_resource_types_with_options(runtime)

    async def describe_ant_chain_resource_types_async(self) -> baas_20180731_models.DescribeAntChainResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_resource_types_with_options_async(runtime)

    def describe_ant_chain_rest_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainRestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainRestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainRest',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainRestResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_rest_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainRestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainRestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainRest',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainRestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_rest(
        self,
        request: baas_20180731_models.DescribeAntChainRestRequest,
    ) -> baas_20180731_models.DescribeAntChainRestResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_rest_with_options(request, runtime)

    async def describe_ant_chain_rest_async(
        self,
        request: baas_20180731_models.DescribeAntChainRestRequest,
    ) -> baas_20180731_models.DescribeAntChainRestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_rest_with_options_async(request, runtime)

    def describe_ant_chain_subnet_list_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainSubnetListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainSubnetList',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainSubnetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_subnet_list_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainSubnetListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainSubnetList',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainSubnetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_subnet_list(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetListRequest,
    ) -> baas_20180731_models.DescribeAntChainSubnetListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_subnet_list_with_options(request, runtime)

    async def describe_ant_chain_subnet_list_async(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetListRequest,
    ) -> baas_20180731_models.DescribeAntChainSubnetListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_subnet_list_with_options_async(request, runtime)

    def describe_ant_chain_subnet_member_list_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetMemberListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainSubnetMemberListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainSubnetMemberList',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainSubnetMemberListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_subnet_member_list_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetMemberListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainSubnetMemberListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainSubnetMemberList',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainSubnetMemberListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_subnet_member_list(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetMemberListRequest,
    ) -> baas_20180731_models.DescribeAntChainSubnetMemberListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_subnet_member_list_with_options(request, runtime)

    async def describe_ant_chain_subnet_member_list_async(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetMemberListRequest,
    ) -> baas_20180731_models.DescribeAntChainSubnetMemberListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_subnet_member_list_with_options_async(request, runtime)

    def describe_ant_chain_subnet_node_list_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetNodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainSubnetNodeListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainSubnetNodeList',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainSubnetNodeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_subnet_node_list_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetNodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainSubnetNodeListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainSubnetNodeList',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainSubnetNodeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_subnet_node_list(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetNodeListRequest,
    ) -> baas_20180731_models.DescribeAntChainSubnetNodeListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_subnet_node_list_with_options(request, runtime)

    async def describe_ant_chain_subnet_node_list_async(
        self,
        request: baas_20180731_models.DescribeAntChainSubnetNodeListRequest,
    ) -> baas_20180731_models.DescribeAntChainSubnetNodeListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_subnet_node_list_with_options_async(request, runtime)

    def describe_ant_chain_transaction_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainTransaction',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainTransactionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_transaction_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainTransaction',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainTransactionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_transaction(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionRequest,
    ) -> baas_20180731_models.DescribeAntChainTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_transaction_with_options(request, runtime)

    async def describe_ant_chain_transaction_async(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionRequest,
    ) -> baas_20180731_models.DescribeAntChainTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_transaction_with_options_async(request, runtime)

    def describe_ant_chain_transaction_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainTransactionNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainTransactionNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainTransactionNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_transaction_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainTransactionNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainTransactionNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainTransactionNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_transaction_new(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionNewRequest,
    ) -> baas_20180731_models.DescribeAntChainTransactionNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_transaction_new_with_options(request, runtime)

    async def describe_ant_chain_transaction_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionNewRequest,
    ) -> baas_20180731_models.DescribeAntChainTransactionNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_transaction_new_with_options_async(request, runtime)

    def describe_ant_chain_transaction_receipt_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionReceiptNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainTransactionReceiptNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainTransactionReceiptNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainTransactionReceiptNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_transaction_receipt_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionReceiptNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainTransactionReceiptNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainTransactionReceiptNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainTransactionReceiptNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_transaction_receipt_new(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionReceiptNewRequest,
    ) -> baas_20180731_models.DescribeAntChainTransactionReceiptNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_transaction_receipt_new_with_options(request, runtime)

    async def describe_ant_chain_transaction_receipt_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionReceiptNewRequest,
    ) -> baas_20180731_models.DescribeAntChainTransactionReceiptNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_transaction_receipt_new_with_options_async(request, runtime)

    def describe_ant_chain_transaction_statistics_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainTransactionStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.end):
            body['End'] = request.end
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainTransactionStatistics',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainTransactionStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_transaction_statistics_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainTransactionStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.end):
            body['End'] = request.end
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainTransactionStatistics',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainTransactionStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_transaction_statistics(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionStatisticsRequest,
    ) -> baas_20180731_models.DescribeAntChainTransactionStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_transaction_statistics_with_options(request, runtime)

    async def describe_ant_chain_transaction_statistics_async(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionStatisticsRequest,
    ) -> baas_20180731_models.DescribeAntChainTransactionStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_transaction_statistics_with_options_async(request, runtime)

    def describe_ant_chain_transaction_statistics_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionStatisticsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainTransactionStatisticsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.end):
            body['End'] = request.end
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainTransactionStatisticsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainTransactionStatisticsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_transaction_statistics_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionStatisticsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainTransactionStatisticsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.end):
            body['End'] = request.end
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainTransactionStatisticsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainTransactionStatisticsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_transaction_statistics_new(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionStatisticsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainTransactionStatisticsNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_transaction_statistics_new_with_options(request, runtime)

    async def describe_ant_chain_transaction_statistics_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainTransactionStatisticsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainTransactionStatisticsNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_transaction_statistics_new_with_options_async(request, runtime)

    def describe_ant_chains_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChains',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chains_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChains',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chains(
        self,
        request: baas_20180731_models.DescribeAntChainsRequest,
    ) -> baas_20180731_models.DescribeAntChainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chains_with_options(request, runtime)

    async def describe_ant_chains_async(
        self,
        request: baas_20180731_models.DescribeAntChainsRequest,
    ) -> baas_20180731_models.DescribeAntChainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chains_with_options_async(request, runtime)

    def describe_ant_chains_new_with_options(
        self,
        request: baas_20180731_models.DescribeAntChainsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chains_new_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntChainsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntChainsNewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainsNew',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntChainsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chains_new(
        self,
        request: baas_20180731_models.DescribeAntChainsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainsNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chains_new_with_options(request, runtime)

    async def describe_ant_chains_new_async(
        self,
        request: baas_20180731_models.DescribeAntChainsNewRequest,
    ) -> baas_20180731_models.DescribeAntChainsNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chains_new_with_options_async(request, runtime)

    def describe_ant_regions_with_options(
        self,
        request: baas_20180731_models.DescribeAntRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntRegionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.locale):
            body['Locale'] = request.locale
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntRegions',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_regions_with_options_async(
        self,
        request: baas_20180731_models.DescribeAntRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAntRegionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.locale):
            body['Locale'] = request.locale
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntRegions',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAntRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_regions(
        self,
        request: baas_20180731_models.DescribeAntRegionsRequest,
    ) -> baas_20180731_models.DescribeAntRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_regions_with_options(request, runtime)

    async def describe_ant_regions_async(
        self,
        request: baas_20180731_models.DescribeAntRegionsRequest,
    ) -> baas_20180731_models.DescribeAntRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_regions_with_options_async(request, runtime)

    def describe_applies_with_options(
        self,
        request: baas_20180731_models.DescribeAppliesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAppliesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeApplies',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAppliesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_applies_with_options_async(
        self,
        request: baas_20180731_models.DescribeAppliesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeAppliesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeApplies',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeAppliesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_applies(
        self,
        request: baas_20180731_models.DescribeAppliesRequest,
    ) -> baas_20180731_models.DescribeAppliesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_applies_with_options(request, runtime)

    async def describe_applies_async(
        self,
        request: baas_20180731_models.DescribeAppliesRequest,
    ) -> baas_20180731_models.DescribeAppliesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_applies_with_options_async(request, runtime)

    def describe_bc_schema_with_options(
        self,
        request: baas_20180731_models.DescribeBcSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBcSchemaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBcSchema',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBcSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bc_schema_with_options_async(
        self,
        request: baas_20180731_models.DescribeBcSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBcSchemaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBcSchema',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBcSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bc_schema(
        self,
        request: baas_20180731_models.DescribeBcSchemaRequest,
    ) -> baas_20180731_models.DescribeBcSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bc_schema_with_options(request, runtime)

    async def describe_bc_schema_async(
        self,
        request: baas_20180731_models.DescribeBcSchemaRequest,
    ) -> baas_20180731_models.DescribeBcSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bc_schema_with_options_async(request, runtime)

    def describe_block_with_options(
        self,
        request: baas_20180731_models.DescribeBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlock',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_block_with_options_async(
        self,
        request: baas_20180731_models.DescribeBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlock',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_block(
        self,
        request: baas_20180731_models.DescribeBlockRequest,
    ) -> baas_20180731_models.DescribeBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_block_with_options(request, runtime)

    async def describe_block_async(
        self,
        request: baas_20180731_models.DescribeBlockRequest,
    ) -> baas_20180731_models.DescribeBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_block_with_options_async(request, runtime)

    def describe_blockchain_application_with_options(
        self,
        request: baas_20180731_models.DescribeBlockchainApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainApplication',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blockchain_application_with_options_async(
        self,
        request: baas_20180731_models.DescribeBlockchainApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainApplication',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blockchain_application(
        self,
        request: baas_20180731_models.DescribeBlockchainApplicationRequest,
    ) -> baas_20180731_models.DescribeBlockchainApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_blockchain_application_with_options(request, runtime)

    async def describe_blockchain_application_async(
        self,
        request: baas_20180731_models.DescribeBlockchainApplicationRequest,
    ) -> baas_20180731_models.DescribeBlockchainApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_blockchain_application_with_options_async(request, runtime)

    def describe_blockchain_config_option_with_options(
        self,
        request: baas_20180731_models.DescribeBlockchainConfigOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainConfigOptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainConfigOption',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainConfigOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blockchain_config_option_with_options_async(
        self,
        request: baas_20180731_models.DescribeBlockchainConfigOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainConfigOptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainConfigOption',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainConfigOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blockchain_config_option(
        self,
        request: baas_20180731_models.DescribeBlockchainConfigOptionRequest,
    ) -> baas_20180731_models.DescribeBlockchainConfigOptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_blockchain_config_option_with_options(request, runtime)

    async def describe_blockchain_config_option_async(
        self,
        request: baas_20180731_models.DescribeBlockchainConfigOptionRequest,
    ) -> baas_20180731_models.DescribeBlockchainConfigOptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_blockchain_config_option_with_options_async(request, runtime)

    def describe_blockchain_create_task_with_options(
        self,
        request: baas_20180731_models.DescribeBlockchainCreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainCreateTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainCreateTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainCreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blockchain_create_task_with_options_async(
        self,
        request: baas_20180731_models.DescribeBlockchainCreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainCreateTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainCreateTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainCreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blockchain_create_task(
        self,
        request: baas_20180731_models.DescribeBlockchainCreateTaskRequest,
    ) -> baas_20180731_models.DescribeBlockchainCreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_blockchain_create_task_with_options(request, runtime)

    async def describe_blockchain_create_task_async(
        self,
        request: baas_20180731_models.DescribeBlockchainCreateTaskRequest,
    ) -> baas_20180731_models.DescribeBlockchainCreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_blockchain_create_task_with_options_async(request, runtime)

    def describe_blockchain_creation_config_options_with_options(
        self,
        request: baas_20180731_models.DescribeBlockchainCreationConfigOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainCreationConfigOptionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainCreationConfigOptions',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainCreationConfigOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blockchain_creation_config_options_with_options_async(
        self,
        request: baas_20180731_models.DescribeBlockchainCreationConfigOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainCreationConfigOptionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainCreationConfigOptions',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainCreationConfigOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blockchain_creation_config_options(
        self,
        request: baas_20180731_models.DescribeBlockchainCreationConfigOptionsRequest,
    ) -> baas_20180731_models.DescribeBlockchainCreationConfigOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_blockchain_creation_config_options_with_options(request, runtime)

    async def describe_blockchain_creation_config_options_async(
        self,
        request: baas_20180731_models.DescribeBlockchainCreationConfigOptionsRequest,
    ) -> baas_20180731_models.DescribeBlockchainCreationConfigOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_blockchain_creation_config_options_with_options_async(request, runtime)

    def describe_blockchain_info_with_options(
        self,
        request: baas_20180731_models.DescribeBlockchainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainInfo',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blockchain_info_with_options_async(
        self,
        request: baas_20180731_models.DescribeBlockchainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainInfo',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blockchain_info(
        self,
        request: baas_20180731_models.DescribeBlockchainInfoRequest,
    ) -> baas_20180731_models.DescribeBlockchainInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_blockchain_info_with_options(request, runtime)

    async def describe_blockchain_info_async(
        self,
        request: baas_20180731_models.DescribeBlockchainInfoRequest,
    ) -> baas_20180731_models.DescribeBlockchainInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_blockchain_info_with_options_async(request, runtime)

    def describe_blockchain_schema_with_options(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainSchemaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainSchema',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blockchain_schema_with_options_async(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainSchemaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainSchema',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blockchain_schema(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaRequest,
    ) -> baas_20180731_models.DescribeBlockchainSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_blockchain_schema_with_options(request, runtime)

    async def describe_blockchain_schema_async(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaRequest,
    ) -> baas_20180731_models.DescribeBlockchainSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_blockchain_schema_with_options_async(request, runtime)

    def describe_blockchain_schema_detail_with_options(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainSchemaDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainSchemaDetail',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainSchemaDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blockchain_schema_detail_with_options_async(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainSchemaDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainSchemaDetail',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainSchemaDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blockchain_schema_detail(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaDetailRequest,
    ) -> baas_20180731_models.DescribeBlockchainSchemaDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_blockchain_schema_detail_with_options(request, runtime)

    async def describe_blockchain_schema_detail_async(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaDetailRequest,
    ) -> baas_20180731_models.DescribeBlockchainSchemaDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_blockchain_schema_detail_with_options_async(request, runtime)

    def describe_blockchain_schema_file_ossproperties_with_options(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaFileOSSPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainSchemaFileOSSPropertiesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainSchemaFileOSSProperties',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainSchemaFileOSSPropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blockchain_schema_file_ossproperties_with_options_async(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaFileOSSPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainSchemaFileOSSPropertiesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBlockchainSchemaFileOSSProperties',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainSchemaFileOSSPropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blockchain_schema_file_ossproperties(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaFileOSSPropertiesRequest,
    ) -> baas_20180731_models.DescribeBlockchainSchemaFileOSSPropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_blockchain_schema_file_ossproperties_with_options(request, runtime)

    async def describe_blockchain_schema_file_ossproperties_async(
        self,
        request: baas_20180731_models.DescribeBlockchainSchemaFileOSSPropertiesRequest,
    ) -> baas_20180731_models.DescribeBlockchainSchemaFileOSSPropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_blockchain_schema_file_ossproperties_with_options_async(request, runtime)

    def describe_blockchain_schema_templates_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainSchemaTemplatesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeBlockchainSchemaTemplates',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainSchemaTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_blockchain_schema_templates_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeBlockchainSchemaTemplatesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeBlockchainSchemaTemplates',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeBlockchainSchemaTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_blockchain_schema_templates(self) -> baas_20180731_models.DescribeBlockchainSchemaTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_blockchain_schema_templates_with_options(runtime)

    async def describe_blockchain_schema_templates_async(self) -> baas_20180731_models.DescribeBlockchainSchemaTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_blockchain_schema_templates_with_options_async(runtime)

    def describe_csigateway_endpoint_with_options(
        self,
        request: baas_20180731_models.DescribeCSIGatewayEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeCSIGatewayEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCSIGatewayEndpoint',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeCSIGatewayEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_csigateway_endpoint_with_options_async(
        self,
        request: baas_20180731_models.DescribeCSIGatewayEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeCSIGatewayEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCSIGatewayEndpoint',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeCSIGatewayEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_csigateway_endpoint(
        self,
        request: baas_20180731_models.DescribeCSIGatewayEndpointRequest,
    ) -> baas_20180731_models.DescribeCSIGatewayEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_csigateway_endpoint_with_options(request, runtime)

    async def describe_csigateway_endpoint_async(
        self,
        request: baas_20180731_models.DescribeCSIGatewayEndpointRequest,
    ) -> baas_20180731_models.DescribeCSIGatewayEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_csigateway_endpoint_with_options_async(request, runtime)

    def describe_candidate_organizations_with_options(
        self,
        request: baas_20180731_models.DescribeCandidateOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeCandidateOrganizationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCandidateOrganizations',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeCandidateOrganizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_candidate_organizations_with_options_async(
        self,
        request: baas_20180731_models.DescribeCandidateOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeCandidateOrganizationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCandidateOrganizations',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeCandidateOrganizationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_candidate_organizations(
        self,
        request: baas_20180731_models.DescribeCandidateOrganizationsRequest,
    ) -> baas_20180731_models.DescribeCandidateOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_candidate_organizations_with_options(request, runtime)

    async def describe_candidate_organizations_async(
        self,
        request: baas_20180731_models.DescribeCandidateOrganizationsRequest,
    ) -> baas_20180731_models.DescribeCandidateOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_candidate_organizations_with_options_async(request, runtime)

    def describe_chaincode_collection_config_with_options(
        self,
        request: baas_20180731_models.DescribeChaincodeCollectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChaincodeCollectionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeChaincodeCollectionConfig',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChaincodeCollectionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_chaincode_collection_config_with_options_async(
        self,
        request: baas_20180731_models.DescribeChaincodeCollectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChaincodeCollectionConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeChaincodeCollectionConfig',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChaincodeCollectionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_chaincode_collection_config(
        self,
        request: baas_20180731_models.DescribeChaincodeCollectionConfigRequest,
    ) -> baas_20180731_models.DescribeChaincodeCollectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_chaincode_collection_config_with_options(request, runtime)

    async def describe_chaincode_collection_config_async(
        self,
        request: baas_20180731_models.DescribeChaincodeCollectionConfigRequest,
    ) -> baas_20180731_models.DescribeChaincodeCollectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_chaincode_collection_config_with_options_async(request, runtime)

    def describe_chaincode_definition_task_with_options(
        self,
        request: baas_20180731_models.DescribeChaincodeDefinitionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChaincodeDefinitionTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeChaincodeDefinitionTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChaincodeDefinitionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_chaincode_definition_task_with_options_async(
        self,
        request: baas_20180731_models.DescribeChaincodeDefinitionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChaincodeDefinitionTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeChaincodeDefinitionTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChaincodeDefinitionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_chaincode_definition_task(
        self,
        request: baas_20180731_models.DescribeChaincodeDefinitionTaskRequest,
    ) -> baas_20180731_models.DescribeChaincodeDefinitionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_chaincode_definition_task_with_options(request, runtime)

    async def describe_chaincode_definition_task_async(
        self,
        request: baas_20180731_models.DescribeChaincodeDefinitionTaskRequest,
    ) -> baas_20180731_models.DescribeChaincodeDefinitionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_chaincode_definition_task_with_options_async(request, runtime)

    def describe_chaincode_upload_policy_with_options(
        self,
        request: baas_20180731_models.DescribeChaincodeUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChaincodeUploadPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeChaincodeUploadPolicy',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChaincodeUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_chaincode_upload_policy_with_options_async(
        self,
        request: baas_20180731_models.DescribeChaincodeUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChaincodeUploadPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeChaincodeUploadPolicy',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChaincodeUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_chaincode_upload_policy(
        self,
        request: baas_20180731_models.DescribeChaincodeUploadPolicyRequest,
    ) -> baas_20180731_models.DescribeChaincodeUploadPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_chaincode_upload_policy_with_options(request, runtime)

    async def describe_chaincode_upload_policy_async(
        self,
        request: baas_20180731_models.DescribeChaincodeUploadPolicyRequest,
    ) -> baas_20180731_models.DescribeChaincodeUploadPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_chaincode_upload_policy_with_options_async(request, runtime)

    def describe_channel_chaincodes_with_options(
        self,
        request: baas_20180731_models.DescribeChannelChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChannelChaincodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeChannelChaincodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChannelChaincodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_chaincodes_with_options_async(
        self,
        request: baas_20180731_models.DescribeChannelChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChannelChaincodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeChannelChaincodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChannelChaincodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_chaincodes(
        self,
        request: baas_20180731_models.DescribeChannelChaincodesRequest,
    ) -> baas_20180731_models.DescribeChannelChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_chaincodes_with_options(request, runtime)

    async def describe_channel_chaincodes_async(
        self,
        request: baas_20180731_models.DescribeChannelChaincodesRequest,
    ) -> baas_20180731_models.DescribeChannelChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_chaincodes_with_options_async(request, runtime)

    def describe_channel_members_with_options(
        self,
        request: baas_20180731_models.DescribeChannelMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChannelMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelMembers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChannelMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_members_with_options_async(
        self,
        request: baas_20180731_models.DescribeChannelMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChannelMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelMembers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChannelMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_members(
        self,
        request: baas_20180731_models.DescribeChannelMembersRequest,
    ) -> baas_20180731_models.DescribeChannelMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_members_with_options(request, runtime)

    async def describe_channel_members_async(
        self,
        request: baas_20180731_models.DescribeChannelMembersRequest,
    ) -> baas_20180731_models.DescribeChannelMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_members_with_options_async(request, runtime)

    def describe_channel_triggers_with_options(
        self,
        request: baas_20180731_models.DescribeChannelTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChannelTriggersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelTriggers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChannelTriggersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_triggers_with_options_async(
        self,
        request: baas_20180731_models.DescribeChannelTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeChannelTriggersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelTriggers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeChannelTriggersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_triggers(
        self,
        request: baas_20180731_models.DescribeChannelTriggersRequest,
    ) -> baas_20180731_models.DescribeChannelTriggersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_triggers_with_options(request, runtime)

    async def describe_channel_triggers_async(
        self,
        request: baas_20180731_models.DescribeChannelTriggersRequest,
    ) -> baas_20180731_models.DescribeChannelTriggersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_triggers_with_options_async(request, runtime)

    def describe_cloud_integration_service_token_with_options(
        self,
        request: baas_20180731_models.DescribeCloudIntegrationServiceTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeCloudIntegrationServiceTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudIntegrationServiceToken',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeCloudIntegrationServiceTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_integration_service_token_with_options_async(
        self,
        request: baas_20180731_models.DescribeCloudIntegrationServiceTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeCloudIntegrationServiceTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.service):
            body['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudIntegrationServiceToken',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeCloudIntegrationServiceTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_integration_service_token(
        self,
        request: baas_20180731_models.DescribeCloudIntegrationServiceTokenRequest,
    ) -> baas_20180731_models.DescribeCloudIntegrationServiceTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_integration_service_token_with_options(request, runtime)

    async def describe_cloud_integration_service_token_async(
        self,
        request: baas_20180731_models.DescribeCloudIntegrationServiceTokenRequest,
    ) -> baas_20180731_models.DescribeCloudIntegrationServiceTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_integration_service_token_with_options_async(request, runtime)

    def describe_cloud_service_organization_status_with_options(
        self,
        request: baas_20180731_models.DescribeCloudServiceOrganizationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeCloudServiceOrganizationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudServiceOrganizationStatus',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeCloudServiceOrganizationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_service_organization_status_with_options_async(
        self,
        request: baas_20180731_models.DescribeCloudServiceOrganizationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeCloudServiceOrganizationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudServiceOrganizationStatus',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeCloudServiceOrganizationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_service_organization_status(
        self,
        request: baas_20180731_models.DescribeCloudServiceOrganizationStatusRequest,
    ) -> baas_20180731_models.DescribeCloudServiceOrganizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_service_organization_status_with_options(request, runtime)

    async def describe_cloud_service_organization_status_async(
        self,
        request: baas_20180731_models.DescribeCloudServiceOrganizationStatusRequest,
    ) -> baas_20180731_models.DescribeCloudServiceOrganizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_service_organization_status_with_options_async(request, runtime)

    def describe_cloud_service_type_status_with_options(
        self,
        request: baas_20180731_models.DescribeCloudServiceTypeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeCloudServiceTypeStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudServiceTypeStatus',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeCloudServiceTypeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_service_type_status_with_options_async(
        self,
        request: baas_20180731_models.DescribeCloudServiceTypeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeCloudServiceTypeStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudServiceTypeStatus',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeCloudServiceTypeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_service_type_status(
        self,
        request: baas_20180731_models.DescribeCloudServiceTypeStatusRequest,
    ) -> baas_20180731_models.DescribeCloudServiceTypeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_service_type_status_with_options(request, runtime)

    async def describe_cloud_service_type_status_async(
        self,
        request: baas_20180731_models.DescribeCloudServiceTypeStatusRequest,
    ) -> baas_20180731_models.DescribeCloudServiceTypeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_service_type_status_with_options_async(request, runtime)

    def describe_consortium_admin_status_with_options(
        self,
        request: baas_20180731_models.DescribeConsortiumAdminStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumAdminStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumAdminStatus',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumAdminStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consortium_admin_status_with_options_async(
        self,
        request: baas_20180731_models.DescribeConsortiumAdminStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumAdminStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumAdminStatus',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumAdminStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consortium_admin_status(
        self,
        request: baas_20180731_models.DescribeConsortiumAdminStatusRequest,
    ) -> baas_20180731_models.DescribeConsortiumAdminStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consortium_admin_status_with_options(request, runtime)

    async def describe_consortium_admin_status_async(
        self,
        request: baas_20180731_models.DescribeConsortiumAdminStatusRequest,
    ) -> baas_20180731_models.DescribeConsortiumAdminStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consortium_admin_status_with_options_async(request, runtime)

    def describe_consortium_chaincodes_with_options(
        self,
        request: baas_20180731_models.DescribeConsortiumChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumChaincodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumChaincodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumChaincodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consortium_chaincodes_with_options_async(
        self,
        request: baas_20180731_models.DescribeConsortiumChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumChaincodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumChaincodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumChaincodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consortium_chaincodes(
        self,
        request: baas_20180731_models.DescribeConsortiumChaincodesRequest,
    ) -> baas_20180731_models.DescribeConsortiumChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consortium_chaincodes_with_options(request, runtime)

    async def describe_consortium_chaincodes_async(
        self,
        request: baas_20180731_models.DescribeConsortiumChaincodesRequest,
    ) -> baas_20180731_models.DescribeConsortiumChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consortium_chaincodes_with_options_async(request, runtime)

    def describe_consortium_channels_with_options(
        self,
        request: baas_20180731_models.DescribeConsortiumChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumChannelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumChannels',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consortium_channels_with_options_async(
        self,
        request: baas_20180731_models.DescribeConsortiumChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumChannelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumChannels',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consortium_channels(
        self,
        request: baas_20180731_models.DescribeConsortiumChannelsRequest,
    ) -> baas_20180731_models.DescribeConsortiumChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consortium_channels_with_options(request, runtime)

    async def describe_consortium_channels_async(
        self,
        request: baas_20180731_models.DescribeConsortiumChannelsRequest,
    ) -> baas_20180731_models.DescribeConsortiumChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consortium_channels_with_options_async(request, runtime)

    def describe_consortium_config_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumConfigResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeConsortiumConfig',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consortium_config_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumConfigResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeConsortiumConfig',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consortium_config(self) -> baas_20180731_models.DescribeConsortiumConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consortium_config_with_options(runtime)

    async def describe_consortium_config_async(self) -> baas_20180731_models.DescribeConsortiumConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consortium_config_with_options_async(runtime)

    def describe_consortium_deletable_with_options(
        self,
        request: baas_20180731_models.DescribeConsortiumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumDeletableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumDeletableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consortium_deletable_with_options_async(
        self,
        request: baas_20180731_models.DescribeConsortiumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumDeletableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumDeletableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consortium_deletable(
        self,
        request: baas_20180731_models.DescribeConsortiumDeletableRequest,
    ) -> baas_20180731_models.DescribeConsortiumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consortium_deletable_with_options(request, runtime)

    async def describe_consortium_deletable_async(
        self,
        request: baas_20180731_models.DescribeConsortiumDeletableRequest,
    ) -> baas_20180731_models.DescribeConsortiumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consortium_deletable_with_options_async(request, runtime)

    def describe_consortium_member_approval_with_options(
        self,
        request: baas_20180731_models.DescribeConsortiumMemberApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumMemberApprovalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumMemberApproval',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumMemberApprovalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consortium_member_approval_with_options_async(
        self,
        request: baas_20180731_models.DescribeConsortiumMemberApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumMemberApprovalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumMemberApproval',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumMemberApprovalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consortium_member_approval(
        self,
        request: baas_20180731_models.DescribeConsortiumMemberApprovalRequest,
    ) -> baas_20180731_models.DescribeConsortiumMemberApprovalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consortium_member_approval_with_options(request, runtime)

    async def describe_consortium_member_approval_async(
        self,
        request: baas_20180731_models.DescribeConsortiumMemberApprovalRequest,
    ) -> baas_20180731_models.DescribeConsortiumMemberApprovalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consortium_member_approval_with_options_async(request, runtime)

    def describe_consortium_members_with_options(
        self,
        request: baas_20180731_models.DescribeConsortiumMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumMembers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consortium_members_with_options_async(
        self,
        request: baas_20180731_models.DescribeConsortiumMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumMembers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consortium_members(
        self,
        request: baas_20180731_models.DescribeConsortiumMembersRequest,
    ) -> baas_20180731_models.DescribeConsortiumMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consortium_members_with_options(request, runtime)

    async def describe_consortium_members_async(
        self,
        request: baas_20180731_models.DescribeConsortiumMembersRequest,
    ) -> baas_20180731_models.DescribeConsortiumMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consortium_members_with_options_async(request, runtime)

    def describe_consortium_orderers_with_options(
        self,
        request: baas_20180731_models.DescribeConsortiumOrderersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumOrderersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumOrderers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumOrderersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consortium_orderers_with_options_async(
        self,
        request: baas_20180731_models.DescribeConsortiumOrderersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumOrderersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiumOrderers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumOrderersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consortium_orderers(
        self,
        request: baas_20180731_models.DescribeConsortiumOrderersRequest,
    ) -> baas_20180731_models.DescribeConsortiumOrderersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consortium_orderers_with_options(request, runtime)

    async def describe_consortium_orderers_async(
        self,
        request: baas_20180731_models.DescribeConsortiumOrderersRequest,
    ) -> baas_20180731_models.DescribeConsortiumOrderersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consortium_orderers_with_options_async(request, runtime)

    def describe_consortium_specs_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumSpecsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeConsortiumSpecs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consortium_specs_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumSpecsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeConsortiumSpecs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consortium_specs(self) -> baas_20180731_models.DescribeConsortiumSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consortium_specs_with_options(runtime)

    async def describe_consortium_specs_async(self) -> baas_20180731_models.DescribeConsortiumSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consortium_specs_with_options_async(runtime)

    def describe_consortiums_with_options(
        self,
        request: baas_20180731_models.DescribeConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiums',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consortiums_with_options_async(
        self,
        request: baas_20180731_models.DescribeConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeConsortiumsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeConsortiums',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeConsortiumsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consortiums(
        self,
        request: baas_20180731_models.DescribeConsortiumsRequest,
    ) -> baas_20180731_models.DescribeConsortiumsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consortiums_with_options(request, runtime)

    async def describe_consortiums_async(
        self,
        request: baas_20180731_models.DescribeConsortiumsRequest,
    ) -> baas_20180731_models.DescribeConsortiumsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consortiums_with_options_async(request, runtime)

    def describe_download_paths_with_options(
        self,
        request: baas_20180731_models.DescribeDownloadPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeDownloadPathsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDownloadPaths',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeDownloadPathsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_paths_with_options_async(
        self,
        request: baas_20180731_models.DescribeDownloadPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeDownloadPathsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDownloadPaths',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeDownloadPathsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_paths(
        self,
        request: baas_20180731_models.DescribeDownloadPathsRequest,
    ) -> baas_20180731_models.DescribeDownloadPathsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_download_paths_with_options(request, runtime)

    async def describe_download_paths_async(
        self,
        request: baas_20180731_models.DescribeDownloadPathsRequest,
    ) -> baas_20180731_models.DescribeDownloadPathsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_paths_with_options_async(request, runtime)

    def describe_download_paths_of_contract_chain_with_options(
        self,
        request: baas_20180731_models.DescribeDownloadPathsOfContractChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeDownloadPathsOfContractChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDownloadPathsOfContractChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeDownloadPathsOfContractChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_paths_of_contract_chain_with_options_async(
        self,
        request: baas_20180731_models.DescribeDownloadPathsOfContractChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeDownloadPathsOfContractChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDownloadPathsOfContractChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeDownloadPathsOfContractChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_paths_of_contract_chain(
        self,
        request: baas_20180731_models.DescribeDownloadPathsOfContractChainRequest,
    ) -> baas_20180731_models.DescribeDownloadPathsOfContractChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_download_paths_of_contract_chain_with_options(request, runtime)

    async def describe_download_paths_of_contract_chain_async(
        self,
        request: baas_20180731_models.DescribeDownloadPathsOfContractChainRequest,
    ) -> baas_20180731_models.DescribeDownloadPathsOfContractChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_paths_of_contract_chain_with_options_async(request, runtime)

    def describe_download_paths_of_notary_chain_with_options(
        self,
        request: baas_20180731_models.DescribeDownloadPathsOfNotaryChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeDownloadPathsOfNotaryChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDownloadPathsOfNotaryChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeDownloadPathsOfNotaryChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_paths_of_notary_chain_with_options_async(
        self,
        request: baas_20180731_models.DescribeDownloadPathsOfNotaryChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeDownloadPathsOfNotaryChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDownloadPathsOfNotaryChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeDownloadPathsOfNotaryChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_paths_of_notary_chain(
        self,
        request: baas_20180731_models.DescribeDownloadPathsOfNotaryChainRequest,
    ) -> baas_20180731_models.DescribeDownloadPathsOfNotaryChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_download_paths_of_notary_chain_with_options(request, runtime)

    async def describe_download_paths_of_notary_chain_async(
        self,
        request: baas_20180731_models.DescribeDownloadPathsOfNotaryChainRequest,
    ) -> baas_20180731_models.DescribeDownloadPathsOfNotaryChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_paths_of_notary_chain_with_options_async(request, runtime)

    def describe_ecosphere_specs_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEcosphereSpecsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeEcosphereSpecs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEcosphereSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ecosphere_specs_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEcosphereSpecsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeEcosphereSpecs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEcosphereSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ecosphere_specs(self) -> baas_20180731_models.DescribeEcosphereSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ecosphere_specs_with_options(runtime)

    async def describe_ecosphere_specs_async(self) -> baas_20180731_models.DescribeEcosphereSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ecosphere_specs_with_options_async(runtime)

    def describe_ethereum_with_options(
        self,
        request: baas_20180731_models.DescribeEthereumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereum',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereum_with_options_async(
        self,
        request: baas_20180731_models.DescribeEthereumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereum',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ethereum(
        self,
        request: baas_20180731_models.DescribeEthereumRequest,
    ) -> baas_20180731_models.DescribeEthereumResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereum_with_options(request, runtime)

    async def describe_ethereum_async(
        self,
        request: baas_20180731_models.DescribeEthereumRequest,
    ) -> baas_20180731_models.DescribeEthereumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereum_with_options_async(request, runtime)

    def describe_ethereum_client_users_with_options(
        self,
        request: baas_20180731_models.DescribeEthereumClientUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumClientUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumClientUsers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumClientUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereum_client_users_with_options_async(
        self,
        request: baas_20180731_models.DescribeEthereumClientUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumClientUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumClientUsers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumClientUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ethereum_client_users(
        self,
        request: baas_20180731_models.DescribeEthereumClientUsersRequest,
    ) -> baas_20180731_models.DescribeEthereumClientUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereum_client_users_with_options(request, runtime)

    async def describe_ethereum_client_users_async(
        self,
        request: baas_20180731_models.DescribeEthereumClientUsersRequest,
    ) -> baas_20180731_models.DescribeEthereumClientUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereum_client_users_with_options_async(request, runtime)

    def describe_ethereum_deletable_with_options(
        self,
        request: baas_20180731_models.DescribeEthereumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumDeletableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumDeletableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereum_deletable_with_options_async(
        self,
        request: baas_20180731_models.DescribeEthereumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumDeletableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumDeletableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ethereum_deletable(
        self,
        request: baas_20180731_models.DescribeEthereumDeletableRequest,
    ) -> baas_20180731_models.DescribeEthereumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereum_deletable_with_options(request, runtime)

    async def describe_ethereum_deletable_async(
        self,
        request: baas_20180731_models.DescribeEthereumDeletableRequest,
    ) -> baas_20180731_models.DescribeEthereumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereum_deletable_with_options_async(request, runtime)

    def describe_ethereum_invitaion_with_options(
        self,
        request: baas_20180731_models.DescribeEthereumInvitaionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumInvitaionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumInvitaion',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumInvitaionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereum_invitaion_with_options_async(
        self,
        request: baas_20180731_models.DescribeEthereumInvitaionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumInvitaionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumInvitaion',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumInvitaionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ethereum_invitaion(
        self,
        request: baas_20180731_models.DescribeEthereumInvitaionRequest,
    ) -> baas_20180731_models.DescribeEthereumInvitaionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereum_invitaion_with_options(request, runtime)

    async def describe_ethereum_invitaion_async(
        self,
        request: baas_20180731_models.DescribeEthereumInvitaionRequest,
    ) -> baas_20180731_models.DescribeEthereumInvitaionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereum_invitaion_with_options_async(request, runtime)

    def describe_ethereum_invitee_with_options(
        self,
        request: baas_20180731_models.DescribeEthereumInviteeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumInviteeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumInvitee',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumInviteeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereum_invitee_with_options_async(
        self,
        request: baas_20180731_models.DescribeEthereumInviteeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumInviteeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumInvitee',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumInviteeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ethereum_invitee(
        self,
        request: baas_20180731_models.DescribeEthereumInviteeRequest,
    ) -> baas_20180731_models.DescribeEthereumInviteeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereum_invitee_with_options(request, runtime)

    async def describe_ethereum_invitee_async(
        self,
        request: baas_20180731_models.DescribeEthereumInviteeRequest,
    ) -> baas_20180731_models.DescribeEthereumInviteeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereum_invitee_with_options_async(request, runtime)

    def describe_ethereum_node_with_options(
        self,
        request: baas_20180731_models.DescribeEthereumNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumNodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumNode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereum_node_with_options_async(
        self,
        request: baas_20180731_models.DescribeEthereumNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumNodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumNode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ethereum_node(
        self,
        request: baas_20180731_models.DescribeEthereumNodeRequest,
    ) -> baas_20180731_models.DescribeEthereumNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereum_node_with_options(request, runtime)

    async def describe_ethereum_node_async(
        self,
        request: baas_20180731_models.DescribeEthereumNodeRequest,
    ) -> baas_20180731_models.DescribeEthereumNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereum_node_with_options_async(request, runtime)

    def describe_ethereum_node_configuration_with_options(
        self,
        request: baas_20180731_models.DescribeEthereumNodeConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumNodeConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumNodeConfiguration',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumNodeConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereum_node_configuration_with_options_async(
        self,
        request: baas_20180731_models.DescribeEthereumNodeConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumNodeConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumNodeConfiguration',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumNodeConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ethereum_node_configuration(
        self,
        request: baas_20180731_models.DescribeEthereumNodeConfigurationRequest,
    ) -> baas_20180731_models.DescribeEthereumNodeConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereum_node_configuration_with_options(request, runtime)

    async def describe_ethereum_node_configuration_async(
        self,
        request: baas_20180731_models.DescribeEthereumNodeConfigurationRequest,
    ) -> baas_20180731_models.DescribeEthereumNodeConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereum_node_configuration_with_options_async(request, runtime)

    def describe_ethereum_node_info_with_options(
        self,
        request: baas_20180731_models.DescribeEthereumNodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumNodeInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumNodeInfo',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumNodeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereum_node_info_with_options_async(
        self,
        request: baas_20180731_models.DescribeEthereumNodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumNodeInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumNodeInfo',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumNodeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ethereum_node_info(
        self,
        request: baas_20180731_models.DescribeEthereumNodeInfoRequest,
    ) -> baas_20180731_models.DescribeEthereumNodeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereum_node_info_with_options(request, runtime)

    async def describe_ethereum_node_info_async(
        self,
        request: baas_20180731_models.DescribeEthereumNodeInfoRequest,
    ) -> baas_20180731_models.DescribeEthereumNodeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereum_node_info_with_options_async(request, runtime)

    def describe_ethereum_node_logs_with_options(
        self,
        request: baas_20180731_models.DescribeEthereumNodeLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumNodeLogsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lines):
            body['Lines'] = request.lines
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumNodeLogs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumNodeLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereum_node_logs_with_options_async(
        self,
        request: baas_20180731_models.DescribeEthereumNodeLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumNodeLogsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lines):
            body['Lines'] = request.lines
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumNodeLogs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumNodeLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ethereum_node_logs(
        self,
        request: baas_20180731_models.DescribeEthereumNodeLogsRequest,
    ) -> baas_20180731_models.DescribeEthereumNodeLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereum_node_logs_with_options(request, runtime)

    async def describe_ethereum_node_logs_async(
        self,
        request: baas_20180731_models.DescribeEthereumNodeLogsRequest,
    ) -> baas_20180731_models.DescribeEthereumNodeLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereum_node_logs_with_options_async(request, runtime)

    def describe_ethereum_nodes_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumNodesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeEthereumNodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereum_nodes_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumNodesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeEthereumNodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ethereum_nodes(self) -> baas_20180731_models.DescribeEthereumNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereum_nodes_with_options(runtime)

    async def describe_ethereum_nodes_async(self) -> baas_20180731_models.DescribeEthereumNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereum_nodes_with_options_async(runtime)

    def describe_ethereums_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeEthereums',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereums_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeEthereumsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeEthereums',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeEthereumsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ethereums(self) -> baas_20180731_models.DescribeEthereumsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereums_with_options(runtime)

    async def describe_ethereums_async(self) -> baas_20180731_models.DescribeEthereumsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereums_with_options_async(runtime)

    def describe_explorer_with_options(
        self,
        request: baas_20180731_models.DescribeExplorerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeExplorerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ex_body):
            query['ExBody'] = request.ex_body
        if not UtilClient.is_unset(request.ex_method):
            query['ExMethod'] = request.ex_method
        if not UtilClient.is_unset(request.ex_url):
            query['ExUrl'] = request.ex_url
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExplorer',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeExplorerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_explorer_with_options_async(
        self,
        request: baas_20180731_models.DescribeExplorerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeExplorerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ex_body):
            query['ExBody'] = request.ex_body
        if not UtilClient.is_unset(request.ex_method):
            query['ExMethod'] = request.ex_method
        if not UtilClient.is_unset(request.ex_url):
            query['ExUrl'] = request.ex_url
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExplorer',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeExplorerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_explorer(
        self,
        request: baas_20180731_models.DescribeExplorerRequest,
    ) -> baas_20180731_models.DescribeExplorerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_explorer_with_options(request, runtime)

    async def describe_explorer_async(
        self,
        request: baas_20180731_models.DescribeExplorerRequest,
    ) -> baas_20180731_models.DescribeExplorerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_explorer_with_options_async(request, runtime)

    def describe_explorer_urlwith_options(
        self,
        request: baas_20180731_models.DescribeExplorerURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeExplorerURLResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExplorerURL',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeExplorerURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_explorer_urlwith_options_async(
        self,
        request: baas_20180731_models.DescribeExplorerURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeExplorerURLResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExplorerURL',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeExplorerURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_explorer_url(
        self,
        request: baas_20180731_models.DescribeExplorerURLRequest,
    ) -> baas_20180731_models.DescribeExplorerURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_explorer_urlwith_options(request, runtime)

    async def describe_explorer_url_async(
        self,
        request: baas_20180731_models.DescribeExplorerURLRequest,
    ) -> baas_20180731_models.DescribeExplorerURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_explorer_urlwith_options_async(request, runtime)

    def describe_fabric_chaincode_endorse_policy_with_options(
        self,
        request: baas_20180731_models.DescribeFabricChaincodeEndorsePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricChaincodeEndorsePolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_name):
            body['ChaincodeName'] = request.chaincode_name
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricChaincodeEndorsePolicy',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricChaincodeEndorsePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_chaincode_endorse_policy_with_options_async(
        self,
        request: baas_20180731_models.DescribeFabricChaincodeEndorsePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricChaincodeEndorsePolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_name):
            body['ChaincodeName'] = request.chaincode_name
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricChaincodeEndorsePolicy',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricChaincodeEndorsePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_chaincode_endorse_policy(
        self,
        request: baas_20180731_models.DescribeFabricChaincodeEndorsePolicyRequest,
    ) -> baas_20180731_models.DescribeFabricChaincodeEndorsePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_chaincode_endorse_policy_with_options(request, runtime)

    async def describe_fabric_chaincode_endorse_policy_async(
        self,
        request: baas_20180731_models.DescribeFabricChaincodeEndorsePolicyRequest,
    ) -> baas_20180731_models.DescribeFabricChaincodeEndorsePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_chaincode_endorse_policy_with_options_async(request, runtime)

    def describe_fabric_chaincode_logs_with_options(
        self,
        request: baas_20180731_models.DescribeFabricChaincodeLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricChaincodeLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chaincode_id):
            query['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.peer_name):
            query['PeerName'] = request.peer_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFabricChaincodeLogs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricChaincodeLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_chaincode_logs_with_options_async(
        self,
        request: baas_20180731_models.DescribeFabricChaincodeLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricChaincodeLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chaincode_id):
            query['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.peer_name):
            query['PeerName'] = request.peer_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFabricChaincodeLogs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricChaincodeLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_chaincode_logs(
        self,
        request: baas_20180731_models.DescribeFabricChaincodeLogsRequest,
    ) -> baas_20180731_models.DescribeFabricChaincodeLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_chaincode_logs_with_options(request, runtime)

    async def describe_fabric_chaincode_logs_async(
        self,
        request: baas_20180731_models.DescribeFabricChaincodeLogsRequest,
    ) -> baas_20180731_models.DescribeFabricChaincodeLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_chaincode_logs_with_options_async(request, runtime)

    def describe_fabric_channel_config_with_options(
        self,
        request: baas_20180731_models.DescribeFabricChannelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricChannelConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricChannelConfig',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricChannelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_channel_config_with_options_async(
        self,
        request: baas_20180731_models.DescribeFabricChannelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricChannelConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricChannelConfig',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricChannelConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_channel_config(
        self,
        request: baas_20180731_models.DescribeFabricChannelConfigRequest,
    ) -> baas_20180731_models.DescribeFabricChannelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_channel_config_with_options(request, runtime)

    async def describe_fabric_channel_config_async(
        self,
        request: baas_20180731_models.DescribeFabricChannelConfigRequest,
    ) -> baas_20180731_models.DescribeFabricChannelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_channel_config_with_options_async(request, runtime)

    def describe_fabric_channel_orderer_with_options(
        self,
        request: baas_20180731_models.DescribeFabricChannelOrdererRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricChannelOrdererResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricChannelOrderer',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricChannelOrdererResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_channel_orderer_with_options_async(
        self,
        request: baas_20180731_models.DescribeFabricChannelOrdererRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricChannelOrdererResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricChannelOrderer',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricChannelOrdererResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_channel_orderer(
        self,
        request: baas_20180731_models.DescribeFabricChannelOrdererRequest,
    ) -> baas_20180731_models.DescribeFabricChannelOrdererResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_channel_orderer_with_options(request, runtime)

    async def describe_fabric_channel_orderer_async(
        self,
        request: baas_20180731_models.DescribeFabricChannelOrdererRequest,
    ) -> baas_20180731_models.DescribeFabricChannelOrdererResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_channel_orderer_with_options_async(request, runtime)

    def describe_fabric_channel_organizations_with_options(
        self,
        request: baas_20180731_models.DescribeFabricChannelOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricChannelOrganizationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricChannelOrganizations',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricChannelOrganizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_channel_organizations_with_options_async(
        self,
        request: baas_20180731_models.DescribeFabricChannelOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricChannelOrganizationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricChannelOrganizations',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricChannelOrganizationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_channel_organizations(
        self,
        request: baas_20180731_models.DescribeFabricChannelOrganizationsRequest,
    ) -> baas_20180731_models.DescribeFabricChannelOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_channel_organizations_with_options(request, runtime)

    async def describe_fabric_channel_organizations_async(
        self,
        request: baas_20180731_models.DescribeFabricChannelOrganizationsRequest,
    ) -> baas_20180731_models.DescribeFabricChannelOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_channel_organizations_with_options_async(request, runtime)

    def describe_fabric_join_request_with_options(
        self,
        request: baas_20180731_models.DescribeFabricJoinRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricJoinRequestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricJoinRequest',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricJoinRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_join_request_with_options_async(
        self,
        request: baas_20180731_models.DescribeFabricJoinRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricJoinRequestResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricJoinRequest',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricJoinRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_join_request(
        self,
        request: baas_20180731_models.DescribeFabricJoinRequestRequest,
    ) -> baas_20180731_models.DescribeFabricJoinRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_join_request_with_options(request, runtime)

    async def describe_fabric_join_request_async(
        self,
        request: baas_20180731_models.DescribeFabricJoinRequestRequest,
    ) -> baas_20180731_models.DescribeFabricJoinRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_join_request_with_options_async(request, runtime)

    def describe_fabric_join_response_with_options(
        self,
        request: baas_20180731_models.DescribeFabricJoinResponseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricJoinResponseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricJoinResponse',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricJoinResponseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_join_response_with_options_async(
        self,
        request: baas_20180731_models.DescribeFabricJoinResponseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricJoinResponseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricJoinResponse',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricJoinResponseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_join_response(
        self,
        request: baas_20180731_models.DescribeFabricJoinResponseRequest,
    ) -> baas_20180731_models.DescribeFabricJoinResponseResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_join_response_with_options(request, runtime)

    async def describe_fabric_join_response_async(
        self,
        request: baas_20180731_models.DescribeFabricJoinResponseRequest,
    ) -> baas_20180731_models.DescribeFabricJoinResponseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_join_response_with_options_async(request, runtime)

    def describe_fabric_management_chaincodes_with_options(
        self,
        request: baas_20180731_models.DescribeFabricManagementChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricManagementChaincodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricManagementChaincodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricManagementChaincodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_management_chaincodes_with_options_async(
        self,
        request: baas_20180731_models.DescribeFabricManagementChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricManagementChaincodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricManagementChaincodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricManagementChaincodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_management_chaincodes(
        self,
        request: baas_20180731_models.DescribeFabricManagementChaincodesRequest,
    ) -> baas_20180731_models.DescribeFabricManagementChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_management_chaincodes_with_options(request, runtime)

    async def describe_fabric_management_chaincodes_async(
        self,
        request: baas_20180731_models.DescribeFabricManagementChaincodesRequest,
    ) -> baas_20180731_models.DescribeFabricManagementChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_management_chaincodes_with_options_async(request, runtime)

    def describe_fabric_organization_chaincode_package_with_options(
        self,
        request: baas_20180731_models.DescribeFabricOrganizationChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricOrganizationChaincodePackageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricOrganizationChaincodePackage',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricOrganizationChaincodePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organization_chaincode_package_with_options_async(
        self,
        request: baas_20180731_models.DescribeFabricOrganizationChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricOrganizationChaincodePackageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricOrganizationChaincodePackage',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricOrganizationChaincodePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_organization_chaincode_package(
        self,
        request: baas_20180731_models.DescribeFabricOrganizationChaincodePackageRequest,
    ) -> baas_20180731_models.DescribeFabricOrganizationChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organization_chaincode_package_with_options(request, runtime)

    async def describe_fabric_organization_chaincode_package_async(
        self,
        request: baas_20180731_models.DescribeFabricOrganizationChaincodePackageRequest,
    ) -> baas_20180731_models.DescribeFabricOrganizationChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organization_chaincode_package_with_options_async(request, runtime)

    def describe_fabric_organization_egress_with_options(
        self,
        request: baas_20180731_models.DescribeFabricOrganizationEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricOrganizationEgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFabricOrganizationEgress',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricOrganizationEgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organization_egress_with_options_async(
        self,
        request: baas_20180731_models.DescribeFabricOrganizationEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricOrganizationEgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFabricOrganizationEgress',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricOrganizationEgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_organization_egress(
        self,
        request: baas_20180731_models.DescribeFabricOrganizationEgressRequest,
    ) -> baas_20180731_models.DescribeFabricOrganizationEgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organization_egress_with_options(request, runtime)

    async def describe_fabric_organization_egress_async(
        self,
        request: baas_20180731_models.DescribeFabricOrganizationEgressRequest,
    ) -> baas_20180731_models.DescribeFabricOrganizationEgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organization_egress_with_options_async(request, runtime)

    def describe_fabric_peer_channels_with_options(
        self,
        request: baas_20180731_models.DescribeFabricPeerChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricPeerChannelsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricPeerChannels',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricPeerChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_peer_channels_with_options_async(
        self,
        request: baas_20180731_models.DescribeFabricPeerChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeFabricPeerChannelsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricPeerChannels',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeFabricPeerChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_peer_channels(
        self,
        request: baas_20180731_models.DescribeFabricPeerChannelsRequest,
    ) -> baas_20180731_models.DescribeFabricPeerChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_peer_channels_with_options(request, runtime)

    async def describe_fabric_peer_channels_async(
        self,
        request: baas_20180731_models.DescribeFabricPeerChannelsRequest,
    ) -> baas_20180731_models.DescribeFabricPeerChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_peer_channels_with_options_async(request, runtime)

    def describe_governance_task_with_options(
        self,
        request: baas_20180731_models.DescribeGovernanceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeGovernanceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGovernanceTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeGovernanceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_governance_task_with_options_async(
        self,
        request: baas_20180731_models.DescribeGovernanceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeGovernanceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGovernanceTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeGovernanceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_governance_task(
        self,
        request: baas_20180731_models.DescribeGovernanceTaskRequest,
    ) -> baas_20180731_models.DescribeGovernanceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_governance_task_with_options(request, runtime)

    async def describe_governance_task_async(
        self,
        request: baas_20180731_models.DescribeGovernanceTaskRequest,
    ) -> baas_20180731_models.DescribeGovernanceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_governance_task_with_options_async(request, runtime)

    def describe_governance_tasks_with_options(
        self,
        request: baas_20180731_models.DescribeGovernanceTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeGovernanceTasksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGovernanceTasks',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeGovernanceTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_governance_tasks_with_options_async(
        self,
        request: baas_20180731_models.DescribeGovernanceTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeGovernanceTasksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGovernanceTasks',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeGovernanceTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_governance_tasks(
        self,
        request: baas_20180731_models.DescribeGovernanceTasksRequest,
    ) -> baas_20180731_models.DescribeGovernanceTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_governance_tasks_with_options(request, runtime)

    async def describe_governance_tasks_async(
        self,
        request: baas_20180731_models.DescribeGovernanceTasksRequest,
    ) -> baas_20180731_models.DescribeGovernanceTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_governance_tasks_with_options_async(request, runtime)

    def describe_invitation_code_with_options(
        self,
        request: baas_20180731_models.DescribeInvitationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeInvitationCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInvitationCode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeInvitationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invitation_code_with_options_async(
        self,
        request: baas_20180731_models.DescribeInvitationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeInvitationCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInvitationCode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeInvitationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invitation_code(
        self,
        request: baas_20180731_models.DescribeInvitationCodeRequest,
    ) -> baas_20180731_models.DescribeInvitationCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invitation_code_with_options(request, runtime)

    async def describe_invitation_code_async(
        self,
        request: baas_20180731_models.DescribeInvitationCodeRequest,
    ) -> baas_20180731_models.DescribeInvitationCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invitation_code_with_options_async(request, runtime)

    def describe_invitation_list_with_options(
        self,
        request: baas_20180731_models.DescribeInvitationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeInvitationListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInvitationList',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeInvitationListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invitation_list_with_options_async(
        self,
        request: baas_20180731_models.DescribeInvitationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeInvitationListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInvitationList',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeInvitationListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invitation_list(
        self,
        request: baas_20180731_models.DescribeInvitationListRequest,
    ) -> baas_20180731_models.DescribeInvitationListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invitation_list_with_options(request, runtime)

    async def describe_invitation_list_async(
        self,
        request: baas_20180731_models.DescribeInvitationListRequest,
    ) -> baas_20180731_models.DescribeInvitationListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invitation_list_with_options_async(request, runtime)

    def describe_inviter_with_options(
        self,
        request: baas_20180731_models.DescribeInviterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeInviterResponse:
        """
        ***\
        
        @param request: DescribeInviterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInviterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInviter',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeInviterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inviter_with_options_async(
        self,
        request: baas_20180731_models.DescribeInviterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeInviterResponse:
        """
        ***\
        
        @param request: DescribeInviterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInviterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInviter',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeInviterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inviter(
        self,
        request: baas_20180731_models.DescribeInviterRequest,
    ) -> baas_20180731_models.DescribeInviterResponse:
        """
        ***\
        
        @param request: DescribeInviterRequest
        @return: DescribeInviterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_inviter_with_options(request, runtime)

    async def describe_inviter_async(
        self,
        request: baas_20180731_models.DescribeInviterRequest,
    ) -> baas_20180731_models.DescribeInviterResponse:
        """
        ***\
        
        @param request: DescribeInviterRequest
        @return: DescribeInviterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_inviter_with_options_async(request, runtime)

    def describe_latest_15blocks_with_options(
        self,
        request: baas_20180731_models.DescribeLatest15BlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeLatest15BlocksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLatest15Blocks',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeLatest15BlocksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_latest_15blocks_with_options_async(
        self,
        request: baas_20180731_models.DescribeLatest15BlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeLatest15BlocksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLatest15Blocks',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeLatest15BlocksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_latest_15blocks(
        self,
        request: baas_20180731_models.DescribeLatest15BlocksRequest,
    ) -> baas_20180731_models.DescribeLatest15BlocksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_latest_15blocks_with_options(request, runtime)

    async def describe_latest_15blocks_async(
        self,
        request: baas_20180731_models.DescribeLatest15BlocksRequest,
    ) -> baas_20180731_models.DescribeLatest15BlocksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_latest_15blocks_with_options_async(request, runtime)

    def describe_latest_15trans_digests_with_options(
        self,
        request: baas_20180731_models.DescribeLatest15TransDigestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeLatest15TransDigestsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLatest15TransDigests',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeLatest15TransDigestsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_latest_15trans_digests_with_options_async(
        self,
        request: baas_20180731_models.DescribeLatest15TransDigestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeLatest15TransDigestsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLatest15TransDigests',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeLatest15TransDigestsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_latest_15trans_digests(
        self,
        request: baas_20180731_models.DescribeLatest15TransDigestsRequest,
    ) -> baas_20180731_models.DescribeLatest15TransDigestsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_latest_15trans_digests_with_options(request, runtime)

    async def describe_latest_15trans_digests_async(
        self,
        request: baas_20180731_models.DescribeLatest15TransDigestsRequest,
    ) -> baas_20180731_models.DescribeLatest15TransDigestsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_latest_15trans_digests_with_options_async(request, runtime)

    def describe_latest_blocks_with_options(
        self,
        request: baas_20180731_models.DescribeLatestBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeLatestBlocksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLatestBlocks',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeLatestBlocksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_latest_blocks_with_options_async(
        self,
        request: baas_20180731_models.DescribeLatestBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeLatestBlocksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLatestBlocks',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeLatestBlocksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_latest_blocks(
        self,
        request: baas_20180731_models.DescribeLatestBlocksRequest,
    ) -> baas_20180731_models.DescribeLatestBlocksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_latest_blocks_with_options(request, runtime)

    async def describe_latest_blocks_async(
        self,
        request: baas_20180731_models.DescribeLatestBlocksRequest,
    ) -> baas_20180731_models.DescribeLatestBlocksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_latest_blocks_with_options_async(request, runtime)

    def describe_latest_transaction_digests_with_options(
        self,
        request: baas_20180731_models.DescribeLatestTransactionDigestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeLatestTransactionDigestsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLatestTransactionDigests',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeLatestTransactionDigestsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_latest_transaction_digests_with_options_async(
        self,
        request: baas_20180731_models.DescribeLatestTransactionDigestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeLatestTransactionDigestsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLatestTransactionDigests',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeLatestTransactionDigestsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_latest_transaction_digests(
        self,
        request: baas_20180731_models.DescribeLatestTransactionDigestsRequest,
    ) -> baas_20180731_models.DescribeLatestTransactionDigestsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_latest_transaction_digests_with_options(request, runtime)

    async def describe_latest_transaction_digests_async(
        self,
        request: baas_20180731_models.DescribeLatestTransactionDigestsRequest,
    ) -> baas_20180731_models.DescribeLatestTransactionDigestsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_latest_transaction_digests_with_options_async(request, runtime)

    def describe_member_role_with_options(
        self,
        request: baas_20180731_models.DescribeMemberRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMemberRoleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMemberRole',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMemberRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_member_role_with_options_async(
        self,
        request: baas_20180731_models.DescribeMemberRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMemberRoleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMemberRole',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMemberRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_member_role(
        self,
        request: baas_20180731_models.DescribeMemberRoleRequest,
    ) -> baas_20180731_models.DescribeMemberRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_member_role_with_options(request, runtime)

    async def describe_member_role_async(
        self,
        request: baas_20180731_models.DescribeMemberRoleRequest,
    ) -> baas_20180731_models.DescribeMemberRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_member_role_with_options_async(request, runtime)

    def describe_members_with_options(
        self,
        request: baas_20180731_models.DescribeMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMembers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_members_with_options_async(
        self,
        request: baas_20180731_models.DescribeMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMembers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_members(
        self,
        request: baas_20180731_models.DescribeMembersRequest,
    ) -> baas_20180731_models.DescribeMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_members_with_options(request, runtime)

    async def describe_members_async(
        self,
        request: baas_20180731_models.DescribeMembersRequest,
    ) -> baas_20180731_models.DescribeMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_members_with_options_async(request, runtime)

    def describe_metric_with_options(
        self,
        request: baas_20180731_models.DescribeMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bizid):
            query['Bizid'] = request.bizid
        body = {}
        if not UtilClient.is_unset(request.inner_ip):
            body['InnerIp'] = request.inner_ip
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.time_area):
            body['TimeArea'] = request.time_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMetric',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_with_options_async(
        self,
        request: baas_20180731_models.DescribeMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bizid):
            query['Bizid'] = request.bizid
        body = {}
        if not UtilClient.is_unset(request.inner_ip):
            body['InnerIp'] = request.inner_ip
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.time_area):
            body['TimeArea'] = request.time_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMetric',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric(
        self,
        request: baas_20180731_models.DescribeMetricRequest,
    ) -> baas_20180731_models.DescribeMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_with_options(request, runtime)

    async def describe_metric_async(
        self,
        request: baas_20180731_models.DescribeMetricRequest,
    ) -> baas_20180731_models.DescribeMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_with_options_async(request, runtime)

    def describe_my_blockchains_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMyBlockchainsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMyBlockchains',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMyBlockchainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_my_blockchains_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMyBlockchainsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMyBlockchains',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMyBlockchainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_my_blockchains(self) -> baas_20180731_models.DescribeMyBlockchainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_my_blockchains_with_options(runtime)

    async def describe_my_blockchains_async(self) -> baas_20180731_models.DescribeMyBlockchainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_my_blockchains_with_options_async(runtime)

    def describe_my_blockchan_infos_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMyBlockchanInfosResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMyBlockchanInfos',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMyBlockchanInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_my_blockchan_infos_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMyBlockchanInfosResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMyBlockchanInfos',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMyBlockchanInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_my_blockchan_infos(self) -> baas_20180731_models.DescribeMyBlockchanInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_my_blockchan_infos_with_options(runtime)

    async def describe_my_blockchan_infos_async(self) -> baas_20180731_models.DescribeMyBlockchanInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_my_blockchan_infos_with_options_async(runtime)

    def describe_my_success_applies_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMySuccessAppliesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMySuccessApplies',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMySuccessAppliesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_my_success_applies_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMySuccessAppliesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMySuccessApplies',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMySuccessAppliesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_my_success_applies(self) -> baas_20180731_models.DescribeMySuccessAppliesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_my_success_applies_with_options(runtime)

    async def describe_my_success_applies_async(self) -> baas_20180731_models.DescribeMySuccessAppliesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_my_success_applies_with_options_async(runtime)

    def describe_my_successful_application_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMySuccessfulApplicationResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMySuccessfulApplication',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMySuccessfulApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_my_successful_application_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeMySuccessfulApplicationResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMySuccessfulApplication',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeMySuccessfulApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_my_successful_application(self) -> baas_20180731_models.DescribeMySuccessfulApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_my_successful_application_with_options(runtime)

    async def describe_my_successful_application_async(self) -> baas_20180731_models.DescribeMySuccessfulApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_my_successful_application_with_options_async(runtime)

    def describe_netstat_urlwith_options(
        self,
        request: baas_20180731_models.DescribeNetstatURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeNetstatURLResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNetstatURL',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeNetstatURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_netstat_urlwith_options_async(
        self,
        request: baas_20180731_models.DescribeNetstatURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeNetstatURLResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNetstatURL',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeNetstatURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_netstat_url(
        self,
        request: baas_20180731_models.DescribeNetstatURLRequest,
    ) -> baas_20180731_models.DescribeNetstatURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_netstat_urlwith_options(request, runtime)

    async def describe_netstat_url_async(
        self,
        request: baas_20180731_models.DescribeNetstatURLRequest,
    ) -> baas_20180731_models.DescribeNetstatURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_netstat_urlwith_options_async(request, runtime)

    def describe_orderer_logs_with_options(
        self,
        request: baas_20180731_models.DescribeOrdererLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrdererLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.orderer_name):
            query['OrdererName'] = request.orderer_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOrdererLogs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrdererLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_orderer_logs_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrdererLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrdererLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.orderer_name):
            query['OrdererName'] = request.orderer_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOrdererLogs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrdererLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_orderer_logs(
        self,
        request: baas_20180731_models.DescribeOrdererLogsRequest,
    ) -> baas_20180731_models.DescribeOrdererLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_orderer_logs_with_options(request, runtime)

    async def describe_orderer_logs_async(
        self,
        request: baas_20180731_models.DescribeOrdererLogsRequest,
    ) -> baas_20180731_models.DescribeOrdererLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_orderer_logs_with_options_async(request, runtime)

    def describe_organization_with_options(
        self,
        request: baas_20180731_models.DescribeOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganization',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_organization_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganization',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_organization(
        self,
        request: baas_20180731_models.DescribeOrganizationRequest,
    ) -> baas_20180731_models.DescribeOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_organization_with_options(request, runtime)

    async def describe_organization_async(
        self,
        request: baas_20180731_models.DescribeOrganizationRequest,
    ) -> baas_20180731_models.DescribeOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_organization_with_options_async(request, runtime)

    def describe_organization_chaincodes_with_options(
        self,
        request: baas_20180731_models.DescribeOrganizationChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationChaincodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationChaincodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationChaincodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_organization_chaincodes_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrganizationChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationChaincodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationChaincodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationChaincodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_organization_chaincodes(
        self,
        request: baas_20180731_models.DescribeOrganizationChaincodesRequest,
    ) -> baas_20180731_models.DescribeOrganizationChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_organization_chaincodes_with_options(request, runtime)

    async def describe_organization_chaincodes_async(
        self,
        request: baas_20180731_models.DescribeOrganizationChaincodesRequest,
    ) -> baas_20180731_models.DescribeOrganizationChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_organization_chaincodes_with_options_async(request, runtime)

    def describe_organization_channels_with_options(
        self,
        request: baas_20180731_models.DescribeOrganizationChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationChannelsResponse:
        """
        ***\
        
        @param request: DescribeOrganizationChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOrganizationChannelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationChannels',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_organization_channels_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrganizationChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationChannelsResponse:
        """
        ***\
        
        @param request: DescribeOrganizationChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOrganizationChannelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationChannels',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_organization_channels(
        self,
        request: baas_20180731_models.DescribeOrganizationChannelsRequest,
    ) -> baas_20180731_models.DescribeOrganizationChannelsResponse:
        """
        ***\
        
        @param request: DescribeOrganizationChannelsRequest
        @return: DescribeOrganizationChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_organization_channels_with_options(request, runtime)

    async def describe_organization_channels_async(
        self,
        request: baas_20180731_models.DescribeOrganizationChannelsRequest,
    ) -> baas_20180731_models.DescribeOrganizationChannelsResponse:
        """
        ***\
        
        @param request: DescribeOrganizationChannelsRequest
        @return: DescribeOrganizationChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_organization_channels_with_options_async(request, runtime)

    def describe_organization_deletable_with_options(
        self,
        request: baas_20180731_models.DescribeOrganizationDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationDeletableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationDeletableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_organization_deletable_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrganizationDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationDeletableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationDeletableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_organization_deletable(
        self,
        request: baas_20180731_models.DescribeOrganizationDeletableRequest,
    ) -> baas_20180731_models.DescribeOrganizationDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_organization_deletable_with_options(request, runtime)

    async def describe_organization_deletable_async(
        self,
        request: baas_20180731_models.DescribeOrganizationDeletableRequest,
    ) -> baas_20180731_models.DescribeOrganizationDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_organization_deletable_with_options_async(request, runtime)

    def describe_organization_members_with_options(
        self,
        request: baas_20180731_models.DescribeOrganizationMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationMembers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_organization_members_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrganizationMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationMembersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationMembers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_organization_members(
        self,
        request: baas_20180731_models.DescribeOrganizationMembersRequest,
    ) -> baas_20180731_models.DescribeOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_organization_members_with_options(request, runtime)

    async def describe_organization_members_async(
        self,
        request: baas_20180731_models.DescribeOrganizationMembersRequest,
    ) -> baas_20180731_models.DescribeOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_organization_members_with_options_async(request, runtime)

    def describe_organization_peers_with_options(
        self,
        request: baas_20180731_models.DescribeOrganizationPeersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationPeersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationPeers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationPeersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_organization_peers_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrganizationPeersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationPeersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationPeers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationPeersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_organization_peers(
        self,
        request: baas_20180731_models.DescribeOrganizationPeersRequest,
    ) -> baas_20180731_models.DescribeOrganizationPeersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_organization_peers_with_options(request, runtime)

    async def describe_organization_peers_async(
        self,
        request: baas_20180731_models.DescribeOrganizationPeersRequest,
    ) -> baas_20180731_models.DescribeOrganizationPeersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_organization_peers_with_options_async(request, runtime)

    def describe_organization_specs_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationSpecsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeOrganizationSpecs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_organization_specs_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationSpecsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeOrganizationSpecs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_organization_specs(self) -> baas_20180731_models.DescribeOrganizationSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_organization_specs_with_options(runtime)

    async def describe_organization_specs_async(self) -> baas_20180731_models.DescribeOrganizationSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_organization_specs_with_options_async(runtime)

    def describe_organization_triggers_with_options(
        self,
        request: baas_20180731_models.DescribeOrganizationTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationTriggersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationTriggers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationTriggersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_organization_triggers_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrganizationTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationTriggersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationTriggers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationTriggersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_organization_triggers(
        self,
        request: baas_20180731_models.DescribeOrganizationTriggersRequest,
    ) -> baas_20180731_models.DescribeOrganizationTriggersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_organization_triggers_with_options(request, runtime)

    async def describe_organization_triggers_async(
        self,
        request: baas_20180731_models.DescribeOrganizationTriggersRequest,
    ) -> baas_20180731_models.DescribeOrganizationTriggersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_organization_triggers_with_options_async(request, runtime)

    def describe_organization_user_certs_with_options(
        self,
        request: baas_20180731_models.DescribeOrganizationUserCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationUserCertsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationUserCerts',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationUserCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_organization_user_certs_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrganizationUserCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationUserCertsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationUserCerts',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationUserCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_organization_user_certs(
        self,
        request: baas_20180731_models.DescribeOrganizationUserCertsRequest,
    ) -> baas_20180731_models.DescribeOrganizationUserCertsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_organization_user_certs_with_options(request, runtime)

    async def describe_organization_user_certs_async(
        self,
        request: baas_20180731_models.DescribeOrganizationUserCertsRequest,
    ) -> baas_20180731_models.DescribeOrganizationUserCertsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_organization_user_certs_with_options_async(request, runtime)

    def describe_organization_users_with_options(
        self,
        request: baas_20180731_models.DescribeOrganizationUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationUsers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_organization_users_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrganizationUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizationUsers',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_organization_users(
        self,
        request: baas_20180731_models.DescribeOrganizationUsersRequest,
    ) -> baas_20180731_models.DescribeOrganizationUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_organization_users_with_options(request, runtime)

    async def describe_organization_users_async(
        self,
        request: baas_20180731_models.DescribeOrganizationUsersRequest,
    ) -> baas_20180731_models.DescribeOrganizationUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_organization_users_with_options_async(request, runtime)

    def describe_organizations_with_options(
        self,
        request: baas_20180731_models.DescribeOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizations',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_organizations_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrganizationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrganizations',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrganizationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_organizations(
        self,
        request: baas_20180731_models.DescribeOrganizationsRequest,
    ) -> baas_20180731_models.DescribeOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_organizations_with_options(request, runtime)

    async def describe_organizations_async(
        self,
        request: baas_20180731_models.DescribeOrganizationsRequest,
    ) -> baas_20180731_models.DescribeOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_organizations_with_options_async(request, runtime)

    def describe_orgnaization_chaincodes_with_options(
        self,
        request: baas_20180731_models.DescribeOrgnaizationChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrgnaizationChaincodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrgnaizationChaincodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrgnaizationChaincodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_orgnaization_chaincodes_with_options_async(
        self,
        request: baas_20180731_models.DescribeOrgnaizationChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOrgnaizationChaincodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOrgnaizationChaincodes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOrgnaizationChaincodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_orgnaization_chaincodes(
        self,
        request: baas_20180731_models.DescribeOrgnaizationChaincodesRequest,
    ) -> baas_20180731_models.DescribeOrgnaizationChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_orgnaization_chaincodes_with_options(request, runtime)

    async def describe_orgnaization_chaincodes_async(
        self,
        request: baas_20180731_models.DescribeOrgnaizationChaincodesRequest,
    ) -> baas_20180731_models.DescribeOrgnaizationChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_orgnaization_chaincodes_with_options_async(request, runtime)

    def describe_oss_properties_with_options(
        self,
        request: baas_20180731_models.DescribeOssPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOssPropertiesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOssProperties',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOssPropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_properties_with_options_async(
        self,
        request: baas_20180731_models.DescribeOssPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeOssPropertiesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOssProperties',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeOssPropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_properties(
        self,
        request: baas_20180731_models.DescribeOssPropertiesRequest,
    ) -> baas_20180731_models.DescribeOssPropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_properties_with_options(request, runtime)

    async def describe_oss_properties_async(
        self,
        request: baas_20180731_models.DescribeOssPropertiesRequest,
    ) -> baas_20180731_models.DescribeOssPropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_properties_with_options_async(request, runtime)

    def describe_peer_logs_with_options(
        self,
        request: baas_20180731_models.DescribePeerLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribePeerLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.peer_name):
            query['PeerName'] = request.peer_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePeerLogs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribePeerLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_peer_logs_with_options_async(
        self,
        request: baas_20180731_models.DescribePeerLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribePeerLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.peer_name):
            query['PeerName'] = request.peer_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePeerLogs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribePeerLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_peer_logs(
        self,
        request: baas_20180731_models.DescribePeerLogsRequest,
    ) -> baas_20180731_models.DescribePeerLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_peer_logs_with_options(request, runtime)

    async def describe_peer_logs_async(
        self,
        request: baas_20180731_models.DescribePeerLogsRequest,
    ) -> baas_20180731_models.DescribePeerLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_peer_logs_with_options_async(request, runtime)

    def describe_public_ant_chain_contract_project_content_tree_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribePublicAntChainContractProjectContentTreeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribePublicAntChainContractProjectContentTree',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribePublicAntChainContractProjectContentTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_public_ant_chain_contract_project_content_tree_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribePublicAntChainContractProjectContentTreeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribePublicAntChainContractProjectContentTree',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribePublicAntChainContractProjectContentTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_public_ant_chain_contract_project_content_tree(self) -> baas_20180731_models.DescribePublicAntChainContractProjectContentTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_public_ant_chain_contract_project_content_tree_with_options(runtime)

    async def describe_public_ant_chain_contract_project_content_tree_async(self) -> baas_20180731_models.DescribePublicAntChainContractProjectContentTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_public_ant_chain_contract_project_content_tree_with_options_async(runtime)

    def describe_public_ant_chain_download_paths_with_options(
        self,
        request: baas_20180731_models.DescribePublicAntChainDownloadPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribePublicAntChainDownloadPathsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePublicAntChainDownloadPaths',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribePublicAntChainDownloadPathsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_public_ant_chain_download_paths_with_options_async(
        self,
        request: baas_20180731_models.DescribePublicAntChainDownloadPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribePublicAntChainDownloadPathsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePublicAntChainDownloadPaths',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribePublicAntChainDownloadPathsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_public_ant_chain_download_paths(
        self,
        request: baas_20180731_models.DescribePublicAntChainDownloadPathsRequest,
    ) -> baas_20180731_models.DescribePublicAntChainDownloadPathsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_public_ant_chain_download_paths_with_options(request, runtime)

    async def describe_public_ant_chain_download_paths_async(
        self,
        request: baas_20180731_models.DescribePublicAntChainDownloadPathsRequest,
    ) -> baas_20180731_models.DescribePublicAntChainDownloadPathsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_public_ant_chain_download_paths_with_options_async(request, runtime)

    def describe_public_cloud_ideenv_configs_with_options(
        self,
        request: baas_20180731_models.DescribePublicCloudIDEEnvConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribePublicCloudIDEEnvConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePublicCloudIDEEnvConfigs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribePublicCloudIDEEnvConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_public_cloud_ideenv_configs_with_options_async(
        self,
        request: baas_20180731_models.DescribePublicCloudIDEEnvConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribePublicCloudIDEEnvConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePublicCloudIDEEnvConfigs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribePublicCloudIDEEnvConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_public_cloud_ideenv_configs(
        self,
        request: baas_20180731_models.DescribePublicCloudIDEEnvConfigsRequest,
    ) -> baas_20180731_models.DescribePublicCloudIDEEnvConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_public_cloud_ideenv_configs_with_options(request, runtime)

    async def describe_public_cloud_ideenv_configs_async(
        self,
        request: baas_20180731_models.DescribePublicCloudIDEEnvConfigsRequest,
    ) -> baas_20180731_models.DescribePublicCloudIDEEnvConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_public_cloud_ideenv_configs_with_options_async(request, runtime)

    def describe_qrcode_access_log_with_options(
        self,
        request: baas_20180731_models.DescribeQRCodeAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeQRCodeAccessLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeQRCodeAccessLog',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeQRCodeAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_qrcode_access_log_with_options_async(
        self,
        request: baas_20180731_models.DescribeQRCodeAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeQRCodeAccessLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeQRCodeAccessLog',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeQRCodeAccessLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_qrcode_access_log(
        self,
        request: baas_20180731_models.DescribeQRCodeAccessLogRequest,
    ) -> baas_20180731_models.DescribeQRCodeAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_qrcode_access_log_with_options(request, runtime)

    async def describe_qrcode_access_log_async(
        self,
        request: baas_20180731_models.DescribeQRCodeAccessLogRequest,
    ) -> baas_20180731_models.DescribeQRCodeAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_qrcode_access_log_with_options_async(request, runtime)

    def describe_qrcode_authority_with_options(
        self,
        request: baas_20180731_models.DescribeQRCodeAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeQRCodeAuthorityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeQRCodeAuthority',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeQRCodeAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_qrcode_authority_with_options_async(
        self,
        request: baas_20180731_models.DescribeQRCodeAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeQRCodeAuthorityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeQRCodeAuthority',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeQRCodeAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_qrcode_authority(
        self,
        request: baas_20180731_models.DescribeQRCodeAuthorityRequest,
    ) -> baas_20180731_models.DescribeQRCodeAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_qrcode_authority_with_options(request, runtime)

    async def describe_qrcode_authority_async(
        self,
        request: baas_20180731_models.DescribeQRCodeAuthorityRequest,
    ) -> baas_20180731_models.DescribeQRCodeAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_qrcode_authority_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> baas_20180731_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> baas_20180731_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def describe_resource_type_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeResourceTypeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeResourceType',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_type_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeResourceTypeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeResourceType',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_type(self) -> baas_20180731_models.DescribeResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_type_with_options(runtime)

    async def describe_resource_type_async(self) -> baas_20180731_models.DescribeResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_type_with_options_async(runtime)

    def describe_resource_types_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeResourceTypes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeResourceTypes',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_types(self) -> baas_20180731_models.DescribeResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_types_with_options(runtime)

    async def describe_resource_types_async(self) -> baas_20180731_models.DescribeResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_types_with_options_async(runtime)

    def describe_root_domain_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeRootDomainResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRootDomain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeRootDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_root_domain_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeRootDomainResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRootDomain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeRootDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_root_domain(self) -> baas_20180731_models.DescribeRootDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_root_domain_with_options(runtime)

    async def describe_root_domain_async(self) -> baas_20180731_models.DescribeRootDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_root_domain_with_options_async(runtime)

    def describe_schema_detail_with_options(
        self,
        request: baas_20180731_models.DescribeSchemaDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSchemaDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSchemaDetail',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSchemaDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_schema_detail_with_options_async(
        self,
        request: baas_20180731_models.DescribeSchemaDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSchemaDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSchemaDetail',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSchemaDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_schema_detail(
        self,
        request: baas_20180731_models.DescribeSchemaDetailRequest,
    ) -> baas_20180731_models.DescribeSchemaDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_schema_detail_with_options(request, runtime)

    async def describe_schema_detail_async(
        self,
        request: baas_20180731_models.DescribeSchemaDetailRequest,
    ) -> baas_20180731_models.DescribeSchemaDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_schema_detail_with_options_async(request, runtime)

    def describe_smart_contract_job_status_with_options(
        self,
        request: baas_20180731_models.DescribeSmartContractJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSmartContractJobStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartContractJobStatus',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSmartContractJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_contract_job_status_with_options_async(
        self,
        request: baas_20180731_models.DescribeSmartContractJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSmartContractJobStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartContractJobStatus',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSmartContractJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_contract_job_status(
        self,
        request: baas_20180731_models.DescribeSmartContractJobStatusRequest,
    ) -> baas_20180731_models.DescribeSmartContractJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_contract_job_status_with_options(request, runtime)

    async def describe_smart_contract_job_status_async(
        self,
        request: baas_20180731_models.DescribeSmartContractJobStatusRequest,
    ) -> baas_20180731_models.DescribeSmartContractJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_contract_job_status_with_options_async(request, runtime)

    def describe_smart_contract_jobs_with_options(
        self,
        request: baas_20180731_models.DescribeSmartContractJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSmartContractJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartContractJobs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSmartContractJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_contract_jobs_with_options_async(
        self,
        request: baas_20180731_models.DescribeSmartContractJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSmartContractJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartContractJobs',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSmartContractJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_contract_jobs(
        self,
        request: baas_20180731_models.DescribeSmartContractJobsRequest,
    ) -> baas_20180731_models.DescribeSmartContractJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_contract_jobs_with_options(request, runtime)

    async def describe_smart_contract_jobs_async(
        self,
        request: baas_20180731_models.DescribeSmartContractJobsRequest,
    ) -> baas_20180731_models.DescribeSmartContractJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_contract_jobs_with_options_async(request, runtime)

    def describe_smart_contract_jobs_by_name_with_options(
        self,
        request: baas_20180731_models.DescribeSmartContractJobsByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSmartContractJobsByNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartContractJobsByName',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSmartContractJobsByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_contract_jobs_by_name_with_options_async(
        self,
        request: baas_20180731_models.DescribeSmartContractJobsByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSmartContractJobsByNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartContractJobsByName',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSmartContractJobsByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_contract_jobs_by_name(
        self,
        request: baas_20180731_models.DescribeSmartContractJobsByNameRequest,
    ) -> baas_20180731_models.DescribeSmartContractJobsByNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_contract_jobs_by_name_with_options(request, runtime)

    async def describe_smart_contract_jobs_by_name_async(
        self,
        request: baas_20180731_models.DescribeSmartContractJobsByNameRequest,
    ) -> baas_20180731_models.DescribeSmartContractJobsByNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_contract_jobs_by_name_with_options_async(request, runtime)

    def describe_smart_contract_result_with_options(
        self,
        request: baas_20180731_models.DescribeSmartContractResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSmartContractResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartContractResult',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSmartContractResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_contract_result_with_options_async(
        self,
        request: baas_20180731_models.DescribeSmartContractResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSmartContractResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartContractResult',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSmartContractResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_contract_result(
        self,
        request: baas_20180731_models.DescribeSmartContractResultRequest,
    ) -> baas_20180731_models.DescribeSmartContractResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_contract_result_with_options(request, runtime)

    async def describe_smart_contract_result_async(
        self,
        request: baas_20180731_models.DescribeSmartContractResultRequest,
    ) -> baas_20180731_models.DescribeSmartContractResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_contract_result_with_options_async(request, runtime)

    def describe_smart_contract_result_content_with_options(
        self,
        request: baas_20180731_models.DescribeSmartContractResultContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSmartContractResultContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartContractResultContent',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSmartContractResultContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_contract_result_content_with_options_async(
        self,
        request: baas_20180731_models.DescribeSmartContractResultContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSmartContractResultContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartContractResultContent',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSmartContractResultContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_contract_result_content(
        self,
        request: baas_20180731_models.DescribeSmartContractResultContentRequest,
    ) -> baas_20180731_models.DescribeSmartContractResultContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_contract_result_content_with_options(request, runtime)

    async def describe_smart_contract_result_content_async(
        self,
        request: baas_20180731_models.DescribeSmartContractResultContentRequest,
    ) -> baas_20180731_models.DescribeSmartContractResultContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_contract_result_content_with_options_async(request, runtime)

    def describe_subscribe_cloud_service_integration_state_with_options(
        self,
        request: baas_20180731_models.DescribeSubscribeCloudServiceIntegrationStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSubscribeCloudServiceIntegrationStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscribeCloudServiceIntegrationState',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSubscribeCloudServiceIntegrationStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscribe_cloud_service_integration_state_with_options_async(
        self,
        request: baas_20180731_models.DescribeSubscribeCloudServiceIntegrationStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeSubscribeCloudServiceIntegrationStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscribeCloudServiceIntegrationState',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeSubscribeCloudServiceIntegrationStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscribe_cloud_service_integration_state(
        self,
        request: baas_20180731_models.DescribeSubscribeCloudServiceIntegrationStateRequest,
    ) -> baas_20180731_models.DescribeSubscribeCloudServiceIntegrationStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_subscribe_cloud_service_integration_state_with_options(request, runtime)

    async def describe_subscribe_cloud_service_integration_state_async(
        self,
        request: baas_20180731_models.DescribeSubscribeCloudServiceIntegrationStateRequest,
    ) -> baas_20180731_models.DescribeSubscribeCloudServiceIntegrationStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscribe_cloud_service_integration_state_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTasksResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTasksResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(self) -> baas_20180731_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(runtime)

    async def describe_tasks_async(self) -> baas_20180731_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(runtime)

    def describe_templates_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTemplatesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeTemplates',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_templates_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTemplatesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeTemplates',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_templates(self) -> baas_20180731_models.DescribeTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_templates_with_options(runtime)

    async def describe_templates_async(self) -> baas_20180731_models.DescribeTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_templates_with_options_async(runtime)

    def describe_transaction_with_options(
        self,
        request: baas_20180731_models.DescribeTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTransaction',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTransactionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transaction_with_options_async(
        self,
        request: baas_20180731_models.DescribeTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTransaction',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTransactionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transaction(
        self,
        request: baas_20180731_models.DescribeTransactionRequest,
    ) -> baas_20180731_models.DescribeTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_transaction_with_options(request, runtime)

    async def describe_transaction_async(
        self,
        request: baas_20180731_models.DescribeTransactionRequest,
    ) -> baas_20180731_models.DescribeTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_transaction_with_options_async(request, runtime)

    def describe_transaction_for_2cbrowser_with_options(
        self,
        request: baas_20180731_models.DescribeTransactionFor2CBrowserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTransactionFor2CBrowserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alipay_auth_code):
            body['AlipayAuthCode'] = request.alipay_auth_code
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTransactionFor2CBrowser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTransactionFor2CBrowserResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transaction_for_2cbrowser_with_options_async(
        self,
        request: baas_20180731_models.DescribeTransactionFor2CBrowserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTransactionFor2CBrowserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alipay_auth_code):
            body['AlipayAuthCode'] = request.alipay_auth_code
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTransactionFor2CBrowser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTransactionFor2CBrowserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transaction_for_2cbrowser(
        self,
        request: baas_20180731_models.DescribeTransactionFor2CBrowserRequest,
    ) -> baas_20180731_models.DescribeTransactionFor2CBrowserResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_transaction_for_2cbrowser_with_options(request, runtime)

    async def describe_transaction_for_2cbrowser_async(
        self,
        request: baas_20180731_models.DescribeTransactionFor2CBrowserRequest,
    ) -> baas_20180731_models.DescribeTransactionFor2CBrowserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_transaction_for_2cbrowser_with_options_async(request, runtime)

    def describe_transaction_qrcode_with_options(
        self,
        request: baas_20180731_models.DescribeTransactionQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTransactionQRCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTransactionQRCode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTransactionQRCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transaction_qrcode_with_options_async(
        self,
        request: baas_20180731_models.DescribeTransactionQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTransactionQRCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTransactionQRCode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTransactionQRCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transaction_qrcode(
        self,
        request: baas_20180731_models.DescribeTransactionQRCodeRequest,
    ) -> baas_20180731_models.DescribeTransactionQRCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_transaction_qrcode_with_options(request, runtime)

    async def describe_transaction_qrcode_async(
        self,
        request: baas_20180731_models.DescribeTransactionQRCodeRequest,
    ) -> baas_20180731_models.DescribeTransactionQRCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_transaction_qrcode_with_options_async(request, runtime)

    def describe_transaction_receipt_for_2cbrowser_with_options(
        self,
        request: baas_20180731_models.DescribeTransactionReceiptFor2CBrowserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTransactionReceiptFor2CBrowserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alipay_auth_code):
            body['AlipayAuthCode'] = request.alipay_auth_code
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTransactionReceiptFor2CBrowser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTransactionReceiptFor2CBrowserResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transaction_receipt_for_2cbrowser_with_options_async(
        self,
        request: baas_20180731_models.DescribeTransactionReceiptFor2CBrowserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTransactionReceiptFor2CBrowserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alipay_auth_code):
            body['AlipayAuthCode'] = request.alipay_auth_code
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTransactionReceiptFor2CBrowser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTransactionReceiptFor2CBrowserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transaction_receipt_for_2cbrowser(
        self,
        request: baas_20180731_models.DescribeTransactionReceiptFor2CBrowserRequest,
    ) -> baas_20180731_models.DescribeTransactionReceiptFor2CBrowserResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_transaction_receipt_for_2cbrowser_with_options(request, runtime)

    async def describe_transaction_receipt_for_2cbrowser_async(
        self,
        request: baas_20180731_models.DescribeTransactionReceiptFor2CBrowserRequest,
    ) -> baas_20180731_models.DescribeTransactionReceiptFor2CBrowserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_transaction_receipt_for_2cbrowser_with_options_async(request, runtime)

    def describe_trigger_with_options(
        self,
        request: baas_20180731_models.DescribeTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrigger',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trigger_with_options_async(
        self,
        request: baas_20180731_models.DescribeTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DescribeTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrigger',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DescribeTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trigger(
        self,
        request: baas_20180731_models.DescribeTriggerRequest,
    ) -> baas_20180731_models.DescribeTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_trigger_with_options(request, runtime)

    async def describe_trigger_async(
        self,
        request: baas_20180731_models.DescribeTriggerRequest,
    ) -> baas_20180731_models.DescribeTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_trigger_with_options_async(request, runtime)

    def destroy_consortium_with_options(
        self,
        request: baas_20180731_models.DestroyConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DestroyConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DestroyConsortium',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DestroyConsortiumResponse(),
            self.call_api(params, req, runtime)
        )

    async def destroy_consortium_with_options_async(
        self,
        request: baas_20180731_models.DestroyConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DestroyConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DestroyConsortium',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DestroyConsortiumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def destroy_consortium(
        self,
        request: baas_20180731_models.DestroyConsortiumRequest,
    ) -> baas_20180731_models.DestroyConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return self.destroy_consortium_with_options(request, runtime)

    async def destroy_consortium_async(
        self,
        request: baas_20180731_models.DestroyConsortiumRequest,
    ) -> baas_20180731_models.DestroyConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destroy_consortium_with_options_async(request, runtime)

    def destroy_ethereum_with_options(
        self,
        request: baas_20180731_models.DestroyEthereumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DestroyEthereumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DestroyEthereum',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DestroyEthereumResponse(),
            self.call_api(params, req, runtime)
        )

    async def destroy_ethereum_with_options_async(
        self,
        request: baas_20180731_models.DestroyEthereumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DestroyEthereumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DestroyEthereum',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DestroyEthereumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def destroy_ethereum(
        self,
        request: baas_20180731_models.DestroyEthereumRequest,
    ) -> baas_20180731_models.DestroyEthereumResponse:
        runtime = util_models.RuntimeOptions()
        return self.destroy_ethereum_with_options(request, runtime)

    async def destroy_ethereum_async(
        self,
        request: baas_20180731_models.DestroyEthereumRequest,
    ) -> baas_20180731_models.DestroyEthereumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destroy_ethereum_with_options_async(request, runtime)

    def destroy_organization_with_options(
        self,
        request: baas_20180731_models.DestroyOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DestroyOrganizationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DestroyOrganization',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DestroyOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def destroy_organization_with_options_async(
        self,
        request: baas_20180731_models.DestroyOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DestroyOrganizationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DestroyOrganization',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DestroyOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def destroy_organization(
        self,
        request: baas_20180731_models.DestroyOrganizationRequest,
    ) -> baas_20180731_models.DestroyOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.destroy_organization_with_options(request, runtime)

    async def destroy_organization_async(
        self,
        request: baas_20180731_models.DestroyOrganizationRequest,
    ) -> baas_20180731_models.DestroyOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destroy_organization_with_options_async(request, runtime)

    def download_all_with_options(
        self,
        request: baas_20180731_models.DownloadAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadAllResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadAll',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_all_with_options_async(
        self,
        request: baas_20180731_models.DownloadAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadAllResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadAll',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_all(
        self,
        request: baas_20180731_models.DownloadAllRequest,
    ) -> baas_20180731_models.DownloadAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_all_with_options(request, runtime)

    async def download_all_async(
        self,
        request: baas_20180731_models.DownloadAllRequest,
    ) -> baas_20180731_models.DownloadAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_all_with_options_async(request, runtime)

    def download_bizview_with_options(
        self,
        request: baas_20180731_models.DownloadBizviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadBizviewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadBizview',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadBizviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_bizview_with_options_async(
        self,
        request: baas_20180731_models.DownloadBizviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadBizviewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadBizview',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadBizviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_bizview(
        self,
        request: baas_20180731_models.DownloadBizviewRequest,
    ) -> baas_20180731_models.DownloadBizviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_bizview_with_options(request, runtime)

    async def download_bizview_async(
        self,
        request: baas_20180731_models.DownloadBizviewRequest,
    ) -> baas_20180731_models.DownloadBizviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_bizview_with_options_async(request, runtime)

    def download_fabric_channel_sdkwith_options(
        self,
        request: baas_20180731_models.DownloadFabricChannelSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadFabricChannelSDKResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadFabricChannelSDK',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadFabricChannelSDKResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_fabric_channel_sdkwith_options_async(
        self,
        request: baas_20180731_models.DownloadFabricChannelSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadFabricChannelSDKResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadFabricChannelSDK',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadFabricChannelSDKResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_fabric_channel_sdk(
        self,
        request: baas_20180731_models.DownloadFabricChannelSDKRequest,
    ) -> baas_20180731_models.DownloadFabricChannelSDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_fabric_channel_sdkwith_options(request, runtime)

    async def download_fabric_channel_sdk_async(
        self,
        request: baas_20180731_models.DownloadFabricChannelSDKRequest,
    ) -> baas_20180731_models.DownloadFabricChannelSDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_fabric_channel_sdkwith_options_async(request, runtime)

    def download_organization_sdkwith_options(
        self,
        request: baas_20180731_models.DownloadOrganizationSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadOrganizationSDKResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadOrganizationSDK',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadOrganizationSDKResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_organization_sdkwith_options_async(
        self,
        request: baas_20180731_models.DownloadOrganizationSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadOrganizationSDKResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadOrganizationSDK',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadOrganizationSDKResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_organization_sdk(
        self,
        request: baas_20180731_models.DownloadOrganizationSDKRequest,
    ) -> baas_20180731_models.DownloadOrganizationSDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_organization_sdkwith_options(request, runtime)

    async def download_organization_sdk_async(
        self,
        request: baas_20180731_models.DownloadOrganizationSDKRequest,
    ) -> baas_20180731_models.DownloadOrganizationSDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_organization_sdkwith_options_async(request, runtime)

    def download_sdk2with_options(
        self,
        request: baas_20180731_models.DownloadSDK2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadSDK2Response:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadSDK2',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadSDK2Response(),
            self.call_api(params, req, runtime)
        )

    async def download_sdk2with_options_async(
        self,
        request: baas_20180731_models.DownloadSDK2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadSDK2Response:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadSDK2',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadSDK2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def download_sdk2(
        self,
        request: baas_20180731_models.DownloadSDK2Request,
    ) -> baas_20180731_models.DownloadSDK2Response:
        runtime = util_models.RuntimeOptions()
        return self.download_sdk2with_options(request, runtime)

    async def download_sdk2_async(
        self,
        request: baas_20180731_models.DownloadSDK2Request,
    ) -> baas_20180731_models.DownloadSDK2Response:
        runtime = util_models.RuntimeOptions()
        return await self.download_sdk2with_options_async(request, runtime)

    def download_sdk_with_options(
        self,
        request: baas_20180731_models.DownloadSdkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadSdkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadSdk',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadSdkResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_sdk_with_options_async(
        self,
        request: baas_20180731_models.DownloadSdkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadSdkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadSdk',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadSdkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_sdk(
        self,
        request: baas_20180731_models.DownloadSdkRequest,
    ) -> baas_20180731_models.DownloadSdkResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_sdk_with_options(request, runtime)

    async def download_sdk_async(
        self,
        request: baas_20180731_models.DownloadSdkRequest,
    ) -> baas_20180731_models.DownloadSdkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_sdk_with_options_async(request, runtime)

    def download_signed_data_with_options(
        self,
        request: baas_20180731_models.DownloadSignedDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadSignedDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadSignedData',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadSignedDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_signed_data_with_options_async(
        self,
        request: baas_20180731_models.DownloadSignedDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DownloadSignedDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadSignedData',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DownloadSignedDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_signed_data(
        self,
        request: baas_20180731_models.DownloadSignedDataRequest,
    ) -> baas_20180731_models.DownloadSignedDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_signed_data_with_options(request, runtime)

    async def download_signed_data_async(
        self,
        request: baas_20180731_models.DownloadSignedDataRequest,
    ) -> baas_20180731_models.DownloadSignedDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_signed_data_with_options_async(request, runtime)

    def duplicate_ant_chain_contract_project_with_options(
        self,
        request: baas_20180731_models.DuplicateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DuplicateAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_version):
            body['ProjectVersion'] = request.project_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DuplicateAntChainContractProject',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DuplicateAntChainContractProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def duplicate_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20180731_models.DuplicateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.DuplicateAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_version):
            body['ProjectVersion'] = request.project_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DuplicateAntChainContractProject',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.DuplicateAntChainContractProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def duplicate_ant_chain_contract_project(
        self,
        request: baas_20180731_models.DuplicateAntChainContractProjectRequest,
    ) -> baas_20180731_models.DuplicateAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.duplicate_ant_chain_contract_project_with_options(request, runtime)

    async def duplicate_ant_chain_contract_project_async(
        self,
        request: baas_20180731_models.DuplicateAntChainContractProjectRequest,
    ) -> baas_20180731_models.DuplicateAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.duplicate_ant_chain_contract_project_with_options_async(request, runtime)

    def freeze_account_with_options(
        self,
        request: baas_20180731_models.FreezeAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.FreezeAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FreezeAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.FreezeAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def freeze_account_with_options_async(
        self,
        request: baas_20180731_models.FreezeAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.FreezeAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FreezeAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.FreezeAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def freeze_account(
        self,
        request: baas_20180731_models.FreezeAccountRequest,
    ) -> baas_20180731_models.FreezeAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.freeze_account_with_options(request, runtime)

    async def freeze_account_async(
        self,
        request: baas_20180731_models.FreezeAccountRequest,
    ) -> baas_20180731_models.FreezeAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.freeze_account_with_options_async(request, runtime)

    def freeze_ant_chain_account_with_options(
        self,
        request: baas_20180731_models.FreezeAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.FreezeAntChainAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FreezeAntChainAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.FreezeAntChainAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def freeze_ant_chain_account_with_options_async(
        self,
        request: baas_20180731_models.FreezeAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.FreezeAntChainAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FreezeAntChainAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.FreezeAntChainAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def freeze_ant_chain_account(
        self,
        request: baas_20180731_models.FreezeAntChainAccountRequest,
    ) -> baas_20180731_models.FreezeAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.freeze_ant_chain_account_with_options(request, runtime)

    async def freeze_ant_chain_account_async(
        self,
        request: baas_20180731_models.FreezeAntChainAccountRequest,
    ) -> baas_20180731_models.FreezeAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.freeze_ant_chain_account_with_options_async(request, runtime)

    def get_applies_with_options(
        self,
        request: baas_20180731_models.GetAppliesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetAppliesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApplies',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetAppliesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_applies_with_options_async(
        self,
        request: baas_20180731_models.GetAppliesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetAppliesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApplies',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetAppliesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_applies(
        self,
        request: baas_20180731_models.GetAppliesRequest,
    ) -> baas_20180731_models.GetAppliesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_applies_with_options(request, runtime)

    async def get_applies_async(
        self,
        request: baas_20180731_models.GetAppliesRequest,
    ) -> baas_20180731_models.GetAppliesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_applies_with_options_async(request, runtime)

    def get_bc_schema_with_options(
        self,
        request: baas_20180731_models.GetBcSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetBcSchemaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBcSchema',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetBcSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bc_schema_with_options_async(
        self,
        request: baas_20180731_models.GetBcSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetBcSchemaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBcSchema',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetBcSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bc_schema(
        self,
        request: baas_20180731_models.GetBcSchemaRequest,
    ) -> baas_20180731_models.GetBcSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bc_schema_with_options(request, runtime)

    async def get_bc_schema_async(
        self,
        request: baas_20180731_models.GetBcSchemaRequest,
    ) -> baas_20180731_models.GetBcSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bc_schema_with_options_async(request, runtime)

    def get_blockchain_create_task_with_options(
        self,
        request: baas_20180731_models.GetBlockchainCreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetBlockchainCreateTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBlockchainCreateTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetBlockchainCreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_blockchain_create_task_with_options_async(
        self,
        request: baas_20180731_models.GetBlockchainCreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetBlockchainCreateTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBlockchainCreateTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetBlockchainCreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_blockchain_create_task(
        self,
        request: baas_20180731_models.GetBlockchainCreateTaskRequest,
    ) -> baas_20180731_models.GetBlockchainCreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_blockchain_create_task_with_options(request, runtime)

    async def get_blockchain_create_task_async(
        self,
        request: baas_20180731_models.GetBlockchainCreateTaskRequest,
    ) -> baas_20180731_models.GetBlockchainCreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_blockchain_create_task_with_options_async(request, runtime)

    def get_blockchain_info_with_options(
        self,
        request: baas_20180731_models.GetBlockchainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetBlockchainInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBlockchainInfo',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetBlockchainInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_blockchain_info_with_options_async(
        self,
        request: baas_20180731_models.GetBlockchainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetBlockchainInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBlockchainInfo',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetBlockchainInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_blockchain_info(
        self,
        request: baas_20180731_models.GetBlockchainInfoRequest,
    ) -> baas_20180731_models.GetBlockchainInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_blockchain_info_with_options(request, runtime)

    async def get_blockchain_info_async(
        self,
        request: baas_20180731_models.GetBlockchainInfoRequest,
    ) -> baas_20180731_models.GetBlockchainInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_blockchain_info_with_options_async(request, runtime)

    def get_my_blockchains_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetMyBlockchainsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMyBlockchains',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetMyBlockchainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_my_blockchains_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetMyBlockchainsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMyBlockchains',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetMyBlockchainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_my_blockchains(self) -> baas_20180731_models.GetMyBlockchainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_my_blockchains_with_options(runtime)

    async def get_my_blockchains_async(self) -> baas_20180731_models.GetMyBlockchainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_my_blockchains_with_options_async(runtime)

    def get_my_success_applies_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetMySuccessAppliesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMySuccessApplies',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetMySuccessAppliesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_my_success_applies_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetMySuccessAppliesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMySuccessApplies',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetMySuccessAppliesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_my_success_applies(self) -> baas_20180731_models.GetMySuccessAppliesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_my_success_applies_with_options(runtime)

    async def get_my_success_applies_async(self) -> baas_20180731_models.GetMySuccessAppliesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_my_success_applies_with_options_async(runtime)

    def get_oss_properties_with_options(
        self,
        request: baas_20180731_models.GetOssPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetOssPropertiesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOssProperties',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetOssPropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_properties_with_options_async(
        self,
        request: baas_20180731_models.GetOssPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetOssPropertiesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOssProperties',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetOssPropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_properties(
        self,
        request: baas_20180731_models.GetOssPropertiesRequest,
    ) -> baas_20180731_models.GetOssPropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oss_properties_with_options(request, runtime)

    async def get_oss_properties_async(
        self,
        request: baas_20180731_models.GetOssPropertiesRequest,
    ) -> baas_20180731_models.GetOssPropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_properties_with_options_async(request, runtime)

    def get_templates_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetTemplatesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetTemplates',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_templates_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.GetTemplatesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetTemplates',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.GetTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_templates(self) -> baas_20180731_models.GetTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_templates_with_options(runtime)

    async def get_templates_async(self) -> baas_20180731_models.GetTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_templates_with_options_async(runtime)

    def install_chaincode_with_options(
        self,
        request: baas_20180731_models.InstallChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.InstallChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstallChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.InstallChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_chaincode_with_options_async(
        self,
        request: baas_20180731_models.InstallChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.InstallChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstallChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.InstallChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_chaincode(
        self,
        request: baas_20180731_models.InstallChaincodeRequest,
    ) -> baas_20180731_models.InstallChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_chaincode_with_options(request, runtime)

    async def install_chaincode_async(
        self,
        request: baas_20180731_models.InstallChaincodeRequest,
    ) -> baas_20180731_models.InstallChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_chaincode_with_options_async(request, runtime)

    def install_fabric_chaincode_package_with_options(
        self,
        request: baas_20180731_models.InstallFabricChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.InstallFabricChaincodePackageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_package_id):
            body['ChaincodePackageId'] = request.chaincode_package_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstallFabricChaincodePackage',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.InstallFabricChaincodePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_fabric_chaincode_package_with_options_async(
        self,
        request: baas_20180731_models.InstallFabricChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.InstallFabricChaincodePackageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_package_id):
            body['ChaincodePackageId'] = request.chaincode_package_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstallFabricChaincodePackage',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.InstallFabricChaincodePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_fabric_chaincode_package(
        self,
        request: baas_20180731_models.InstallFabricChaincodePackageRequest,
    ) -> baas_20180731_models.InstallFabricChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_fabric_chaincode_package_with_options(request, runtime)

    async def install_fabric_chaincode_package_async(
        self,
        request: baas_20180731_models.InstallFabricChaincodePackageRequest,
    ) -> baas_20180731_models.InstallFabricChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_fabric_chaincode_package_with_options_async(request, runtime)

    def instantiate_chaincode_with_options(
        self,
        request: baas_20180731_models.InstantiateChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.InstantiateChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.collection_config):
            body['CollectionConfig'] = request.collection_config
        if not UtilClient.is_unset(request.endorse_policy):
            body['EndorsePolicy'] = request.endorse_policy
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstantiateChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.InstantiateChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def instantiate_chaincode_with_options_async(
        self,
        request: baas_20180731_models.InstantiateChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.InstantiateChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.collection_config):
            body['CollectionConfig'] = request.collection_config
        if not UtilClient.is_unset(request.endorse_policy):
            body['EndorsePolicy'] = request.endorse_policy
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InstantiateChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.InstantiateChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def instantiate_chaincode(
        self,
        request: baas_20180731_models.InstantiateChaincodeRequest,
    ) -> baas_20180731_models.InstantiateChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.instantiate_chaincode_with_options(request, runtime)

    async def instantiate_chaincode_async(
        self,
        request: baas_20180731_models.InstantiateChaincodeRequest,
    ) -> baas_20180731_models.InstantiateChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.instantiate_chaincode_with_options_async(request, runtime)

    def invite_user_with_options(
        self,
        request: baas_20180731_models.InviteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.InviteUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.user_email):
            body['UserEmail'] = request.user_email
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InviteUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.InviteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def invite_user_with_options_async(
        self,
        request: baas_20180731_models.InviteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.InviteUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.user_email):
            body['UserEmail'] = request.user_email
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InviteUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.InviteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invite_user(
        self,
        request: baas_20180731_models.InviteUserRequest,
    ) -> baas_20180731_models.InviteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.invite_user_with_options(request, runtime)

    async def invite_user_async(
        self,
        request: baas_20180731_models.InviteUserRequest,
    ) -> baas_20180731_models.InviteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invite_user_with_options_async(request, runtime)

    def join_channel_with_options(
        self,
        request: baas_20180731_models.JoinChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.JoinChannelResponse:
        """
        ***\
        
        @param request: JoinChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: JoinChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.do):
            query['Do'] = request.do
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='JoinChannel',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.JoinChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_channel_with_options_async(
        self,
        request: baas_20180731_models.JoinChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.JoinChannelResponse:
        """
        ***\
        
        @param request: JoinChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: JoinChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.do):
            query['Do'] = request.do
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='JoinChannel',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.JoinChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_channel(
        self,
        request: baas_20180731_models.JoinChannelRequest,
    ) -> baas_20180731_models.JoinChannelResponse:
        """
        ***\
        
        @param request: JoinChannelRequest
        @return: JoinChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.join_channel_with_options(request, runtime)

    async def join_channel_async(
        self,
        request: baas_20180731_models.JoinChannelRequest,
    ) -> baas_20180731_models.JoinChannelResponse:
        """
        ***\
        
        @param request: JoinChannelRequest
        @return: JoinChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.join_channel_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: baas_20180731_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: baas_20180731_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: baas_20180731_models.ListTagResourcesRequest,
    ) -> baas_20180731_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: baas_20180731_models.ListTagResourcesRequest,
    ) -> baas_20180731_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_trigger_with_options(
        self,
        request: baas_20180731_models.ModifyTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ModifyTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTrigger',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ModifyTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_trigger_with_options_async(
        self,
        request: baas_20180731_models.ModifyTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ModifyTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTrigger',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ModifyTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_trigger(
        self,
        request: baas_20180731_models.ModifyTriggerRequest,
    ) -> baas_20180731_models.ModifyTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_trigger_with_options(request, runtime)

    async def modify_trigger_async(
        self,
        request: baas_20180731_models.ModifyTriggerRequest,
    ) -> baas_20180731_models.ModifyTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_trigger_with_options_async(request, runtime)

    def operate_user_with_options(
        self,
        request: baas_20180731_models.OperateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.OperateUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.OperateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_user_with_options_async(
        self,
        request: baas_20180731_models.OperateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.OperateUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.OperateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_user(
        self,
        request: baas_20180731_models.OperateUserRequest,
    ) -> baas_20180731_models.OperateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_user_with_options(request, runtime)

    async def operate_user_async(
        self,
        request: baas_20180731_models.OperateUserRequest,
    ) -> baas_20180731_models.OperateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_user_with_options_async(request, runtime)

    def process_cloud_idecontract_transaction_with_options(
        self,
        request: baas_20180731_models.ProcessCloudIDEContractTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ProcessCloudIDEContractTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.transaction):
            body['Transaction'] = request.transaction
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ProcessCloudIDEContractTransaction',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ProcessCloudIDEContractTransactionResponse(),
            self.call_api(params, req, runtime)
        )

    async def process_cloud_idecontract_transaction_with_options_async(
        self,
        request: baas_20180731_models.ProcessCloudIDEContractTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ProcessCloudIDEContractTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.transaction):
            body['Transaction'] = request.transaction
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ProcessCloudIDEContractTransaction',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ProcessCloudIDEContractTransactionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def process_cloud_idecontract_transaction(
        self,
        request: baas_20180731_models.ProcessCloudIDEContractTransactionRequest,
    ) -> baas_20180731_models.ProcessCloudIDEContractTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return self.process_cloud_idecontract_transaction_with_options(request, runtime)

    async def process_cloud_idecontract_transaction_async(
        self,
        request: baas_20180731_models.ProcessCloudIDEContractTransactionRequest,
    ) -> baas_20180731_models.ProcessCloudIDEContractTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.process_cloud_idecontract_transaction_with_options_async(request, runtime)

    def process_public_cloud_idecontract_transaction_with_options(
        self,
        request: baas_20180731_models.ProcessPublicCloudIDEContractTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ProcessPublicCloudIDEContractTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.transaction):
            body['Transaction'] = request.transaction
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ProcessPublicCloudIDEContractTransaction',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ProcessPublicCloudIDEContractTransactionResponse(),
            self.call_api(params, req, runtime)
        )

    async def process_public_cloud_idecontract_transaction_with_options_async(
        self,
        request: baas_20180731_models.ProcessPublicCloudIDEContractTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ProcessPublicCloudIDEContractTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.transaction):
            body['Transaction'] = request.transaction
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ProcessPublicCloudIDEContractTransaction',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ProcessPublicCloudIDEContractTransactionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def process_public_cloud_idecontract_transaction(
        self,
        request: baas_20180731_models.ProcessPublicCloudIDEContractTransactionRequest,
    ) -> baas_20180731_models.ProcessPublicCloudIDEContractTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return self.process_public_cloud_idecontract_transaction_with_options(request, runtime)

    async def process_public_cloud_idecontract_transaction_async(
        self,
        request: baas_20180731_models.ProcessPublicCloudIDEContractTransactionRequest,
    ) -> baas_20180731_models.ProcessPublicCloudIDEContractTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.process_public_cloud_idecontract_transaction_with_options_async(request, runtime)

    def query_block_with_options(
        self,
        request: baas_20180731_models.QueryBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryBlockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryBlock',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_block_with_options_async(
        self,
        request: baas_20180731_models.QueryBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryBlockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryBlock',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_block(
        self,
        request: baas_20180731_models.QueryBlockRequest,
    ) -> baas_20180731_models.QueryBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_block_with_options(request, runtime)

    async def query_block_async(
        self,
        request: baas_20180731_models.QueryBlockRequest,
    ) -> baas_20180731_models.QueryBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_block_with_options_async(request, runtime)

    def query_consortium_deletable_with_options(
        self,
        request: baas_20180731_models.QueryConsortiumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryConsortiumDeletableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConsortiumDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryConsortiumDeletableResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_consortium_deletable_with_options_async(
        self,
        request: baas_20180731_models.QueryConsortiumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryConsortiumDeletableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConsortiumDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryConsortiumDeletableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_consortium_deletable(
        self,
        request: baas_20180731_models.QueryConsortiumDeletableRequest,
    ) -> baas_20180731_models.QueryConsortiumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_consortium_deletable_with_options(request, runtime)

    async def query_consortium_deletable_async(
        self,
        request: baas_20180731_models.QueryConsortiumDeletableRequest,
    ) -> baas_20180731_models.QueryConsortiumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_consortium_deletable_with_options_async(request, runtime)

    def query_ethereum_deletable_with_options(
        self,
        request: baas_20180731_models.QueryEthereumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryEthereumDeletableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEthereumDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryEthereumDeletableResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ethereum_deletable_with_options_async(
        self,
        request: baas_20180731_models.QueryEthereumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryEthereumDeletableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEthereumDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryEthereumDeletableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ethereum_deletable(
        self,
        request: baas_20180731_models.QueryEthereumDeletableRequest,
    ) -> baas_20180731_models.QueryEthereumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ethereum_deletable_with_options(request, runtime)

    async def query_ethereum_deletable_async(
        self,
        request: baas_20180731_models.QueryEthereumDeletableRequest,
    ) -> baas_20180731_models.QueryEthereumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ethereum_deletable_with_options_async(request, runtime)

    def query_metric_with_options(
        self,
        request: baas_20180731_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bizid):
            query['Bizid'] = request.bizid
        body = {}
        if not UtilClient.is_unset(request.inner_ip):
            body['InnerIp'] = request.inner_ip
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.time_area):
            body['TimeArea'] = request.time_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMetric',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_with_options_async(
        self,
        request: baas_20180731_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bizid):
            query['Bizid'] = request.bizid
        body = {}
        if not UtilClient.is_unset(request.inner_ip):
            body['InnerIp'] = request.inner_ip
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.time_area):
            body['TimeArea'] = request.time_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMetric',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric(
        self,
        request: baas_20180731_models.QueryMetricRequest,
    ) -> baas_20180731_models.QueryMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_metric_with_options(request, runtime)

    async def query_metric_async(
        self,
        request: baas_20180731_models.QueryMetricRequest,
    ) -> baas_20180731_models.QueryMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_with_options_async(request, runtime)

    def query_organization_deletable_with_options(
        self,
        request: baas_20180731_models.QueryOrganizationDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryOrganizationDeletableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrganizationDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryOrganizationDeletableResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_organization_deletable_with_options_async(
        self,
        request: baas_20180731_models.QueryOrganizationDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryOrganizationDeletableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrganizationDeletable',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryOrganizationDeletableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_organization_deletable(
        self,
        request: baas_20180731_models.QueryOrganizationDeletableRequest,
    ) -> baas_20180731_models.QueryOrganizationDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_organization_deletable_with_options(request, runtime)

    async def query_organization_deletable_async(
        self,
        request: baas_20180731_models.QueryOrganizationDeletableRequest,
    ) -> baas_20180731_models.QueryOrganizationDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_organization_deletable_with_options_async(request, runtime)

    def query_transaction_with_options(
        self,
        request: baas_20180731_models.QueryTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTransaction',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryTransactionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transaction_with_options_async(
        self,
        request: baas_20180731_models.QueryTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.QueryTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTransaction',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.QueryTransactionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transaction(
        self,
        request: baas_20180731_models.QueryTransactionRequest,
    ) -> baas_20180731_models.QueryTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_transaction_with_options(request, runtime)

    async def query_transaction_async(
        self,
        request: baas_20180731_models.QueryTransactionRequest,
    ) -> baas_20180731_models.QueryTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_transaction_with_options_async(request, runtime)

    def reject_user_with_options(
        self,
        request: baas_20180731_models.RejectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.RejectUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RejectUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.RejectUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_user_with_options_async(
        self,
        request: baas_20180731_models.RejectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.RejectUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RejectUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.RejectUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_user(
        self,
        request: baas_20180731_models.RejectUserRequest,
    ) -> baas_20180731_models.RejectUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.reject_user_with_options(request, runtime)

    async def reject_user_async(
        self,
        request: baas_20180731_models.RejectUserRequest,
    ) -> baas_20180731_models.RejectUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reject_user_with_options_async(request, runtime)

    def rename_blockchain_with_options(
        self,
        request: baas_20180731_models.RenameBlockchainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.RenameBlockchainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.new_name):
            body['NewName'] = request.new_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameBlockchain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.RenameBlockchainResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_blockchain_with_options_async(
        self,
        request: baas_20180731_models.RenameBlockchainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.RenameBlockchainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.new_name):
            body['NewName'] = request.new_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameBlockchain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.RenameBlockchainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_blockchain(
        self,
        request: baas_20180731_models.RenameBlockchainRequest,
    ) -> baas_20180731_models.RenameBlockchainResponse:
        runtime = util_models.RuntimeOptions()
        return self.rename_blockchain_with_options(request, runtime)

    async def rename_blockchain_async(
        self,
        request: baas_20180731_models.RenameBlockchainRequest,
    ) -> baas_20180731_models.RenameBlockchainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rename_blockchain_with_options_async(request, runtime)

    def reset_ant_chain_certificate_with_options(
        self,
        request: baas_20180731_models.ResetAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetAntChainCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetAntChainCertificate',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetAntChainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_ant_chain_certificate_with_options_async(
        self,
        request: baas_20180731_models.ResetAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetAntChainCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetAntChainCertificate',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetAntChainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_ant_chain_certificate(
        self,
        request: baas_20180731_models.ResetAntChainCertificateRequest,
    ) -> baas_20180731_models.ResetAntChainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_ant_chain_certificate_with_options(request, runtime)

    async def reset_ant_chain_certificate_async(
        self,
        request: baas_20180731_models.ResetAntChainCertificateRequest,
    ) -> baas_20180731_models.ResetAntChainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_ant_chain_certificate_with_options_async(request, runtime)

    def reset_ant_chain_user_certificate_with_options(
        self,
        request: baas_20180731_models.ResetAntChainUserCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetAntChainUserCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetAntChainUserCertificate',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetAntChainUserCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_ant_chain_user_certificate_with_options_async(
        self,
        request: baas_20180731_models.ResetAntChainUserCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetAntChainUserCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetAntChainUserCertificate',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetAntChainUserCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_ant_chain_user_certificate(
        self,
        request: baas_20180731_models.ResetAntChainUserCertificateRequest,
    ) -> baas_20180731_models.ResetAntChainUserCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_ant_chain_user_certificate_with_options(request, runtime)

    async def reset_ant_chain_user_certificate_async(
        self,
        request: baas_20180731_models.ResetAntChainUserCertificateRequest,
    ) -> baas_20180731_models.ResetAntChainUserCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_ant_chain_user_certificate_with_options_async(request, runtime)

    def reset_certificate_with_options(
        self,
        request: baas_20180731_models.ResetCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetCertificate',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_certificate_with_options_async(
        self,
        request: baas_20180731_models.ResetCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetCertificate',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_certificate(
        self,
        request: baas_20180731_models.ResetCertificateRequest,
    ) -> baas_20180731_models.ResetCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_certificate_with_options(request, runtime)

    async def reset_certificate_async(
        self,
        request: baas_20180731_models.ResetCertificateRequest,
    ) -> baas_20180731_models.ResetCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_certificate_with_options_async(request, runtime)

    def reset_organization_user_password_with_options(
        self,
        request: baas_20180731_models.ResetOrganizationUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetOrganizationUserPasswordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetOrganizationUserPassword',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetOrganizationUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_organization_user_password_with_options_async(
        self,
        request: baas_20180731_models.ResetOrganizationUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetOrganizationUserPasswordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetOrganizationUserPassword',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetOrganizationUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_organization_user_password(
        self,
        request: baas_20180731_models.ResetOrganizationUserPasswordRequest,
    ) -> baas_20180731_models.ResetOrganizationUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_organization_user_password_with_options(request, runtime)

    async def reset_organization_user_password_async(
        self,
        request: baas_20180731_models.ResetOrganizationUserPasswordRequest,
    ) -> baas_20180731_models.ResetOrganizationUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_organization_user_password_with_options_async(request, runtime)

    def reset_public_ant_chain_certificate_with_options(
        self,
        request: baas_20180731_models.ResetPublicAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetPublicAntChainCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetPublicAntChainCertificate',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetPublicAntChainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_public_ant_chain_certificate_with_options_async(
        self,
        request: baas_20180731_models.ResetPublicAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetPublicAntChainCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetPublicAntChainCertificate',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetPublicAntChainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_public_ant_chain_certificate(
        self,
        request: baas_20180731_models.ResetPublicAntChainCertificateRequest,
    ) -> baas_20180731_models.ResetPublicAntChainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_public_ant_chain_certificate_with_options(request, runtime)

    async def reset_public_ant_chain_certificate_async(
        self,
        request: baas_20180731_models.ResetPublicAntChainCertificateRequest,
    ) -> baas_20180731_models.ResetPublicAntChainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_public_ant_chain_certificate_with_options_async(request, runtime)

    def reset_user_with_options(
        self,
        request: baas_20180731_models.ResetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_with_options_async(
        self,
        request: baas_20180731_models.ResetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.ResetUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetUser',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.ResetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user(
        self,
        request: baas_20180731_models.ResetUserRequest,
    ) -> baas_20180731_models.ResetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_user_with_options(request, runtime)

    async def reset_user_async(
        self,
        request: baas_20180731_models.ResetUserRequest,
    ) -> baas_20180731_models.ResetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_user_with_options_async(request, runtime)

    def schema_detail_with_options(
        self,
        request: baas_20180731_models.SchemaDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.SchemaDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SchemaDetail',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.SchemaDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def schema_detail_with_options_async(
        self,
        request: baas_20180731_models.SchemaDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.SchemaDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SchemaDetail',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.SchemaDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def schema_detail(
        self,
        request: baas_20180731_models.SchemaDetailRequest,
    ) -> baas_20180731_models.SchemaDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.schema_detail_with_options(request, runtime)

    async def schema_detail_async(
        self,
        request: baas_20180731_models.SchemaDetailRequest,
    ) -> baas_20180731_models.SchemaDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.schema_detail_with_options_async(request, runtime)

    def start_smart_contract_job_with_options(
        self,
        request: baas_20180731_models.StartSmartContractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.StartSmartContractJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_name):
            body['JobName'] = request.job_name
        if not UtilClient.is_unset(request.source_opt):
            body['SourceOpt'] = request.source_opt
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSmartContractJob',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.StartSmartContractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_smart_contract_job_with_options_async(
        self,
        request: baas_20180731_models.StartSmartContractJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.StartSmartContractJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_name):
            body['JobName'] = request.job_name
        if not UtilClient.is_unset(request.source_opt):
            body['SourceOpt'] = request.source_opt
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSmartContractJob',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.StartSmartContractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_smart_contract_job(
        self,
        request: baas_20180731_models.StartSmartContractJobRequest,
    ) -> baas_20180731_models.StartSmartContractJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_smart_contract_job_with_options(request, runtime)

    async def start_smart_contract_job_async(
        self,
        request: baas_20180731_models.StartSmartContractJobRequest,
    ) -> baas_20180731_models.StartSmartContractJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_smart_contract_job_with_options_async(request, runtime)

    def submit_fabric_chaincode_definition_with_options(
        self,
        request: baas_20180731_models.SubmitFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.SubmitFabricChaincodeDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_package_id):
            body['ChaincodePackageId'] = request.chaincode_package_id
        if not UtilClient.is_unset(request.chaincode_version):
            body['ChaincodeVersion'] = request.chaincode_version
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.collection_config):
            body['CollectionConfig'] = request.collection_config
        if not UtilClient.is_unset(request.endorse_policy):
            body['EndorsePolicy'] = request.endorse_policy
        if not UtilClient.is_unset(request.init_required):
            body['InitRequired'] = request.init_required
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitFabricChaincodeDefinition',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.SubmitFabricChaincodeDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fabric_chaincode_definition_with_options_async(
        self,
        request: baas_20180731_models.SubmitFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.SubmitFabricChaincodeDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_package_id):
            body['ChaincodePackageId'] = request.chaincode_package_id
        if not UtilClient.is_unset(request.chaincode_version):
            body['ChaincodeVersion'] = request.chaincode_version
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.collection_config):
            body['CollectionConfig'] = request.collection_config
        if not UtilClient.is_unset(request.endorse_policy):
            body['EndorsePolicy'] = request.endorse_policy
        if not UtilClient.is_unset(request.init_required):
            body['InitRequired'] = request.init_required
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitFabricChaincodeDefinition',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.SubmitFabricChaincodeDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_fabric_chaincode_definition(
        self,
        request: baas_20180731_models.SubmitFabricChaincodeDefinitionRequest,
    ) -> baas_20180731_models.SubmitFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_fabric_chaincode_definition_with_options(request, runtime)

    async def submit_fabric_chaincode_definition_async(
        self,
        request: baas_20180731_models.SubmitFabricChaincodeDefinitionRequest,
    ) -> baas_20180731_models.SubmitFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_fabric_chaincode_definition_with_options_async(request, runtime)

    def sync_fabric_chaincode_status_with_options(
        self,
        request: baas_20180731_models.SyncFabricChaincodeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.SyncFabricChaincodeStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncFabricChaincodeStatus',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.SyncFabricChaincodeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_fabric_chaincode_status_with_options_async(
        self,
        request: baas_20180731_models.SyncFabricChaincodeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.SyncFabricChaincodeStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncFabricChaincodeStatus',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.SyncFabricChaincodeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_fabric_chaincode_status(
        self,
        request: baas_20180731_models.SyncFabricChaincodeStatusRequest,
    ) -> baas_20180731_models.SyncFabricChaincodeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_fabric_chaincode_status_with_options(request, runtime)

    async def sync_fabric_chaincode_status_async(
        self,
        request: baas_20180731_models.SyncFabricChaincodeStatusRequest,
    ) -> baas_20180731_models.SyncFabricChaincodeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_fabric_chaincode_status_with_options_async(request, runtime)

    def synchronize_chaincode_with_options(
        self,
        request: baas_20180731_models.SynchronizeChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.SynchronizeChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SynchronizeChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.SynchronizeChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def synchronize_chaincode_with_options_async(
        self,
        request: baas_20180731_models.SynchronizeChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.SynchronizeChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SynchronizeChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.SynchronizeChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def synchronize_chaincode(
        self,
        request: baas_20180731_models.SynchronizeChaincodeRequest,
    ) -> baas_20180731_models.SynchronizeChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.synchronize_chaincode_with_options(request, runtime)

    async def synchronize_chaincode_async(
        self,
        request: baas_20180731_models.SynchronizeChaincodeRequest,
    ) -> baas_20180731_models.SynchronizeChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.synchronize_chaincode_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: baas_20180731_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
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
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: baas_20180731_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
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
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: baas_20180731_models.TagResourcesRequest,
    ) -> baas_20180731_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: baas_20180731_models.TagResourcesRequest,
    ) -> baas_20180731_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unfreeze_account_with_options(
        self,
        request: baas_20180731_models.UnfreezeAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UnfreezeAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnfreezeAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UnfreezeAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def unfreeze_account_with_options_async(
        self,
        request: baas_20180731_models.UnfreezeAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UnfreezeAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnfreezeAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UnfreezeAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unfreeze_account(
        self,
        request: baas_20180731_models.UnfreezeAccountRequest,
    ) -> baas_20180731_models.UnfreezeAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.unfreeze_account_with_options(request, runtime)

    async def unfreeze_account_async(
        self,
        request: baas_20180731_models.UnfreezeAccountRequest,
    ) -> baas_20180731_models.UnfreezeAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unfreeze_account_with_options_async(request, runtime)

    def unfreeze_ant_chain_account_with_options(
        self,
        request: baas_20180731_models.UnfreezeAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UnfreezeAntChainAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnfreezeAntChainAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UnfreezeAntChainAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def unfreeze_ant_chain_account_with_options_async(
        self,
        request: baas_20180731_models.UnfreezeAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UnfreezeAntChainAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnfreezeAntChainAccount',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UnfreezeAntChainAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unfreeze_ant_chain_account(
        self,
        request: baas_20180731_models.UnfreezeAntChainAccountRequest,
    ) -> baas_20180731_models.UnfreezeAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.unfreeze_ant_chain_account_with_options(request, runtime)

    async def unfreeze_ant_chain_account_async(
        self,
        request: baas_20180731_models.UnfreezeAntChainAccountRequest,
    ) -> baas_20180731_models.UnfreezeAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unfreeze_ant_chain_account_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: baas_20180731_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
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
            action='UntagResources',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: baas_20180731_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
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
            action='UntagResources',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: baas_20180731_models.UntagResourcesRequest,
    ) -> baas_20180731_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: baas_20180731_models.UntagResourcesRequest,
    ) -> baas_20180731_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_ant_chain_with_options(
        self,
        request: baas_20180731_models.UpdateAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.ant_chain_name):
            body['AntChainName'] = request.ant_chain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_with_options_async(
        self,
        request: baas_20180731_models.UpdateAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.ant_chain_name):
            body['AntChainName'] = request.ant_chain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChain',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ant_chain(
        self,
        request: baas_20180731_models.UpdateAntChainRequest,
    ) -> baas_20180731_models.UpdateAntChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_with_options(request, runtime)

    async def update_ant_chain_async(
        self,
        request: baas_20180731_models.UpdateAntChainRequest,
    ) -> baas_20180731_models.UpdateAntChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_with_options_async(request, runtime)

    def update_ant_chain_consortium_with_options(
        self,
        request: baas_20180731_models.UpdateAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_description):
            body['ConsortiumDescription'] = request.consortium_description
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.consortium_name):
            body['ConsortiumName'] = request.consortium_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChainConsortium',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainConsortiumResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_consortium_with_options_async(
        self,
        request: baas_20180731_models.UpdateAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_description):
            body['ConsortiumDescription'] = request.consortium_description
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.consortium_name):
            body['ConsortiumName'] = request.consortium_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChainConsortium',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainConsortiumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ant_chain_consortium(
        self,
        request: baas_20180731_models.UpdateAntChainConsortiumRequest,
    ) -> baas_20180731_models.UpdateAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_consortium_with_options(request, runtime)

    async def update_ant_chain_consortium_async(
        self,
        request: baas_20180731_models.UpdateAntChainConsortiumRequest,
    ) -> baas_20180731_models.UpdateAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_consortium_with_options_async(request, runtime)

    def update_ant_chain_contract_content_with_options(
        self,
        request: baas_20180731_models.UpdateAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainContractContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_id):
            body['ContentId'] = request.content_id
        if not UtilClient.is_unset(request.content_name):
            body['ContentName'] = request.content_name
        if not UtilClient.is_unset(request.parent_content_id):
            body['ParentContentId'] = request.parent_content_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChainContractContent',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainContractContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_contract_content_with_options_async(
        self,
        request: baas_20180731_models.UpdateAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainContractContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_id):
            body['ContentId'] = request.content_id
        if not UtilClient.is_unset(request.content_name):
            body['ContentName'] = request.content_name
        if not UtilClient.is_unset(request.parent_content_id):
            body['ParentContentId'] = request.parent_content_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChainContractContent',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainContractContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ant_chain_contract_content(
        self,
        request: baas_20180731_models.UpdateAntChainContractContentRequest,
    ) -> baas_20180731_models.UpdateAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_contract_content_with_options(request, runtime)

    async def update_ant_chain_contract_content_async(
        self,
        request: baas_20180731_models.UpdateAntChainContractContentRequest,
    ) -> baas_20180731_models.UpdateAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_contract_content_with_options_async(request, runtime)

    def update_ant_chain_contract_project_with_options(
        self,
        request: baas_20180731_models.UpdateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_description):
            body['ProjectDescription'] = request.project_description
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_version):
            body['ProjectVersion'] = request.project_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChainContractProject',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainContractProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20180731_models.UpdateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_description):
            body['ProjectDescription'] = request.project_description
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_version):
            body['ProjectVersion'] = request.project_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChainContractProject',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainContractProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ant_chain_contract_project(
        self,
        request: baas_20180731_models.UpdateAntChainContractProjectRequest,
    ) -> baas_20180731_models.UpdateAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_contract_project_with_options(request, runtime)

    async def update_ant_chain_contract_project_async(
        self,
        request: baas_20180731_models.UpdateAntChainContractProjectRequest,
    ) -> baas_20180731_models.UpdateAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_contract_project_with_options_async(request, runtime)

    def update_ant_chain_member_with_options(
        self,
        request: baas_20180731_models.UpdateAntChainMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.member_id):
            body['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.member_name):
            body['MemberName'] = request.member_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChainMember',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_member_with_options_async(
        self,
        request: baas_20180731_models.UpdateAntChainMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.member_id):
            body['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.member_name):
            body['MemberName'] = request.member_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChainMember',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ant_chain_member(
        self,
        request: baas_20180731_models.UpdateAntChainMemberRequest,
    ) -> baas_20180731_models.UpdateAntChainMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_member_with_options(request, runtime)

    async def update_ant_chain_member_async(
        self,
        request: baas_20180731_models.UpdateAntChainMemberRequest,
    ) -> baas_20180731_models.UpdateAntChainMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_member_with_options_async(request, runtime)

    def update_ant_chain_qrcode_authorization_with_options(
        self,
        request: baas_20180731_models.UpdateAntChainQRCodeAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainQRCodeAuthorizationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.authorization_type):
            body['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChainQRCodeAuthorization',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainQRCodeAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_qrcode_authorization_with_options_async(
        self,
        request: baas_20180731_models.UpdateAntChainQRCodeAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateAntChainQRCodeAuthorizationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.authorization_type):
            body['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.qrcode_type):
            body['QRCodeType'] = request.qrcode_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAntChainQRCodeAuthorization',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateAntChainQRCodeAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ant_chain_qrcode_authorization(
        self,
        request: baas_20180731_models.UpdateAntChainQRCodeAuthorizationRequest,
    ) -> baas_20180731_models.UpdateAntChainQRCodeAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_qrcode_authorization_with_options(request, runtime)

    async def update_ant_chain_qrcode_authorization_async(
        self,
        request: baas_20180731_models.UpdateAntChainQRCodeAuthorizationRequest,
    ) -> baas_20180731_models.UpdateAntChainQRCodeAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_qrcode_authorization_with_options_async(request, runtime)

    def update_blockchain_schema_with_options(
        self,
        request: baas_20180731_models.UpdateBlockchainSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateBlockchainSchemaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.category_configs):
            body['CategoryConfigs'] = request.category_configs
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.schema_name):
            body['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBlockchainSchema',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateBlockchainSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_blockchain_schema_with_options_async(
        self,
        request: baas_20180731_models.UpdateBlockchainSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateBlockchainSchemaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.category_configs):
            body['CategoryConfigs'] = request.category_configs
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.schema_name):
            body['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBlockchainSchema',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateBlockchainSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_blockchain_schema(
        self,
        request: baas_20180731_models.UpdateBlockchainSchemaRequest,
    ) -> baas_20180731_models.UpdateBlockchainSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_blockchain_schema_with_options(request, runtime)

    async def update_blockchain_schema_async(
        self,
        request: baas_20180731_models.UpdateBlockchainSchemaRequest,
    ) -> baas_20180731_models.UpdateBlockchainSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_blockchain_schema_with_options_async(request, runtime)

    def update_channel_config_with_options(
        self,
        request: baas_20180731_models.UpdateChannelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateChannelConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_timeout):
            body['BatchTimeout'] = request.batch_timeout
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.max_message_count):
            body['MaxMessageCount'] = request.max_message_count
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.preferred_max_bytes):
            body['PreferredMaxBytes'] = request.preferred_max_bytes
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateChannelConfig',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateChannelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_channel_config_with_options_async(
        self,
        request: baas_20180731_models.UpdateChannelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateChannelConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_timeout):
            body['BatchTimeout'] = request.batch_timeout
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.max_message_count):
            body['MaxMessageCount'] = request.max_message_count
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.preferred_max_bytes):
            body['PreferredMaxBytes'] = request.preferred_max_bytes
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateChannelConfig',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateChannelConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_channel_config(
        self,
        request: baas_20180731_models.UpdateChannelConfigRequest,
    ) -> baas_20180731_models.UpdateChannelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_channel_config_with_options(request, runtime)

    async def update_channel_config_async(
        self,
        request: baas_20180731_models.UpdateChannelConfigRequest,
    ) -> baas_20180731_models.UpdateChannelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_channel_config_with_options_async(request, runtime)

    def update_ethereum_with_options(
        self,
        request: baas_20180731_models.UpdateEthereumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateEthereumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEthereum',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateEthereumResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ethereum_with_options_async(
        self,
        request: baas_20180731_models.UpdateEthereumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateEthereumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEthereum',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateEthereumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ethereum(
        self,
        request: baas_20180731_models.UpdateEthereumRequest,
    ) -> baas_20180731_models.UpdateEthereumResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ethereum_with_options(request, runtime)

    async def update_ethereum_async(
        self,
        request: baas_20180731_models.UpdateEthereumRequest,
    ) -> baas_20180731_models.UpdateEthereumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ethereum_with_options_async(request, runtime)

    def update_ethereum_client_user_password_with_options(
        self,
        request: baas_20180731_models.UpdateEthereumClientUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateEthereumClientUserPasswordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEthereumClientUserPassword',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateEthereumClientUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ethereum_client_user_password_with_options_async(
        self,
        request: baas_20180731_models.UpdateEthereumClientUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateEthereumClientUserPasswordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEthereumClientUserPassword',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateEthereumClientUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ethereum_client_user_password(
        self,
        request: baas_20180731_models.UpdateEthereumClientUserPasswordRequest,
    ) -> baas_20180731_models.UpdateEthereumClientUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ethereum_client_user_password_with_options(request, runtime)

    async def update_ethereum_client_user_password_async(
        self,
        request: baas_20180731_models.UpdateEthereumClientUserPasswordRequest,
    ) -> baas_20180731_models.UpdateEthereumClientUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ethereum_client_user_password_with_options_async(request, runtime)

    def update_ethereum_node_with_options(
        self,
        request: baas_20180731_models.UpdateEthereumNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateEthereumNodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEthereumNode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateEthereumNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ethereum_node_with_options_async(
        self,
        request: baas_20180731_models.UpdateEthereumNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateEthereumNodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEthereumNode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateEthereumNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ethereum_node(
        self,
        request: baas_20180731_models.UpdateEthereumNodeRequest,
    ) -> baas_20180731_models.UpdateEthereumNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ethereum_node_with_options(request, runtime)

    async def update_ethereum_node_async(
        self,
        request: baas_20180731_models.UpdateEthereumNodeRequest,
    ) -> baas_20180731_models.UpdateEthereumNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ethereum_node_with_options_async(request, runtime)

    def update_ethereum_node_configuration_with_options(
        self,
        request: baas_20180731_models.UpdateEthereumNodeConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateEthereumNodeConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip):
            body['IP'] = request.ip
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_pub):
            body['NodePub'] = request.node_pub
        if not UtilClient.is_unset(request.p_2p_port):
            body['P2pPort'] = request.p_2p_port
        if not UtilClient.is_unset(request.raft_port):
            body['RaftPort'] = request.raft_port
        if not UtilClient.is_unset(request.rpc_port):
            body['RpcPort'] = request.rpc_port
        if not UtilClient.is_unset(request.tmport):
            body['TMPort'] = request.tmport
        if not UtilClient.is_unset(request.tmpub):
            body['TMPub'] = request.tmpub
        if not UtilClient.is_unset(request.wsport):
            body['WSPort'] = request.wsport
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEthereumNodeConfiguration',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateEthereumNodeConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ethereum_node_configuration_with_options_async(
        self,
        request: baas_20180731_models.UpdateEthereumNodeConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateEthereumNodeConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip):
            body['IP'] = request.ip
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_pub):
            body['NodePub'] = request.node_pub
        if not UtilClient.is_unset(request.p_2p_port):
            body['P2pPort'] = request.p_2p_port
        if not UtilClient.is_unset(request.raft_port):
            body['RaftPort'] = request.raft_port
        if not UtilClient.is_unset(request.rpc_port):
            body['RpcPort'] = request.rpc_port
        if not UtilClient.is_unset(request.tmport):
            body['TMPort'] = request.tmport
        if not UtilClient.is_unset(request.tmpub):
            body['TMPub'] = request.tmpub
        if not UtilClient.is_unset(request.wsport):
            body['WSPort'] = request.wsport
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEthereumNodeConfiguration',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateEthereumNodeConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ethereum_node_configuration(
        self,
        request: baas_20180731_models.UpdateEthereumNodeConfigurationRequest,
    ) -> baas_20180731_models.UpdateEthereumNodeConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ethereum_node_configuration_with_options(request, runtime)

    async def update_ethereum_node_configuration_async(
        self,
        request: baas_20180731_models.UpdateEthereumNodeConfigurationRequest,
    ) -> baas_20180731_models.UpdateEthereumNodeConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ethereum_node_configuration_with_options_async(request, runtime)

    def update_governance_task_with_options(
        self,
        request: baas_20180731_models.UpdateGovernanceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateGovernanceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.task_action):
            body['TaskAction'] = request.task_action
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGovernanceTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateGovernanceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_governance_task_with_options_async(
        self,
        request: baas_20180731_models.UpdateGovernanceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateGovernanceTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.task_action):
            body['TaskAction'] = request.task_action
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGovernanceTask',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateGovernanceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_governance_task(
        self,
        request: baas_20180731_models.UpdateGovernanceTaskRequest,
    ) -> baas_20180731_models.UpdateGovernanceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_governance_task_with_options(request, runtime)

    async def update_governance_task_async(
        self,
        request: baas_20180731_models.UpdateGovernanceTaskRequest,
    ) -> baas_20180731_models.UpdateGovernanceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_governance_task_with_options_async(request, runtime)

    def update_member_role_with_options(
        self,
        request: baas_20180731_models.UpdateMemberRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateMemberRoleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMemberRole',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateMemberRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_member_role_with_options_async(
        self,
        request: baas_20180731_models.UpdateMemberRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateMemberRoleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMemberRole',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateMemberRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_member_role(
        self,
        request: baas_20180731_models.UpdateMemberRoleRequest,
    ) -> baas_20180731_models.UpdateMemberRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_member_role_with_options(request, runtime)

    async def update_member_role_async(
        self,
        request: baas_20180731_models.UpdateMemberRoleRequest,
    ) -> baas_20180731_models.UpdateMemberRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_member_role_with_options_async(request, runtime)

    def update_qrcode_authority_with_options(
        self,
        request: baas_20180731_models.UpdateQRCodeAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateQRCodeAuthorityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorized):
            body['Authorized'] = request.authorized
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQRCodeAuthority',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateQRCodeAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_qrcode_authority_with_options_async(
        self,
        request: baas_20180731_models.UpdateQRCodeAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateQRCodeAuthorityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorized):
            body['Authorized'] = request.authorized
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQRCodeAuthority',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateQRCodeAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_qrcode_authority(
        self,
        request: baas_20180731_models.UpdateQRCodeAuthorityRequest,
    ) -> baas_20180731_models.UpdateQRCodeAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_qrcode_authority_with_options(request, runtime)

    async def update_qrcode_authority_async(
        self,
        request: baas_20180731_models.UpdateQRCodeAuthorityRequest,
    ) -> baas_20180731_models.UpdateQRCodeAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_qrcode_authority_with_options_async(request, runtime)

    def update_schema_with_options(
        self,
        request: baas_20180731_models.UpdateSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateSchemaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.category_configs):
            body['CategoryConfigs'] = request.category_configs
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.schema_name):
            body['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSchema',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_schema_with_options_async(
        self,
        request: baas_20180731_models.UpdateSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpdateSchemaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bizid):
            body['Bizid'] = request.bizid
        if not UtilClient.is_unset(request.category_configs):
            body['CategoryConfigs'] = request.category_configs
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.schema_id):
            body['SchemaId'] = request.schema_id
        if not UtilClient.is_unset(request.schema_name):
            body['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSchema',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpdateSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_schema(
        self,
        request: baas_20180731_models.UpdateSchemaRequest,
    ) -> baas_20180731_models.UpdateSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_schema_with_options(request, runtime)

    async def update_schema_async(
        self,
        request: baas_20180731_models.UpdateSchemaRequest,
    ) -> baas_20180731_models.UpdateSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_schema_with_options_async(request, runtime)

    def upgrade_chaincode_with_options(
        self,
        request: baas_20180731_models.UpgradeChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpgradeChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.collection_config):
            body['CollectionConfig'] = request.collection_config
        if not UtilClient.is_unset(request.endorse_policy):
            body['EndorsePolicy'] = request.endorse_policy
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpgradeChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_chaincode_with_options_async(
        self,
        request: baas_20180731_models.UpgradeChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpgradeChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.collection_config):
            body['CollectionConfig'] = request.collection_config
        if not UtilClient.is_unset(request.endorse_policy):
            body['EndorsePolicy'] = request.endorse_policy
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeChaincode',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpgradeChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_chaincode(
        self,
        request: baas_20180731_models.UpgradeChaincodeRequest,
    ) -> baas_20180731_models.UpgradeChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_chaincode_with_options(request, runtime)

    async def upgrade_chaincode_async(
        self,
        request: baas_20180731_models.UpgradeChaincodeRequest,
    ) -> baas_20180731_models.UpgradeChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_chaincode_with_options_async(request, runtime)

    def upgrade_fabric_chaincode_definition_with_options(
        self,
        request: baas_20180731_models.UpgradeFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpgradeFabricChaincodeDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.chaincode_package_id):
            body['ChaincodePackageId'] = request.chaincode_package_id
        if not UtilClient.is_unset(request.chaincode_version):
            body['ChaincodeVersion'] = request.chaincode_version
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.collection_config):
            body['CollectionConfig'] = request.collection_config
        if not UtilClient.is_unset(request.endorse_policy):
            body['EndorsePolicy'] = request.endorse_policy
        if not UtilClient.is_unset(request.init_required):
            body['InitRequired'] = request.init_required
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeFabricChaincodeDefinition',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpgradeFabricChaincodeDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_fabric_chaincode_definition_with_options_async(
        self,
        request: baas_20180731_models.UpgradeFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20180731_models.UpgradeFabricChaincodeDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.chaincode_package_id):
            body['ChaincodePackageId'] = request.chaincode_package_id
        if not UtilClient.is_unset(request.chaincode_version):
            body['ChaincodeVersion'] = request.chaincode_version
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.collection_config):
            body['CollectionConfig'] = request.collection_config
        if not UtilClient.is_unset(request.endorse_policy):
            body['EndorsePolicy'] = request.endorse_policy
        if not UtilClient.is_unset(request.init_required):
            body['InitRequired'] = request.init_required
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeFabricChaincodeDefinition',
            version='2018-07-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20180731_models.UpgradeFabricChaincodeDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_fabric_chaincode_definition(
        self,
        request: baas_20180731_models.UpgradeFabricChaincodeDefinitionRequest,
    ) -> baas_20180731_models.UpgradeFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_fabric_chaincode_definition_with_options(request, runtime)

    async def upgrade_fabric_chaincode_definition_async(
        self,
        request: baas_20180731_models.UpgradeFabricChaincodeDefinitionRequest,
    ) -> baas_20180731_models.UpgradeFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_fabric_chaincode_definition_with_options_async(request, runtime)
