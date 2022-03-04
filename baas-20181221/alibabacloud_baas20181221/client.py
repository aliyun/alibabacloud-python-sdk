# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

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
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.is_accepted):
            body['IsAccepted'] = request.is_accepted
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AcceptFabricInvitation',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.AcceptFabricInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_fabric_invitation_with_options_async(
        self,
        request: baas_20181221_models.AcceptFabricInvitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.AcceptFabricInvitationResponse:
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
            action='AcceptFabricInvitation',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.AcceptFabricInvitationResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ApplyAntChainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ant_chain_certificate_with_options_async(
        self,
        request: baas_20181221_models.ApplyAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ApplyAntChainCertificateResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ApplyAntChainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ant_chain_certificate_with_key_auto_creation_with_options_async(
        self,
        request: baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ApplyAntChainCertificateWithKeyAutoCreationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def approve_fabric_chaincode_definition_with_options(
        self,
        request: baas_20181221_models.ApproveFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ApproveFabricChaincodeDefinitionResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ApproveFabricChaincodeDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_fabric_chaincode_definition_with_options_async(
        self,
        request: baas_20181221_models.ApproveFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ApproveFabricChaincodeDefinitionResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ApproveFabricChaincodeDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_fabric_chaincode_definition(
        self,
        request: baas_20181221_models.ApproveFabricChaincodeDefinitionRequest,
    ) -> baas_20181221_models.ApproveFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_fabric_chaincode_definition_with_options(request, runtime)

    async def approve_fabric_chaincode_definition_async(
        self,
        request: baas_20181221_models.ApproveFabricChaincodeDefinitionRequest,
    ) -> baas_20181221_models.ApproveFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_fabric_chaincode_definition_with_options_async(request, runtime)

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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse(),
            self.call_api(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.domain_code):
            body['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckFabricConsortiumDomain',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CheckFabricConsortiumDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_fabric_consortium_domain_with_options_async(
        self,
        request: baas_20181221_models.CheckFabricConsortiumDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CheckFabricConsortiumDomainResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_code):
            body['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckFabricConsortiumDomain',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CheckFabricConsortiumDomainResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.domain_code):
            body['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckFabricOrganizationDomain',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CheckFabricOrganizationDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_fabric_organization_domain_with_options_async(
        self,
        request: baas_20181221_models.CheckFabricOrganizationDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CheckFabricOrganizationDomainResponse:
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
            action='CheckFabricOrganizationDomain',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CheckFabricOrganizationDomainResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.consortium_id):
            query['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmFabricConsortiumMember',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ConfirmFabricConsortiumMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_fabric_consortium_member_with_options_async(
        self,
        request: baas_20181221_models.ConfirmFabricConsortiumMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ConfirmFabricConsortiumMemberResponse:
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
            action='ConfirmFabricConsortiumMember',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ConfirmFabricConsortiumMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CopyAntChainContractProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20181221_models.CopyAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CopyAntChainContractProjectResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CopyAntChainContractProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateAntChainAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_chain_account_with_options_async(
        self,
        request: baas_20181221_models.CreateAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainAccountResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateAntChainAccountResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_chain_account_with_key_pair_auto_creation_with_options_async(
        self,
        request: baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateAntChainAccountWithKeyPairAutoCreationResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateAntChainConsortiumResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_chain_consortium_with_options_async(
        self,
        request: baas_20181221_models.CreateAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainConsortiumResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateAntChainConsortiumResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateAntChainContractContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_chain_contract_content_with_options_async(
        self,
        request: baas_20181221_models.CreateAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainContractContentResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateAntChainContractContentResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateAntChainContractProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20181221_models.CreateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateAntChainContractProjectResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateAntChainContractProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='CreateFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChaincodeResponse:
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
            action='CreateFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_fabric_chaincode_package_with_options(
        self,
        request: baas_20181221_models.CreateFabricChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChaincodePackageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.oss_url):
            body['OssUrl'] = request.oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFabricChaincodePackage',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricChaincodePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fabric_chaincode_package_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChaincodePackageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.oss_url):
            body['OssUrl'] = request.oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFabricChaincodePackage',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricChaincodePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fabric_chaincode_package(
        self,
        request: baas_20181221_models.CreateFabricChaincodePackageRequest,
    ) -> baas_20181221_models.CreateFabricChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fabric_chaincode_package_with_options(request, runtime)

    async def create_fabric_chaincode_package_async(
        self,
        request: baas_20181221_models.CreateFabricChaincodePackageRequest,
    ) -> baas_20181221_models.CreateFabricChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fabric_chaincode_package_with_options_async(request, runtime)

    def create_fabric_channel_with_options(
        self,
        request: baas_20181221_models.CreateFabricChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChannelResponse:
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
            action='CreateFabricChannel',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fabric_channel_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChannelResponse:
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
            action='CreateFabricChannel',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricChannelResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFabricChannelMember',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricChannelMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fabric_channel_member_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricChannelMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricChannelMemberResponse:
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
            action='CreateFabricChannelMember',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricChannelMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.channel_policy):
            body['ChannelPolicy'] = request.channel_policy
        if not UtilClient.is_unset(request.consortium_description):
            body['ConsortiumDescription'] = request.consortium_description
        if not UtilClient.is_unset(request.consortium_name):
            body['ConsortiumName'] = request.consortium_name
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.orderer_type):
            body['OrdererType'] = request.orderer_type
        if not UtilClient.is_unset(request.orderers_count):
            body['OrderersCount'] = request.orderers_count
        if not UtilClient.is_unset(request.organization):
            body['Organization'] = request.organization
        if not UtilClient.is_unset(request.payment_duration):
            body['PaymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            body['PaymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.peers_count):
            body['PeersCount'] = request.peers_count
        if not UtilClient.is_unset(request.spec_name):
            body['SpecName'] = request.spec_name
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFabricConsortium',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricConsortiumResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fabric_consortium_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel_policy):
            body['ChannelPolicy'] = request.channel_policy
        if not UtilClient.is_unset(request.consortium_description):
            body['ConsortiumDescription'] = request.consortium_description
        if not UtilClient.is_unset(request.consortium_name):
            body['ConsortiumName'] = request.consortium_name
        if not UtilClient.is_unset(request.domain):
            body['Domain'] = request.domain
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.orderer_type):
            body['OrdererType'] = request.orderer_type
        if not UtilClient.is_unset(request.orderers_count):
            body['OrderersCount'] = request.orderers_count
        if not UtilClient.is_unset(request.organization):
            body['Organization'] = request.organization
        if not UtilClient.is_unset(request.payment_duration):
            body['PaymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            body['PaymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.peers_count):
            body['PeersCount'] = request.peers_count
        if not UtilClient.is_unset(request.spec_name):
            body['SpecName'] = request.spec_name
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFabricConsortium',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricConsortiumResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='CreateFabricConsortiumMember',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricConsortiumMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fabric_consortium_member_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricConsortiumMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricConsortiumMemberResponse:
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
            action='CreateFabricConsortiumMember',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricConsortiumMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.organization_name):
            query['OrganizationName'] = request.organization_name
        if not UtilClient.is_unset(request.spec_name):
            query['SpecName'] = request.spec_name
        body = {}
        if not UtilClient.is_unset(request.payment_duration):
            body['PaymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            body['PaymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.peers_count):
            body['PeersCount'] = request.peers_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFabricOrganization',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fabric_organization_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.organization_name):
            query['OrganizationName'] = request.organization_name
        if not UtilClient.is_unset(request.spec_name):
            query['SpecName'] = request.spec_name
        body = {}
        if not UtilClient.is_unset(request.payment_duration):
            body['PaymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            body['PaymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.peers_count):
            body['PeersCount'] = request.peers_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFabricOrganization',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='CreateFabricOrganizationUser',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricOrganizationUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fabric_organization_user_with_options_async(
        self,
        request: baas_20181221_models.CreateFabricOrganizationUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.CreateFabricOrganizationUserResponse:
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
            action='CreateFabricOrganizationUser',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.CreateFabricOrganizationUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainConsortium',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DeleteAntChainConsortiumResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ant_chain_consortium_with_options_async(
        self,
        request: baas_20181221_models.DeleteAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainConsortiumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainConsortium',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DeleteAntChainConsortiumResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.content_id):
            body['ContentId'] = request.content_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainContractContent',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DeleteAntChainContractContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ant_chain_contract_content_with_options_async(
        self,
        request: baas_20181221_models.DeleteAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainContractContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content_id):
            body['ContentId'] = request.content_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainContractContent',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DeleteAntChainContractContentResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainContractProject',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DeleteAntChainContractProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20181221_models.DeleteAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainContractProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAntChainContractProject',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DeleteAntChainContractProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ant_chain_mini_app_qrcode_authorized_user_with_options_async(
        self,
        request: baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DeleteAntChainMiniAppQRCodeAuthorizedUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DeleteFabricChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.DeleteFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DeleteFabricChaincodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DeleteFabricChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_accounts_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainAccountsResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainAccountsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_accounts_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainAccountsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainAccountsV2Response:
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
            action='DescribeAntChainAccountsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainAccountsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_accounts_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainAccountsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainAccountsV2Response:
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
            action='DescribeAntChainAccountsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainAccountsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_accounts_v2(
        self,
        request: baas_20181221_models.DescribeAntChainAccountsV2Request,
    ) -> baas_20181221_models.DescribeAntChainAccountsV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_accounts_v2with_options(request, runtime)

    async def describe_ant_chain_accounts_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainAccountsV2Request,
    ) -> baas_20181221_models.DescribeAntChainAccountsV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_accounts_v2with_options_async(request, runtime)

    def describe_ant_chain_block_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainBlockResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_block_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainBlockResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainBlockResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_block_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainBlockV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainBlockV2Response:
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
            action='DescribeAntChainBlockV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainBlockV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_block_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainBlockV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainBlockV2Response:
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
            action='DescribeAntChainBlockV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainBlockV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_block_v2(
        self,
        request: baas_20181221_models.DescribeAntChainBlockV2Request,
    ) -> baas_20181221_models.DescribeAntChainBlockV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_block_v2with_options(request, runtime)

    async def describe_ant_chain_block_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainBlockV2Request,
    ) -> baas_20181221_models.DescribeAntChainBlockV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_block_v2with_options_async(request, runtime)

    def describe_ant_chain_certificate_applications_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainCertificateApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainCertificateApplicationsResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainCertificateApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_certificate_applications_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainCertificateApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainCertificateApplicationsResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainCertificateApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_certificate_applications_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainCertificateApplicationsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainCertificateApplicationsV2Response:
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
            action='DescribeAntChainCertificateApplicationsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainCertificateApplicationsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_certificate_applications_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainCertificateApplicationsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainCertificateApplicationsV2Response:
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
            action='DescribeAntChainCertificateApplicationsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainCertificateApplicationsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_certificate_applications_v2(
        self,
        request: baas_20181221_models.DescribeAntChainCertificateApplicationsV2Request,
    ) -> baas_20181221_models.DescribeAntChainCertificateApplicationsV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_certificate_applications_v2with_options(request, runtime)

    async def describe_ant_chain_certificate_applications_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainCertificateApplicationsV2Request,
    ) -> baas_20181221_models.DescribeAntChainCertificateApplicationsV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_certificate_applications_v2with_options_async(request, runtime)

    def describe_ant_chain_consortiums_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainConsortiumsResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainConsortiumsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_consortiums_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainConsortiumsResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainConsortiumsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_consortiums_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainConsortiumsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainConsortiumsV2Response:
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
            action='DescribeAntChainConsortiumsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainConsortiumsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_consortiums_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainConsortiumsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainConsortiumsV2Response:
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
            action='DescribeAntChainConsortiumsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainConsortiumsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_consortiums_v2(
        self,
        request: baas_20181221_models.DescribeAntChainConsortiumsV2Request,
    ) -> baas_20181221_models.DescribeAntChainConsortiumsV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_consortiums_v2with_options(request, runtime)

    async def describe_ant_chain_consortiums_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainConsortiumsV2Request,
    ) -> baas_20181221_models.DescribeAntChainConsortiumsV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_consortiums_v2with_options_async(request, runtime)

    def describe_ant_chain_contract_project_content_tree_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectContentTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectContentTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainContractProjectContentTree',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainContractProjectContentTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_contract_project_content_tree_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectContentTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectContentTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainContractProjectContentTree',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainContractProjectContentTreeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_contract_project_content_tree_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectContentTreeV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectContentTreeV2Response:
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
            action='DescribeAntChainContractProjectContentTreeV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainContractProjectContentTreeV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_contract_project_content_tree_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectContentTreeV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectContentTreeV2Response:
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
            action='DescribeAntChainContractProjectContentTreeV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainContractProjectContentTreeV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_contract_project_content_tree_v2(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectContentTreeV2Request,
    ) -> baas_20181221_models.DescribeAntChainContractProjectContentTreeV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_contract_project_content_tree_v2with_options(request, runtime)

    async def describe_ant_chain_contract_project_content_tree_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectContentTreeV2Request,
    ) -> baas_20181221_models.DescribeAntChainContractProjectContentTreeV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_contract_project_content_tree_v2with_options_async(request, runtime)

    def describe_ant_chain_contract_projects_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectsResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainContractProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_contract_projects_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectsResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainContractProjectsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_contract_projects_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectsV2Response:
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
            action='DescribeAntChainContractProjectsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainContractProjectsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_contract_projects_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainContractProjectsV2Response:
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
            action='DescribeAntChainContractProjectsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainContractProjectsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_contract_projects_v2(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectsV2Request,
    ) -> baas_20181221_models.DescribeAntChainContractProjectsV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_contract_projects_v2with_options(request, runtime)

    async def describe_ant_chain_contract_projects_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainContractProjectsV2Request,
    ) -> baas_20181221_models.DescribeAntChainContractProjectsV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_contract_projects_v2with_options_async(request, runtime)

    def describe_ant_chain_download_paths_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainDownloadPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainDownloadPathsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainDownloadPaths',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainDownloadPathsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_download_paths_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainDownloadPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainDownloadPathsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainDownloadPaths',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainDownloadPathsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_download_paths_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainDownloadPathsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainDownloadPathsV2Response:
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
            action='DescribeAntChainDownloadPathsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainDownloadPathsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_download_paths_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainDownloadPathsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainDownloadPathsV2Response:
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
            action='DescribeAntChainDownloadPathsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainDownloadPathsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_download_paths_v2(
        self,
        request: baas_20181221_models.DescribeAntChainDownloadPathsV2Request,
    ) -> baas_20181221_models.DescribeAntChainDownloadPathsV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_download_paths_v2with_options(request, runtime)

    async def describe_ant_chain_download_paths_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainDownloadPathsV2Request,
    ) -> baas_20181221_models.DescribeAntChainDownloadPathsV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_download_paths_v2with_options_async(request, runtime)

    def describe_ant_chain_information_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainInformationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainInformation',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_information_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainInformationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainInformation',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainInformationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_information_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainInformationV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainInformationV2Response:
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
            action='DescribeAntChainInformationV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainInformationV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_information_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainInformationV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainInformationV2Response:
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
            action='DescribeAntChainInformationV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainInformationV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_information_v2(
        self,
        request: baas_20181221_models.DescribeAntChainInformationV2Request,
    ) -> baas_20181221_models.DescribeAntChainInformationV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_information_v2with_options(request, runtime)

    async def describe_ant_chain_information_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainInformationV2Request,
    ) -> baas_20181221_models.DescribeAntChainInformationV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_information_v2with_options_async(request, runtime)

    def describe_ant_chain_latest_blocks_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainLatestBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestBlocksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestBlocks',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainLatestBlocksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_latest_blocks_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainLatestBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestBlocksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestBlocks',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainLatestBlocksResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_latest_blocks_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainLatestBlocksV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestBlocksV2Response:
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
            action='DescribeAntChainLatestBlocksV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainLatestBlocksV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_latest_blocks_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainLatestBlocksV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestBlocksV2Response:
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
            action='DescribeAntChainLatestBlocksV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainLatestBlocksV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_latest_blocks_v2(
        self,
        request: baas_20181221_models.DescribeAntChainLatestBlocksV2Request,
    ) -> baas_20181221_models.DescribeAntChainLatestBlocksV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_latest_blocks_v2with_options(request, runtime)

    async def describe_ant_chain_latest_blocks_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainLatestBlocksV2Request,
    ) -> baas_20181221_models.DescribeAntChainLatestBlocksV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_latest_blocks_v2with_options_async(request, runtime)

    def describe_ant_chain_latest_transaction_digests_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainLatestTransactionDigestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestTransactionDigestsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestTransactionDigests',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainLatestTransactionDigestsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_latest_transaction_digests_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainLatestTransactionDigestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestTransactionDigestsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainLatestTransactionDigests',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainLatestTransactionDigestsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_latest_transaction_digests_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainLatestTransactionDigestsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestTransactionDigestsV2Response:
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
            action='DescribeAntChainLatestTransactionDigestsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainLatestTransactionDigestsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_latest_transaction_digests_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainLatestTransactionDigestsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainLatestTransactionDigestsV2Response:
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
            action='DescribeAntChainLatestTransactionDigestsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainLatestTransactionDigestsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_latest_transaction_digests_v2(
        self,
        request: baas_20181221_models.DescribeAntChainLatestTransactionDigestsV2Request,
    ) -> baas_20181221_models.DescribeAntChainLatestTransactionDigestsV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_latest_transaction_digests_v2with_options(request, runtime)

    async def describe_ant_chain_latest_transaction_digests_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainLatestTransactionDigestsV2Request,
    ) -> baas_20181221_models.DescribeAntChainLatestTransactionDigestsV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_latest_transaction_digests_v2with_options_async(request, runtime)

    def describe_ant_chain_members_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMembersResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_members_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMembersResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMembersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_members_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMembersV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMembersV2Response:
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
            action='DescribeAntChainMembersV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMembersV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_members_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMembersV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMembersV2Response:
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
            action='DescribeAntChainMembersV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMembersV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_members_v2(
        self,
        request: baas_20181221_models.DescribeAntChainMembersV2Request,
    ) -> baas_20181221_models.DescribeAntChainMembersV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_members_v2with_options(request, runtime)

    async def describe_ant_chain_members_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainMembersV2Request,
    ) -> baas_20181221_models.DescribeAntChainMembersV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_members_v2with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_qrcode_access_log_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_qrcode_access_log_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_mini_app_browser_qrcode_access_log_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Response:
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
            action='DescribeAntChainMiniAppBrowserQRCodeAccessLogV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_qrcode_access_log_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Response:
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
            action='DescribeAntChainMiniAppBrowserQRCodeAccessLogV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_mini_app_browser_qrcode_access_log_v2(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Request,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_qrcode_access_log_v2with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_qrcode_access_log_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Request,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_qrcode_access_log_v2with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_qrcode_authorized_users_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_qrcode_authorized_users_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_mini_app_browser_qrcode_authorized_users_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Response:
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
            action='DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_qrcode_authorized_users_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Response:
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
            action='DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_mini_app_browser_qrcode_authorized_users_v2(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Request,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_qrcode_authorized_users_v2with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_qrcode_authorized_users_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Request,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_qrcode_authorized_users_v2with_options_async(request, runtime)

    def describe_ant_chain_mini_app_browser_transaction_qrcode_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_transaction_qrcode_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_mini_app_browser_transaction_qrcode_new_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_mini_app_browser_transaction_qrcode_new_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_mini_app_browser_transaction_qrcode_new(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewRequest,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_mini_app_browser_transaction_qrcode_new_with_options(request, runtime)

    async def describe_ant_chain_mini_app_browser_transaction_qrcode_new_async(
        self,
        request: baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewRequest,
    ) -> baas_20181221_models.DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_mini_app_browser_transaction_qrcode_new_with_options_async(request, runtime)

    def describe_ant_chain_nodes_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainNodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainNodes',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_nodes_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainNodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainNodes',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainNodesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_nodes_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainNodesV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainNodesV2Response:
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
            action='DescribeAntChainNodesV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainNodesV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_nodes_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainNodesV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainNodesV2Response:
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
            action='DescribeAntChainNodesV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainNodesV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_nodes_v2(
        self,
        request: baas_20181221_models.DescribeAntChainNodesV2Request,
    ) -> baas_20181221_models.DescribeAntChainNodesV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_nodes_v2with_options(request, runtime)

    async def describe_ant_chain_nodes_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainNodesV2Request,
    ) -> baas_20181221_models.DescribeAntChainNodesV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_nodes_v2with_options_async(request, runtime)

    def describe_ant_chain_qrcode_authorization_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainQRCodeAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainQRCodeAuthorizationResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainQRCodeAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_qrcode_authorization_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainQRCodeAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainQRCodeAuthorizationResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainQRCodeAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_qrcode_authorization_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainQRCodeAuthorizationV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainQRCodeAuthorizationV2Response:
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
            action='DescribeAntChainQRCodeAuthorizationV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainQRCodeAuthorizationV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_qrcode_authorization_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainQRCodeAuthorizationV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainQRCodeAuthorizationV2Response:
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
            action='DescribeAntChainQRCodeAuthorizationV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainQRCodeAuthorizationV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_qrcode_authorization_v2(
        self,
        request: baas_20181221_models.DescribeAntChainQRCodeAuthorizationV2Request,
    ) -> baas_20181221_models.DescribeAntChainQRCodeAuthorizationV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_qrcode_authorization_v2with_options(request, runtime)

    async def describe_ant_chain_qrcode_authorization_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainQRCodeAuthorizationV2Request,
    ) -> baas_20181221_models.DescribeAntChainQRCodeAuthorizationV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_qrcode_authorization_v2with_options_async(request, runtime)

    def describe_ant_chain_transaction_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_transaction_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.hash):
            body['Hash'] = request.hash
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAntChainTransactionReceipt',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionReceiptResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_transaction_receipt_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionReceiptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionReceiptResponse:
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
            action='DescribeAntChainTransactionReceipt',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionReceiptResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_transaction_receipt_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionReceiptV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionReceiptV2Response:
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
            action='DescribeAntChainTransactionReceiptV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionReceiptV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_transaction_receipt_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionReceiptV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionReceiptV2Response:
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
            action='DescribeAntChainTransactionReceiptV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionReceiptV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_transaction_receipt_v2(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionReceiptV2Request,
    ) -> baas_20181221_models.DescribeAntChainTransactionReceiptV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_transaction_receipt_v2with_options(request, runtime)

    async def describe_ant_chain_transaction_receipt_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionReceiptV2Request,
    ) -> baas_20181221_models.DescribeAntChainTransactionReceiptV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_transaction_receipt_v2with_options_async(request, runtime)

    def describe_ant_chain_transaction_statistics_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionStatisticsResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_transaction_statistics_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionStatisticsResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chain_transaction_statistics_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionStatisticsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionStatisticsV2Response:
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
            action='DescribeAntChainTransactionStatisticsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionStatisticsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_transaction_statistics_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionStatisticsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionStatisticsV2Response:
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
            action='DescribeAntChainTransactionStatisticsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionStatisticsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_transaction_statistics_v2(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionStatisticsV2Request,
    ) -> baas_20181221_models.DescribeAntChainTransactionStatisticsV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_transaction_statistics_v2with_options(request, runtime)

    async def describe_ant_chain_transaction_statistics_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionStatisticsV2Request,
    ) -> baas_20181221_models.DescribeAntChainTransactionStatisticsV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_transaction_statistics_v2with_options_async(request, runtime)

    def describe_ant_chain_transaction_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionV2Response:
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
            action='DescribeAntChainTransactionV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chain_transaction_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainTransactionV2Response:
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
            action='DescribeAntChainTransactionV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainTransactionV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chain_transaction_v2(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionV2Request,
    ) -> baas_20181221_models.DescribeAntChainTransactionV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chain_transaction_v2with_options(request, runtime)

    async def describe_ant_chain_transaction_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainTransactionV2Request,
    ) -> baas_20181221_models.DescribeAntChainTransactionV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chain_transaction_v2with_options_async(request, runtime)

    def describe_ant_chains_with_options(
        self,
        request: baas_20181221_models.DescribeAntChainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainsResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chains_with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainsResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ant_chains_v2with_options(
        self,
        request: baas_20181221_models.DescribeAntChainsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainsV2Response:
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
            action='DescribeAntChainsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_ant_chains_v2with_options_async(
        self,
        request: baas_20181221_models.DescribeAntChainsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeAntChainsV2Response:
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
            action='DescribeAntChainsV2',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeAntChainsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ant_chains_v2(
        self,
        request: baas_20181221_models.DescribeAntChainsV2Request,
    ) -> baas_20181221_models.DescribeAntChainsV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_ant_chains_v2with_options(request, runtime)

    async def describe_ant_chains_v2_async(
        self,
        request: baas_20181221_models.DescribeAntChainsV2Request,
    ) -> baas_20181221_models.DescribeAntChainsV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ant_chains_v2with_options_async(request, runtime)

    def describe_ethereum_deletable_with_options(
        self,
        request: baas_20181221_models.DescribeEthereumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeEthereumDeletableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumDeletable',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeEthereumDeletableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ethereum_deletable_with_options_async(
        self,
        request: baas_20181221_models.DescribeEthereumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeEthereumDeletableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ethereum_id):
            body['EthereumId'] = request.ethereum_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEthereumDeletable',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeEthereumDeletableResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricCandidateOrganizations',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricCandidateOrganizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_candidate_organizations_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricCandidateOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricCandidateOrganizationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricCandidateOrganizations',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricCandidateOrganizationsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_fabric_chaincode_definition_task_with_options(
        self,
        request: baas_20181221_models.DescribeFabricChaincodeDefinitionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricChaincodeDefinitionTaskResponse:
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
            action='DescribeFabricChaincodeDefinitionTask',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricChaincodeDefinitionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_chaincode_definition_task_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricChaincodeDefinitionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricChaincodeDefinitionTaskResponse:
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
            action='DescribeFabricChaincodeDefinitionTask',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricChaincodeDefinitionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_chaincode_definition_task(
        self,
        request: baas_20181221_models.DescribeFabricChaincodeDefinitionTaskRequest,
    ) -> baas_20181221_models.DescribeFabricChaincodeDefinitionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_chaincode_definition_task_with_options(request, runtime)

    async def describe_fabric_chaincode_definition_task_async(
        self,
        request: baas_20181221_models.DescribeFabricChaincodeDefinitionTaskRequest,
    ) -> baas_20181221_models.DescribeFabricChaincodeDefinitionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_chaincode_definition_task_with_options_async(request, runtime)

    def describe_fabric_chaincode_upload_policy_with_options(
        self,
        request: baas_20181221_models.DescribeFabricChaincodeUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricChaincodeUploadPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricChaincodeUploadPolicy',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricChaincodeUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_chaincode_upload_policy_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricChaincodeUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricChaincodeUploadPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricChaincodeUploadPolicy',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricChaincodeUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFabricChannelMembers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricChannelMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_channel_members_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricChannelMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricChannelMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFabricChannelMembers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricChannelMembersResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricConsortiumAdminStatus',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumAdminStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_consortium_admin_status_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumAdminStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumAdminStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricConsortiumAdminStatus',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumAdminStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricConsortiumChaincodes',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumChaincodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_consortium_chaincodes_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumChaincodesResponse:
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
            action='DescribeFabricConsortiumChaincodes',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumChaincodesResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='DescribeFabricConsortiumChannels',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_consortium_channels_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumChannelsResponse:
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
            action='DescribeFabricConsortiumChannels',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumChannelsResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DescribeFabricConsortiumConfig',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_consortium_config_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumConfigResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeFabricConsortiumConfig',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='DescribeFabricConsortiumDeletable',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumDeletableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_consortium_deletable_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumDeletableResponse:
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
            action='DescribeFabricConsortiumDeletable',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumDeletableResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='DescribeFabricConsortiumMemberApproval',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumMemberApprovalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_consortium_member_approval_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumMemberApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumMemberApprovalResponse:
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
            action='DescribeFabricConsortiumMemberApproval',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumMemberApprovalResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricConsortiumMembers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_consortium_members_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumMembersResponse:
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
            action='DescribeFabricConsortiumMembers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumMembersResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricConsortiumOrderers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumOrderersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_consortium_orderers_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumOrderersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumOrderersResponse:
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
            action='DescribeFabricConsortiumOrderers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumOrderersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_fabric_consortium_specs_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumSpecsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeFabricConsortiumSpecs',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_consortium_specs_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumSpecsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeFabricConsortiumSpecs',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_consortium_specs(self) -> baas_20181221_models.DescribeFabricConsortiumSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_consortium_specs_with_options(runtime)

    async def describe_fabric_consortium_specs_async(self) -> baas_20181221_models.DescribeFabricConsortiumSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_consortium_specs_with_options_async(runtime)

    def describe_fabric_consortiums_with_options(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumsResponse:
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
            action='DescribeFabricConsortiums',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_consortiums_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricConsortiumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricConsortiumsResponse:
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
            action='DescribeFabricConsortiums',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricConsortiumsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_fabric_explorer_with_options(
        self,
        request: baas_20181221_models.DescribeFabricExplorerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricExplorerResponse:
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
            action='DescribeFabricExplorer',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricExplorerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_explorer_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricExplorerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricExplorerResponse:
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
            action='DescribeFabricExplorer',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricExplorerResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricInvitationCode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricInvitationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_invitation_code_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricInvitationCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricInvitationCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consortium_id):
            body['ConsortiumId'] = request.consortium_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricInvitationCode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricInvitationCodeResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricInviter',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricInviterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_inviter_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricInviterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricInviterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricInviter',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricInviterResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='DescribeFabricOrdererLogs',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrdererLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_orderer_logs_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrdererLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrdererLogsResponse:
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
            action='DescribeFabricOrdererLogs',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrdererLogsResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='DescribeFabricOrganization',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organization_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationResponse:
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
            action='DescribeFabricOrganization',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_fabric_organization_chaincode_package_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationChaincodePackageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricOrganizationChaincodePackage',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationChaincodePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organization_chaincode_package_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationChaincodePackageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricOrganizationChaincodePackage',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationChaincodePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_organization_chaincode_package(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChaincodePackageRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organization_chaincode_package_with_options(request, runtime)

    async def describe_fabric_organization_chaincode_package_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChaincodePackageRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organization_chaincode_package_with_options_async(request, runtime)

    def describe_fabric_organization_chaincodes_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationChaincodesResponse:
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
            action='DescribeFabricOrganizationChaincodes',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationChaincodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organization_chaincodes_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChaincodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationChaincodesResponse:
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
            action='DescribeFabricOrganizationChaincodes',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationChaincodesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_fabric_organization_channels_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationChannelsResponse:
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
            action='DescribeFabricOrganizationChannels',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organization_channels_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationChannelsResponse:
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
            action='DescribeFabricOrganizationChannels',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fabric_organization_channels(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChannelsRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fabric_organization_channels_with_options(request, runtime)

    async def describe_fabric_organization_channels_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationChannelsRequest,
    ) -> baas_20181221_models.DescribeFabricOrganizationChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fabric_organization_channels_with_options_async(request, runtime)

    def describe_fabric_organization_deletable_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationDeletableResponse:
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
            action='DescribeFabricOrganizationDeletable',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationDeletableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organization_deletable_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationDeletableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationDeletableResponse:
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
            action='DescribeFabricOrganizationDeletable',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationDeletableResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.organization_id):
            body['OrganizationId'] = request.organization_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFabricOrganizationMembers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organization_members_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationMembersResponse:
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
            action='DescribeFabricOrganizationMembers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationMembersResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='DescribeFabricOrganizationPeers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationPeersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organization_peers_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationPeersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationPeersResponse:
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
            action='DescribeFabricOrganizationPeers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationPeersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_fabric_organization_specs_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationSpecsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeFabricOrganizationSpecs',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organization_specs_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationSpecsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeFabricOrganizationSpecs',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationSpecsResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='DescribeFabricOrganizationUsers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organization_users_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationUsersResponse:
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
            action='DescribeFabricOrganizationUsers',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationUsersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_fabric_organizations_with_options(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationsResponse:
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
            action='DescribeFabricOrganizations',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_organizations_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricOrganizationsResponse:
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
            action='DescribeFabricOrganizations',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricOrganizationsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_fabric_peer_logs_with_options(
        self,
        request: baas_20181221_models.DescribeFabricPeerLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricPeerLogsResponse:
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
            action='DescribeFabricPeerLogs',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricPeerLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fabric_peer_logs_with_options_async(
        self,
        request: baas_20181221_models.DescribeFabricPeerLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeFabricPeerLogsResponse:
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
            action='DescribeFabricPeerLogs',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeFabricPeerLogsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: baas_20181221_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DescribeRootDomain',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeRootDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_root_domain_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeRootDomainResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRootDomain',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeRootDomainResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DescribeTasksResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='DownloadFabricOrganizationSDK',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DownloadFabricOrganizationSDKResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_fabric_organization_sdkwith_options_async(
        self,
        request: baas_20181221_models.DownloadFabricOrganizationSDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.DownloadFabricOrganizationSDKResponse:
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
            action='DownloadFabricOrganizationSDK',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.DownloadFabricOrganizationSDKResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.FreezeAntChainAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def freeze_ant_chain_account_with_options_async(
        self,
        request: baas_20181221_models.FreezeAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.FreezeAntChainAccountResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.FreezeAntChainAccountResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='InstallFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.InstallFabricChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.InstallFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.InstallFabricChaincodeResponse:
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
            action='InstallFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.InstallFabricChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def install_fabric_chaincode_package_with_options(
        self,
        request: baas_20181221_models.InstallFabricChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.InstallFabricChaincodePackageResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.InstallFabricChaincodePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_fabric_chaincode_package_with_options_async(
        self,
        request: baas_20181221_models.InstallFabricChaincodePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.InstallFabricChaincodePackageResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.InstallFabricChaincodePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_fabric_chaincode_package(
        self,
        request: baas_20181221_models.InstallFabricChaincodePackageRequest,
    ) -> baas_20181221_models.InstallFabricChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_fabric_chaincode_package_with_options(request, runtime)

    async def install_fabric_chaincode_package_async(
        self,
        request: baas_20181221_models.InstallFabricChaincodePackageRequest,
    ) -> baas_20181221_models.InstallFabricChaincodePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_fabric_chaincode_package_with_options_async(request, runtime)

    def instantiate_fabric_chaincode_with_options(
        self,
        request: baas_20181221_models.InstantiateFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.InstantiateFabricChaincodeResponse:
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
            action='InstantiateFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.InstantiateFabricChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def instantiate_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.InstantiateFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.InstantiateFabricChaincodeResponse:
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
            action='InstantiateFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.InstantiateFabricChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='JoinFabricChannel',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.JoinFabricChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_fabric_channel_with_options_async(
        self,
        request: baas_20181221_models.JoinFabricChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.JoinFabricChannelResponse:
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
            action='JoinFabricChannel',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.JoinFabricChannelResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: baas_20181221_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ListTagResourcesResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetAntChainCertificate',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ResetAntChainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_ant_chain_certificate_with_options_async(
        self,
        request: baas_20181221_models.ResetAntChainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ResetAntChainCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetAntChainCertificate',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ResetAntChainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetAntChainUserCertificate',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ResetAntChainUserCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_ant_chain_user_certificate_with_options_async(
        self,
        request: baas_20181221_models.ResetAntChainUserCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ResetAntChainUserCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ant_chain_id):
            body['AntChainId'] = request.ant_chain_id
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetAntChainUserCertificate',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ResetAntChainUserCertificateResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='ResetFabricOrganizationUserPassword',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ResetFabricOrganizationUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_fabric_organization_user_password_with_options_async(
        self,
        request: baas_20181221_models.ResetFabricOrganizationUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.ResetFabricOrganizationUserPasswordResponse:
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
            action='ResetFabricOrganizationUserPassword',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.ResetFabricOrganizationUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
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

    def submit_fabric_chaincode_definition_with_options(
        self,
        request: baas_20181221_models.SubmitFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.SubmitFabricChaincodeDefinitionResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.SubmitFabricChaincodeDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fabric_chaincode_definition_with_options_async(
        self,
        request: baas_20181221_models.SubmitFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.SubmitFabricChaincodeDefinitionResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.SubmitFabricChaincodeDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_fabric_chaincode_definition(
        self,
        request: baas_20181221_models.SubmitFabricChaincodeDefinitionRequest,
    ) -> baas_20181221_models.SubmitFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_fabric_chaincode_definition_with_options(request, runtime)

    async def submit_fabric_chaincode_definition_async(
        self,
        request: baas_20181221_models.SubmitFabricChaincodeDefinitionRequest,
    ) -> baas_20181221_models.SubmitFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_fabric_chaincode_definition_with_options_async(request, runtime)

    def synchronize_fabric_chaincode_with_options(
        self,
        request: baas_20181221_models.SynchronizeFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.SynchronizeFabricChaincodeResponse:
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
            action='SynchronizeFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.SynchronizeFabricChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def synchronize_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.SynchronizeFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.SynchronizeFabricChaincodeResponse:
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
            action='SynchronizeFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.SynchronizeFabricChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: baas_20181221_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.TagResourcesResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UnfreezeAntChainAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def unfreeze_ant_chain_account_with_options_async(
        self,
        request: baas_20181221_models.UnfreezeAntChainAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UnfreezeAntChainAccountResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UnfreezeAntChainAccountResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: baas_20181221_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UntagResourcesResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainConsortiumResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_consortium_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainConsortiumResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainConsortiumResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainContractContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_contract_content_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainContractContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainContractContentResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainContractContentResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainContractProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_contract_project_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainContractProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainContractProjectResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainContractProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_member_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainMemberResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainQRCodeAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ant_chain_qrcode_authorization_with_options_async(
        self,
        request: baas_20181221_models.UpdateAntChainQRCodeAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpdateAntChainQRCodeAuthorizationResponse:
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpdateAntChainQRCodeAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
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
            action='UpgradeFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpgradeFabricChaincodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_fabric_chaincode_with_options_async(
        self,
        request: baas_20181221_models.UpgradeFabricChaincodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpgradeFabricChaincodeResponse:
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
            action='UpgradeFabricChaincode',
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpgradeFabricChaincodeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def upgrade_fabric_chaincode_definition_with_options(
        self,
        request: baas_20181221_models.UpgradeFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpgradeFabricChaincodeDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.chaincode_package_id):
            body['ChaincodePackageId'] = request.chaincode_package_id
        if not UtilClient.is_unset(request.chaincode_version):
            body['ChaincodeVersion'] = request.chaincode_version
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpgradeFabricChaincodeDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_fabric_chaincode_definition_with_options_async(
        self,
        request: baas_20181221_models.UpgradeFabricChaincodeDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> baas_20181221_models.UpgradeFabricChaincodeDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chaincode_id):
            body['ChaincodeId'] = request.chaincode_id
        if not UtilClient.is_unset(request.chaincode_package_id):
            body['ChaincodePackageId'] = request.chaincode_package_id
        if not UtilClient.is_unset(request.chaincode_version):
            body['ChaincodeVersion'] = request.chaincode_version
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
            version='2018-12-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_20181221_models.UpgradeFabricChaincodeDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_fabric_chaincode_definition(
        self,
        request: baas_20181221_models.UpgradeFabricChaincodeDefinitionRequest,
    ) -> baas_20181221_models.UpgradeFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_fabric_chaincode_definition_with_options(request, runtime)

    async def upgrade_fabric_chaincode_definition_async(
        self,
        request: baas_20181221_models.UpgradeFabricChaincodeDefinitionRequest,
    ) -> baas_20181221_models.UpgradeFabricChaincodeDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_fabric_chaincode_definition_with_options_async(request, runtime)
