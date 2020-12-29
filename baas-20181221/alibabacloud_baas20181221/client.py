# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_baas20181221 import models as baas_20181221_models
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

    def accept_fabric_invitation_with_options(
        self,
        request: baas_20181221_models.AcceptFabricInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.AcceptFabricInvitationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.AcceptFabricInvitationResponse().from_map(
            self.do_rpcrequest('AcceptFabricInvitation', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def accept_fabric_invitation_with_options_async(
        self,
        request: baas_20181221_models.AcceptFabricInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.AcceptFabricInvitationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.AcceptFabricInvitationResponse().from_map(
            await self.do_rpcrequest_async('AcceptFabricInvitation', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def accept_fabric_invitation(
        self,
        request: baas_20181221_models.AcceptFabricInvitationRequest,
    ) -> baas_20181221_models.AcceptFabricInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_fabric_invitation_with_options(request, runtime)

    async def accept_fabric_invitation_async(
        self,
        request: baas_20181221_models.AcceptFabricInvitationRequest,
    ) -> baas_20181221_models.AcceptFabricInvitationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_fabric_invitation_with_options_async(request, runtime)

    def apply_ant_chain_certificate_with_options(
        self,
        request: baas_20181221_models.ApplyAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ApplyAntChainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ApplyAntChainCertificateResponse().from_map(
            self.do_rpcrequest('ApplyAntChainCertificate', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_ant_chain_certificate_with_options_async(
        self,
        request: baas_20181221_models.ApplyAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ApplyAntChainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ApplyAntChainCertificateResponse().from_map(
            await self.do_rpcrequest_async('ApplyAntChainCertificate', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_ant_chain_certificate(
        self,
        request: baas_20181221_models.ApplyAntChainCertificateRequest,
    ) -> baas_20181221_models.ApplyAntChainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_ant_chain_certificate_with_options(request, runtime)

    async def apply_ant_chain_certificate_async(
        self,
        request: baas_20181221_models.ApplyAntChainCertificateRequest,
    ) -> baas_20181221_models.ApplyAntChainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_ant_chain_certificate_with_options_async(request, runtime)

    def apply_ant_chain_certificate_with_key_auto_creation_with_options(
        self,
        request: baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationResponse().from_map(
            self.do_rpcrequest('ApplyAntChainCertificateWithKeyAutoCreation', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_ant_chain_certificate_with_key_auto_creation_with_options_async(
        self,
        request: baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationResponse().from_map(
            await self.do_rpcrequest_async('ApplyAntChainCertificateWithKeyAutoCreation', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_ant_chain_certificate_with_key_auto_creation(
        self,
        request: baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationRequest,
    ) -> baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_ant_chain_certificate_with_key_auto_creation_with_options(request, runtime)

    async def apply_ant_chain_certificate_with_key_auto_creation_async(
        self,
        request: baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationRequest,
    ) -> baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_ant_chain_certificate_with_key_auto_creation_with_options_async(request, runtime)

    def batch_add_ant_chain_mini_app_qrcode_authorized_users_with_options(
        self,
        tmp_req: baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_list):
            request.phone_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_list, 'PhoneList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse().from_map(
            self.do_rpcrequest('BatchAddAntChainMiniAppQRCodeAuthorizedUsers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_add_ant_chain_mini_app_qrcode_authorized_users_with_options_async(
        self,
        tmp_req: baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_list):
            request.phone_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_list, 'PhoneList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse().from_map(
            await self.do_rpcrequest_async('BatchAddAntChainMiniAppQRCodeAuthorizedUsers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_add_ant_chain_mini_app_qrcode_authorized_users(
        self,
        request: baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersRequest,
    ) -> baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_add_ant_chain_mini_app_qrcode_authorized_users_with_options(request, runtime)

    async def batch_add_ant_chain_mini_app_qrcode_authorized_users_async(
        self,
        request: baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersRequest,
    ) -> baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_ant_chain_mini_app_qrcode_authorized_users_with_options_async(request, runtime)

    def check_fabric_consortium_domain_with_options(
        self,
        request: baas_20181221_models.CheckFabricConsortiumDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CheckFabricConsortiumDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CheckFabricConsortiumDomainResponse().from_map(
            self.do_rpcrequest('CheckFabricConsortiumDomain', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_fabric_consortium_domain_with_options_async(
        self,
        request: baas_20181221_models.CheckFabricConsortiumDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CheckFabricConsortiumDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CheckFabricConsortiumDomainResponse().from_map(
            await self.do_rpcrequest_async('CheckFabricConsortiumDomain', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_fabric_consortium_domain(
        self,
        request: baas_20181221_models.CheckFabricConsortiumDomainRequest,
    ) -> baas_20181221_models.CheckFabricConsortiumDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_fabric_consortium_domain_with_options(request, runtime)

    async def check_fabric_consortium_domain_async(
        self,
        request: baas_20181221_models.CheckFabricConsortiumDomainRequest,
    ) -> baas_20181221_models.CheckFabricConsortiumDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_fabric_consortium_domain_with_options_async(request, runtime)

    def check_fabric_organization_domain_with_options(
        self,
        request: baas_20181221_models.CheckFabricOrganizationDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CheckFabricOrganizationDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CheckFabricOrganizationDomainResponse().from_map(
            self.do_rpcrequest('CheckFabricOrganizationDomain', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_fabric_organization_domain_with_options_async(
        self,
        request: baas_20181221_models.CheckFabricOrganizationDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CheckFabricOrganizationDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CheckFabricOrganizationDomainResponse().from_map(
            await self.do_rpcrequest_async('CheckFabricOrganizationDomain', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_fabric_organization_domain(
        self,
        request: baas_20181221_models.CheckFabricOrganizationDomainRequest,
    ) -> baas_20181221_models.CheckFabricOrganizationDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_fabric_organization_domain_with_options(request, runtime)

    async def check_fabric_organization_domain_async(
        self,
        request: baas_20181221_models.CheckFabricOrganizationDomainRequest,
    ) -> baas_20181221_models.CheckFabricOrganizationDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_fabric_organization_domain_with_options_async(request, runtime)

    def confirm_fabric_consortium_member_with_options(
        self,
        request: baas_20181221_models.ConfirmFabricConsortiumMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ConfirmFabricConsortiumMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ConfirmFabricConsortiumMemberResponse().from_map(
            self.do_rpcrequest('ConfirmFabricConsortiumMember', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def confirm_fabric_consortium_member_with_options_async(
        self,
        request: baas_20181221_models.ConfirmFabricConsortiumMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ConfirmFabricConsortiumMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ConfirmFabricConsortiumMemberResponse().from_map(
            await self.do_rpcrequest_async('ConfirmFabricConsortiumMember', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def confirm_fabric_consortium_member(
        self,
        request: baas_20181221_models.ConfirmFabricConsortiumMemberRequest,
    ) -> baas_20181221_models.ConfirmFabricConsortiumMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_fabric_consortium_member_with_options(request, runtime)

    async def confirm_fabric_consortium_member_async(
        self,
        request: baas_20181221_models.ConfirmFabricConsortiumMemberRequest,
    ) -> baas_20181221_models.ConfirmFabricConsortiumMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_fabric_consortium_member_with_options_async(request, runtime)

    def copy_ant_chain_contract_project_with_options(
        self,
        request: baas_20181221_models.CopyAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CopyAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CopyAntChainContractProjectResponse().from_map(
            self.do_rpcrequest('CopyAntChainContractProject', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def copy_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20181221_models.CopyAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CopyAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CopyAntChainContractProjectResponse().from_map(
            await self.do_rpcrequest_async('CopyAntChainContractProject', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_ant_chain_contract_project(
        self,
        request: baas_20181221_models.CopyAntChainContractProjectRequest,
    ) -> baas_20181221_models.CopyAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_ant_chain_contract_project_with_options(request, runtime)

    async def copy_ant_chain_contract_project_async(
        self,
        request: baas_20181221_models.CopyAntChainContractProjectRequest,
    ) -> baas_20181221_models.CopyAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_ant_chain_contract_project_with_options_async(request, runtime)

    def create_ant_chain_account_with_options(
        self,
        request: baas_20181221_models.CreateAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateAntChainAccountResponse().from_map(
            self.do_rpcrequest('CreateAntChainAccount', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ant_chain_account_with_options_async(
        self,
        request: baas_20181221_models.CreateAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateAntChainAccountResponse().from_map(
            await self.do_rpcrequest_async('CreateAntChainAccount', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ant_chain_account(
        self,
        request: baas_20181221_models.CreateAntChainAccountRequest,
    ) -> baas_20181221_models.CreateAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ant_chain_account_with_options(request, runtime)

    async def create_ant_chain_account_async(
        self,
        request: baas_20181221_models.CreateAntChainAccountRequest,
    ) -> baas_20181221_models.CreateAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ant_chain_account_with_options_async(request, runtime)

    def create_ant_chain_account_with_key_pair_auto_creation_with_options(
        self,
        request: baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationResponse().from_map(
            self.do_rpcrequest('CreateAntChainAccountWithKeyPairAutoCreation', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ant_chain_account_with_key_pair_auto_creation_with_options_async(
        self,
        request: baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationResponse().from_map(
            await self.do_rpcrequest_async('CreateAntChainAccountWithKeyPairAutoCreation', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ant_chain_account_with_key_pair_auto_creation(
        self,
        request: baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationRequest,
    ) -> baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ant_chain_account_with_key_pair_auto_creation_with_options(request, runtime)

    async def create_ant_chain_account_with_key_pair_auto_creation_async(
        self,
        request: baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationRequest,
    ) -> baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ant_chain_account_with_key_pair_auto_creation_with_options_async(request, runtime)

    def create_ant_chain_consortium_with_options(
        self,
        request: baas_20181221_models.CreateAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateAntChainConsortiumResponse().from_map(
            self.do_rpcrequest('CreateAntChainConsortium', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ant_chain_consortium_with_options_async(
        self,
        request: baas_20181221_models.CreateAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateAntChainConsortiumResponse().from_map(
            await self.do_rpcrequest_async('CreateAntChainConsortium', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ant_chain_consortium(
        self,
        request: baas_20181221_models.CreateAntChainConsortiumRequest,
    ) -> baas_20181221_models.CreateAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ant_chain_consortium_with_options(request, runtime)

    async def create_ant_chain_consortium_async(
        self,
        request: baas_20181221_models.CreateAntChainConsortiumRequest,
    ) -> baas_20181221_models.CreateAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ant_chain_consortium_with_options_async(request, runtime)

    def create_ant_chain_contract_content_with_options(
        self,
        request: baas_20181221_models.CreateAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainContractContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateAntChainContractContentResponse().from_map(
            self.do_rpcrequest('CreateAntChainContractContent', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ant_chain_contract_content_with_options_async(
        self,
        request: baas_20181221_models.CreateAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainContractContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateAntChainContractContentResponse().from_map(
            await self.do_rpcrequest_async('CreateAntChainContractContent', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ant_chain_contract_content(
        self,
        request: baas_20181221_models.CreateAntChainContractContentRequest,
    ) -> baas_20181221_models.CreateAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ant_chain_contract_content_with_options(request, runtime)

    async def create_ant_chain_contract_content_async(
        self,
        request: baas_20181221_models.CreateAntChainContractContentRequest,
    ) -> baas_20181221_models.CreateAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ant_chain_contract_content_with_options_async(request, runtime)

    def create_ant_chain_contract_project_with_options(
        self,
        request: baas_20181221_models.CreateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateAntChainContractProjectResponse().from_map(
            self.do_rpcrequest('CreateAntChainContractProject', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20181221_models.CreateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateAntChainContractProjectResponse().from_map(
            await self.do_rpcrequest_async('CreateAntChainContractProject', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ant_chain_contract_project(
        self,
        request: baas_20181221_models.CreateAntChainContractProjectRequest,
    ) -> baas_20181221_models.CreateAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ant_chain_contract_project_with_options(request, runtime)

    async def create_ant_chain_contract_project_async(
        self,
        request: baas_20181221_models.CreateAntChainContractProjectRequest,
    ) -> baas_20181221_models.CreateAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ant_chain_contract_project_with_options_async(request, runtime)

    def create_fabric_chaincode_with_options(
        self,
        request: baas_20181221_models.CreateFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricChaincodeResponse().from_map(
            self.do_rpcrequest('CreateFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricChaincodeResponse().from_map(
            await self.do_rpcrequest_async('CreateFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_fabric_chaincode(
        self,
        request: baas_20181221_models.CreateFabricChaincodeRequest,
    ) -> baas_20181221_models.CreateFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fabric_chaincode_with_options(request, runtime)

    async def create_fabric_chaincode_async(
        self,
        request: baas_20181221_models.CreateFabricChaincodeRequest,
    ) -> baas_20181221_models.CreateFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fabric_chaincode_with_options_async(request, runtime)

    def create_fabric_channel_with_options(
        self,
        request: baas_20181221_models.CreateFabricChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricChannelResponse().from_map(
            self.do_rpcrequest('CreateFabricChannel', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_fabric_channel_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricChannelResponse().from_map(
            await self.do_rpcrequest_async('CreateFabricChannel', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_fabric_channel(
        self,
        request: baas_20181221_models.CreateFabricChannelRequest,
    ) -> baas_20181221_models.CreateFabricChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fabric_channel_with_options(request, runtime)

    async def create_fabric_channel_async(
        self,
        request: baas_20181221_models.CreateFabricChannelRequest,
    ) -> baas_20181221_models.CreateFabricChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fabric_channel_with_options_async(request, runtime)

    def create_fabric_channel_member_with_options(
        self,
        request: baas_20181221_models.CreateFabricChannelMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChannelMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricChannelMemberResponse().from_map(
            self.do_rpcrequest('CreateFabricChannelMember', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_fabric_channel_member_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricChannelMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChannelMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricChannelMemberResponse().from_map(
            await self.do_rpcrequest_async('CreateFabricChannelMember', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_fabric_channel_member(
        self,
        request: baas_20181221_models.CreateFabricChannelMemberRequest,
    ) -> baas_20181221_models.CreateFabricChannelMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fabric_channel_member_with_options(request, runtime)

    async def create_fabric_channel_member_async(
        self,
        request: baas_20181221_models.CreateFabricChannelMemberRequest,
    ) -> baas_20181221_models.CreateFabricChannelMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fabric_channel_member_with_options_async(request, runtime)

    def create_fabric_consortium_with_options(
        self,
        request: baas_20181221_models.CreateFabricConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricConsortiumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricConsortiumResponse().from_map(
            self.do_rpcrequest('CreateFabricConsortium', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_fabric_consortium_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricConsortiumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricConsortiumResponse().from_map(
            await self.do_rpcrequest_async('CreateFabricConsortium', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_fabric_consortium(
        self,
        request: baas_20181221_models.CreateFabricConsortiumRequest,
    ) -> baas_20181221_models.CreateFabricConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fabric_consortium_with_options(request, runtime)

    async def create_fabric_consortium_async(
        self,
        request: baas_20181221_models.CreateFabricConsortiumRequest,
    ) -> baas_20181221_models.CreateFabricConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fabric_consortium_with_options_async(request, runtime)

    def create_fabric_consortium_member_with_options(
        self,
        request: baas_20181221_models.CreateFabricConsortiumMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricConsortiumMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricConsortiumMemberResponse().from_map(
            self.do_rpcrequest('CreateFabricConsortiumMember', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_fabric_consortium_member_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricConsortiumMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricConsortiumMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricConsortiumMemberResponse().from_map(
            await self.do_rpcrequest_async('CreateFabricConsortiumMember', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_fabric_consortium_member(
        self,
        request: baas_20181221_models.CreateFabricConsortiumMemberRequest,
    ) -> baas_20181221_models.CreateFabricConsortiumMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fabric_consortium_member_with_options(request, runtime)

    async def create_fabric_consortium_member_async(
        self,
        request: baas_20181221_models.CreateFabricConsortiumMemberRequest,
    ) -> baas_20181221_models.CreateFabricConsortiumMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fabric_consortium_member_with_options_async(request, runtime)

    def create_fabric_organization_with_options(
        self,
        request: baas_20181221_models.CreateFabricOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricOrganizationResponse().from_map(
            self.do_rpcrequest('CreateFabricOrganization', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_fabric_organization_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricOrganizationResponse().from_map(
            await self.do_rpcrequest_async('CreateFabricOrganization', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_fabric_organization(
        self,
        request: baas_20181221_models.CreateFabricOrganizationRequest,
    ) -> baas_20181221_models.CreateFabricOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fabric_organization_with_options(request, runtime)

    async def create_fabric_organization_async(
        self,
        request: baas_20181221_models.CreateFabricOrganizationRequest,
    ) -> baas_20181221_models.CreateFabricOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fabric_organization_with_options_async(request, runtime)

    def create_fabric_organization_user_with_options(
        self,
        request: baas_20181221_models.CreateFabricOrganizationUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricOrganizationUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricOrganizationUserResponse().from_map(
            self.do_rpcrequest('CreateFabricOrganizationUser', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_fabric_organization_user_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricOrganizationUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricOrganizationUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.CreateFabricOrganizationUserResponse().from_map(
            await self.do_rpcrequest_async('CreateFabricOrganizationUser', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_fabric_organization_user(
        self,
        request: baas_20181221_models.CreateFabricOrganizationUserRequest,
    ) -> baas_20181221_models.CreateFabricOrganizationUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fabric_organization_user_with_options(request, runtime)

    async def create_fabric_organization_user_async(
        self,
        request: baas_20181221_models.CreateFabricOrganizationUserRequest,
    ) -> baas_20181221_models.CreateFabricOrganizationUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fabric_organization_user_with_options_async(request, runtime)

    def delete_ant_chain_consortium_with_options(
        self,
        request: baas_20181221_models.DeleteAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DeleteAntChainConsortiumResponse().from_map(
            self.do_rpcrequest('DeleteAntChainConsortium', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ant_chain_consortium_with_options_async(
        self,
        request: baas_20181221_models.DeleteAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DeleteAntChainConsortiumResponse().from_map(
            await self.do_rpcrequest_async('DeleteAntChainConsortium', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ant_chain_consortium(
        self,
        request: baas_20181221_models.DeleteAntChainConsortiumRequest,
    ) -> baas_20181221_models.DeleteAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ant_chain_consortium_with_options(request, runtime)

    async def delete_ant_chain_consortium_async(
        self,
        request: baas_20181221_models.DeleteAntChainConsortiumRequest,
    ) -> baas_20181221_models.DeleteAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ant_chain_consortium_with_options_async(request, runtime)

    def delete_ant_chain_contract_content_with_options(
        self,
        request: baas_20181221_models.DeleteAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainContractContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DeleteAntChainContractContentResponse().from_map(
            self.do_rpcrequest('DeleteAntChainContractContent', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ant_chain_contract_content_with_options_async(
        self,
        request: baas_20181221_models.DeleteAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainContractContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DeleteAntChainContractContentResponse().from_map(
            await self.do_rpcrequest_async('DeleteAntChainContractContent', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ant_chain_contract_content(
        self,
        request: baas_20181221_models.DeleteAntChainContractContentRequest,
    ) -> baas_20181221_models.DeleteAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ant_chain_contract_content_with_options(request, runtime)

    async def delete_ant_chain_contract_content_async(
        self,
        request: baas_20181221_models.DeleteAntChainContractContentRequest,
    ) -> baas_20181221_models.DeleteAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ant_chain_contract_content_with_options_async(request, runtime)

    def delete_ant_chain_contract_project_with_options(
        self,
        request: baas_20181221_models.DeleteAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DeleteAntChainContractProjectResponse().from_map(
            self.do_rpcrequest('DeleteAntChainContractProject', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20181221_models.DeleteAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DeleteAntChainContractProjectResponse().from_map(
            await self.do_rpcrequest_async('DeleteAntChainContractProject', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ant_chain_contract_project(
        self,
        request: baas_20181221_models.DeleteAntChainContractProjectRequest,
    ) -> baas_20181221_models.DeleteAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ant_chain_contract_project_with_options(request, runtime)

    async def delete_ant_chain_contract_project_async(
        self,
        request: baas_20181221_models.DeleteAntChainContractProjectRequest,
    ) -> baas_20181221_models.DeleteAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ant_chain_contract_project_with_options_async(request, runtime)

    def delete_ant_chain_mini_app_qrcode_authorized_user_with_options(
        self,
        request: baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse().from_map(
            self.do_rpcrequest('DeleteAntChainMiniAppQRCodeAuthorizedUser', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ant_chain_mini_app_qrcode_authorized_user_with_options_async(
        self,
        request: baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse().from_map(
            await self.do_rpcrequest_async('DeleteAntChainMiniAppQRCodeAuthorizedUser', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ant_chain_mini_app_qrcode_authorized_user(
        self,
        request: baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserRequest,
    ) -> baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ant_chain_mini_app_qrcode_authorized_user_with_options(request, runtime)

    async def delete_ant_chain_mini_app_qrcode_authorized_user_async(
        self,
        request: baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserRequest,
    ) -> baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ant_chain_mini_app_qrcode_authorized_user_with_options_async(request, runtime)

    def delete_fabric_chaincode_with_options(
        self,
        request: baas_20181221_models.DeleteFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DeleteFabricChaincodeResponse().from_map(
            self.do_rpcrequest('DeleteFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.DeleteFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DeleteFabricChaincodeResponse().from_map(
            await self.do_rpcrequest_async('DeleteFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_fabric_chaincode(
        self,
        request: baas_20181221_models.DeleteFabricChaincodeRequest,
    ) -> baas_20181221_models.DeleteFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_fabric_chaincode_with_options(request, runtime)

    async def delete_fabric_chaincode_async(
        self,
        request: baas_20181221_models.DeleteFabricChaincodeRequest,
    ) -> baas_20181221_models.DeleteFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_fabric_chaincode_with_options_async(request, runtime)

    def describe_ant_chain_accounts_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainAccountsResponse().from_map(
            self.do_rpcrequest('DescribeAntChainAccounts', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_accounts_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainAccountsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainAccounts', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_accounts(
        self,
        request: baas_20181221_models.DescribeAntChainAccountsRequest,
    ) -> baas_20181221_models.DescribeAntChainAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_accounts_with_options(request, runtime)

    async def describe_ant_chain_accounts_async(
        self,
        request: baas_20181221_models.DescribeAntChainAccountsRequest,
    ) -> baas_20181221_models.DescribeAntChainAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_accounts_with_options_async(request, runtime)

    def describe_ant_chain_block_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainBlockResponse().from_map(
            self.do_rpcrequest('DescribeAntChainBlock', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_block_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainBlockResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainBlock', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_block(
        self,
        request: baas_20181221_models.DescribeAntChainBlockRequest,
    ) -> baas_20181221_models.DescribeAntChainBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_block_with_options(request, runtime)

    async def describe_ant_chain_block_async(
        self,
        request: baas_20181221_models.DescribeAntChainBlockRequest,
    ) -> baas_20181221_models.DescribeAntChainBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_block_with_options_async(request, runtime)

    def describe_ant_chain_certificate_applications_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainCertificateApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainCertificateApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainCertificateApplicationsResponse().from_map(
            self.do_rpcrequest('DescribeAntChainCertificateApplications', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_certificate_applications_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainCertificateApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainCertificateApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainCertificateApplicationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainCertificateApplications', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_certificate_applications(
        self,
        request: baas_20181221_models.DescribeAntChainCertificateApplicationsRequest,
    ) -> baas_20181221_models.DescribeAntChainCertificateApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_certificate_applications_with_options(request, runtime)

    async def describe_ant_chain_certificate_applications_async(
        self,
        request: baas_20181221_models.DescribeAntChainCertificateApplicationsRequest,
    ) -> baas_20181221_models.DescribeAntChainCertificateApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_certificate_applications_with_options_async(request, runtime)

    def describe_ant_chain_consortiums_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainConsortiumsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainConsortiumsResponse().from_map(
            self.do_rpcrequest('DescribeAntChainConsortiums', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_consortiums_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainConsortiumsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainConsortiumsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainConsortiums', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_consortiums(
        self,
        request: baas_20181221_models.DescribeAntChainConsortiumsRequest,
    ) -> baas_20181221_models.DescribeAntChainConsortiumsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_consortiums_with_options(request, runtime)

    async def describe_ant_chain_consortiums_async(
        self,
        request: baas_20181221_models.DescribeAntChainConsortiumsRequest,
    ) -> baas_20181221_models.DescribeAntChainConsortiumsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_consortiums_with_options_async(request, runtime)

    def describe_ant_chain_contract_project_content_tree_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectContentTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectContentTreeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainContractProjectContentTreeResponse().from_map(
            self.do_rpcrequest('DescribeAntChainContractProjectContentTree', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_contract_project_content_tree_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectContentTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectContentTreeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainContractProjectContentTreeResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainContractProjectContentTree', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_contract_project_content_tree(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectContentTreeRequest,
    ) -> baas_20181221_models.DescribeAntChainContractProjectContentTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_contract_project_content_tree_with_options(request, runtime)

    async def describe_ant_chain_contract_project_content_tree_async(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectContentTreeRequest,
    ) -> baas_20181221_models.DescribeAntChainContractProjectContentTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_contract_project_content_tree_with_options_async(request, runtime)

    def describe_ant_chain_contract_projects_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainContractProjectsResponse().from_map(
            self.do_rpcrequest('DescribeAntChainContractProjects', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_contract_projects_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainContractProjectsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainContractProjects', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_contract_projects(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectsRequest,
    ) -> baas_20181221_models.DescribeAntChainContractProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_contract_projects_with_options(request, runtime)

    async def describe_ant_chain_contract_projects_async(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectsRequest,
    ) -> baas_20181221_models.DescribeAntChainContractProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_contract_projects_with_options_async(request, runtime)

    def describe_ant_chain_download_paths_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainDownloadPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainDownloadPathsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainDownloadPathsResponse().from_map(
            self.do_rpcrequest('DescribeAntChainDownloadPaths', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_download_paths_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainDownloadPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainDownloadPathsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainDownloadPathsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainDownloadPaths', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_download_paths(
        self,
        request: baas_20181221_models.DescribeAntChainDownloadPathsRequest,
    ) -> baas_20181221_models.DescribeAntChainDownloadPathsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_download_paths_with_options(request, runtime)

    async def describe_ant_chain_download_paths_async(
        self,
        request: baas_20181221_models.DescribeAntChainDownloadPathsRequest,
    ) -> baas_20181221_models.DescribeAntChainDownloadPathsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_download_paths_with_options_async(request, runtime)

    def describe_ant_chain_information_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainInformationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainInformationResponse().from_map(
            self.do_rpcrequest('DescribeAntChainInformation', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_information_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainInformationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainInformationResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainInformation', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_information(
        self,
        request: baas_20181221_models.DescribeAntChainInformationRequest,
    ) -> baas_20181221_models.DescribeAntChainInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_information_with_options(request, runtime)

    async def describe_ant_chain_information_async(
        self,
        request: baas_20181221_models.DescribeAntChainInformationRequest,
    ) -> baas_20181221_models.DescribeAntChainInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_information_with_options_async(request, runtime)

    def describe_ant_chain_latest_blocks_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainLatestBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestBlocksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainLatestBlocksResponse().from_map(
            self.do_rpcrequest('DescribeAntChainLatestBlocks', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_latest_blocks_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainLatestBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestBlocksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainLatestBlocksResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainLatestBlocks', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_latest_blocks(
        self,
        request: baas_20181221_models.DescribeAntChainLatestBlocksRequest,
    ) -> baas_20181221_models.DescribeAntChainLatestBlocksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_latest_blocks_with_options(request, runtime)

    async def describe_ant_chain_latest_blocks_async(
        self,
        request: baas_20181221_models.DescribeAntChainLatestBlocksRequest,
    ) -> baas_20181221_models.DescribeAntChainLatestBlocksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_latest_blocks_with_options_async(request, runtime)

    def describe_ant_chain_latest_transaction_digests_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainLatestTransactionDigestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestTransactionDigestsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainLatestTransactionDigestsResponse().from_map(
            self.do_rpcrequest('DescribeAntChainLatestTransactionDigests', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_latest_transaction_digests_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainLatestTransactionDigestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestTransactionDigestsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainLatestTransactionDigestsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainLatestTransactionDigests', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_latest_transaction_digests(
        self,
        request: baas_20181221_models.DescribeAntChainLatestTransactionDigestsRequest,
    ) -> baas_20181221_models.DescribeAntChainLatestTransactionDigestsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_latest_transaction_digests_with_options(request, runtime)

    async def describe_ant_chain_latest_transaction_digests_async(
        self,
        request: baas_20181221_models.DescribeAntChainLatestTransactionDigestsRequest,
    ) -> baas_20181221_models.DescribeAntChainLatestTransactionDigestsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_latest_transaction_digests_with_options_async(request, runtime)

    def describe_ant_chain_members_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainMembersResponse().from_map(
            self.do_rpcrequest('DescribeAntChainMembers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_members_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainMembersResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainMembers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_members(
        self,
        request: baas_20181221_models.DescribeAntChainMembersRequest,
    ) -> baas_20181221_models.DescribeAntChainMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_members_with_options(request, runtime)

    async def describe_ant_chain_members_async(
        self,
        request: baas_20181221_models.DescribeAntChainMembersRequest,
    ) -> baas_20181221_models.DescribeAntChainMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_members_with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_qrcode_access_log_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse().from_map(
            self.do_rpcrequest('DescribeAntChainMiniAppBrowserQRCodeAccessLog', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_qrcode_access_log_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainMiniAppBrowserQRCodeAccessLog', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_mini_app_browser_qrcode_access_log(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_qrcode_access_log_with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_qrcode_access_log_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_qrcode_access_log_with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_qrcode_authorized_users_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse().from_map(
            self.do_rpcrequest('DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_qrcode_authorized_users_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_mini_app_browser_qrcode_authorized_users(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_qrcode_authorized_users_with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_qrcode_authorized_users_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_qrcode_authorized_users_with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_transaction_qrcode_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse().from_map(
            self.do_rpcrequest('DescribeAntChainMiniAppBrowserTransactionQRCode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_transaction_qrcode_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainMiniAppBrowserTransactionQRCode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_mini_app_browser_transaction_qrcode(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeRequest,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_transaction_qrcode_with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_transaction_qrcode_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeRequest,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_transaction_qrcode_with_options_async(request, runtime)

    def describe_ant_chain_nodes_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainNodesResponse().from_map(
            self.do_rpcrequest('DescribeAntChainNodes', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_nodes_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainNodesResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainNodes', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_nodes(
        self,
        request: baas_20181221_models.DescribeAntChainNodesRequest,
    ) -> baas_20181221_models.DescribeAntChainNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_nodes_with_options(request, runtime)

    async def describe_ant_chain_nodes_async(
        self,
        request: baas_20181221_models.DescribeAntChainNodesRequest,
    ) -> baas_20181221_models.DescribeAntChainNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_nodes_with_options_async(request, runtime)

    def describe_ant_chain_qrcode_authorization_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainQRCodeAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainQRCodeAuthorizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainQRCodeAuthorizationResponse().from_map(
            self.do_rpcrequest('DescribeAntChainQRCodeAuthorization', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_qrcode_authorization_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainQRCodeAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainQRCodeAuthorizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainQRCodeAuthorizationResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainQRCodeAuthorization', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_qrcode_authorization(
        self,
        request: baas_20181221_models.DescribeAntChainQRCodeAuthorizationRequest,
    ) -> baas_20181221_models.DescribeAntChainQRCodeAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_qrcode_authorization_with_options(request, runtime)

    async def describe_ant_chain_qrcode_authorization_async(
        self,
        request: baas_20181221_models.DescribeAntChainQRCodeAuthorizationRequest,
    ) -> baas_20181221_models.DescribeAntChainQRCodeAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_qrcode_authorization_with_options_async(request, runtime)

    def describe_ant_chains_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainsResponse().from_map(
            self.do_rpcrequest('DescribeAntChains', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chains_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChains', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chains(
        self,
        request: baas_20181221_models.DescribeAntChainsRequest,
    ) -> baas_20181221_models.DescribeAntChainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chains_with_options(request, runtime)

    async def describe_ant_chains_async(
        self,
        request: baas_20181221_models.DescribeAntChainsRequest,
    ) -> baas_20181221_models.DescribeAntChainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chains_with_options_async(request, runtime)

    def describe_ant_chain_transaction_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainTransactionResponse().from_map(
            self.do_rpcrequest('DescribeAntChainTransaction', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_transaction_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainTransactionResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainTransaction', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_transaction(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionRequest,
    ) -> baas_20181221_models.DescribeAntChainTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_transaction_with_options(request, runtime)

    async def describe_ant_chain_transaction_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionRequest,
    ) -> baas_20181221_models.DescribeAntChainTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_transaction_with_options_async(request, runtime)

    def describe_ant_chain_transaction_receipt_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionReceiptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionReceiptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainTransactionReceiptResponse().from_map(
            self.do_rpcrequest('DescribeAntChainTransactionReceipt', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_transaction_receipt_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionReceiptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionReceiptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainTransactionReceiptResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainTransactionReceipt', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_transaction_receipt(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionReceiptRequest,
    ) -> baas_20181221_models.DescribeAntChainTransactionReceiptResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_transaction_receipt_with_options(request, runtime)

    async def describe_ant_chain_transaction_receipt_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionReceiptRequest,
    ) -> baas_20181221_models.DescribeAntChainTransactionReceiptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_transaction_receipt_with_options_async(request, runtime)

    def describe_ant_chain_transaction_statistics_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainTransactionStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeAntChainTransactionStatistics', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ant_chain_transaction_statistics_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeAntChainTransactionStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAntChainTransactionStatistics', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ant_chain_transaction_statistics(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionStatisticsRequest,
    ) -> baas_20181221_models.DescribeAntChainTransactionStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_transaction_statistics_with_options(request, runtime)

    async def describe_ant_chain_transaction_statistics_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionStatisticsRequest,
    ) -> baas_20181221_models.DescribeAntChainTransactionStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_transaction_statistics_with_options_async(request, runtime)

    def describe_ethereum_deletable_with_options(
        self,
        request: baas_20181221_models.DescribeEthereumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeEthereumDeletableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeEthereumDeletableResponse().from_map(
            self.do_rpcrequest('DescribeEthereumDeletable', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ethereum_deletable_with_options_async(
        self,
        request: baas_20181221_models.DescribeEthereumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeEthereumDeletableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeEthereumDeletableResponse().from_map(
            await self.do_rpcrequest_async('DescribeEthereumDeletable', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ethereum_deletable(
        self,
        request: baas_20181221_models.DescribeEthereumDeletableRequest,
    ) -> baas_20181221_models.DescribeEthereumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ethereum_deletable_with_options(request, runtime)

    async def describe_ethereum_deletable_async(
        self,
        request: baas_20181221_models.DescribeEthereumDeletableRequest,
    ) -> baas_20181221_models.DescribeEthereumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ethereum_deletable_with_options_async(request, runtime)

    def describe_fabric_candidate_organizations_with_options(
        self,
        request: baas_20181221_models.DescribeFabricCandidateOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricCandidateOrganizationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricCandidateOrganizationsResponse().from_map(
            self.do_rpcrequest('DescribeFabricCandidateOrganizations', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_candidate_organizations_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricCandidateOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricCandidateOrganizationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricCandidateOrganizationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricCandidateOrganizations', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_candidate_organizations(
        self,
        request: baas_20181221_models.DescribeFabricCandidateOrganizationsRequest,
    ) -> baas_20181221_models.DescribeFabricCandidateOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_candidate_organizations_with_options(request, runtime)

    async def describe_fabric_candidate_organizations_async(
        self,
        request: baas_20181221_models.DescribeFabricCandidateOrganizationsRequest,
    ) -> baas_20181221_models.DescribeFabricCandidateOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_candidate_organizations_with_options_async(request, runtime)

    def describe_fabric_chaincode_upload_policy_with_options(
        self,
        request: baas_20181221_models.DescribeFabricChaincodeUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricChaincodeUploadPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricChaincodeUploadPolicyResponse().from_map(
            self.do_rpcrequest('DescribeFabricChaincodeUploadPolicy', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_chaincode_upload_policy_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricChaincodeUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricChaincodeUploadPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricChaincodeUploadPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricChaincodeUploadPolicy', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_chaincode_upload_policy(
        self,
        request: baas_20181221_models.DescribeFabricChaincodeUploadPolicyRequest,
    ) -> baas_20181221_models.DescribeFabricChaincodeUploadPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_chaincode_upload_policy_with_options(request, runtime)

    async def describe_fabric_chaincode_upload_policy_async(
        self,
        request: baas_20181221_models.DescribeFabricChaincodeUploadPolicyRequest,
    ) -> baas_20181221_models.DescribeFabricChaincodeUploadPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_chaincode_upload_policy_with_options_async(request, runtime)

    def describe_fabric_channel_members_with_options(
        self,
        request: baas_20181221_models.DescribeFabricChannelMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricChannelMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricChannelMembersResponse().from_map(
            self.do_rpcrequest('DescribeFabricChannelMembers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_channel_members_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricChannelMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricChannelMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricChannelMembersResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricChannelMembers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_channel_members(
        self,
        request: baas_20181221_models.DescribeFabricChannelMembersRequest,
    ) -> baas_20181221_models.DescribeFabricChannelMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_channel_members_with_options(request, runtime)

    async def describe_fabric_channel_members_async(
        self,
        request: baas_20181221_models.DescribeFabricChannelMembersRequest,
    ) -> baas_20181221_models.DescribeFabricChannelMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_channel_members_with_options_async(request, runtime)

    def describe_fabric_consortium_admin_status_with_options(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumAdminStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumAdminStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumAdminStatusResponse().from_map(
            self.do_rpcrequest('DescribeFabricConsortiumAdminStatus', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_consortium_admin_status_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumAdminStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumAdminStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumAdminStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricConsortiumAdminStatus', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_consortium_admin_status(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumAdminStatusRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumAdminStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_consortium_admin_status_with_options(request, runtime)

    async def describe_fabric_consortium_admin_status_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumAdminStatusRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumAdminStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_consortium_admin_status_with_options_async(request, runtime)

    def describe_fabric_consortium_chaincodes_with_options(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumChaincodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumChaincodesResponse().from_map(
            self.do_rpcrequest('DescribeFabricConsortiumChaincodes', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_consortium_chaincodes_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumChaincodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumChaincodesResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricConsortiumChaincodes', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_consortium_chaincodes(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumChaincodesRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_consortium_chaincodes_with_options(request, runtime)

    async def describe_fabric_consortium_chaincodes_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumChaincodesRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_consortium_chaincodes_with_options_async(request, runtime)

    def describe_fabric_consortium_channels_with_options(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumChannelsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumChannelsResponse().from_map(
            self.do_rpcrequest('DescribeFabricConsortiumChannels', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_consortium_channels_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumChannelsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumChannelsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricConsortiumChannels', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_consortium_channels(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumChannelsRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_consortium_channels_with_options(request, runtime)

    async def describe_fabric_consortium_channels_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumChannelsRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_consortium_channels_with_options_async(request, runtime)

    def describe_fabric_consortium_config_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumConfigResponse:
        req = open_api_models.OpenApiRequest()
        return baas_20181221_models.DescribeFabricConsortiumConfigResponse().from_map(
            self.do_rpcrequest('DescribeFabricConsortiumConfig', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_consortium_config_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumConfigResponse:
        req = open_api_models.OpenApiRequest()
        return baas_20181221_models.DescribeFabricConsortiumConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricConsortiumConfig', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_consortium_config(self) -> baas_20181221_models.DescribeFabricConsortiumConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_consortium_config_with_options(runtime)

    async def describe_fabric_consortium_config_async(self) -> baas_20181221_models.DescribeFabricConsortiumConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_consortium_config_with_options_async(runtime)

    def describe_fabric_consortium_deletable_with_options(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumDeletableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumDeletableResponse().from_map(
            self.do_rpcrequest('DescribeFabricConsortiumDeletable', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_consortium_deletable_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumDeletableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumDeletableResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricConsortiumDeletable', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_consortium_deletable(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumDeletableRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_consortium_deletable_with_options(request, runtime)

    async def describe_fabric_consortium_deletable_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumDeletableRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_consortium_deletable_with_options_async(request, runtime)

    def describe_fabric_consortium_member_approval_with_options(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumMemberApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumMemberApprovalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumMemberApprovalResponse().from_map(
            self.do_rpcrequest('DescribeFabricConsortiumMemberApproval', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_consortium_member_approval_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumMemberApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumMemberApprovalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumMemberApprovalResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricConsortiumMemberApproval', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_consortium_member_approval(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumMemberApprovalRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumMemberApprovalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_consortium_member_approval_with_options(request, runtime)

    async def describe_fabric_consortium_member_approval_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumMemberApprovalRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumMemberApprovalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_consortium_member_approval_with_options_async(request, runtime)

    def describe_fabric_consortium_members_with_options(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumMembersResponse().from_map(
            self.do_rpcrequest('DescribeFabricConsortiumMembers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_consortium_members_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumMembersResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricConsortiumMembers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_consortium_members(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumMembersRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_consortium_members_with_options(request, runtime)

    async def describe_fabric_consortium_members_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumMembersRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_consortium_members_with_options_async(request, runtime)

    def describe_fabric_consortium_orderers_with_options(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumOrderersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumOrderersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumOrderersResponse().from_map(
            self.do_rpcrequest('DescribeFabricConsortiumOrderers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_consortium_orderers_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumOrderersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumOrderersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumOrderersResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricConsortiumOrderers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_consortium_orderers(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumOrderersRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumOrderersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_consortium_orderers_with_options(request, runtime)

    async def describe_fabric_consortium_orderers_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumOrderersRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumOrderersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_consortium_orderers_with_options_async(request, runtime)

    def describe_fabric_consortiums_with_options(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumsResponse().from_map(
            self.do_rpcrequest('DescribeFabricConsortiums', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_consortiums_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricConsortiumsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricConsortiums', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_consortiums(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumsRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_consortiums_with_options(request, runtime)

    async def describe_fabric_consortiums_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumsRequest,
    ) -> baas_20181221_models.DescribeFabricConsortiumsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_consortiums_with_options_async(request, runtime)

    def describe_fabric_consortium_specs_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumSpecsResponse:
        req = open_api_models.OpenApiRequest()
        return baas_20181221_models.DescribeFabricConsortiumSpecsResponse().from_map(
            self.do_rpcrequest('DescribeFabricConsortiumSpecs', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_consortium_specs_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumSpecsResponse:
        req = open_api_models.OpenApiRequest()
        return baas_20181221_models.DescribeFabricConsortiumSpecsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricConsortiumSpecs', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_consortium_specs(self) -> baas_20181221_models.DescribeFabricConsortiumSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_consortium_specs_with_options(runtime)

    async def describe_fabric_consortium_specs_async(self) -> baas_20181221_models.DescribeFabricConsortiumSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_consortium_specs_with_options_async(runtime)

    def describe_fabric_explorer_with_options(
        self,
        request: baas_20181221_models.DescribeFabricExplorerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricExplorerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricExplorerResponse().from_map(
            self.do_rpcrequest('DescribeFabricExplorer', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_explorer_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricExplorerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricExplorerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricExplorerResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricExplorer', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_explorer(
        self,
        request: baas_20181221_models.DescribeFabricExplorerRequest,
    ) -> baas_20181221_models.DescribeFabricExplorerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_explorer_with_options(request, runtime)

    async def describe_fabric_explorer_async(
        self,
        request: baas_20181221_models.DescribeFabricExplorerRequest,
    ) -> baas_20181221_models.DescribeFabricExplorerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_explorer_with_options_async(request, runtime)

    def describe_fabric_invitation_code_with_options(
        self,
        request: baas_20181221_models.DescribeFabricInvitationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricInvitationCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricInvitationCodeResponse().from_map(
            self.do_rpcrequest('DescribeFabricInvitationCode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_invitation_code_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricInvitationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricInvitationCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricInvitationCodeResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricInvitationCode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_invitation_code(
        self,
        request: baas_20181221_models.DescribeFabricInvitationCodeRequest,
    ) -> baas_20181221_models.DescribeFabricInvitationCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_invitation_code_with_options(request, runtime)

    async def describe_fabric_invitation_code_async(
        self,
        request: baas_20181221_models.DescribeFabricInvitationCodeRequest,
    ) -> baas_20181221_models.DescribeFabricInvitationCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_invitation_code_with_options_async(request, runtime)

    def describe_fabric_inviter_with_options(
        self,
        request: baas_20181221_models.DescribeFabricInviterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricInviterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricInviterResponse().from_map(
            self.do_rpcrequest('DescribeFabricInviter', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_inviter_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricInviterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricInviterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricInviterResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricInviter', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_inviter(
        self,
        request: baas_20181221_models.DescribeFabricInviterRequest,
    ) -> baas_20181221_models.DescribeFabricInviterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_inviter_with_options(request, runtime)

    async def describe_fabric_inviter_async(
        self,
        request: baas_20181221_models.DescribeFabricInviterRequest,
    ) -> baas_20181221_models.DescribeFabricInviterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_inviter_with_options_async(request, runtime)

    def describe_fabric_orderer_logs_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrdererLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrdererLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrdererLogsResponse().from_map(
            self.do_rpcrequest('DescribeFabricOrdererLogs', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_orderer_logs_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrdererLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrdererLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrdererLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricOrdererLogs', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_orderer_logs(
        self,
        request: baas_20181221_models.DescribeFabricOrdererLogsRequest,
    ) -> baas_20181221_models.DescribeFabricOrdererLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_orderer_logs_with_options(request, runtime)

    async def describe_fabric_orderer_logs_async(
        self,
        request: baas_20181221_models.DescribeFabricOrdererLogsRequest,
    ) -> baas_20181221_models.DescribeFabricOrdererLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_orderer_logs_with_options_async(request, runtime)

    def describe_fabric_organization_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationResponse().from_map(
            self.do_rpcrequest('DescribeFabricOrganization', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_organization_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricOrganization', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_organization(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organization_with_options(request, runtime)

    async def describe_fabric_organization_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organization_with_options_async(request, runtime)

    def describe_fabric_organization_chaincodes_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationChaincodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationChaincodesResponse().from_map(
            self.do_rpcrequest('DescribeFabricOrganizationChaincodes', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_organization_chaincodes_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationChaincodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationChaincodesResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricOrganizationChaincodes', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_organization_chaincodes(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChaincodesRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organization_chaincodes_with_options(request, runtime)

    async def describe_fabric_organization_chaincodes_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChaincodesRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationChaincodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organization_chaincodes_with_options_async(request, runtime)

    def describe_fabric_organization_deletable_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationDeletableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationDeletableResponse().from_map(
            self.do_rpcrequest('DescribeFabricOrganizationDeletable', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_organization_deletable_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationDeletableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationDeletableResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricOrganizationDeletable', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_organization_deletable(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationDeletableRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organization_deletable_with_options(request, runtime)

    async def describe_fabric_organization_deletable_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationDeletableRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationDeletableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organization_deletable_with_options_async(request, runtime)

    def describe_fabric_organization_members_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationMembersResponse().from_map(
            self.do_rpcrequest('DescribeFabricOrganizationMembers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_organization_members_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationMembersResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricOrganizationMembers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_organization_members(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationMembersRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organization_members_with_options(request, runtime)

    async def describe_fabric_organization_members_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationMembersRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organization_members_with_options_async(request, runtime)

    def describe_fabric_organization_peers_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationPeersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationPeersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationPeersResponse().from_map(
            self.do_rpcrequest('DescribeFabricOrganizationPeers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_organization_peers_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationPeersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationPeersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationPeersResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricOrganizationPeers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_organization_peers(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationPeersRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationPeersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organization_peers_with_options(request, runtime)

    async def describe_fabric_organization_peers_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationPeersRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationPeersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organization_peers_with_options_async(request, runtime)

    def describe_fabric_organizations_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationsResponse().from_map(
            self.do_rpcrequest('DescribeFabricOrganizations', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_organizations_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricOrganizations', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_organizations(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationsRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organizations_with_options(request, runtime)

    async def describe_fabric_organizations_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationsRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organizations_with_options_async(request, runtime)

    def describe_fabric_organization_specs_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationSpecsResponse:
        req = open_api_models.OpenApiRequest()
        return baas_20181221_models.DescribeFabricOrganizationSpecsResponse().from_map(
            self.do_rpcrequest('DescribeFabricOrganizationSpecs', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_organization_specs_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationSpecsResponse:
        req = open_api_models.OpenApiRequest()
        return baas_20181221_models.DescribeFabricOrganizationSpecsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricOrganizationSpecs', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_organization_specs(self) -> baas_20181221_models.DescribeFabricOrganizationSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organization_specs_with_options(runtime)

    async def describe_fabric_organization_specs_async(self) -> baas_20181221_models.DescribeFabricOrganizationSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organization_specs_with_options_async(runtime)

    def describe_fabric_organization_users_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationUsersResponse().from_map(
            self.do_rpcrequest('DescribeFabricOrganizationUsers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_organization_users_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricOrganizationUsersResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricOrganizationUsers', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_organization_users(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationUsersRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organization_users_with_options(request, runtime)

    async def describe_fabric_organization_users_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationUsersRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organization_users_with_options_async(request, runtime)

    def describe_fabric_peer_logs_with_options(
        self,
        request: baas_20181221_models.DescribeFabricPeerLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricPeerLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricPeerLogsResponse().from_map(
            self.do_rpcrequest('DescribeFabricPeerLogs', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_fabric_peer_logs_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricPeerLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricPeerLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeFabricPeerLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFabricPeerLogs', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_fabric_peer_logs(
        self,
        request: baas_20181221_models.DescribeFabricPeerLogsRequest,
    ) -> baas_20181221_models.DescribeFabricPeerLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_peer_logs_with_options(request, runtime)

    async def describe_fabric_peer_logs_async(
        self,
        request: baas_20181221_models.DescribeFabricPeerLogsRequest,
    ) -> baas_20181221_models.DescribeFabricPeerLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_peer_logs_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: baas_20181221_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: baas_20181221_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: baas_20181221_models.DescribeRegionsRequest,
    ) -> baas_20181221_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: baas_20181221_models.DescribeRegionsRequest,
    ) -> baas_20181221_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_root_domain_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeRootDomainResponse:
        req = open_api_models.OpenApiRequest()
        return baas_20181221_models.DescribeRootDomainResponse().from_map(
            self.do_rpcrequest('DescribeRootDomain', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_root_domain_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeRootDomainResponse:
        req = open_api_models.OpenApiRequest()
        return baas_20181221_models.DescribeRootDomainResponse().from_map(
            await self.do_rpcrequest_async('DescribeRootDomain', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_root_domain(self) -> baas_20181221_models.DescribeRootDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_root_domain_with_options(runtime)

    async def describe_root_domain_async(self) -> baas_20181221_models.DescribeRootDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_root_domain_with_options_async(runtime)

    def describe_tasks_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeTasksResponse:
        req = open_api_models.OpenApiRequest()
        return baas_20181221_models.DescribeTasksResponse().from_map(
            self.do_rpcrequest('DescribeTasks', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeTasksResponse:
        req = open_api_models.OpenApiRequest()
        return baas_20181221_models.DescribeTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeTasks', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tasks(self) -> baas_20181221_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(runtime)

    async def describe_tasks_async(self) -> baas_20181221_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(runtime)

    def download_fabric_organization_sdkwith_options(
        self,
        request: baas_20181221_models.DownloadFabricOrganizationSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DownloadFabricOrganizationSDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DownloadFabricOrganizationSDKResponse().from_map(
            self.do_rpcrequest('DownloadFabricOrganizationSDK', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_fabric_organization_sdkwith_options_async(
        self,
        request: baas_20181221_models.DownloadFabricOrganizationSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DownloadFabricOrganizationSDKResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.DownloadFabricOrganizationSDKResponse().from_map(
            await self.do_rpcrequest_async('DownloadFabricOrganizationSDK', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_fabric_organization_sdk(
        self,
        request: baas_20181221_models.DownloadFabricOrganizationSDKRequest,
    ) -> baas_20181221_models.DownloadFabricOrganizationSDKResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_fabric_organization_sdkwith_options(request, runtime)

    async def download_fabric_organization_sdk_async(
        self,
        request: baas_20181221_models.DownloadFabricOrganizationSDKRequest,
    ) -> baas_20181221_models.DownloadFabricOrganizationSDKResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_fabric_organization_sdkwith_options_async(request, runtime)

    def freeze_ant_chain_account_with_options(
        self,
        request: baas_20181221_models.FreezeAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.FreezeAntChainAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.FreezeAntChainAccountResponse().from_map(
            self.do_rpcrequest('FreezeAntChainAccount', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def freeze_ant_chain_account_with_options_async(
        self,
        request: baas_20181221_models.FreezeAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.FreezeAntChainAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.FreezeAntChainAccountResponse().from_map(
            await self.do_rpcrequest_async('FreezeAntChainAccount', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def freeze_ant_chain_account(
        self,
        request: baas_20181221_models.FreezeAntChainAccountRequest,
    ) -> baas_20181221_models.FreezeAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.freeze_ant_chain_account_with_options(request, runtime)

    async def freeze_ant_chain_account_async(
        self,
        request: baas_20181221_models.FreezeAntChainAccountRequest,
    ) -> baas_20181221_models.FreezeAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.freeze_ant_chain_account_with_options_async(request, runtime)

    def install_fabric_chaincode_with_options(
        self,
        request: baas_20181221_models.InstallFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.InstallFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.InstallFabricChaincodeResponse().from_map(
            self.do_rpcrequest('InstallFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def install_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.InstallFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.InstallFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.InstallFabricChaincodeResponse().from_map(
            await self.do_rpcrequest_async('InstallFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def install_fabric_chaincode(
        self,
        request: baas_20181221_models.InstallFabricChaincodeRequest,
    ) -> baas_20181221_models.InstallFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_fabric_chaincode_with_options(request, runtime)

    async def install_fabric_chaincode_async(
        self,
        request: baas_20181221_models.InstallFabricChaincodeRequest,
    ) -> baas_20181221_models.InstallFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_fabric_chaincode_with_options_async(request, runtime)

    def instantiate_fabric_chaincode_with_options(
        self,
        request: baas_20181221_models.InstantiateFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.InstantiateFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.InstantiateFabricChaincodeResponse().from_map(
            self.do_rpcrequest('InstantiateFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def instantiate_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.InstantiateFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.InstantiateFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.InstantiateFabricChaincodeResponse().from_map(
            await self.do_rpcrequest_async('InstantiateFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def instantiate_fabric_chaincode(
        self,
        request: baas_20181221_models.InstantiateFabricChaincodeRequest,
    ) -> baas_20181221_models.InstantiateFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.instantiate_fabric_chaincode_with_options(request, runtime)

    async def instantiate_fabric_chaincode_async(
        self,
        request: baas_20181221_models.InstantiateFabricChaincodeRequest,
    ) -> baas_20181221_models.InstantiateFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.instantiate_fabric_chaincode_with_options_async(request, runtime)

    def join_fabric_channel_with_options(
        self,
        request: baas_20181221_models.JoinFabricChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.JoinFabricChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.JoinFabricChannelResponse().from_map(
            self.do_rpcrequest('JoinFabricChannel', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_fabric_channel_with_options_async(
        self,
        request: baas_20181221_models.JoinFabricChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.JoinFabricChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.JoinFabricChannelResponse().from_map(
            await self.do_rpcrequest_async('JoinFabricChannel', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_fabric_channel(
        self,
        request: baas_20181221_models.JoinFabricChannelRequest,
    ) -> baas_20181221_models.JoinFabricChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_fabric_channel_with_options(request, runtime)

    async def join_fabric_channel_async(
        self,
        request: baas_20181221_models.JoinFabricChannelRequest,
    ) -> baas_20181221_models.JoinFabricChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_fabric_channel_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: baas_20181221_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: baas_20181221_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: baas_20181221_models.ListTagResourcesRequest,
    ) -> baas_20181221_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: baas_20181221_models.ListTagResourcesRequest,
    ) -> baas_20181221_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def reset_ant_chain_certificate_with_options(
        self,
        request: baas_20181221_models.ResetAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ResetAntChainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ResetAntChainCertificateResponse().from_map(
            self.do_rpcrequest('ResetAntChainCertificate', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_ant_chain_certificate_with_options_async(
        self,
        request: baas_20181221_models.ResetAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ResetAntChainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ResetAntChainCertificateResponse().from_map(
            await self.do_rpcrequest_async('ResetAntChainCertificate', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_ant_chain_certificate(
        self,
        request: baas_20181221_models.ResetAntChainCertificateRequest,
    ) -> baas_20181221_models.ResetAntChainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_ant_chain_certificate_with_options(request, runtime)

    async def reset_ant_chain_certificate_async(
        self,
        request: baas_20181221_models.ResetAntChainCertificateRequest,
    ) -> baas_20181221_models.ResetAntChainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_ant_chain_certificate_with_options_async(request, runtime)

    def reset_ant_chain_user_certificate_with_options(
        self,
        request: baas_20181221_models.ResetAntChainUserCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ResetAntChainUserCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ResetAntChainUserCertificateResponse().from_map(
            self.do_rpcrequest('ResetAntChainUserCertificate', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_ant_chain_user_certificate_with_options_async(
        self,
        request: baas_20181221_models.ResetAntChainUserCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ResetAntChainUserCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ResetAntChainUserCertificateResponse().from_map(
            await self.do_rpcrequest_async('ResetAntChainUserCertificate', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_ant_chain_user_certificate(
        self,
        request: baas_20181221_models.ResetAntChainUserCertificateRequest,
    ) -> baas_20181221_models.ResetAntChainUserCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_ant_chain_user_certificate_with_options(request, runtime)

    async def reset_ant_chain_user_certificate_async(
        self,
        request: baas_20181221_models.ResetAntChainUserCertificateRequest,
    ) -> baas_20181221_models.ResetAntChainUserCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_ant_chain_user_certificate_with_options_async(request, runtime)

    def reset_fabric_organization_user_password_with_options(
        self,
        request: baas_20181221_models.ResetFabricOrganizationUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ResetFabricOrganizationUserPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ResetFabricOrganizationUserPasswordResponse().from_map(
            self.do_rpcrequest('ResetFabricOrganizationUserPassword', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_fabric_organization_user_password_with_options_async(
        self,
        request: baas_20181221_models.ResetFabricOrganizationUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ResetFabricOrganizationUserPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.ResetFabricOrganizationUserPasswordResponse().from_map(
            await self.do_rpcrequest_async('ResetFabricOrganizationUserPassword', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_fabric_organization_user_password(
        self,
        request: baas_20181221_models.ResetFabricOrganizationUserPasswordRequest,
    ) -> baas_20181221_models.ResetFabricOrganizationUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_fabric_organization_user_password_with_options(request, runtime)

    async def reset_fabric_organization_user_password_async(
        self,
        request: baas_20181221_models.ResetFabricOrganizationUserPasswordRequest,
    ) -> baas_20181221_models.ResetFabricOrganizationUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_fabric_organization_user_password_with_options_async(request, runtime)

    def synchronize_fabric_chaincode_with_options(
        self,
        request: baas_20181221_models.SynchronizeFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.SynchronizeFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.SynchronizeFabricChaincodeResponse().from_map(
            self.do_rpcrequest('SynchronizeFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def synchronize_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.SynchronizeFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.SynchronizeFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.SynchronizeFabricChaincodeResponse().from_map(
            await self.do_rpcrequest_async('SynchronizeFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def synchronize_fabric_chaincode(
        self,
        request: baas_20181221_models.SynchronizeFabricChaincodeRequest,
    ) -> baas_20181221_models.SynchronizeFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.synchronize_fabric_chaincode_with_options(request, runtime)

    async def synchronize_fabric_chaincode_async(
        self,
        request: baas_20181221_models.SynchronizeFabricChaincodeRequest,
    ) -> baas_20181221_models.SynchronizeFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.synchronize_fabric_chaincode_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: baas_20181221_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: baas_20181221_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: baas_20181221_models.TagResourcesRequest,
    ) -> baas_20181221_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: baas_20181221_models.TagResourcesRequest,
    ) -> baas_20181221_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unfreeze_ant_chain_account_with_options(
        self,
        request: baas_20181221_models.UnfreezeAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UnfreezeAntChainAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UnfreezeAntChainAccountResponse().from_map(
            self.do_rpcrequest('UnfreezeAntChainAccount', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unfreeze_ant_chain_account_with_options_async(
        self,
        request: baas_20181221_models.UnfreezeAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UnfreezeAntChainAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UnfreezeAntChainAccountResponse().from_map(
            await self.do_rpcrequest_async('UnfreezeAntChainAccount', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unfreeze_ant_chain_account(
        self,
        request: baas_20181221_models.UnfreezeAntChainAccountRequest,
    ) -> baas_20181221_models.UnfreezeAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.unfreeze_ant_chain_account_with_options(request, runtime)

    async def unfreeze_ant_chain_account_async(
        self,
        request: baas_20181221_models.UnfreezeAntChainAccountRequest,
    ) -> baas_20181221_models.UnfreezeAntChainAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unfreeze_ant_chain_account_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: baas_20181221_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: baas_20181221_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: baas_20181221_models.UntagResourcesRequest,
    ) -> baas_20181221_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: baas_20181221_models.UntagResourcesRequest,
    ) -> baas_20181221_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_ant_chain_with_options(
        self,
        request: baas_20181221_models.UpdateAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainResponse().from_map(
            self.do_rpcrequest('UpdateAntChain', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ant_chain_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainResponse().from_map(
            await self.do_rpcrequest_async('UpdateAntChain', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ant_chain(
        self,
        request: baas_20181221_models.UpdateAntChainRequest,
    ) -> baas_20181221_models.UpdateAntChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_with_options(request, runtime)

    async def update_ant_chain_async(
        self,
        request: baas_20181221_models.UpdateAntChainRequest,
    ) -> baas_20181221_models.UpdateAntChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_with_options_async(request, runtime)

    def update_ant_chain_consortium_with_options(
        self,
        request: baas_20181221_models.UpdateAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainConsortiumResponse().from_map(
            self.do_rpcrequest('UpdateAntChainConsortium', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ant_chain_consortium_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainConsortiumResponse().from_map(
            await self.do_rpcrequest_async('UpdateAntChainConsortium', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ant_chain_consortium(
        self,
        request: baas_20181221_models.UpdateAntChainConsortiumRequest,
    ) -> baas_20181221_models.UpdateAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_consortium_with_options(request, runtime)

    async def update_ant_chain_consortium_async(
        self,
        request: baas_20181221_models.UpdateAntChainConsortiumRequest,
    ) -> baas_20181221_models.UpdateAntChainConsortiumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_consortium_with_options_async(request, runtime)

    def update_ant_chain_contract_content_with_options(
        self,
        request: baas_20181221_models.UpdateAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainContractContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainContractContentResponse().from_map(
            self.do_rpcrequest('UpdateAntChainContractContent', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ant_chain_contract_content_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainContractContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainContractContentResponse().from_map(
            await self.do_rpcrequest_async('UpdateAntChainContractContent', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ant_chain_contract_content(
        self,
        request: baas_20181221_models.UpdateAntChainContractContentRequest,
    ) -> baas_20181221_models.UpdateAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_contract_content_with_options(request, runtime)

    async def update_ant_chain_contract_content_async(
        self,
        request: baas_20181221_models.UpdateAntChainContractContentRequest,
    ) -> baas_20181221_models.UpdateAntChainContractContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_contract_content_with_options_async(request, runtime)

    def update_ant_chain_contract_project_with_options(
        self,
        request: baas_20181221_models.UpdateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainContractProjectResponse().from_map(
            self.do_rpcrequest('UpdateAntChainContractProject', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainContractProjectResponse().from_map(
            await self.do_rpcrequest_async('UpdateAntChainContractProject', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ant_chain_contract_project(
        self,
        request: baas_20181221_models.UpdateAntChainContractProjectRequest,
    ) -> baas_20181221_models.UpdateAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_contract_project_with_options(request, runtime)

    async def update_ant_chain_contract_project_async(
        self,
        request: baas_20181221_models.UpdateAntChainContractProjectRequest,
    ) -> baas_20181221_models.UpdateAntChainContractProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_contract_project_with_options_async(request, runtime)

    def update_ant_chain_member_with_options(
        self,
        request: baas_20181221_models.UpdateAntChainMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainMemberResponse().from_map(
            self.do_rpcrequest('UpdateAntChainMember', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ant_chain_member_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainMemberResponse().from_map(
            await self.do_rpcrequest_async('UpdateAntChainMember', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ant_chain_member(
        self,
        request: baas_20181221_models.UpdateAntChainMemberRequest,
    ) -> baas_20181221_models.UpdateAntChainMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_member_with_options(request, runtime)

    async def update_ant_chain_member_async(
        self,
        request: baas_20181221_models.UpdateAntChainMemberRequest,
    ) -> baas_20181221_models.UpdateAntChainMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_member_with_options_async(request, runtime)

    def update_ant_chain_qrcode_authorization_with_options(
        self,
        request: baas_20181221_models.UpdateAntChainQRCodeAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainQRCodeAuthorizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainQRCodeAuthorizationResponse().from_map(
            self.do_rpcrequest('UpdateAntChainQRCodeAuthorization', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ant_chain_qrcode_authorization_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainQRCodeAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainQRCodeAuthorizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpdateAntChainQRCodeAuthorizationResponse().from_map(
            await self.do_rpcrequest_async('UpdateAntChainQRCodeAuthorization', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ant_chain_qrcode_authorization(
        self,
        request: baas_20181221_models.UpdateAntChainQRCodeAuthorizationRequest,
    ) -> baas_20181221_models.UpdateAntChainQRCodeAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ant_chain_qrcode_authorization_with_options(request, runtime)

    async def update_ant_chain_qrcode_authorization_async(
        self,
        request: baas_20181221_models.UpdateAntChainQRCodeAuthorizationRequest,
    ) -> baas_20181221_models.UpdateAntChainQRCodeAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ant_chain_qrcode_authorization_with_options_async(request, runtime)

    def upgrade_fabric_chaincode_with_options(
        self,
        request: baas_20181221_models.UpgradeFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpgradeFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpgradeFabricChaincodeResponse().from_map(
            self.do_rpcrequest('UpgradeFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.UpgradeFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpgradeFabricChaincodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return baas_20181221_models.UpgradeFabricChaincodeResponse().from_map(
            await self.do_rpcrequest_async('UpgradeFabricChaincode', '2018-12-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_fabric_chaincode(
        self,
        request: baas_20181221_models.UpgradeFabricChaincodeRequest,
    ) -> baas_20181221_models.UpgradeFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_fabric_chaincode_with_options(request, runtime)

    async def upgrade_fabric_chaincode_async(
        self,
        request: baas_20181221_models.UpgradeFabricChaincodeRequest,
    ) -> baas_20181221_models.UpgradeFabricChaincodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_fabric_chaincode_with_options_async(request, runtime)
